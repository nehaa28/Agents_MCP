from mcp.context_store import get_context, update_context

# def planner_agent():
#     print("[PlannerAgent] Analyzing input")
#     user_input = get_context().get("user_input", "")
#     task = "lookup" if "what is" in user_input.lower() else "respond"
#     update_context("task", task)

# with langgraph
def planner_agent(state):
    user_input = state["user_input"]
    task = "lookup" if "what is" in user_input.lower() else "respond"
    update_context("task", task)
    return {"task": task}
