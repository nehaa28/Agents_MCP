import os
from openai import OpenAI
from dotenv import load_dotenv
from mcp.context_store import get_context, update_context
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

load_dotenv()

# client = OpenAI(
#     api_key=os.getenv("OPENAI_API_KEY"),
#     base_url=os.getenv("OPENAI_BASE_URL")  # e.g., https://api.groq.com/openai/v1
# )

# def knowledge_agent():
#     context = get_context()
#     task = context.get("task", "")
#     user_input = context.get("user_input", "")

#     if task == "lookup":
#         print("[KnowledgeAgent] Using LLM to respond")

#         response = client.chat.completions.create(
#             model="llama3-8b-8192",
#             messages=[
#                 {"role": "user", "content": user_input}
#             ]
#         )

#         answer = response.choices[0].message.content
#         update_context("llm_response", answer)
#     else:
#         update_context("llm_response", "No lookup needed.")

# with langgraph
llm = ChatOpenAI(
    model="llama3-8b-8192",
    base_url=os.getenv("OPENAI_BASE_URL"),
    api_key=os.getenv("OPENAI_API_KEY"),
    temperature=0.3,
)

def knowledge_agent(state):
    context = get_context()
    task = context.get("task", "")
    user_input = context.get("user_input", "")
    if task == "lookup":
        prompt = ChatPromptTemplate.from_messages([
            ("user", "{question}")
        ])
        chain = prompt | llm
        result = chain.invoke({"question": user_input})
        answer = result.content
    else:
        answer = "No lookup needed."

    update_context("llm_response", answer)
    return {"llm_response": answer}