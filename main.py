from agents import Agent, Runner,OpenAIChatCompletionsModel,  set_tracing_disabled, function_tool
from dotenv import load_dotenv
from agents.run import RunConfig
import os
from openai import AsyncOpenAI
import _asyncio
import chainlit as cl

load_dotenv()
# set_tracing_disabled(True)

api_key= os.getenv("GEMINI_API_KEY")

if not api_key:
    raise RuntimeError("key not found")

external_client=AsyncOpenAI(
    api_key=api_key,
     base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)
model=OpenAIChatCompletionsModel(
    model="gemini-1.5-flash",
    openai_client=external_client
)
config= RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)
agent =Agent(
    name= "Assistant",
    instructions="You are a helpful assistant",
    model=model
)

result = Runner.run_sync(agent,"Tell me about PIAIC", run_config=config)
print(result.final_output)

