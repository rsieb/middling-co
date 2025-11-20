# Middling Company - AutoGen Agent Team

## Overview

This directory contains the AutoGen-based conversational agent team for Middling Company. Unlike traditional workflow-based systems, these agents **self-organize through conversation** to handle startup operations organically.

**Key Philosophy**: We're simulating how a real early-stage startup works - chaotic, undefined, everyone doing everything - not optimizing a mature company's operations.

---

## Quick Start

### 1. Install Dependencies

```bash
cd autogen-agents
pip install -r requirements.txt
```

### 2. Set Up Environment

```bash
# Copy the example environment file
cp .env.example .env

# Edit .env and add your OpenAI API key
# OPENAI_API_KEY=sk-...
```

### 3. Run Your First Scenario

```bash
# Run a predefined crisis scenario
python run_scenario.py --scenario crisis

# Or run a custom scenario
python run_scenario.py --custom "A potential investor just emailed asking for our pitch deck. We don't have one. What do we do?"
```

---

## How It Works

### The Team

**You have 4 agents:**

1. **Alice** - Product + Code + Support generalist
2. **Bob** - Marketing + Ops + Data generalist
3. **Charlie** - Customer Success + Ops + Documentation generalist
4. **Founder** - You (strategic guidance, final decisions)

**Important**: These are NOT specialists. They're generalists who self-organize based on the task.

### The Conversation Model

When you give the team a task:

1. **Founder initiates** with a problem/question
2. **Agents discuss** in a group chat format
3. **They self-organize**:
   - Volunteer for tasks they're suited for
   - Ask each other questions
   - Debate approaches
   - Reach conclusions organically
4. **Conversation terminates** when:
   - Task is complete
   - Max rounds reached (50)
   - Founder terminates manually

**This is messy by design** - it's how real startups work!

---

## Interaction Patterns

### Will Agents Ask You for Guidance?

**It depends on the scenario.**

**If you use `human_input_mode="NEVER"`** (current default):
- Agents discuss among themselves
- Founder agent is AI-powered
- Fully autonomous (you observe)
- Good for: Seeing how agents self-organize without human intervention

**If you change to `human_input_mode="ALWAYS"`**:
- Agents will pause and ask for your input
- You participate in the conversation
- More realistic human-in-loop
- Good for: Actually running the company, not just observing

**If you use `human_input_mode="TERMINATE"`** (recommended for most cases):
- Agents work autonomously
- But you can type input to jump in anytime
- Type "exit" to let them continue without you
- Good for: Observing but intervening when needed

### How to Change Interaction Mode

Edit `team_config.py`:

```python
FOUNDER_CONFIG = {
    "name": "Founder",
    "human_input_mode": "TERMINATE",  # Change this
    # Options: "NEVER", "ALWAYS", "TERMINATE"
}
```

### How to Kickstart a Scenario

**Option 1: Use predefined scenarios**

```bash
python run_scenario.py --scenario crisis
python run_scenario.py --scenario planning
python run_scenario.py --scenario operations
python run_scenario.py --scenario strategy
python run_scenario.py --scenario opportunity
```

**Option 2: Create custom scenarios**

```bash
python run_scenario.py --custom "Your scenario description here"
```

**Option 3: Interactive mode** (coming soon)

```bash
python interactive_session.py
# Then type scenarios in real-time
```

---

## Understanding What Happens

### Step-by-Step Conversation Flow

**1. You initiate a scenario**
```bash
python run_scenario.py --scenario crisis
```

**2. Founder agent sees the problem**
```
SCENARIO: Customer tweeted we lost their data...
```

**3. Agents start discussing**
```
Alice: "I'll investigate the data loss issue. Let me check our logs..."

Bob: "While Alice investigates, I'll draft a public response. We should acknowledge quickly."

Charlie: "I can reach out to the customer directly via DM to help recover their data."

Alice: [simulates investigation] "Found the issue - it's a sync bug when users have >1000 items..."

Bob: "Here's my draft tweet: [shares text]. Too defensive?"

Charlie: "Yeah, be more direct. Try this: [revised version]"

Alice: "I'm deploying a fix now. Charlie, once it's live, can you verify with the customer?"

[Conversation continues until resolved]
```

**4. Conversation terminates when:**
- Agents agree the task is done
- Someone says "TERMINATE"
- Max rounds reached
- You intervene (if human-in-loop mode)

### What You'll See in the Output

```
================================================================================
MIDDLING COMPANY - AGENT TEAM CONVERSATION
================================================================================

SCENARIO:
[Your scenario description]

================================================================================

CONVERSATION START:

Founder (to chat_manager):
[Initial message]

Alice (to chat_manager):
[Alice's response]

Bob (to chat_manager):
[Bob's response]

...

================================================================================
CONVERSATION END
================================================================================
```

### Observing vs Participating

**Observer Mode** (default):
- You watch what happens
- Agents self-organize completely
- Good for research/learning
- No interruptions needed

**Participant Mode**:
- Change `human_input_mode` to `"ALWAYS"` or `"TERMINATE"`
- Agents will prompt you for input
- You guide decisions in real-time
- Good for actually running operations

---

## Available Scenarios

### Crisis
Customer emergency requiring immediate response and investigation.

**What to observe:**
- How do agents divide work?
- Who takes ownership?
- Do they ask clarifying questions?

### Opportunity
Time-sensitive market opportunity requiring quick decision.

**What to observe:**
- Do they debate approach?
- How do they balance speed vs quality?
- Who drives to conclusion?

### Planning
Strategic planning with multiple options and tradeoffs.

**What to observe:**
- Can agents reach consensus?
- Do they challenge each other?
- How do they prioritize?

### Operations
Multiple competing priorities requiring triage.

**What to observe:**
- How do they prioritize?
- Do they split work effectively?
- Can they handle parallel tasks?

### Strategy
Long-term decision with ambiguous right answer.

**What to observe:**
- Quality of debate?
- Do they consider multiple perspectives?
- How do they decide when there's no clear answer?

---

## Cost Management

### Token Usage & Provider Options

AutoGen conversations use tokens (costs money). We support multiple providers for maximum cost control:

**🎯 Recommended: OpenRouter with cheap OSS models**

**Provider Comparison:**

| Provider | Model | Cost per 1M tokens | 1000 scenarios | Notes |
|----------|-------|-------------------|----------------|-------|
| **OpenRouter** | qwen/qwen-2.5-72b | **$0.50** | **$5-10** | ⭐ **RECOMMENDED** - Chinese OSS, ultra-cheap |
| **OpenRouter** | llama-3.1-70b | **$0.60** | **$6-12** | Open source, excellent quality |
| **OpenRouter** | mistral-large | $2 | $20-40 | Good middle ground |
| OpenAI | gpt-4o-mini | $150 | $150-300 | Standard option |
| OpenAI | gpt-4o | $2,500 | $2,500+ | Expensive |
| Anthropic | claude-3-haiku | $250 | $250-500 | Good quality |

**🔥 Cost Savings: Using Qwen 2.5 saves 300x compared to GPT-4o!**

**Your $500-1000/month budget:**
- With Qwen 2.5: **50,000-100,000 scenarios/month** ✅
- With GPT-4o-mini: **1,500-3,000 scenarios/month** ✅
- With GPT-4o: **150-200 scenarios/month** ⚠️

### How to Switch Providers

**Option 1: Use OpenRouter (Recommended)**

Edit `.env`:
```bash
MODEL_PROVIDER=openrouter
OPENROUTER_API_KEY=your-key-here
DEFAULT_MODEL=qwen/qwen-2.5-72b-instruct

# Or try other cheap models:
# DEFAULT_MODEL=meta-llama/llama-3.1-70b-instruct
# DEFAULT_MODEL=mistralai/mistral-large
```

**Option 2: Use OpenAI**

Edit `.env`:
```bash
MODEL_PROVIDER=openai
OPENAI_API_KEY=your-key-here
DEFAULT_MODEL=gpt-4o-mini
```

**Option 3: Use Anthropic**

Edit `.env`:
```bash
MODEL_PROVIDER=anthropic
ANTHROPIC_API_KEY=your-key-here
DEFAULT_MODEL=claude-3-haiku
```

**You can switch anytime** - just change the `.env` file and restart!

### Additional Cost Controls

**1. Set max_round limits**:
```python
# In team_config.py
GROUP_CHAT_CONFIG = {
    "max_round": 50,  # Prevent infinite conversations
}
```

**2. Monitor costs**:
- OpenRouter: Check dashboard at openrouter.ai
- OpenAI: Check usage.openai.com
- Track per-scenario costs in your learnings

**3. Use TERMINATE strategically**:
- Agents should say "TERMINATE" when done
- Prevents unnecessary back-and-forth
- Saves tokens

**4. A/B test model quality vs cost**:
- Run same scenario on Qwen vs GPT-4o-mini
- Document quality differences
- Find the sweet spot

### Estimated Costs by Model

**Using Qwen 2.5 (OpenRouter):**

| Scenario Type | Rounds | Est. Tokens | Est. Cost |
|---------------|--------|-------------|-----------|
| Simple crisis | 10-15 | 5,000 | **$0.0025** |
| Planning | 20-30 | 10,000 | **$0.005** |
| Strategy debate | 30-50 | 15,000 | **$0.0075** |

**Using GPT-4o-mini (OpenAI):**

| Scenario Type | Rounds | Est. Tokens | Est. Cost |
|---------------|--------|-------------|-----------|
| Simple crisis | 10-15 | 5,000 | $0.75 |
| Planning | 20-30 | 10,000 | $1.50 |
| Strategy debate | 30-50 | 15,000 | $2.25 |

**Recommendation**: Start with Qwen 2.5 on OpenRouter. If quality isn't good enough, try Llama 3.1 or upgrade to GPT-4o-mini for specific scenarios.

---

## What You'll Learn

### Expected Insights

**Week 1-2:**
- Do agents self-organize or get stuck?
- What roles emerge naturally?
- When do conversations reach conclusions vs loop?

**Month 1:**
- What coordination patterns work?
- When do agents need human intervention?
- What's the cost of unstructured collaboration?

**Month 3:**
- What should become workflows (move to CrewAI)?
- What should stay conversational?
- How does startup chaos mature into process?

### Document Everything

Create `/autogen-agents/learnings/` and document:

- **Patterns observed**: What emerges repeatedly?
- **Failure modes**: When do conversations fail?
- **Human triggers**: When did you need to intervene?
- **Cost data**: What scenarios are expensive?
- **Emergent roles**: What job titles appeared naturally?

---

## Troubleshooting

### "No module named autogen"
```bash
pip install pyautogen
```

### "OpenAI API key not found"
```bash
# Make sure .env exists with OPENAI_API_KEY set
cp .env.example .env
# Edit .env and add your key
```

### "Conversation never terminates"
- Check `max_round` setting in `team_config.py`
- Agents should say "TERMINATE" when done
- You can kill the process (Ctrl+C) and adjust

### "Too expensive!"
- Use `gpt-4o-mini` instead of `gpt-4`
- Lower `max_round` limit
- Monitor OpenAI dashboard

### "Agents repeat themselves"
- This can happen - it's emergent behavior
- Document it as a learning
- Try adjusting system messages
- Consider it realistic (humans repeat too!)

---

## Next Steps

### Week 1: Experiment
1. Run all 5 predefined scenarios
2. Observe what happens
3. Document patterns in `/learnings/week1.md`

### Week 2: Custom Scenarios
1. Create your own realistic startup scenarios
2. Test edge cases
3. Find failure modes

### Week 3-4: Refinement
1. Adjust agent system messages based on learnings
2. Add new scenarios based on what you discover
3. Start comparing to how you'd handle it as a human

### Month 2-3: Patterns
1. What roles emerged?
2. What coordination mechanisms work?
3. When should structure be introduced?

### Month 3+: Maturation
1. Identify repetitive tasks
2. Consider CrewAI for workflows
3. Keep strategy conversational
4. Document the transition

---

## File Structure

```
autogen-agents/
├── README.md                 # This file
├── requirements.txt          # Python dependencies
├── .env.example             # Environment template
├── .env                     # Your API keys (git-ignored)
├── team_config.py           # Agent definitions
├── run_scenario.py          # Main script
├── learnings/               # Document your observations
│   ├── week1.md
│   ├── week2.md
│   └── patterns.md
└── scenarios/               # Custom scenarios (create as you go)
    └── custom_scenarios.py
```

---

## Philosophy Reminder

**This is NOT about efficiency.** It's about understanding:

- Can agents self-organize like humans?
- What patterns emerge from chaos?
- When does conversation beat workflow?
- How do startups mature from messy to structured?

**Embrace the messiness.** That's the point.

---

## Support

- **Issues**: Open a GitHub issue in the main repo
- **Questions**: Check `/research/framework-decision-autogen-vs-crewai.md` for context
- **Learning**: Document everything in `/learnings/`

---

## Key Differences from Traditional Approaches

| Traditional (CrewAI) | Middling (AutoGen) |
|---------------------|-------------------|
| Predefined workflows | Emergent coordination |
| Specialists with narrow roles | Generalists with broad skills |
| Task assignments | Volunteer ownership |
| Optimized efficiency | Realistic chaos |
| Clear accountability | Negotiated ownership |
| Best for mature orgs | Best for early startups |

**We chose AutoGen because we're simulating Day 1 startup reality, not Year 5 operations.**

---

## What Makes This Different

**Most AI agent frameworks:**
- Assume you know the workflow
- Require predefined roles
- Optimize for efficiency
- Best for structured problems

**This approach:**
- Assumes you DON'T know the workflow yet
- Lets roles emerge from conversation
- Accepts inefficiency as realistic
- Best for ambiguous startup problems

**The "weakness" is the feature.**

---

*For detailed decision rationale, see `/research/framework-decision-autogen-vs-crewai.md`*
