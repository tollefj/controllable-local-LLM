from pydantic import BaseModel


class PythonCodeOutput(BaseModel):
    code: str


def generate_code(prompt: str):
    output = generate(
        system_prompt="You are an AI assistant and expert in Python programming. You will generate perfect and executable Python code based on the given prompt.",
        prompt=prompt,
        model=model,
        # schema=PythonCodeOutput.model_json_schema(),
        num_ctx=1000,
        num_predict=5000,
        temperature=0.0,  # experiment with this one
    )
    # if output and "code" in output:
    #     return output["code"]
    code = "\n".join(
        [line for line in output.split("\n") if not line.startswith("```")]
    )
    with open("tmp.py", "w") as f:
        f.write(code)


generate_code(
    "create a function `get_weather` that randomly returns either 'Rainy', 'Chance of a glimpse of the sun'"
)
from tmp import get_weather

get_weather()
