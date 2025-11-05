# Bedrock AgentCore + Strands To-Do App - Learning Project

Welcome! This is a beginner-friendly project to help you learn **Amazon Bedrock AgentCore** and the **Strands** framework by building a simple to-do list agent.

## Table of Contents

- [What is Bedrock AgentCore?](#what-is-bedrock-agentcore)
- [What is Strands?](#what-is-strands)
- [Project Overview](#project-overview)
- [Quick Start (5 Minutes)](#quick-start-5-minutes)
- [Full Setup Guide](#full-setup-guide)
- [AWS Credentials Setup](#aws-credentials-setup)
- [IAM User Setup (Best Practice)](#iam-user-setup-best-practice)
- [Running the Agent](#running-the-agent)
- [How It Works](#how-it-works)
- [Configuration](#configuration)
- [Learning Guide](#learning-guide)
- [Troubleshooting](#troubleshooting)
- [Deployment to AgentCore](#deployment-to-agentcore)
- [Resources](#resources)

---

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

### Project Structure

```
AgentCoreStrandsToDo/
├── README.md              # This comprehensive guide
├── requirements.txt       # Python dependencies
├── todo_agent.py          # Main agent implementation
├── config.yaml           # AgentCore configuration (model settings)
├── .env                   # Environment variables (gitignored)
└── .gitignore            # Git ignore file
```

---

## Quick Start (5 Minutes)

### Prerequisites Check

```bash
# Check Python version (need 3.8+)
python3 --version

# Check if virtual environment exists
test -d .venv && echo "Virtual environment exists" || echo "Create with: python3 -m venv .venv"
```

### Step 1: Activate Virtual Environment

```bash
# Navigate to project directory
cd /Users/hbreedlove/Development/AgentCoreStrandsToDo

# Activate virtual environment
source .venv/bin/activate  # On macOS/Linux
# OR
# .venv\Scripts\activate  # On Windows

# You should see (.venv) in your prompt
```

### Step 2: Install Dependencies (if not already done)

```bash
pip install -r requirements.txt
```

### Step 3: Verify AWS Credentials

```bash
# Test credentials are loaded
python3 -c "import os; from dotenv import load_dotenv; load_dotenv(); print('AWS_ACCESS_KEY_ID:', 'SET' if os.getenv('AWS_ACCESS_KEY_ID') else 'NOT SET')"
```

### Step 4: Run the Agent

```bash
python3 todo_agent.py
```

Try these commands:
- `Add task: Test the agent`
- `List all tasks`
- `Mark task 1 as complete`
- `Delete task 2`

Press `Ctrl+C` or type `exit` to quit.

### Step 5: Test the Agent

The agent runs in interactive mode. Try commands like:
- `Add task: Buy groceries`
- `List all tasks`
- `Mark task 1 as complete`
- `Delete task 2`
- `exit` or `quit` to stop

---

## Full Setup Guide

### Prerequisites

Make sure you have:
- **Python 3.8 or later** (3.13.3 verified working)
- **AWS Account** with appropriate permissions
- **Virtual environment** (recommended)

### Step 1: Create Virtual Environment

```bash
# Create virtual environment
python3 -m venv .venv

# Activate it
source .venv/bin/activate  # On macOS/Linux
# .venv\Scripts\activate  # On Windows
```

**To deactivate later:** Simply type `deactivate`

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

**Expected packages:**
- `strands-agents` (1.14.0+)
- `strands-agents-tools` (0.2.13+)
- `python-dotenv` (1.2.1+)
- `PyYAML` (6.0.3+)
- `bedrock-agentcore-starter-toolkit` (optional, for deployment)

**Note:** If you get "package not found" errors:
1. Check the [AWS Bedrock AgentCore documentation](https://docs.aws.amazon.com/bedrock-agentcore/) for installation instructions
2. Look at the [bedrock-agentcore-starter-toolkit GitHub repo](https://github.com/aws/bedrock-agentcore-starter-toolkit)
3. The exact package names may vary as these are relatively new services

### Step 3: Configure AWS Credentials

See [AWS Credentials Setup](#aws-credentials-setup) section below.

### Step 4: Configure Environment Variables

Create a `.env` file in the project root:

```bash
# Create .env file
cat > .env << EOF
AWS_ACCESS_KEY_ID=your-access-key-id
AWS_SECRET_ACCESS_KEY=your-secret-access-key
AWS_REGION=us-east-1
EOF
```

**Security Note:** The `.env` file is already in `.gitignore` and won't be committed to version control.

### Step 5: Verify Setup

```bash
# Test Python imports
python3 -c "from strands import Agent; print('✓ Strands import works')"

# Test AWS credentials
python3 -c "import os; from dotenv import load_dotenv; load_dotenv(); print('AWS_ACCESS_KEY_ID:', 'SET' if os.getenv('AWS_ACCESS_KEY_ID') else 'NOT SET')"

# Test Bedrock access (optional)
python3 -c "import boto3; from dotenv import load_dotenv; import os; load_dotenv(); client = boto3.client('bedrock-runtime', region_name=os.getenv('AWS_REGION', 'us-east-1')); print('✓ Bedrock client initialized')"
```

---

## AWS Credentials Setup

### Option 1: Using .env File (Recommended)

You can store your AWS credentials in a `.env` file instead of using `aws configure`.

**Best Practice:** Create a dedicated IAM user (see [IAM User Setup](#iam-user-setup-best-practice) section).

#### Quick Setup

1. **Create `.env` file:**
   ```bash
   # Create .env file
   cat > .env << EOF
   AWS_ACCESS_KEY_ID=your-access-key-id
   AWS_SECRET_ACCESS_KEY=your-secret-access-key
   AWS_REGION=us-east-1
   EOF
   ```

2. **Get AWS Credentials:**
   - Go to [AWS IAM Console](https://console.aws.amazon.com/iam/)
   - Navigate to **Users** → Your username → **Security credentials**
   - Click **Create access key**
   - Choose "Command Line Interface (CLI)"
   - **Copy both values immediately** (you can only see the secret once!)
   - Paste them into your `.env` file

#### Detailed Guide

For step-by-step screenshots and detailed instructions, see:
- [How to Find AWS Credentials](https://console.aws.amazon.com/iam/home#/security_credentials)
- Navigate: AWS Console → IAM → Users → [Your Username] → Security credentials → Access keys → Create access key

### Option 2: Using AWS CLI

If you prefer, you can use AWS CLI:

```bash
aws configure
```

This stores credentials in `~/.aws/credentials` instead of `.env`.

### How It Works

- The code automatically loads `.env` on startup using `python-dotenv`
- `boto3` (used by Strands) automatically reads these environment variables
- The `.env` file is gitignored (never committed to version control)
- Credentials are loaded as environment variables, so boto3 picks them up automatically

### Security Notes

✅ **DO:**
- Keep `.env` in `.gitignore` (already done)
- Never commit `.env` to git
- Use a dedicated IAM user (not root account)
- Grant only necessary permissions

❌ **DON'T:**
- Commit `.env` to version control
- Share `.env` files
- Put credentials in code
- Use root account credentials

### Testing Your Setup

After setting up `.env`, test that it works:

```bash
source .venv/bin/activate
python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('AWS_ACCESS_KEY_ID:', os.getenv('AWS_ACCESS_KEY_ID')[:10] + '...' if os.getenv('AWS_ACCESS_KEY_ID') else 'NOT SET')"
```

---

## IAM User Setup (Best Practice)

**⚠️ Important: Don't use your root account!** Create a dedicated IAM user for this project.

### Why Create a Separate IAM User?

✅ **Benefits:**
- **Security**: Root account has full access - if compromised, your entire AWS account is at risk
- **Principle of Least Privilege**: User only has permissions needed for Bedrock/AgentCore
- **Audit Trail**: Easier to track what this specific project is doing
- **Easy Cleanup**: Can delete the user when the experiment is done
- **Cost Control**: Can attach spending limits/alerts to the user
- **Best Practice**: AWS recommends IAM users for all programmatic access

### Step-by-Step: Create IAM User

#### Step 1: Navigate to IAM
1. Go to [AWS Console](https://console.aws.amazon.com)
2. Search for "IAM" or go to: https://console.aws.amazon.com/iam/
3. Make sure you're in the right region (doesn't matter for IAM, it's global)

#### Step 2: Create User
1. Click **Users** in the left sidebar
2. Click **Create user** button (top right)

#### Step 3: Set User Details
1. **User name**: Enter something descriptive like `bedrock-agentcore-dev` or `todo-agent-experiment`
2. **Provide user access to the AWS Management Console**: 
   - ❌ Leave unchecked (we're using programmatic access only)
3. Click **Next**

#### Step 4: Set Permissions (Most Important!)

**Option A: Attach AWS Managed Policy (Easiest)**
1. Select **Attach policies directly**
2. Search for "bedrock" in the policy search box
3. Select: **AmazonBedrockFullAccess** (or **AmazonBedrockReadOnly** if full access is too much)
4. Click **Next**

**Option B: Custom Policy (More Secure - Recommended)**

If you want to be more restrictive:

1. Click **Create policy** (opens new tab)
2. Click **JSON** tab
3. Paste this policy (gives only Bedrock permissions):
```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "bedrock:InvokeModel",
                "bedrock:InvokeModelWithResponseStream",
                "bedrock:ListFoundationModels",
                "bedrock:GetFoundationModel",
                "bedrock-agentcore:*"
            ],
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "aws-marketplace:ViewSubscriptions",
                "aws-marketplace:Subscribe"
            ],
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "logs:CreateLogGroup",
                "logs:CreateLogStream",
                "logs:PutLogEvents"
            ],
            "Resource": "arn:aws:logs:*:*:*"
        }
    ]
}
```
4. Click **Next**
5. Name it: `BedrockAgentCoreExperimentPolicy`
6. Click **Create policy**
7. Go back to the user creation tab
8. Refresh and select your new policy
9. Click **Next**

#### Step 5: Review and Create
1. Review the user details
2. Click **Create user**

#### Step 6: Create Access Keys
1. Click on the newly created user
2. Go to **Security credentials** tab
3. Scroll to **Access keys** section
4. Click **Create access key**
5. Select **Command Line Interface (CLI)**
6. Check confirmation box
7. Click **Next** → **Create access key**
8. **⚠️ IMPORTANT**: Copy both:
   - **Access key ID**
   - **Secret access key**
9. Download the CSV or copy both values
10. Click **Done**

#### Step 7: Add to Your .env File

Add the credentials to your `.env` file:
```
AWS_ACCESS_KEY_ID=AKIAIOSFODNN7EXAMPLE
AWS_SECRET_ACCESS_KEY=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
AWS_REGION=us-east-1
```

### Permissions Explained

**Minimum Required Permissions:**
- **`bedrock:InvokeModel`** - To call Bedrock models (Claude, etc.)
- **`bedrock:ListFoundationModels`** - To see available models
- **`bedrock-agentcore:*`** - For AgentCore features (if using AgentCore deployment)
- **`aws-marketplace:ViewSubscriptions`** - Required when using Converse API with tools (AWS requirement)

**Optional (but helpful):**
- **CloudWatch Logs** - To see agent logs and debug issues

### Model Access

**Good News:** As of late 2024, AWS has streamlined Bedrock model access. You **no longer need to manually request access** to serverless models - they're automatically available in your region. Access is controlled through IAM policies instead.

If you encounter "AccessDenied" errors:
1. Check that your IAM user has the correct permissions
2. Verify your region matches where models are available (common: `us-east-1`, `us-west-2`, `eu-west-1`)
3. Check CloudWatch logs for detailed error messages

### Cleaning Up Later

When your experiment is done:

1. **Deactivate access keys** (don't delete yet):
   - IAM → Users → Your user → Security credentials
   - Find your access key → Actions → Deactivate
   - Test that nothing breaks

2. **Delete the user**:
   - IAM → Users → Select user → Delete user
   - This removes all keys and permissions

### Quick Reference

- [IAM Users Console](https://console.aws.amazon.com/iam/home#/users)
- [Create User Direct Link](https://console.aws.amazon.com/iam/home#/users$new)
- [Bedrock Model Access](https://console.aws.amazon.com/bedrock/home?region=us-east-1#/modelaccess)

---

## Running the Agent

### Interactive Mode

Run the agent and chat with it:

```bash
source .venv/bin/activate
python todo_agent.py
```

**Example Commands:**
- `Add task: Buy groceries`
- `List all tasks`
- `Mark task 1 as complete`
- `Delete task 2`
- `exit` or `quit` to stop

### Testing the Agent

The agent runs in interactive mode. Simply run:

```bash
python3 todo_agent.py
```

Then try commands like:
- "Add task: Buy groceries"
- "List all tasks"
- "Mark task 1 as complete"
- "Delete task 2"

---

## How It Works

### Architecture Overview

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

### The Agent Loop

1. **User Input**: You send a message to the agent
2. **Agent Processing**: The Strands agent uses an LLM (via Bedrock) to understand the intent
3. **Tool Execution**: The agent decides which tools to use (e.g., read/write to-do list)
4. **Response**: The agent generates a response and returns it

### Key Concepts

**Agent**: The main AI entity that processes requests. Created using the Strands `Agent` class.

**Tools**: Functions the agent can call (like reading/writing files). Examples:
- `add_task()` - Adds a new task
- `list_tasks()` - Lists all tasks
- `complete_task()` - Marks a task as completed
- `delete_task()` - Removes a task

**System Prompt**: Instructions that guide the agent's behavior. This tells the agent:
- What its role is
- What it can do
- How to behave

**Strands**: The framework that ties everything together - provides the `Agent` class and handles integration with Bedrock.

### Step-by-Step Example

Let's trace through what happens when you say "Add task: Buy groceries":

1. **You Type Input**: `Add task: Buy groceries`

2. **Agent Receives Input**: The agent processes your message

3. **Agent Processes (Behind the Scenes)**:
   - Agent sends your message to Bedrock LLM (Claude)
   - LLM analyzes: "User wants to add a task"
   - LLM decides: "I should call the `add_task` tool"
   - LLM extracts: `task_description = "Buy groceries"`

4. **Tool Execution**:
   ```python
   add_task("Buy groceries")
   # This function:
   # - Loads current todos
   # - Creates new task with ID 3
   # - Saves to JSON file
   # - Returns: "Added task #3: Buy groceries"
   ```

5. **Agent Generates Response**: Agent receives tool result and formats a friendly response:
   ```
   Agent: I've added "Buy groceries" to your list as task #3!
   ```

### Natural Language Understanding

The agent uses an LLM (Large Language Model) to understand what you mean, even if you phrase it differently:

- "Add task: Buy groceries"
- "I need to remember to buy groceries"
- "Add 'Buy groceries' to my todo list"

All of these can trigger the same `add_task` tool!

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

---

## Configuration

### config.yaml

The `config.yaml` file contains deployment and model configuration:

```yaml
# Agent metadata
agent:
  name: todo-list-agent
  description: A simple to-do list management agent using Strands framework
  version: "1.0.0"

# Runtime configuration
runtime:
  python_version: "3.11"
  env_vars:
    - AWS_REGION
    - AWS_PROFILE
    - BEDROCK_MODEL_ID

# Deployment settings
deployment:
  region: us-east-1
  resource_prefix: todo-agent

# Model configuration
model:
  # Default model uses Claude 3 Haiku for fast, cost-effective responses
  # Options: anthropic.claude-3-haiku-20240307-v1:0 (fastest),
  #          anthropic.claude-3-sonnet-20240229-v1:0 (balanced),
  #          anthropic.claude-3-5-sonnet-20240620-v1:0 (most capable)
  default_model: "anthropic.claude-3-haiku-20240307-v1:0"
  temperature: 0.7
  max_tokens: 1000
```

The code automatically reads the model configuration from `config.yaml` (or from the `BEDROCK_MODEL_ID` environment variable). The model ID must include the version suffix (e.g., `-v1:0`). Falls back to defaults if the file doesn't exist or YAML parsing fails.

### Environment Variables (.env)

Your `.env` file should contain:
```
AWS_ACCESS_KEY_ID=your-access-key-id
AWS_SECRET_ACCESS_KEY=your-secret-access-key
AWS_REGION=us-east-1
```

---

## Learning Guide

### Understanding the Code

The main agent code is in `todo_agent.py`. Key components:

#### 1. The Agent

```python
agent = Agent(
    tools=[add_task, list_tasks, complete_task, delete_task],
    system_prompt=SYSTEM_PROMPT
)
```

**What's happening:**
- `tools`: These are functions the agent can call
- `system_prompt`: Instructions telling the agent how to behave

#### 2. Tools (Functions)

Tools are functions the agent can execute. They're like the agent's "hands" - they do the actual work.

Example:
```python
def add_task(task_description: str) -> str:
    todos = load_todos()
    # ... code to add task ...
    save_todos(todos)
    return "Task added!"
```

When you say "Add task: Buy groceries", the agent:
1. Understands your intent
2. Calls `add_task("Buy groceries")`
3. Returns a response

#### 3. System Prompt

The system prompt is like giving your agent a job description:

```python
SYSTEM_PROMPT = """You are a helpful to-do list manager..."""
```

This tells the agent:
- What its role is
- What it can do
- How to behave

**Try it:** Change the system prompt and see how the agent's personality changes!

#### 4. The Conversation Loop

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

### Experimenting and Learning

#### Experiment 1: Change the System Prompt

Try making the agent more casual:
```python
SYSTEM_PROMPT = """You're a chill to-do list buddy. Keep it casual and friendly!"""
```

Or more formal:
```python
SYSTEM_PROMPT = """You are a professional task management assistant. 
Maintain a formal and efficient tone."""
```

#### Experiment 2: Add a New Tool

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

#### Experiment 3: Understand Tool Responses

Add print statements to see what's happening:

```python
def add_task(task_description: str) -> str:
    print(f"DEBUG: add_task called with: {task_description}")
    todos = load_todos()
    print(f"DEBUG: Current todo count: {len(todos)}")
    # ... rest of function
```

### Common Questions

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

### Debugging Tips

1. **Print statements** - Add `print()` to see what's happening
2. **Check JSON file** - Open `todo_list.json` to see state
3. **Test tools directly** - Call tools without the agent
4. **Simplify** - Start with one tool, add more gradually

### Learning Path

1. **Start Simple**: Run the basic agent and see how it responds
2. **Experiment**: Modify the system prompt and see how behavior changes
3. **Add Features**: Try adding new tools (like searching tasks)
4. **Customize**: Adjust the agent's personality or capabilities
5. **Deploy**: Once comfortable, deploy to AgentCore

---

## Troubleshooting

### Common Issues

**Issue**: "Module not found" errors
- **Solution**: Make sure your virtual environment is activated and dependencies are installed
  ```bash
  source .venv/bin/activate
  pip install -r requirements.txt
  ```

**Issue**: AWS credentials not working
- **Solution**: 
  - Verify `.env` file exists and has correct values
  - Check for extra spaces in `.env`
  - Test with: `python3 -c "import os; from dotenv import load_dotenv; load_dotenv(); print('AWS_ACCESS_KEY_ID:', 'SET' if os.getenv('AWS_ACCESS_KEY_ID') else 'NOT SET')"`

**Issue**: "AccessDenied" when using Bedrock
- **Solution**: 
  - Check that your IAM user has `bedrock:InvokeModel` permission
  - Verify your region matches where models are available
  - Check CloudWatch logs for detailed error messages

**Issue**: "Invalid credentials"
- **Solution**: 
  - Double-check you copied both keys correctly
  - Make sure there are no extra spaces in `.env`
  - Verify the keys are Active in IAM console

**Issue**: Agent not understanding commands
- **Solution**: The agent uses a system prompt. Try being more explicit:
  - Instead of: "Buy groceries"
  - Try: "Add task: Buy groceries"

**Issue**: "No credentials found"
- **Solution**: Configure AWS credentials (see [AWS Credentials Setup](#aws-credentials-setup))

**Issue**: Import errors
- **Solution**: Make sure virtual environment is activated

### Package Installation Issues

If you get errors about `bedrock-agentcore` or `strands`:

1. **Check package names**: The exact package names may vary. Try:
   ```bash
   pip install strands-agents strands-agents-tools
   ```

2. **Check official documentation**: Visit https://docs.aws.amazon.com/bedrock-agentcore/

3. **Check GitHub**: Look at the [bedrock-agentcore-starter-toolkit GitHub repo](https://github.com/aws/bedrock-agentcore-starter-toolkit)

4. **API Variations**: The Strands API might differ slightly. Common variations:
   ```python
   # Option 1
   from strands import Agent
   
   # Option 2
   from strands_agents import Agent
   
   # Option 3 (from starter toolkit)
   from bedrock_agentcore.strands import Agent
   ```

### Getting Help

If you're stuck:
1. **Check the guides**: Review this README thoroughly
2. **Review code comments**: Well-documented for learning
3. **Test incrementally**: Get one thing working, then add more
4. **AWS Documentation**: Official docs for AgentCore
5. **Experiment**: Try things - that's how you learn!

---

## Deployment to AgentCore

Once you're happy with your local agent, you can deploy it to AWS Bedrock AgentCore.

### Prerequisites

- Your agent works locally
- AWS credentials configured
- IAM user has `bedrock-agentcore:*` permissions

### Deployment Steps

1. **Configure deployment**:
   ```bash
   agentcore configure
   ```

2. **Deploy**:
   ```bash
   agentcore launch
   ```

3. **Monitor**: Check CloudWatch logs for agent activity

### Configuration

The `config.yaml` file contains deployment settings:
- Agent name and description
- Runtime configuration
- Region settings
- Model configuration

---

## Resources

### Official Documentation

- [Amazon Bedrock AgentCore Documentation](https://docs.aws.amazon.com/bedrock-agentcore/)
- [AWS Bedrock Console](https://us-east-1.console.aws.amazon.com/bedrock-agentcore/home?region=us-east-1#)
- [Strands Framework Documentation](https://github.com/strands/strands-agents)

### AWS Console Links

- [IAM Console](https://console.aws.amazon.com/iam/)
- [Bedrock Console](https://console.aws.amazon.com/bedrock/home)
- [Create Access Key](https://console.aws.amazon.com/iam/home#/security_credentials)

### Next Steps

After mastering this project, consider:
- Adding more sophisticated task management (priorities, due dates)
- Integrating with AWS services (DynamoDB for storage)
- Creating a web interface
- Adding multiple agents that collaborate
- Exploring other Strands capabilities

---

## Success Checklist

You'll know you've mastered this when you can:

- ✅ Run the agent locally without errors
- ✅ Explain what an agent and tools are
- ✅ Modify the system prompt and see behavior change
- ✅ Add a new tool function
- ✅ Understand how the agent processes requests
- ✅ Deploy to AgentCore (optional but recommended)

---

## Questions?

Feel free to experiment and modify the code. That's the best way to learn!

**Remember:** The goal is understanding, not perfection. Enjoy the journey! 🚀
