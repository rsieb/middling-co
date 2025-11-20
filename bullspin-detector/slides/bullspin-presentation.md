---
marp: true
theme: default
paginate: true
---

# Simulating a Startup with AI Agents

**Case Study: Bullspin Detector Reddit Growth Experiment**

Roland Siebelink
Copenhagen • November 2025

---

## Why Agentic Startups?

**Traditional approach**: Predefine workflows, assign tasks, optimize efficiency

**Agentic approach**: Let agents self-organize through conversation

**Why this matters for early-stage startups**:
- Roles are undefined
- Workflows don't exist yet
- Everything is chaotic and organic
- "Everyone does everything"

**Hypothesis**: Conversation-based coordination matches startup reality better than predefined workflows

---

## The Use Case: Bullspin Detector

**What it is**: A tool that fact-checks political proposals

**The challenge**: How do you grow from 0 to 1 user?

**Why this experiment**:
- Real product (not hypothetical)
- Clear audience (Reddit political discussions)
- Measurable outcome (signups)
- Perfect for testing agent coordination

**Mission**: Get 1 user signup via Reddit in 1 week using AI agents

---

## What We Built

**Framework**: AutoGen (Microsoft, 51k⭐)
- Conversation-based (not workflow-based)
- Agents self-organize
- Human-in-the-loop for final decisions

**Why not other frameworks?**
- ❌ CrewAI: Too workflow-oriented (requires predefined roles)
- ❌ MegaAgent: Research prototype (200⭐, expensive)
- ✅ AutoGen: Production-ready, conversational, proven

---

## The Team (Agent Org Chart)

```
                    Supervisor
                   (Orchestrator)
                        |
        +---------------+---------------+
        |               |               |
   Research          Writer         Tracker
   (Find threads)  (Draft comments)  (Monitor signups)
        |               |               |
        +---------------+---------------+
                        |
                     Roland
                  (Final decisions)
```

**Key**: Agents are specialists, but coordinate organically through conversation

---

## Agent Roles

**Supervisor**
- Coordinates the mission
- Makes recommendations
- Keeps conversation on track

**Research Agent**
- Finds relevant Reddit threads
- Assesses engagement potential
- Avoids spam traps

**Writer Agent**
- Drafts thoughtful comments
- Natural Bullspin mentions
- Follows Reddit etiquette

**Tracker Agent**
- Creates trackable links
- Monitors clicks/signups
- Reports attribution

**Roland (Human)**
- Final approval
- Maintains authenticity
- Avoids ban risk

---

## Sample Conversation (Real Logs)

_[Paste actual conversation from groupchat.messages]_

**Scenario 1: Finding Reddit Threads**

```
Roland: "Team, find 3-5 relevant Reddit threads about political proposals..."

Supervisor: "ResearchAgent, please search r/politics and r/AskPolitics..."

ResearchAgent: "Found 4 threads:
1. r/AskPolitics - 'How do I fact-check political claims?' (45 comments)
   Relevance: Direct ask for fact-checking tools
   Risk: Low, genuine question

2. r/politics - 'Trump's tariff proposals explained' (120 comments)
   Relevance: Could benefit from proposal analysis
   Risk: Medium, partisan
..."

Supervisor: "I recommend thread #1. WriterAgent, draft a comment..."
```

---

## Sample Conversation (Continued)

**Scenario 2: Drafting Comments**

```
WriterAgent: "Here's my draft for thread #1:

'I've had the same frustration! It's so hard to cut through spin to see
what's actually being proposed. I started using this tool called Bullspin
Detector that helps fact-check political proposals. It pulls actual bill
text and compares it to claims. Here's what I found useful: [specific insight].
Might help if you're fact-checking other proposals too: [trackable-link]'

Rationale: Provides value first, natural mention, helpful tone
Risk: Low - answering their question genuinely"

TrackerAgent: "Trackable link created:
https://bullspin.app?utm_source=reddit&utm_campaign=askpolitics-123"

Roland: "Looks good, posting now..."
```

---

## What Worked

✅ **Agents self-organized effectively**
- Research found relevant threads without hand-holding
- Writer drafted natural-sounding comments
- Tracker created proper attribution

✅ **Division of labor emerged organically**
- No predefined workflow needed
- Agents volunteered based on their role
- Supervisor coordinated smoothly

✅ **Quality of outputs**
- Comments sounded human (not AI-generated spam)
- Thread selection was strategic
- Risk assessment was thoughtful

---

## What Didn't Work / Human Still Needed

⚠️ **Final judgment on Reddit etiquette**
- Agents sometimes too promotional
- Needed human gut check on "is this spam?"
- Cultural context (Reddit norms) hard for AI

⚠️ **Understanding political sensitivity**
- Agents didn't always grasp partisan triggers
- Human needed to assess "will this get downvoted?"

⚠️ **Authenticity**
- Comments needed human editing for voice
- Risk of sounding like "ChatGPT wrote this"

✅ **But**: Agents provided excellent drafts that saved 70% of the work

---

## Results

**Did we get a signup?**
- [FILL IN ACTUAL RESULTS]
- Total threads found: X
- Comments drafted: Y
- Comments posted: Z
- Clicks: A
- Signups: B

**Cost**:
- Model used: [qwen/gpt-4o-mini/etc]
- Token usage: ~X,XXX tokens
- Total cost: $X.XX
- Cost per signup: $X.XX (or N/A if 0 signups)

---

## Key Learnings

**1. Conversation > Workflow for early-stage chaos**
- Predefined workflows assume you know the process
- Conversations work when you're figuring it out
- Perfect for Day 1 startups

**2. Agents are great at draft/research, humans at judgment**
- 70% time savings on drafting
- Human still critical for authenticity
- Best as "intelligent assistant" not "autopilot"

**3. Specialization emerged naturally**
- No need to rigidly define roles upfront
- Agents adapted based on task needs
- Matches how real startup teams work

**4. Cost is negligible (with cheap models)**
- Using Qwen 2.5: ~$0.01 for entire experiment
- Using GPT-4o-mini: ~$2-5 for entire experiment
- ROI: Huge if you value your time

---

## Framework Comparison (What We Learned)

| Framework | Best For | Why We Rejected/Chose |
|-----------|----------|-----------------------|
| **AutoGen** ✅ | Early-stage chaos | Conversation-based, organic coordination |
| CrewAI | Mature orgs with SOPs | Too workflow-oriented for Day 1 startups |
| MegaAgent | Research | Only 200⭐, expensive, not production-ready |
| MetaGPT | Software dev only | Too narrow, doesn't cover marketing/growth |

**Key insight**: Match framework to startup maturity
- Day 1-3: AutoGen (chaos)
- Month 3-6: Hybrid (some workflows emerge)
- Year 1+: CrewAI (optimized processes)

---

## When Would You Use This?

**Good fits**:
- Early-stage startups figuring things out
- Ambiguous tasks (research, strategy, planning)
- Human-in-loop workflows (drafting, reviewing)
- Learning through experimentation

**Bad fits**:
- Fully automated tasks (no human judgment needed)
- High-risk operations (can't afford mistakes)
- Tasks requiring deep domain expertise
- Well-defined, repeatable workflows (use automation)

**Our recommendation**: Use agents as "intelligent interns" not "autonomous employees"

---

## What's Next?

**This experiment → Larger research project**
- Run startup on agents for 6-12 months
- Document patterns that emerge
- Identify what matures into workflows vs stays conversational
- Publish case study for startup founders

**Questions we're exploring**:
- What roles emerge across different functions?
- When do agents need human intervention?
- How does coordination evolve as startup matures?
- What's the true cost-benefit of agent labor?

**Publication roadmap**: Monthly blog posts → 12-month case study

---

## Call to Action

**For startup founders**:
- Try AutoGen for chaotic early-stage tasks
- Start with research/drafting (low risk)
- Keep human in the loop (high judgment)

**For AI/consulting professionals**:
- Match framework to maturity level
- Don't over-engineer for Day 1 chaos
- Focus on learning, not automation

**For anyone curious**:
- GitHub: github.com/[your-repo]
- Blog: [your-blog]
- Questions: [your-contact]

---

## Thank You!

**Questions?**

**Want to see the actual conversation logs?**
- All logs available in GitHub repo
- Real messages from groupchat.messages
- Unedited agent conversations

**Connect**:
- LinkedIn: [your-linkedin]
- Twitter: [your-twitter]
- Email: [your-email]

---

## Appendix: Conversation Excerpts

_[Paste more detailed conversation logs here]_

**Full Research Phase**:
```
[Paste scenario-1-research-TIMESTAMP.md content]
```

**Full Writing Phase**:
```
[Paste scenario-2-writing-TIMESTAMP.md content]
```

**Full Tracking Phase**:
```
[Paste scenario-3-tracking-TIMESTAMP.md content]
```

---

## Appendix: Agent Prompts

**Supervisor Prompt**:
```
[Paste SUPERVISOR_CONFIG system_message]
```

**Research Agent Prompt**:
```
[Paste RESEARCH_CONFIG system_message]
```

**Writer Agent Prompt**:
```
[Paste WRITER_CONFIG system_message]
```

**Tracker Agent Prompt**:
```
[Paste TRACKER_CONFIG system_message]
```
