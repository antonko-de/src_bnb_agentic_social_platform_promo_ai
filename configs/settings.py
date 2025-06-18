from pydantic import BaseModel, Field
import yaml
from pathlib import Path

class LLMSettings(BaseModel):
    ''''name says it all'''

    openai_api_key: str = Field(...)

    # models used by different agents
    market_intelligence_agent_model: str = Field(...)
    content_creation_agent_model: str = Field(...)
    pricing_optimization_agent_model: str = Field(...)
    campaing_management_agent_model: str = Field(...)
    content_evaluator_agent_model: str = Field(...)
    smedia_publisher_agent_model: str = Field(...)

    #max tokens
    max_tokens_intelligence: int = Field(...)
    max_tokens_content_creation: int = Field(...)
    max_tokens_pricing_optimization: int = Field(...)
    max_tokens_campaing_management: int = Field(...)
    max_tokens_content_evaluator: int = Field(...)
    max_tokens_smedia_publisher: int = Field(...)


class PropertySettings(BaseModel):
    ''''name says it all'''
    property_id: str = Field(...)
    property_name: str = Field(...)
    property_description: str = Field(...)
    property_location: str = Field(...)
    property_type: str = Field(...)
    property_bedrooms: int = Field(...)
    max_guests: int = Field(...)
    property_bathrooms: int = Field(...)



# funcs start here

def load_llm_yaml_config(file_path: str) -> LLMSettings:
    with open(file_path, 'r') as file:
        config = yaml.safe_load(file)
    return LLMSettings(**config)



def load_property_yaml_config(file_path: str) -> PropertySettings:
    with open(file_path, 'r') as file:
        config = yaml.safe_load(file)
    return PropertySettings(**config)



llm_settings = load_llm_yaml_config(Path(__file__).parent / 'llm_config.yaml')
property_settings = load_property_yaml_config(Path(__file__).parent / 'property_config.yaml')


