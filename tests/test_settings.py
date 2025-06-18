from configs.settings import load_llm_yaml_config, load_property_yaml_config

def test_llm_settings():
    llm_settings = load_llm_yaml_config('tests/test_llm_settings.yaml')
    assert llm_settings.max_tokens_campaing_management == 2
    assert llm_settings.market_intelligence_agent_model == "test"
    assert llm_settings.content_creation_agent_model == "test"
    assert llm_settings.pricing_optimization_agent_model == "test"
    assert llm_settings.campaing_management_agent_model == "test"
    assert llm_settings.content_evaluator_agent_model == "test"

def test_property_settings():
    property_settings = load_property_yaml_config('tests/test_property_settings.yaml')
    assert property_settings.property_id == "1234567890"
    assert property_settings.property_name == "Test Spot"
    assert property_settings.property_description == "test description"
    assert property_settings.property_location == "test location"
    assert property_settings.property_type == "Studio"
    assert property_settings.max_guests == 2
    assert property_settings.property_bathrooms == 1

