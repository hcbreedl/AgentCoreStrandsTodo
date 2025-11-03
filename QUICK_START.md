# Quick Start Guide

Get up and running with your to-do agent in 5 minutes!

## Prerequisites Check

```bash
# Check Python version (need 3.8+)
python3 --version

# Check AWS CLI is installed
aws --version

# Check AWS credentials are configured
aws sts get-caller-identity
```

If any of these fail, fix them first:
- **Python**: Install from [python.org](https://www.python.org/)
- **AWS CLI**: `pip install awscli` or use installer
- **AWS Credentials**: `aws configure`

## Step-by-Step Setup

### 1. Create Virtual Environment (2 minutes)

```bash
# Navigate to project directory
cd /Users/hbreedlove/Development/aws-experiment

# Create virtual environment
python3 -m venv .venv

# Activate it
source .venv/bin/activate  # On macOS/Linux
# OR
# .venv\Scripts\activate  # On Windows

# You should see (.venv) in your prompt
```

### 2. Install Dependencies (1 minute)

```bash
pip install -r requirements.txt
```

If you get errors about `bedrock-agentcore` or `strands`, you may need to:
1. Request access to Bedrock in AWS Console
2. Check that the package versions exist

**Note**: The exact package names may vary. Check the [official documentation](https://docs.aws.amazon.com/bedrock-agentcore/) for the latest package names.

### 3. Set Environment Variables (1 minute)

Create a `.env` file (copy from `.env.example` if provided):

```bash
# Create .env file
cat > .env << EOF
AWS_REGION=us-east-1
EOF
```

Or manually create `.env` with:
```
AWS_REGION=us-east-1
```

### 4. Test Locally (1 minute)

```bash
# Run the agent
python todo_agent.py
```

Try these commands:
- `Add task: Test the agent`
- `List all tasks`
- `Mark task 1 as complete`

Press `Ctrl+C` or type `exit` to quit.

### 5. (Optional) Run Tests

```bash
# Run automated tests
python test_agent.py test

# Or run interactive demo
python test_agent.py demo
```

## Troubleshooting

### "ModuleNotFoundError: No module named 'strands'"

The package might have a different name. Try:
```bash
pip install strands-agents strands-agents-tools
```

Or check the official Strands documentation for the correct package name.

### "AWS credentials not found"

```bash
aws configure
# Enter your:
# - AWS Access Key ID
# - AWS Secret Access Key
# - Default region (e.g., us-east-1)
# - Default output format (json)
```

### "AccessDenied" when using Bedrock

1. Go to AWS Console → Bedrock
2. Request access to the models you want to use
3. Wait for approval (usually instant for AWS accounts)
4. Try again

### Agent not understanding commands

The agent uses a system prompt. Try being more explicit:
- Instead of: "Buy groceries"
- Try: "Add task: Buy groceries"

## What's Next?

1. **Read LEARNING_GUIDE.md** - Understand how the code works
2. **Experiment** - Modify the system prompt, add tools
3. **Deploy** - When ready, deploy to AgentCore (see README.md)

## Common First-Time Questions

**Q: Do I need AWS credits/money to test locally?**
A: Testing locally may still use AWS Bedrock API calls, which have costs. Check AWS pricing.

**Q: Can I use this without deploying to AgentCore?**
A: Yes! The local version works independently. Deployment is optional.

**Q: What if the packages don't install?**
A: The Strands and AgentCore SDKs might be in preview or have different names. Check AWS documentation for the latest package names.

**Q: How do I see what the agent is doing?**
A: Add print statements to the tool functions to see when they're called.

## Getting Help

- Check README.md for more details
- Review LEARNING_GUIDE.md for code explanations
- Check AWS Bedrock AgentCore documentation
- Look at Strands framework documentation

Happy coding! 🚀

