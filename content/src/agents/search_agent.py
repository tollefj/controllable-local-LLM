from agents.agent import Agent
from pydantic import BaseModel, Field
from typing import List, Literal


class SearchAgent(Agent):
    def __init__(self, model, topic):
        super().__init__(model)
        self.topic = topic

    def system(self):
        return "You are tasked with reformulating a topic into a boolean AND/OR search string suitable for search engines to retrieve data about a research project. Maximum 5 operations. It MUST include 'dataset' or 'data sources'. Output in JSON according to the provided schema."

    def prompt(self):
        return f"Generate a Google keyword search that will help the user find datasets on the topic of {self.topic}. Do not constrain the search to specific sites. Use your knowledge of the topic to generate a comprehensive search string."

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
