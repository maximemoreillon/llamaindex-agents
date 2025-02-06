from llama_index.core.agent.workflow import (
    AgentWorkflow,
    FunctionAgent,
    ReActAgent,
)
from llama_index.core.tools import FunctionTool
from llama_index.llms.openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# Define some tools
def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b


def subtract(a: int, b: int) -> int:
    """Subtract two numbers."""
    return a - b


# Create agent configs
# NOTE: we can use FunctionAgent or ReActAgent here.
# FunctionAgent works for LLMs with a function calling API.
# ReActAgent works for any LLM.
calculator_agent = FunctionAgent(
    name="calculator",
    description="Performs basic arithmetic operations",
    system_prompt="You are a calculator assistant.",
    tools=[
        FunctionTool.from_defaults(fn=add),
        FunctionTool.from_defaults(fn=subtract),
    ],
    llm=OpenAI(model="gpt-4"),
)

retriever_agent = FunctionAgent(
    name="retriever",
    description="Manages data retrieval",
    system_prompt="You are a retrieval assistant.",
    llm=OpenAI(model="gpt-4"),
)

# Create and run the workflow
workflow = AgentWorkflow(
    agents=[calculator_agent, retriever_agent], root_agent="calculator"
)

# Run the system
async def main():
  response = await workflow.run(user_msg="Can you add 5 and 3?")
  print(response)



if __name__ == "__main__":
    import asyncio
    asyncio.run(main())