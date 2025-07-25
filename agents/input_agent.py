from mcp.context_store import update_context

# def input_agent(user_input):
#     print("[InputAgent] Received input")
#     update_context("user_input", user_input)

# with langgraph
def input_agent(state):
    user_input = state["user_input"]
    update_context("user_input", user_input)
    return {"user_input": user_input}
