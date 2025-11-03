"""
Simple test script for the to-do agent.

This script tests the agent with some example commands
to make sure everything is working correctly.
"""

from todo_agent import handle_user_input, load_todos, save_todos
import os
import json

# Test data file
TEST_FILE = "test_todo_list.json"


def setup_test():
    """Set up a clean test environment."""
    # Backup original if exists
    original_file = "todo_list.json"
    if os.path.exists(original_file):
        # Keep original for now
        pass
    
    # Initialize with empty list for testing
    with open(TEST_FILE, 'w') as f:
        json.dump([], f)
    
    print("✅ Test environment set up")


def cleanup_test():
    """Clean up test files."""
    if os.path.exists(TEST_FILE):
        os.remove(TEST_FILE)
        print("✅ Test files cleaned up")


def run_tests():
    """Run a series of test commands."""
    print("\n" + "="*60)
    print("🧪 Testing To-Do Agent")
    print("="*60 + "\n")
    
    # Temporarily use test file
    global TODO_FILE
    import todo_agent
    original_file = todo_agent.TODO_FILE
    todo_agent.TODO_FILE = TEST_FILE
    
    test_commands = [
        "List all tasks",
        "Add task: Buy groceries",
        "Add task: Finish homework",
        "Add task: Call mom",
        "List all tasks",
        "Mark task 1 as complete",
        "List all tasks",
        "Delete task 2",
        "List all tasks",
    ]
    
    print("Running test commands...\n")
    for i, command in enumerate(test_commands, 1):
        print(f"Test {i}: {command}")
        print("-" * 40)
        try:
            response = handle_user_input(command)
            print(f"Response: {response}\n")
        except Exception as e:
            print(f"❌ Error: {e}\n")
    
    # Restore original file
    todo_agent.TODO_FILE = original_file
    
    print("="*60)
    print("✅ Tests completed!")
    print("="*60)


def interactive_demo():
    """Run an interactive demo with the agent."""
    print("\n" + "="*60)
    print("🎮 Interactive Demo Mode")
    print("="*60)
    print("\nTry these example commands:")
    print("  • 'Add task: Learn about Bedrock AgentCore'")
    print("  • 'List all tasks'")
    print("  • 'Mark task 1 as complete'")
    print("  • 'Delete task 2'")
    print("\nOr try your own natural language commands!\n")
    
    from todo_agent import main
    main()


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        setup_test()
        try:
            run_tests()
        finally:
            cleanup_test()
    elif len(sys.argv) > 1 and sys.argv[1] == "demo":
        interactive_demo()
    else:
        print("Usage:")
        print("  python test_agent.py test  - Run automated tests")
        print("  python test_agent.py demo  - Run interactive demo")
        print("\nOr run the main agent directly:")
        print("  python todo_agent.py")

