from agents.agent import Agent
from pydantic import BaseModel, Field
from typing import List, Literal


class WebAgent(Agent):
    def __init__(self, model, query):
        super().__init__(model)
        self.query = query

    def system(self):
        return f"You are an AI assistant tasked with searching the web for information on the topic of {self.query}."

    def prompt(self):
        return f"From the topic of {self.query}, create a search query ."

    def schema(self):
        class SearchSchema(BaseModel):
            search: str

        return SearchSchema.model_json_schema()

    def __call__(self, output_key: str = "search"):
        output = self.generate(
            system_prompt=self.system(),
            prompt=self.prompt(),
            schema=self.schema(),
            model=self.model,
            num_ctx=1000,
            num_predict=200,
            temperature=0.0,
        )
        if output:
            return output[output_key]
