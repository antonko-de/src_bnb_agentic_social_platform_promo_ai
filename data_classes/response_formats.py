from pydantic import BaseModel

class MarketIntelligenceResponse(BaseModel):
    """
    A response format for the market intelligence agent.
    """
    positioning_analysis: str
    
    competitive_benchmark_reference_points: dict

    actionable_recommendations: str

    loation_specific_insights: dict

    revenue_optomization_for_your_property: dict