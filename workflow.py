from llama_index.core.workflow import (
    Event,
    StartEvent,
    StopEvent,
    Workflow,
    step,
)
from dotenv import load_dotenv
from llama_index.llms.openai import OpenAI
import asyncio
from agent import agent as colorAgent

load_dotenv()

class ColorEvent(Event):
    color: str
    occasion: str


class OutfitCololorFlow(Workflow):
    llm = OpenAI()

    @step
    async def recommend_color(self, ev: StartEvent) -> ColorEvent:
        occasion = ev.occasion

        prompt = f"What color should I wear for {occasion}."
        response = colorAgent.chat(prompt)
        return ColorEvent(color=str(response), occasion=occasion)

    @step
    async def critique_color(self, ev: ColorEvent) -> StopEvent:
        color = ev.color
        occasion = ev.occasion

        prompt = f"For the occation of {occasion}, what do you think of wearing an outfit of the color {color}."
        response = await self.llm.acomplete(prompt)
        return StopEvent(result=str(response))


w = OutfitCololorFlow(timeout=60, verbose=False)

async def main():
    result = await w.run(occasion="my friend's wedding")
    print(str(result))

if __name__ == "__main__":
    
    asyncio.run(main())
