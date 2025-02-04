import logging
from typing import List, Optional

from ollama import ChatResponse, chat
from pydantic.types import JsonSchemaValue

logger = logging.getLogger(__name__)


def generate(
    system_prompt: str,
    prompt: str,
    model: str,
    schema: Optional[JsonSchemaValue] = None,
    parse: bool = True,
    num_ctx: int = 48000,
    num_predict: int = 4000,
    temperature: float = 0.0,
) -> str:
    response: ChatResponse = chat(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt},
        ],
        options={
            "num_ctx": num_ctx,
            "num_predict": num_predict,
            "top_k": 100,
            "top_p": 0.8,
            "temperature": temperature,
            "seed": 0,  # this is not needed when temp is 0
            "repeat_penalty": 1.3,  # remain default for json outputs, from experience.
        },
        format=schema,
        stream=False,
    )
    res = response.message.content
    if parse and schema:
        try:
            res = eval(res)
        except Exception:
            logger.error(f"Failed to parse response: {res}")
            res = None
    return res


if __name__ == "__main__":
    # prompt = "give me 5 interesting facts about the universe"
    prompt = "Give me a simple recipe for a delicious citrusy cake. Make sure units are in grams when it makes sense. Temperatures should be in C."
    print(generate(prompt))
