from pydantic import BaseModel


class Models(BaseModel):
    llama_3_2_1b: str = "hf.co/bartowski/Llama-3.2-1B-Instruct-GGUF:Q6_K_L"
    llama_3_2_3b: str = "hf.co/unsloth/Llama-3.2-3B-Instruct-GGUF:Q6_K"
    llama_3_1_8b: str = "hf.co/bartowski/Meta-Llama-3.1-8B-Instruct-GGUF:IQ4_NL"
    mistral_sm_24b: str = "hf.co/bartowski/Mistral-Small-24B-Instruct-2501-GGUF:Q4_K_M"
    deepseek_qwen_32: str = "hf.co/unsloth/DeepSeek-R1-Distill-Qwen-32B-GGUF:Q4_K_M"


def get_models() -> str:
    return sorted(list(Models.model_fields.keys()))


def load_model(model_id: str = "llama_3_2_1b") -> str:
    return Models.model_fields[model_id].default
