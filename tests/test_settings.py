from configs.settings import load_yaml_config

def test_settings():
    settings = load_yaml_config('tests/test_settings.yaml')
    assert settings.max_tokens == 2
    assert settings.market_intelligence_agent_model == "test_model"
    assert settings.content_creation_agent_model == "test_model"
    assert settings.pricing_optimization_agent_model == "test_model"
    assert settings.campaing_management_agent_model == "test_model"
    assert settings.content_evaluator_agent_model == "test_model"