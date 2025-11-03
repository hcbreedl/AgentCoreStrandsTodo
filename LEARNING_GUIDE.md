# Learning Guide: Understanding Your To-Do Agent

This guide walks you through the code to help you understand how everything works.

## Architecture Overview

```
┌─────────────┐
│   User      │
│  Input      │
└──────┬──────┘
       │
       ▼
┌─────────────────┐
│  todo_agent.py  │
│                 │
│  ┌───────────┐  │
│  │  Agent    │──┼──► Bedrock LLM
│  │ (Strands) │  │    (Claude, etc.)
│  └─────┬─────┘  │
│        │        │
│        ▼        │
│  ┌───────────┐  │
│  │   Tools   │  │
│  │ (Functions)│ │
│  └─────┬─────┘  │
│        │        │
│        ▼        │
│  ┌───────────┐  │
│  │ todo_list │  │
│  │  .json    │  │
│  └───────────┘  │
└─────────────────┘
```

## Key Components Explained

### 1. The Agent (`Agent` class from Strands)

The agent is the "brain" of your application. It:
- Understands natural language input
- Decides which tools to use
- Generates responses

```python
agent = Agent(
    tools=[add_task, list_tasks, complete_task, delete_task],
    system_prompt=SYSTEM_PROMPT
)
```

**What's happening:**
- `tools`: These are functions the agent can call
- `system_prompt`: Instructions telling the agent how to behave

### 2. Tools (Functions)

Tools are functions the agent can execute. They're like the agent's "hands" - they do the actual work.

Example:
```python
def add_task(task_description: str) -> str:
    # This function adds a task to the list
    todos = load_todos()
    # ... code to add task ...
    return "Task added!"
```

When you say "Add task: Buy groceries", the agent:
1. Understands your intent
2. Calls `add_task("Buy groceries")`
3. Returns a response

### 3. System Prompt

The system prompt is like giving your agent a job description:

```python
SYSTEM_PROMPT = """You are a helpful to-do list manager..."""
```

This tells the agent:
- What its role is
- What it can do
- How to behave

**Try it:** Change the system prompt and see how the agent's personality changes!

### 4. The Conversation Loop

```python
while True:
    user_input = input("You: ")
    response = agent(user_input)
    print(response)
```

This is the basic conversation pattern:
1. Get input from user
2. Send to agent
3. Agent processes (maybe uses tools)
4. Return response
5. Repeat

## How It Works: Step-by-Step Example

Let's trace through what happens when you say "Add task: Buy groceries":

### Step 1: You Type Input
```
You: Add task: Buy groceries
```

### Step 2: Agent Receives Input
```python
response = agent("Add task: Buy groceries")
```

### Step 3: Agent Processes (Behind the Scenes)
1. Agent sends your message to Bedrock LLM (Claude)
2. LLM analyzes: "User wants to add a task"
3. LLM decides: "I should call the `add_task` tool"
4. LLM extracts: task_description = "Buy groceries"

### Step 4: Tool Execution
```python
add_task("Buy groceries")
# This function:
# - Loads current todos
# - Creates new task with ID 3
# - Saves to JSON file
# - Returns: "Added task #3: Buy groceries"
```

### Step 5: Agent Generates Response
Agent receives tool result and formats a friendly response:
```
Agent: I've added "Buy groceries" to your list as task #3!
```

## Key Concepts to Understand

### Natural Language Understanding

The agent uses an LLM (Large Language Model) to understand what you mean, even if you phrase it differently:

- "Add task: Buy groceries"
- "I need to remember to buy groceries"
- "Add 'Buy groceries' to my todo list"

All of these can trigger the same `add_task` tool!

### Tool Selection

The agent automatically decides which tool to use based on:
- Your input
- The system prompt
- Tool descriptions

You don't need to manually route commands!

### State Management

The to-do list is stored in `todo_list.json`. This persists between sessions.

```python
# Load: Get current state
todos = load_todos()

# Modify: Update state
todos.append(new_task)

# Save: Persist changes
save_todos(todos)
```

## Experimenting and Learning

### Experiment 1: Change the System Prompt

Try making the agent more casual:
```python
SYSTEM_PROMPT = """You're a chill to-do list buddy. Keep it casual and friendly!"""
```

Or more formal:
```python
SYSTEM_PROMPT = """You are a professional task management assistant. 
Maintain a formal and efficient tone."""
```

### Experiment 2: Add a New Tool

Try adding a "search tasks" tool:

```python
def search_tasks(keyword: str) -> str:
    """Find tasks containing a keyword."""
    todos = load_todos()
    matches = [t for t in todos if keyword.lower() in t['task'].lower()]
    # Format and return results
    return formatted_results
```

Then add it to the agent:
```python
agent = Agent(
    tools=[add_task, list_tasks, complete_task, delete_task, search_tasks],
    system_prompt=SYSTEM_PROMPT
)
```

### Experiment 3: Understand Tool Responses

Add print statements to see what's happening:

```python
def add_task(task_description: str) -> str:
    print(f"DEBUG: add_task called with: {task_description}")
    todos = load_todos()
    print(f"DEBUG: Current todo count: {len(todos)}")
    # ... rest of function
```

## Common Questions

**Q: Why use Strands instead of calling Bedrock directly?**
A: Strands provides:
- Simpler API
- Built-in tool management
- Easier agent creation
- Better abstraction

**Q: What if the agent uses the wrong tool?**
A: The system prompt helps guide tool selection. Make it more specific about when to use each tool.

**Q: Can I use multiple models?**
A: Yes! You can configure which Bedrock model to use in your code or environment.

**Q: How does this scale?**
A: When deployed to AgentCore, AWS handles scaling, load balancing, and infrastructure.

## Next Steps

1. **Run it locally** - See how it works
2. **Modify the system prompt** - Change behavior
3. **Add more tools** - Expand capabilities
4. **Deploy to AgentCore** - See it in production
5. **Add error handling** - Make it more robust
6. **Use a database** - Replace JSON file with DynamoDB

## Debugging Tips

1. **Print statements** - Add print() to see what's happening
2. **Check JSON file** - Open `todo_list.json` to see state
3. **Test tools directly** - Call tools without the agent
4. **Simplify** - Start with one tool, add more gradually

Happy learning! 🚀

