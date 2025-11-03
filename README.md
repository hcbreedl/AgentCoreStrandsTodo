# Bedrock AgentCore + Strands To-Do App - Learning Project

Welcome! This is a beginner-friendly project to help you learn **Amazon Bedrock AgentCore** and the **Strands** framework by building a simple to-do list agent.

## What is Bedrock AgentCore?

**Amazon Bedrock AgentCore** is a fully managed service from AWS that allows you to:
- Build, deploy, and manage AI agents
- Scale your agents automatically
- Integrate with AWS services easily
- Handle the infrastructure so you can focus on agent logic

Think of it as a platform where you can deploy your AI agents and AWS handles all the backend infrastructure.

## What is Strands?

**Strands** is a Python framework that makes it easy to build AI agents. It provides:
- Simple abstractions for creating agents
- Built-in tools and utilities
- Easy integration with Bedrock models
- A clean API for agent interactions

## Project Overview

This project creates a simple to-do list agent that can:
- ✅ Add new tasks
- 📋 List all tasks
- ✔️ Mark tasks as completed
- 🗑️ Delete tasks

## Project Structure

```
aws-experiment/
├── README.md              # This file - explains everything
├── requirements.txt       # Python dependencies
├── todo_agent.py          # Main agent implementation
├── config.yaml           # AgentCore configuration
└── .env.example          # Environment variables template
```

## Getting Started

### Step 1: Prerequisites

Make sure you have:
- Python 3.8 or later
- AWS CLI configured with appropriate credentials
- AWS Bedrock access (you may need to request access in the AWS console)

### Step 2: Set Up Virtual Environment

```bash
# Create a virtual environment (recommended)
python3 -m venv .venv

# Activate it
# On macOS/Linux:
source .venv/bin/activate
# On Windows:
# .venv\Scripts\activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

**Note**: The Strands packages may need to be installed from AWS's package repository or GitHub rather than PyPI. If you get "package not found" errors:

1. Check the [AWS Bedrock AgentCore documentation](https://docs.aws.amazon.com/bedrock-agentcore/) for installation instructions
2. Look at the [bedrock-agentcore-starter-toolkit GitHub repo](https://github.com/aws/bedrock-agentcore-starter-toolkit)
3. The starter toolkit may include Strands or provide installation instructions

The exact package names and installation methods may vary as these are relatively new services.

### Step 4: Configure AWS Credentials

Make sure your AWS credentials are configured. You can check this with:

```bash
aws sts get-caller-identity
```

If you need to configure credentials:
```bash
aws configure
```

### Step 5: Set Up Environment Variables

Copy `.env.example` to `.env` and fill in your values:

```bash
cp .env.example .env
```

### Step 6: Test Locally

Run the agent locally to test it:

```bash
python todo_agent.py
```

Try commands like:
- "Add task: Buy groceries"
- "List all tasks"
- "Mark task 1 as complete"
- "Delete task 2"

### Step 7: Deploy to AgentCore

Once you're happy with your local agent:

```bash
# Configure deployment
agentcore configure

# Deploy
agentcore launch
```

## How It Works

### The Agent Loop

1. **User Input**: You send a message to the agent
2. **Agent Processing**: The Strands agent uses an LLM (via Bedrock) to understand the intent
3. **Tool Execution**: The agent decides which tools to use (e.g., read/write to-do list)
4. **Response**: The agent generates a response and returns it

### Key Concepts

**Agent**: The main AI entity that processes requests
**Tools**: Functions the agent can call (like reading/writing files)
**System Prompt**: Instructions that guide the agent's behavior
**Strands**: The framework that ties everything together

## Learning Path

1. **Start Simple**: Run the basic agent and see how it responds
2. **Experiment**: Modify the system prompt and see how behavior changes
3. **Add Features**: Try adding new tools (like searching tasks)
4. **Customize**: Adjust the agent's personality or capabilities
5. **Deploy**: Once comfortable, deploy to AgentCore

## Next Steps

After mastering this project, consider:
- Adding more sophisticated task management (priorities, due dates)
- Integrating with AWS services (DynamoDB for storage)
- Creating a web interface
- Adding multiple agents that collaborate
- Exploring other Strands capabilities

## Resources

- [Amazon Bedrock AgentCore Documentation](https://docs.aws.amazon.com/bedrock-agentcore/)
- [Strands Framework Documentation](https://github.com/strands/strands-agents)
- [AWS Bedrock Console](https://us-east-1.console.aws.amazon.com/bedrock-agentcore/home?region=us-east-1#)

## Troubleshooting

**Issue**: "Module not found" errors
- **Solution**: Make sure your virtual environment is activated and dependencies are installed

**Issue**: AWS credentials not working
- **Solution**: Run `aws configure` and verify with `aws sts get-caller-identity`

**Issue**: Bedrock access denied
- **Solution**: Request access to Bedrock models in the AWS console

## Questions?

Feel free to experiment and modify the code. That's the best way to learn!

