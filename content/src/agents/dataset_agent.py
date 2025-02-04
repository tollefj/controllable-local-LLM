from agents.agent import Agent
from pydantic import BaseModel, Field
from typing import List, Literal


class DatasetAgent(Agent):
    def __init__(self, model, topic, language):
        super().__init__(model)
        self.topic = topic
        self.language = language

    def system(self):
        return f"You are a helpful assistant that extracts information about datasets about {self.topic}."

    def prompt(self, markdown_file_path):
        data = None
        with open(markdown_file_path) as f:
            data = f.read()
        if len(data) > 5000:
            return "The provided data is too long [DEBUG mode]."
        if not data:
            return "No data provided."
        return f"From the provided information:\n{data}\nFind details about specific datasets (in {self.language} preferably), including information about its language, links, and labels. Determine if the dataset is relevant to the topic of {self.topic} and is in the {self.language} language, specified by the 'relevant' field. Output in JSON."

    def schema(self):
        class DatasetLabel(BaseModel):
            label: str = Field(
                title="Label or category",
                description="The label of the dataset, such as the name of a category.",
            )

        class DatasetSchema(BaseModel):
            name: str
            language: str
            labels: List[DatasetLabel]
            relevant: Literal["yes", "no"]

        class DatasetFinderSchema(BaseModel):
            datasets: List[DatasetSchema]

        return DatasetFinderSchema.model_json_schema()

    def __call__(self, markdown_file_path: str, output_key: str = "datasets"):
        output = self.generate(
            system_prompt=self.system(),
            prompt=self.prompt(markdown_file_path=markdown_file_path),
            schema=self.schema(),
            model=self.model,
            num_ctx=1000,
            temperature=0.0,
        )
        if output:
            return output[output_key]
        return None
