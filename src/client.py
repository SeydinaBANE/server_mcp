from langchain_core.messages import HumanMessage
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.agents import create_agent
from langchain_groq import ChatGroq
from langfuse.langchain import CallbackHandler

from dotenv import load_dotenv
load_dotenv()

import asyncio

async def main():
    client = MultiServerMCPClient(
        {
            "math": {
                "command": "python",
                "args": ["mathserver.py"],
                "transport": "stdio"
            },
            "weather": {
                "url": "http://127.0.0.1:8000/mcp",
                "transport": "streamable_http"
            }
        }
    )

    tools = await client.get_tools()
    print("Les outils disponibles:", [t.name for t in tools])

    model = ChatGroq(model="openai/gpt-oss-120b")

    agent = create_agent(
        model=model,
        tools=tools,
        system_prompt='Tu est un assistant qui a ta disposition des outils que tu peut utliser')

    math_response = await agent.ainvoke(
        {"messages": [HumanMessage(content="la temperature au senegal")]},
        config={'callbacks': [CallbackHandler()]}
    )

    print("La réponse à votre question:", math_response["messages"][-1].content)

asyncio.run(main())