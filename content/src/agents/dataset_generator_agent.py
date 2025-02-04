from agents.agent import Agent
from pydantic import BaseModel, Field
from typing import List, Literal


class DataGenerationAgent(Agent):
    def __init__(
        self,
        model,
        topic: str,
        label_schema: dict,
        num_samples: int = 4,  # number of new labels to generate
        text_strategy: str = "sentences",
    ):
        super().__init__(model)
        self.topic = topic
        self.label_schema = label_schema
        self.num_samples = num_samples
        self.text_strategy = text_strategy

    def system(self):
        pass

    def prompt(self):
        return f"Generate {self.num_samples} unique sample {self.text_strategy} as if from realistic sources. The samples should pass as extracted from social media posts, official documents or statements online, and not necessarily be from the very beginning of a document, but rather found in the middle of a longer piece of text. It should be connected to the of '{self.topic}'. Use the annotation definitions below: {self.label_schema.model_json_schema()}. Think creatively, and avoid similar language. Output in JSON."

    def schema(self):
        class DataSample(BaseModel):
            text: str
            # text: str = Field(
            #     title="Text",
            #     description="The text of the data sample on the topic of {TOPIC}.",
            #     # min_length=200,
            #     # max_length=500,
            # )
            labels: List[self.label_schema]

        class DataGenerationSchema(BaseModel):
            samples: List[DataSample]

        return DataGenerationSchema.model_json_schema()

    def __call__(
        self,
        output_key: str = "samples",
    ):
        output = self.generate(
            system_prompt=self.system(),
            prompt=self.prompt(),
            schema=self.schema(),
            model=self.model,
            num_ctx=4000,
            num_predict=3000,
            temperature=1.0,  # we keep a high temp for more "creative" text generation
        )
        if output:
            return output[output_key]
