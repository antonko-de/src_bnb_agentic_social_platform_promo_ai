from agents import Agent
from configs.settings import settings
from bnb_agents.instructions import *

market_intelligence_agent = Agent(
    name="Market Intelligence Agent",
    description="A market intelligence agent that can help with market research and analysis",
    instructions=intelligence_agent_instructions,
    model=settings.market_intelligence_agent_model,
    max_tokens=settings.max_tokens,
    tools=[],
)

content_creation_agent = Agent(
    name="Content Creation Agent",
    description="A content creation agent that can help with content creation and optimization",
    instructions=content_creation_agent_instructions,
    model=settings.content_creation_agent_model,
    max_tokens=settings.max_tokens,
    tools=[],
)

pricing_optimization_agent = Agent(
    name="Pricing Optimization Agent",
    description="A pricing optimization agent that can help with pricing optimization and analysis",
    instructions=pricing_optimization_agent_instructions,
    model=settings.pricing_optimization_agent_model,
    max_tokens=settings.max_tokens,
    tools=[],
)

campaing_management_agent = Agent(
    name="Campaing Management Agent",
    description="A campaing management agent that can help with campaing management and optimization",
    instructions=campaing_management_agent_instructions,
    model=settings.campaing_management_agent_model,
    max_tokens=settings.max_tokens,
    tools=[],
)

content_evaluator_agent = Agent(
    name="Content Evaluator Agent",
    description="A content evaluator agent that can help with content evaluation and optimization",
    instructions=content_evaluator_agent_instructions,
    model=settings.content_evaluator_agent_model,
    max_tokens=settings.max_tokens,
    tools=[],
)