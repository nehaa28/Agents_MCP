# from langchain_core.prompts import ChatPromptTemplate
# from langchain_core.runnables import RunnableLambda, RunnablePassthrough
# from langchain_openai import ChatOpenAI
# from dotenv import load_dotenv
# import os

# from mcp.context_store import init_context, get_context, update_context

# # Load Groq creds from .env
# load_dotenv()

# llm = ChatOpenAI(
#     model="llama3-8b-8192",
#     base_url=os.getenv("OPENAI_BASE_URL"),
#     api_key=os.getenv("OPENAI_API_KEY"),
#     temperature=0.3,
# )

# # Agent functions
# def input_agent_chain(user_input: str):
#     update_context("user_input", user_input)
#     return user_input

# def planner_agent_chain(user_input: str) -> str:
#     if "what is" in user_input.lower():
#         task = "lookup"
#     else:
#         task = "respond"
#     update_context("task", task)
#     return task

# def knowledge_agent_chain(task: str) -> str:
#     context = get_context()
#     user_input = context.get("user_input", "")
#     if task == "lookup":
#         prompt = ChatPromptTemplate.from_messages([
#             ("user", "{input}")
#         ])
#         chain = prompt | llm
#         response = chain.invoke({"input": user_input})
#         answer = response.content
#         update_context("llm_response", answer)
#         return answer
#     else:
#         response = "No lookup needed."
#         update_context("llm_response", response)
#         return response

# # LangChain graph
# def run_pipeline():
#     init_context()
#     user_input = input("User: ")

#     # Chain with LangChain Runnable pattern
#     pipeline = (
#         RunnableLambda(input_agent_chain)
#         | RunnableLambda(planner_agent_chain)
#         | RunnableLambda(knowledge_agent_chain)
#     )

#     final_response = pipeline.invoke(user_input)

#     print("\n[Final Output]")
#     print(final_response)

# if __name__ == "__main__":
#     run_pipeline()

from langgraph.graph import StateGraph, END
from agents.input_agent import input_agent
from agents.planner_agent import planner_agent
from agents.knowledge_agent import knowledge_agent
from mcp.context_store import init_context, get_context

def main():
    init_context()
    user_input = input("User: ")

    # ✅ Correct: pass state_schema=dict
    builder = StateGraph(state_schema=dict)

    # Add agent nodes
    builder.add_node("InputAgent", input_agent)
    builder.add_node("PlannerAgent", planner_agent)
    builder.add_node("KnowledgeAgent", knowledge_agent)

    # Set execution order
    builder.set_entry_point("InputAgent")
    builder.add_edge("InputAgent", "PlannerAgent")
    builder.add_edge("PlannerAgent", "KnowledgeAgent")
    builder.add_edge("KnowledgeAgent", END)

    # Compile and run the graph
    graph = builder.compile()
    final_state = graph.invoke({"user_input": user_input})

    print("\n[Final Output]")
    print(final_state.get("llm_response", "[No response]"))

if __name__ == "__main__":
    main()

