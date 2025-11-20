# Quick Start Guide - 5 Minutes to Your First Agent Conversation

## Step 1: Install (1 minute)

```bash
cd /home/user/middling-co/autogen-agents
pip install -r requirements.txt
```

## Step 2: Configure (2 minutes)

```bash
# Copy environment template
cp .env.example .env

# Edit .env and add your API key
# For OpenRouter (recommended - ultra cheap):
```

Edit `.env`:
```bash
MODEL_PROVIDER=openrouter
OPENROUTER_API_KEY=your-openrouter-key-here
DEFAULT_MODEL=qwen/qwen-2.5-72b-instruct
```

**Don't have OpenRouter?** Use OpenAI instead:
```bash
MODEL_PROVIDER=openai
OPENAI_API_KEY=sk-your-key-here
DEFAULT_MODEL=gpt-4o-mini
```

## Step 3: Run Your First Scenario (2 minutes)

```bash
python run_scenario.py --scenario crisis
```

**Watch as Alice, Bob, and Charlie self-organize to handle a customer crisis!**

---

## What Just Happened?

You gave your 3-person startup team a crisis:
> "Customer tweeted we lost their data..."

They discussed it among themselves:
- Alice investigated the technical issue
- Bob drafted the public response
- Charlie reached out to the customer directly
- They coordinated to resolve it

**No predefined workflow. Just conversation. Just like a real startup.**

---

## Try More Scenarios

```bash
# Strategic planning
python run_scenario.py --scenario planning

# Multiple competing priorities
python run_scenario.py --scenario operations

# Market opportunity
python run_scenario.py --scenario opportunity

# Long-term strategy debate
python run_scenario.py --scenario strategy
```

---

## Create Your Own Scenario

```bash
python run_scenario.py --custom "A competitor just launched the exact feature we're building. What do we do?"
```

---

## Cost Check

**With OpenRouter + Qwen 2.5:**
- Each scenario: ~$0.0025-0.0075 (less than a penny!)
- Your $500 budget = 50,000+ scenarios

**With OpenAI + GPT-4o-mini:**
- Each scenario: ~$0.75-2.25
- Your $500 budget = ~200-700 scenarios

**Both work great. OpenRouter is just 300x cheaper.**

---

## What to Observe

As you run scenarios, watch for:

1. **Self-organization**: Do agents volunteer for tasks they're suited for?
2. **Collaboration**: Do they ask each other questions?
3. **Debate**: Do they challenge assumptions?
4. **Ownership**: Who takes responsibility?
5. **Conclusion**: Do conversations reach decisions or loop?

**Document everything** in `/autogen-agents/learnings/`

---

## Next Steps

1. **Week 1**: Run all 5 scenarios, observe patterns
2. **Week 2**: Create custom scenarios for your specific startup operations
3. **Week 3**: Document what you learned
4. **Month 2**: Start comparing to how you'd handle these as a human
5. **Month 3**: Identify what should become workflows (CrewAI) vs stay conversational

---

## Troubleshooting

**"No module named autogen"**
```bash
pip install pyautogen
```

**"API key not found"**
```bash
# Make sure .env exists and has your key
cat .env
```

**"Too expensive"**
```bash
# Switch to OpenRouter in .env
MODEL_PROVIDER=openrouter
DEFAULT_MODEL=qwen/qwen-2.5-72b-instruct
```

---

## Full Documentation

See `README.md` for comprehensive documentation.

See `/research/framework-decision-autogen-vs-crewai.md` for why we chose this approach.

---

**You're ready to run a startup on AI agents. Let's go!**
