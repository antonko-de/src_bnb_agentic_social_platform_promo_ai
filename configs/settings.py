from pydantic import BaseModel, Field
import yaml
from pathlib import Path

class Settings(BaseModel):

    openai_api_key: str = Field(...)

    # models used by different agents
    market_intelligence_agent_model: str = Field(...)
    content_creation_agent_model: str = Field(...)
    pricing_optimization_agent_model: str = Field(...)
    campaing_management_agent_model: str = Field(...)

    max_tokens: int = Field(...)

def load_yaml_config(file_path: str) -> Settings:
    with open(file_path, 'r') as file:
        config = yaml.safe_load(file)
    return Settings(**config)

settings = load_yaml_config(Path(__file__).parent / 'config.yaml')


