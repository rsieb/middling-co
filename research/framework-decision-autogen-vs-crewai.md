# Framework Decision: AutoGen vs CrewAI for Middling Company

**Date**: November 20, 2025
**Status**: DECISION MADE - AutoGen selected
**Previous Approach**: GitHub-native with predefined agents (see agent-framework-analysis.md)
**New Approach**: Conversational agents with organic self-organization

---

## Executive Summary

**Decision: Use AutoGen as the primary framework for Middling Company operations.**

**Reasoning**:
- Early-stage startups are inherently chaotic, undefined, and organic
- Agents should self-organize like real startup employees, not follow predefined workflows
- We're simulating startup reality, not optimizing operational efficiency
- Conversational model (AutoGen) matches actual startup behavior better than team-based workflows (CrewAI)

**Key Insight**: The "messiness" of conversation-based coordination is a feature, not a bug, when simulating real startups.

---

## The Core Question

**What are we actually trying to do?**

❌ NOT: Automate a mature company's operations efficiently
✅ YES: Simulate how a real early-stage startup actually works

This reframing changes everything.

---

## Framework Comparison: Team-Based vs Conversation-Based

### The Fundamental Difference

| Dimension | **Team-Based (CrewAI)** | **Conversation-Based (AutoGen)** |
|-----------|------------------------|----------------------------------|
| **Mental Model** | Org chart with job descriptions | Group chat / meeting room |
| **Coordination** | Task assignments and handoffs | Back-and-forth discussion |
| **Structure** | Top-down, predefined workflows | Bottom-up, emergent from dialogue |
| **Control Flow** | You define who does what and when | Agents decide who should speak next |
| **Communication** | Linear handoffs (A→B→C) | Dynamic conversation (A↔B↔C) |
| **Real-World Analog** | Assembly line, RACI matrix | Slack thread, brainstorming session |
| **Predictability** | High (same flow every time) | Low (conversation varies) |
| **Flexibility** | Lower (must predefine tasks) | Higher (adapts dynamically) |
| **Efficiency** | Faster for known processes | Slower (communication overhead) |
| **Token Usage** | Lower (direct handoffs) | Higher (conversational back-and-forth) |
| **Debuggability** | Easier (linear flow) | Harder (emergent behavior) |
| **Best For** | Automating SOPs | Solving novel problems |
| **Failure Mode** | Wrong task sequence | Conversation loops/derails |

---

## Visual Comparison: Same Task, Both Models

### Task: Handle a customer billing complaint

**CrewAI (Team-Based) Execution:**
```
1. Billing Specialist investigates
   ↓ (produces report)
2. Customer Service receives report → drafts response
   ↓ (produces draft)
3. Manager receives draft → approves
   ↓
4. Done
```
**Characteristics**: Linear, predictable, efficient, requires predefined roles

**AutoGen (Conversation-Based) Execution:**
```
Manager: "Customer says they were double-charged. Investigate and respond."
  ↓
BillingSpecialist: "Checking records... Found it - we did double-charge on Jan 15."
  ↓
CustomerService: "@BillingSpecialist what's our refund policy timeline?"
  ↓
BillingSpecialist: "3-5 business days for refunds"
  ↓
CustomerService: "Here's my draft response: [text]. Does this work?"
  ↓
Manager: "Good tone but offer a courtesy credit too. Revise."
  ↓
CustomerService: "Revised: [updated]. Better?"
  ↓
Manager: "Approved. Send it."
```
**Characteristics**: Dynamic, clarifying questions, iteration, emergent order

---

## Why AutoGen Matches Startup Reality

### Real Early-Stage Startup (5am Slack):
```
"Customer is freaking out about billing, someone handle this?"

"I'll look - wait, do we even have access to Stripe dashboard?"

"Yeah I can check... oh crap we double-charged them"

"How do we refund?"

"I think there's a button... trying now..."

"What do we tell the customer?"

"Just say we're fixing it and will confirm in 30 min?"

"Should we offer them a free month or something?"

"Yeah probably, we screwed up"

"Okay sending email now"

"Wait let me read it first"

"Looks good, send it"
```

**This is a conversation, not a workflow.**

### What Startups DON'T Have (That CrewAI Requires):

❌ Clearly defined roles
❌ Standard operating procedures
❌ Predefined task sequences
❌ Clean handoffs between functions
❌ Repeatable workflows
❌ Organizational structure

### What Startups DO Have (That AutoGen Models):

✅ Chaotic coordination
✅ Everyone doing everything
✅ "Figure it out as we go"
✅ Real-time collaboration
✅ Unclear accountability
✅ Messy communication

**AutoGen's "weaknesses" are actually realistic startup features:**

| AutoGen "Weakness" | Startup Reality |
|-------------------|-----------------|
| Conversations can be inefficient | So are real startups! |
| Agents might ask redundant questions | Junior employees do this too |
| Order of operations is unpredictable | Just like real startup chaos |
| Conversations can derail or loop | So do real Slack threads! |
| Higher token costs from back-and-forth | Startup inefficiency is expensive IRL too |
| Less "optimized" than workflows | Startups aren't optimized, they're scrappy |

---

## When Each Model Shines

### CrewAI (Team-Based) Is Better When:

✅ **Workflow is known and repeatable**
- "Every support ticket: triage → respond → QA"
- You want predictability and consistency

✅ **Handoffs are clean**
- Agent A produces complete artifact → Agent B consumes it
- Like an assembly line

✅ **You want tight control**
- "Billing must always happen before customer communication"
- Compliance, audit requirements

✅ **Parallel execution makes sense**
- "Five researchers each take a different competitor"

✅ **Automating processes you already understand**
- You have existing SOPs
- You know what "good" looks like

**Use cases**: Customer support (at scale), content production pipelines, code review workflows

---

### AutoGen (Conversation-Based) Is Better When:

✅ **The problem needs discussion to solve**
- "Should we pivot our product strategy?"
- Requires back-and-forth, debate

✅ **Requirements are unclear upfront**
- "Plan next quarter's roadmap"
- Task unfolds as agents explore

✅ **Human-in-loop is important**
- Human participates in conversation
- Real-time steering of agent work

✅ **Collaboration is messy**
- "Three agents debug a complex issue together"
- Order should emerge from needs

✅ **You want agents to coordinate themselves**
- Don't want to define every handoff
- Agents figure out who should do what

**Use cases**: Strategic planning, root cause analysis, brainstorming, early-stage startup operations

---

## Startup Maturity Spectrum

This reveals a potential insight for publications:

```
DAY 1 STARTUP  →  GROWING STARTUP  →  SCALING COMPANY
   (AutoGen)         (Hybrid)            (CrewAI)

"Slack chaos"      "Some SOPs"         "Defined workflows"
Everyone does      Emerging roles      Clear job descriptions
everything         Some processes      Optimized processes
```

**Research Question**: "As startups mature, do they naturally move from conversation-based to team-based coordination? When should that transition happen?"

**Middling Company Approach**:
- **Months 0-3**: Pure AutoGen (chaos, everything is a discussion)
- **Months 3-6**: Hybrid (some processes emerge, but still messy)
- **Months 6-12**: Introduce CrewAI for repetitive tasks (support, content)

**Publication Angle**: "How do coordination patterns evolve as AI-native startups mature?"

---

## Other Frameworks Considered (From Reddit Thread)

### MegaAgent (200⭐, ACL 2025)
**Approach**: Self-organizing hierarchies, dynamic agent spawning

**Why We Rejected It**:
- ❌ Only 200 stars (vs 50k for AutoGen) = warning sign, not "hidden gem"
- ❌ Research prototype, not production-ready
- ❌ Expensive ($50/task, 25M tokens in examples)
- ❌ Reddit post appears to be promotional/marketing
- ❌ No production usage documented
- ❌ 0 releases, 4 contributors, 31 commits total
- ⚠️ Academic credibility (ACL 2025) doesn't equal production viability

**Key Learning**: Dramatic claims ("found 70 datacenters vs 19!") need verification. Star count matters - 200 vs 50,000 is a 250x difference in community validation.

**When It Might Be Useful**: Research projects, academic exploration, comparing academic vs production frameworks

---

### MetaGPT (59k⭐)
**Approach**: Software development roles (PM/Engineer/QA)

**Why We Rejected It**:
- ❌ Too narrow - only software development
- ❌ Doesn't address marketing, support, finance, operations
- ❌ Fixed roles don't match early startup flexibility

---

### AgentVerse (4.8k⭐)
**Approach**: Boss sets goal → group chat → boss clears and respins roles

**Why We Rejected It**:
- ❌ Agents recreated each round (lose context)
- ❌ No persistence = bad for continuous operations
- ❌ "Clear and respin" antithetical to organizational memory

---

## Final Framework Selection

### Winner: AutoGen (51.8k⭐, Microsoft)

**Why AutoGen**:
1. ✅ **Matches startup chaos** - organic, undefined, messy
2. ✅ **Agents self-organize** - realistic human behavior
3. ✅ **Conversation-based** - how startups actually coordinate
4. ✅ **Microsoft-backed** - production-ready, won't disappear
5. ✅ **51k stars** - massive, proven community
6. ✅ **Human-in-loop native** - UserProxy agent for founder participation
7. ✅ **Best for consulting** - matches client reality (chaos)

**When We'll Add CrewAI**:
- Month 3-6: Once patterns emerge, optimize repetitive tasks
- Example: Support tickets become workflow, strategy stays conversational
- Simulates startup maturation: chaos → process

---

## What We'll Actually Learn (That We Couldn't with CrewAI)

### With CrewAI (Team-Based):
- Can we automate well-defined processes?
- How to optimize workflows?

### With AutoGen (Conversation-Based):
- ✅ **Can agents handle ambiguity** like startup employees?
- ✅ **Do they self-organize** around problems?
- ✅ **When do conversations reach conclusions** vs get stuck?
- ✅ **What happens when nobody's role is clearly defined?**
- ✅ **How do agents decide who should do what?**
- ✅ **What's the cost of operating without clear SOPs?**
- ✅ **When does chaos become productive vs wasteful?**
- ✅ **What coordination mechanisms emerge naturally?**

**These are the questions startup founders actually face.**

---

## AutoGen Agent Design: Generalists, Not Specialists

### Wrong Approach (CrewAI-style):
```python
support_specialist = Agent(role="Support Specialist", ...)
marketing_specialist = Agent(role="Marketing Specialist", ...)
engineering_specialist = Agent(role="Engineering Specialist", ...)
```

### Right Approach (AutoGen-style):
```python
alice = AssistantAgent(
    name="Alice",
    system_message="Early employee: product + code + support. Jump in where needed."
)

bob = AssistantAgent(
    name="Bob",
    system_message="Early employee: marketing + ops + data. Wear many hats."
)

charlie = AssistantAgent(
    name="Charlie",
    system_message="Early employee: design + code + customer success. Do what needs doing."
)
```

**Key Difference**: No rigid role boundaries. Agents have broad capabilities and self-select tasks based on conversation.

---

## Real Startup Scenarios to Test

**Scenario 1: Crisis**
```
"Customer tweeted we lost their data. Handle this ASAP."
```
Observe: Who takes what? How do they coordinate? Do they ask for help?

**Scenario 2: Opportunity**
```
"Someone on Reddit asked for exactly what we're building. How should we respond?"
```
Observe: Who drafts? Who reviews? Is there debate?

**Scenario 3: Planning**
```
"We have 2 weeks to launch. What should we build vs cut?"
```
Observe: Do agents reach consensus? Do they challenge each other?

**Scenario 4: Operations**
```
"We have 5 support tickets, a blog post due Friday, and a bug in production. Prioritize."
```
Observe: How do they triage? Who takes ownership?

---

## Expected Challenges (And Why They're Valuable)

### Challenge 1: Conversations Don't Conclude
**What could happen**: Agents debate endlessly
**Real startup equivalent**: Analysis paralysis
**What we'll learn**: When do humans need to step in? What helps reach conclusions?
**Publication**: "Decision-Making Patterns in Agent-Run Startups"

### Challenge 2: Unclear Accountability
**What could happen**: Task falls through cracks
**Real startup equivalent**: "I thought you were handling that?"
**What we'll learn**: How do agents establish ownership?
**Publication**: "Accountability Without Job Descriptions"

### Challenge 3: Inefficiency / Redundant Work
**What could happen**: Duplicated effort
**Real startup equivalent**: Poor communication
**What we'll learn**: What coordination mechanisms emerge naturally?
**Publication**: "The Cost of Chaos: Measuring Inefficiency"

### Challenge 4: Cost (Token Usage)
**What could happen**: Lots of conversation = lots of tokens
**Real startup equivalent**: Meetings are expensive
**What we'll learn**: What's the ROI of discussion vs action?
**Publication**: "Economics of Agent Communication"

---

## Repository Health Comparison

For transparency, here's why we trust AutoGen:

| Metric | MegaAgent | CrewAI | AutoGen |
|--------|-----------|--------|---------|
| **Stars** | 225 | 40,600 | 51,800 |
| **Forks** | 30 | 5,400 | 7,900 |
| **Contributors** | 4 | Many | Many |
| **Commits** | 31 | Active | 3,779 |
| **Releases** | 0 | Yes | Yes |
| **Production Use** | None | 100k+ devs | Enterprise |
| **Backing** | Academic lab | VC-funded | Microsoft |
| **Status** | Research | Production | Production |

**Takeaway**: 250x difference in stars (225 vs 51,800) is a signal, not noise.

---

## Why This Is Better for Consulting Practice

**If we used CrewAI**:
- Learn to automate workflows
- Clients say: "But we don't have workflows yet, we're a startup"
- Insights don't apply to early-stage companies

**Using AutoGen**:
- Learn how agents handle startup chaos
- Clients say: "That's exactly our situation!"
- Insights apply to their reality (messy, undefined, scrappy)

**Better Consulting Positioning**:
- ❌ "We'll help you define agent workflows" (clients don't have workflows)
- ✅ "We'll help you run your startup with AI agents despite the chaos" (clients live in chaos)

---

## Implementation Approach

### Week 1: AutoGen Setup + First Experiments
- Install AutoGen
- Create 3-4 generalist agents (not specialists)
- Run first startup scenarios (crisis, opportunity, planning)
- Document what emerges

### Month 2-3: Observe Patterns
- What roles emerge naturally?
- When do conversations work vs fail?
- What coordination mechanisms appear?
- Where do humans need to intervene?

### Month 3-6: Add Structure Where Patterns Emerge
- If support tickets become repetitive → introduce CrewAI workflow
- Keep strategy/planning conversational (AutoGen)
- Document the transition

### Publication Roadmap
- **Week 2**: "First Week Running a Startup on AutoGen"
- **Month 1**: "Emergent Roles: What Job Titles Appeared Without Being Designed"
- **Month 3**: "When Conversations Beat Workflows (And Vice Versa)"
- **Month 6**: "From Chaos to Process: How AI Startups Mature"
- **Month 12**: "Running a Company on AI Agents: 12-Month Case Study"

---

## Key Decisions Made

1. ✅ **AutoGen as primary framework** (conversation-based)
2. ✅ **Generalist agents** (not role-specialists)
3. ✅ **Embrace messiness** as realistic startup simulation
4. ❌ **Reject MegaAgent** (research prototype, 200 stars, expensive)
5. ⏸️ **Defer CrewAI** to month 3-6 for comparison/maturation
6. ✅ **Focus on learning** over efficiency
7. ✅ **Simulate reality** over optimizing operations

---

## Success Metrics

### Technical Success
- Agents complete real startup tasks without predefined workflows
- Conversations reach conclusions (not loop infinitely)
- Self-organization emerges (agents figure out who does what)
- Cost stays within budget ($500-1000/month)

### Learning Success
- Document 10+ emergent patterns
- Identify when conversations work vs fail
- Understand human intervention triggers
- Create framework for startup maturation

### Publication Success
- 5+ blog posts from learnings
- 1 comprehensive case study (12 months)
- Speaking opportunities at startup events
- Consulting leads from demonstrated expertise

---

## Risks & Mitigations

### Risk 1: Conversations Never Conclude
**Mitigation**: Set max_round limits, human can terminate and decide

### Risk 2: Agents Don't Self-Organize
**Mitigation**: Adjust system messages to encourage ownership, document findings

### Risk 3: Too Expensive (Token Usage)
**Mitigation**: Use cheaper models (GPT-4o-mini), monitor costs, set budgets

### Risk 4: No Patterns Emerge
**Mitigation**: Still valuable - "chaos stays chaotic" is a finding worth publishing

---

## Next Steps

1. ✅ Document this decision (this file)
2. ⏭️ Set up AutoGen in repository
3. ⏭️ Create initial generalist agents
4. ⏭️ Write usage guide for how to work with the agents
5. ⏭️ Run first startup scenario
6. ⏭️ Document observations

---

## References

- AutoGen: https://github.com/microsoft/autogen (51.8k⭐)
- CrewAI: https://github.com/crewAIInc/crewAI (40.6k⭐)
- MegaAgent: https://github.com/Xtra-Computing/MegaAgent (225⭐)
- Reddit Discussion: r/AI_Agents - MegaAgent comparison post

---

*This decision represents a significant pivot from the earlier GitHub-native predefined workflow approach (see agent-framework-analysis.md). The key insight: we're simulating startup reality, not optimizing mature operations.*
