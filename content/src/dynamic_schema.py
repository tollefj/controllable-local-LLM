import re
from typing import Any, Dict, List, Literal

from pydantic import BaseModel, Field


def dynamic_schema(generated_data: List[Dict[str, Any]]):
    assert (
        "possible_values" in generated_data[0]
    ), "generated_data must have 'possible_values' key"
    assert "name" in generated_data[0], "generated_data must have 'name' key"
    assert (
        "description" in generated_data[0]
    ), "generated_data must have 'description' key"

    annotations = {}
    field_definitions = {}

    for d in generated_data:
        # ensure we have a valid field name
        field_name = re.sub(r"[^\w]", "_", d["name"])
        # we don't know the type, so we use literals for the possible values (instead of str...)
        field_type = Literal[tuple(d["possible_values"])]
        annotations[field_name] = field_type
        field_definitions[field_name] = Field(..., description=d["description"])

    DynamicDataModel: BaseModel = type(
        "DynamicDataModel",
        (BaseModel,),
        {"__annotations__": annotations, **field_definitions},
    )
    return DynamicDataModel
