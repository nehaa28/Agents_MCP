import json
import os

CONTEXT_FILE = "mcp/context.json"

def init_context():
    if not os.path.exists(CONTEXT_FILE):
        with open(CONTEXT_FILE, "w") as f:
            json.dump({}, f)

def get_context():
    with open(CONTEXT_FILE, "r") as f:
        return json.load(f)

def update_context(key, value):
    context = get_context()
    context[key] = value
    with open(CONTEXT_FILE, "w") as f:
        json.dump(context, f, indent=2)
