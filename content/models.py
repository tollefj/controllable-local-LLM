from pydantic import BaseModel


class Models(BaseModel):
    llama_3_2_1b: str = "hf.co/bartowski/Llama-3.2-1B-Instruct-GGUF:Q6_K_L"
    llama_3_2_3b: str = "hf.co/unsloth/Llama-3.2-3B-Instruct-GGUF:Q5_K_M"
    llama_3_1_8b: str = "hf.co/bartowski/Meta-Llama-3.1-8B-Instruct-GGUF:IQ4_NL"
    deepseek_qwen_32b: str = "hc.co/unsloth/DeepSeek-R1-Distill-Qwen-32B-GGUF:Q4_K_M"


def show_models() -> str:
    print(list(Models.model_fields.keys()))


def load_model(model_id: str = "llama_3_2_1b") -> str:
    return Models.model_fields[model_id].default
