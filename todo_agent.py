"""
Simple To-Do List Agent using Strands Framework and Bedrock AgentCore

This is a beginner-friendly example that demonstrates:
- Creating an agent with Strands
- Using tools to read/write data
- Handling user interactions
- Managing a simple to-do list

The agent uses Bedrock models via Strands to understand natural language
and manage your to-do list.
"""

import json
import os
from typing import List, Dict, Any

# Strands imports - these provide the agent framework
try:
    from strands import Agent
    from strands_tools import file_read, file_write
except ImportError:
    print("Error: Make sure you've installed the required packages:")
    print("  pip install strands-agents strands-agents-tools")
    raise

# Configuration
TODO_FILE = "todo_list.json"


# System prompt - this tells the agent how to behave
SYSTEM_PROMPT = """You are a helpful to-do list manager assistant. 

Your capabilities:
1. Add new tasks to the to-do list
2. List all tasks (showing their status)
3. Mark tasks as completed
4. Delete tasks from the list

Always be friendly and helpful. When listing tasks, show them in a clear format
with numbers. When a user asks to "add a task", extract the task description
and add it to the list. When they say "complete" or "mark as done", update
the task status.

Store the to-do list in a JSON file. The format should be:
[
    {"id": 1, "task": "Buy groceries", "completed": false},
    {"id": 2, "task": "Finish homework", "completed": true}
]
"""


def load_todos() -> List[Dict[str, Any]]:
    """Load the to-do list from the JSON file."""
    if os.path.exists(TODO_FILE):
        try:
            with open(TODO_FILE, 'r') as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []
    return []


def save_todos(todos: List[Dict[str, Any]]) -> None:
    """Save the to-do list to the JSON file."""
    with open(TODO_FILE, 'w') as f:
        json.dump(todos, f, indent=2)


def add_task(task_description: str) -> str:
    """
    Tool function: Add a new task to the to-do list.
    
    This is a tool the agent can call to add tasks.
    """
    todos = load_todos()
    
    # Find the next available ID
    next_id = max([t.get('id', 0) for t in todos] + [0]) + 1
    
    new_task = {
        "id": next_id,
        "task": task_description,
        "completed": False
    }
    
    todos.append(new_task)
    save_todos(todos)
    
    return f"Added task #{next_id}: {task_description}"


def list_tasks() -> str:
    """
    Tool function: List all tasks in the to-do list.
    
    This tool reads the current tasks and formats them for display.
    """
    todos = load_todos()
    
    if not todos:
        return "Your to-do list is empty! Add some tasks to get started."
    
    result = "📋 Your To-Do List:\n\n"
    for task in todos:
        status = "✅" if task.get('completed', False) else "⏳"
        result += f"{status} Task #{task['id']}: {task['task']}\n"
    
    return result


def complete_task(task_id: int) -> str:
    """
    Tool function: Mark a task as completed.
    
    Args:
        task_id: The ID of the task to mark as completed
    """
    todos = load_todos()
    
    for task in todos:
        if task['id'] == task_id:
            task['completed'] = True
            save_todos(todos)
            return f"✅ Marked task #{task_id} as completed: {task['task']}"
    
    return f"❌ Task #{task_id} not found."


def delete_task(task_id: int) -> str:
    """
    Tool function: Delete a task from the to-do list.
    
    Args:
        task_id: The ID of the task to delete
    """
    todos = load_todos()
    
    original_count = len(todos)
    todos = [t for t in todos if t['id'] != task_id]
    
    if len(todos) < original_count:
        save_todos(todos)
        return f"🗑️ Deleted task #{task_id}"
    else:
        return f"❌ Task #{task_id} not found."


# Create the agent with our tools
# Tools are functions the agent can call when needed
agent = Agent(
    tools=[add_task, list_tasks, complete_task, delete_task],
    system_prompt=SYSTEM_PROMPT
)


def handle_user_input(user_input: str) -> str:
    """
    Process user input and return the agent's response.
    
    This is the main function that connects user input to the agent.
    """
    try:
        # The agent processes the input and decides which tools to use
        response = agent(user_input)
        
        # Extract the text response
        # Note: The exact format may vary based on Strands version
        if hasattr(response, 'message'):
            if isinstance(response.message, dict):
                content = response.message.get('content', [])
                if content and isinstance(content[0], dict):
                    return content[0].get('text', str(response.message))
            return str(response.message)
        else:
            return str(response)
            
    except Exception as e:
        return f"Sorry, I encountered an error: {str(e)}"


def main():
    """
    Main function for local testing.
    
    This creates an interactive loop where you can chat with the agent.
    """
    print("=" * 60)
    print("🤖 To-Do List Agent - Powered by Strands & Bedrock AgentCore")
    print("=" * 60)
    print("\nI can help you manage your to-do list!")
    print("Try commands like:")
    print("  - 'Add task: Buy groceries'")
    print("  - 'List all tasks'")
    print("  - 'Mark task 1 as complete'")
    print("  - 'Delete task 2'")
    print("\nType 'exit' or 'quit' to stop.\n")
    
    while True:
        try:
            # Get user input
            user_input = input("You: ").strip()
            
            if not user_input:
                continue
            
            # Check for exit commands
            if user_input.lower() in ['exit', 'quit', 'bye']:
                print("\n👋 Goodbye! Have a productive day!")
                break
            
            # Process with the agent
            print("\nAgent: ", end="")
            response = handle_user_input(user_input)
            print(response)
            print()  # Blank line for readability
            
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"\n❌ Error: {e}\n")


if __name__ == "__main__":
    # Run the interactive agent
    main()

