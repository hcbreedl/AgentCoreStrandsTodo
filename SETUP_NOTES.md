# Setup Notes - Important Information

## About Package Installation

Amazon Bedrock AgentCore and Strands are relatively new services. The exact package names and installation methods may vary. Here's what you need to know:

### Option 1: Using the Starter Toolkit (Recommended)

The `bedrock-agentcore-starter-toolkit` is the easiest way to get started:

```bash
pip install bedrock-agentcore-starter-toolkit
```

This toolkit may include Strands or provide a template project that shows the correct way to use it.

### Option 2: Check Official Documentation

1. Visit: https://docs.aws.amazon.com/bedrock-agentcore/
2. Look for Python SDK installation instructions
3. Check the "Getting Started" guide for package names

### Option 3: Use the Starter Toolkit Template

The starter toolkit likely includes example projects. You can:

```bash
# Install toolkit
pip install bedrock-agentcore-starter-toolkit

# Create a new project from template (if available)
agentcore init my-agent

# Or check their GitHub for examples
```

## API Variations

The Strands API might differ slightly from what's shown in `todo_agent.py`. Common variations:

### Possible Import Patterns:

```python
# Option 1
from strands import Agent
from strands.tools import file_read, file_write

# Option 2
from strands_agents import Agent
from strands_agents.tools import file_read, file_write

# Option 3 (from starter toolkit)
from bedrock_agentcore.strands import Agent

# Option 4 (tool-based)
from strands import Agent, Tool
```

### Possible Agent Creation Patterns:

```python
# Pattern 1: Tools as functions
agent = Agent(tools=[add_task, list_tasks], system_prompt=prompt)

# Pattern 2: Tools as Tool objects
agent = Agent(tools=[Tool(add_task), Tool(list_tasks)], system_prompt=prompt)

# Pattern 3: Different initialization
agent = Agent(
    model="anthropic.claude-3-sonnet",
    tools=[...],
    system_prompt=prompt
)
```

## Adapting the Code

If the imports don't work:

1. **Check error messages** - They often suggest the correct import path
2. **Look at examples** - Check AWS documentation or GitHub for working examples
3. **Start simple** - Get a basic agent working first, then add features
4. **Ask for help** - AWS forums, GitHub issues, or AWS support

## The Code Structure Still Applies

Even if the exact API differs, the **concepts** in this project are correct:

✅ Agent-based architecture  
✅ Tool functions that the agent can call  
✅ System prompts to guide behavior  
✅ Natural language interaction  
✅ State management (JSON file)

You'll just need to adapt the imports and API calls to match the actual Strands implementation.

## Getting the Latest Information

- **AWS Console**: https://us-east-1.console.aws.amazon.com/bedrock-agentcore/
- **Documentation**: https://docs.aws.amazon.com/bedrock-agentcore/
- **GitHub**: Search for "bedrock-agentcore" repositories
- **AWS Blog**: Look for recent posts about AgentCore

## Alternative: Start with the Toolkit Template

If you're having trouble, consider:

1. Using the starter toolkit's example/template
2. Getting that working first
3. Then adapting the concepts from this project

The learning path is more important than the exact syntax!

## Questions to Ask

If you can't find the packages:

1. **Is AgentCore in preview?** - May require AWS account approval
2. **Are packages in a private repo?** - May need AWS package repository access
3. **Is Strands separate?** - Might be included in AgentCore SDK
4. **Are there setup scripts?** - The starter toolkit might handle this

Remember: The goal is to learn the concepts. The exact API will become clear once you have access to the official documentation and examples!

