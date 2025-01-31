from agent import agent as colorAgent
from llama_index.core.agent import ReActAgent
from llama_index.llms.openai import OpenAI
from llama_index.core.tools import QueryEngineTool, ToolMetadata
from dotenv import load_dotenv
load_dotenv()


# initialize llm
llm = OpenAI(model="gpt-4o-mini")


query_engine_tools = [
    QueryEngineTool(
        query_engine=colorAgent,
        metadata=ToolMetadata(
            name="color_agent", description="Agent that recommends colors"
        ),
    ),

]

outer_agent = ReActAgent.from_tools(query_engine_tools, llm=llm, verbose=True)


outer_agent.chat("What color should I wear for my friend's wedding?")
