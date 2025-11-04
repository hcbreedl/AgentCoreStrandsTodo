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
from typing import List, Dict, Any, Optional

# Load environment variables from .env file (for AWS credentials)
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

# Load YAML config if available
try:
    import yaml
    CONFIG_AVAILABLE = True
except ImportError:
    CONFIG_AVAILABLE = False

# Strands imports - these provide the agent framework
try:
    from strands import Agent
except ImportError:
    print("Error: Make sure you've installed the required packages:")
    print("  pip install strands-agents strands-agents-tools")
    raise

# Configuration
TODO_FILE = "todo_list.json"


def load_config() -> Dict[str, Any]:
    """Load configuration from config.yaml if available."""
    config = {}
    if CONFIG_AVAILABLE and os.path.exists("config.yaml"):
        try:
            with open("config.yaml", 'r') as f:
                config = yaml.safe_load(f) or {}
        except Exception as e:
            print(f"Warning: Could not load config.yaml: {e}")
    return config


def get_model_id() -> Optional[str]:
    """Get the model ID from config or environment variables."""
    # Check environment variable first
    model_id = os.getenv("BEDROCK_MODEL_ID")
    if model_id:
        return model_id
    
    # Check config.yaml
    config = load_config()
    if config.get("model") and config["model"].get("default_model"):
        return config["model"]["default_model"]
    
    return None


# System prompt - this tells the agent how to behave
SYSTEM_PROMPT = """You are a helpful to-do list manager. Be concise and direct.

Your capabilities:
1. Add tasks to the list
2. List all tasks
3. Mark tasks as completed
4. Delete tasks

When a user asks to add a task, extract the task description and add it. 
When listing tasks, show them clearly. Keep responses brief and focused."""


def load_todos() -> List[Dict[str, Any]]:
    """Load the to-do list from the JSON file."""
    if os.path.exists(TODO_FILE):
        try:
            with open(TODO_FILE, 'r') as f:
                data = json.load(f)
                # Ensure we have a list
                if isinstance(data, list):
                    return data
                return []
        except json.JSONDecodeError:
            print(f"Warning: {TODO_FILE} contains invalid JSON. Starting with empty list.")
            return []
        except (IOError, OSError, PermissionError) as e:
            print(f"Error reading {TODO_FILE}: {e}")
            return []
    return []


def save_todos(todos: List[Dict[str, Any]]) -> None:
    """Save the to-do list to the JSON file."""
    try:
        # Ensure directory exists
        os.makedirs(os.path.dirname(os.path.abspath(TODO_FILE)) or '.', exist_ok=True)
        with open(TODO_FILE, 'w') as f:
            json.dump(todos, f, indent=2)
    except (IOError, OSError, PermissionError) as e:
        raise RuntimeError(f"Failed to save todos to {TODO_FILE}: {e}")


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
    try:
        save_todos(todos)
        return f"Added task #{next_id}: {task_description}"
    except RuntimeError as e:
        return f"❌ Error saving task: {str(e)}"


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
        if not isinstance(task, dict):
            continue  # Skip invalid entries
        status = "✅" if task.get('completed', False) else "⏳"
        task_id = task.get('id', '?')
        task_desc = task.get('task', '(No description)')
        result += f"{status} Task #{task_id}: {task_desc}\n"
    
    return result


def complete_task(task_id: int) -> str:
    """
    Tool function: Mark a task as completed.
    
    Args:
        task_id: The ID of the task to mark as completed
    """
    todos = load_todos()
    
    for task in todos:
        if isinstance(task, dict) and task.get('id') == task_id:
            task['completed'] = True
            try:
                save_todos(todos)
                task_desc = task.get('task', 'task')
                return f"✅ Marked task #{task_id} as completed: {task_desc}"
            except RuntimeError as e:
                return f"❌ Error saving task: {str(e)}"
    
    return f"❌ Task #{task_id} not found."


def delete_task(task_id: int) -> str:
    """
    Tool function: Delete a task from the to-do list.
    
    Args:
        task_id: The ID of the task to delete
    """
    todos = load_todos()
    
    original_count = len(todos)
    todos = [t for t in todos if not (isinstance(t, dict) and t.get('id') == task_id)]
    
    if len(todos) < original_count:
        try:
            save_todos(todos)
            return f"🗑️ Deleted task #{task_id}"
        except RuntimeError as e:
            return f"❌ Error saving after deletion: {str(e)}"
    else:
        return f"❌ Task #{task_id} not found."


# Create the agent with our tools
# Tools are functions the agent can call when needed
def create_agent():
    """Create and configure the agent with model from config."""
    agent_kwargs = {
        "tools": [add_task, list_tasks, complete_task, delete_task],
        "system_prompt": SYSTEM_PROMPT
    }
    
    # Add model if available
    # Different Strands versions may use different parameter names
    # Try common variations: model_id, model, model_name, bedrock_model_id
    model_id = get_model_id()
    if model_id:
        print(f"Using model: {model_id}")
        # Try most common parameter names
        # We'll pass it and let Agent handle it - if it doesn't accept it, 
        # we'll catch the error and try alternatives
        last_error = None
        for param_name in ["model_id", "model", "model_name", "bedrock_model_id"]:
            try:
                kwargs = {**agent_kwargs, param_name: model_id}
                return Agent(**kwargs)
            except (TypeError, ValueError) as e:
                last_error = e
                continue  # Try next parameter name
        
        # If all parameter names failed, try without model parameter
        if last_error:
            print(f"Warning: Could not set model parameter. Using Agent defaults. Error: {last_error}")
    
    # If model parameter doesn't work or no model specified, use defaults
    return Agent(**agent_kwargs)

agent = create_agent()


def extract_text_from_response(response) -> str:
    """Extract text from Strands AgentResult object."""
    # Strands AgentResult format: response.message.content[0].text
    if hasattr(response, 'message'):
        msg = response.message
        if isinstance(msg, dict):
            content = msg.get('content', [])
            if content and len(content) > 0:
                first_item = content[0]
                if isinstance(first_item, dict):
                    text = first_item.get('text', '')
                    if text:
                        return text.strip()
                elif isinstance(first_item, str):
                    return first_item.strip()
        elif isinstance(msg, str):
            return msg.strip()
    
    # Fallback: string conversion
    return str(response).strip()


def handle_user_input(user_input: str) -> str:
    """Process user input and return the agent's response."""
    try:
        response = agent(user_input)
        text = extract_text_from_response(response)
        return text if text else ""
            
    except Exception as e:
        error_msg = str(e)
        if "ValidationException" in error_msg and "model identifier is invalid" in error_msg:
            model_id = get_model_id()
            return f"❌ Invalid model identifier: {model_id if model_id else '(not set)'}\n" \
                   f"Please check your config.yaml or BEDROCK_MODEL_ID environment variable."
        elif "AccessDenied" in error_msg or "credentials" in error_msg.lower():
            return f"❌ AWS Credentials Error: {error_msg}\n" \
                   f"Please check your AWS credentials in .env file or AWS configuration."
        return f"Sorry, I encountered an error: {error_msg}"


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
            # The Strands AgentResult automatically prints the response when called
            # So we don't need to print it again - just call handle_user_input
            handle_user_input(user_input)
            print("\n")  # Blank line for readability
            
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"\n❌ Error: {e}\n")


if __name__ == "__main__":
    # Run the interactive agent
    main()

