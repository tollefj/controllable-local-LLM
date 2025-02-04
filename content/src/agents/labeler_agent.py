from agents.agent import Agent
from pydantic import BaseModel, Field
from typing import List, Dict, Any, Literal


def filter_labels(filtered_datasets: List[Dict[str, Any]]):
    filtered_labels = set()
    for dataset in filtered_datasets:
        for label in dataset["labels"]:
            filtered_labels.add(label["label"].lower())

    return list(filtered_labels)


class LabelerAgent(Agent):
    def __init__(
        self, model, topic: str, datasets: List[Dict[str, Any]], num_labels: int
    ):
        super().__init__(model)
        self.topic = topic
        self.labels = filter_labels(datasets)
        self.labels_str = ", ".join(self.labels)
        self.num_labels = num_labels

    def system(self):
        return f"You are an assistant that labels datasets based on the topic of {self.topic}."

    def prompt(self):
        return f"From the provided list of previously found labels from datasets on {self.topic}: {self.labels_str}\nCreate a list of {self.num_labels} label categories. Determine the name, a description, and list of possible values. Output in JSON."

    def schema(self):
        class DatasetLabel(BaseModel):
            label_name: str
            description: str
            possible_values: List[str]

        class LabelerSchema(BaseModel):
            labels: List[DatasetLabel]

        return LabelerSchema.model_json_schema()

    def __call__(self, output_key: str = "labels"):
        output = self.generate(
            system_prompt=self.system(),
            prompt=self.prompt(),
            schema=self.schema(),
            model=self.model,
            num_ctx=10000,
            temperature=0.2,
        )
        if output:
            return output[output_key]
