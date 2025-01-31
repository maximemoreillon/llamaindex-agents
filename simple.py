from llama_index.core.agent import ReActAgent
from llama_index.llms.openai import OpenAI
from llama_index.core.tools import FunctionTool
from dotenv import load_dotenv

load_dotenv()

# initialize llm
llm = OpenAI(model="gpt-4o-mini")

def provideAColorSuggestion(x) -> str:
    """Provides a color suggestion"""
    return "Yellow"


color_tool = FunctionTool.from_defaults(fn=provideAColorSuggestion)

# initialize openai agent
agent = ReActAgent.from_tools(tools=[color_tool], llm=llm, verbose=True)



if __name__ == "__main__":
    agent.chat("What color should I wear for my friend's wedding?")
