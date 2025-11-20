# 🧠 Agentic Startup Setup for Bullspin Detector (Autogen MVP)

**Date**: November 20, 2025
**Timeline**: 1-week MVP sprint → Copenhagen presentation
**Framework**: AutoGen (conversational agents)
**Target**: Drive 1 real user signup via organic Reddit engagement

---

## 🎯 Objective

**Simulate the feel of an early-stage startup team using AI agents.**

- **Focus**: Coordination, delegation, and learning—not automation
- **Learning goal**: Observe how agents self-organize around a real growth task
- **Success metric**: **1 user signup** for Bullspin Detector via Reddit
- **Secondary goal**: Generate conversation logs for Copenhagen presentation

**Why Bullspin Detector?**
- Real mini-app (not hypothetical)
- Clear value proposition (detect political BS)
- Natural Reddit audience (r/politics, r/AskPolitics, r/NeutralPolitics)
- Trackable outcome (signups)

---

## 🧱 Agent Architecture (MVP Stack)

### 1. Supervisor Agent (Roland - You)
- **Role**: Orchestrates workflow, ensures mission alignment
- **Mission**: Drive early traction for Bullspin Detector through Reddit outreach
- **Behavior**:
  - Assigns tasks to specialist agents
  - Requests clarification when needed
  - Makes final judgment calls
  - Keeps conversation logs coherent
- **Implementation**: `UserProxyAgent` with `human_input_mode="TERMINATE"`

### 2. Research Agent
- **Role**: Finds relevant Reddit threads discussing political proposals
- **Input**:
  - Current events (e.g., "Trump tariff proposals")
  - Subreddit lists (r/politics, r/AskPolitics, r/NeutralPolitics)
  - Optional keywords
- **Output**:
  - Thread URLs
  - Thread summaries
  - Relevance scores
  - Recommended engagement approach
- **Tools**: Web search, Reddit API (or manual with web search)

### 3. Writer Agent
- **Role**: Writes thoughtful, human-like Reddit comments with Bullspin link
- **Constraints**:
  - Avoid spammy tone
  - Inject link naturally
  - Provide genuine value (not just promotion)
  - Follow Reddit etiquette (no self-promotion spam)
- **Uses**: Prewritten positioning blurb for Bullspin Detector
- **Output**: Draft comment for human review

### 4. Tracker Agent
- **Role**: Detects and logs click-throughs or signups using trackable links
- **Output**:
  - Logs of clicks/signups
  - Notifications of impact (e.g., "Signup confirmed from r/AskPolitics")
  - Attribution data (which thread, which comment)
- **Tools**: Bitly or UTM parameters + analytics check

### 5. User Proxy Agent ("Roland")
- **Role**: Human-in-the-loop for final judgment and edits
- **Mode**: `TERMINATE` (agents wait for your review before posting)
- **Why**:
  - Reddit requires authentic human voice
  - Avoid spam/ban risk
  - Learn from agent drafts but maintain control

---

## 🖥️ How It Runs

### Environment
- **Primary**: Jupyter Notebook (`bullspin_mvp.ipynb`)
- **Alternative**: Python script (`bullspin_agents.py`)

### Execution Flow
1. **Manual trigger** (for now): Run notebook cell or script
2. **Supervisor initiates**: "Find 3 relevant Reddit threads about [current topic]"
3. **Research agent** searches and reports back
4. **Supervisor** selects 1-2 threads
5. **Writer agent** drafts comments
6. **Roland (you)** reviews and approves/edits
7. **Manual posting** (agents don't actually post - you do)
8. **Tracker agent** monitors for signups

### Persistence
- **All messages** stored in `groupchat.messages`
- **Logs exported** to `.json`, `.md`, or `.txt` for permanent reference
- **Learnings documented** in `/learnings/` directory

### Scaling Up (Future)
- Cron-triggered daily research
- Slack-activated bot
- Automated tracking dashboard
- Integration with analytics

---

## 🧩 Directory Structure

```
bullspin-detector/
├── README.md                       # This file
├── agentic/
│   ├── bullspin_mvp.ipynb         # Primary notebook - START HERE
│   ├── bullspin_agents.py         # Modular agent definitions
│   ├── config.py                  # Bullspin-specific config
│   ├── logs/
│   │   ├── run-001.md             # Agent conversation logs
│   │   ├── run-001.json
│   │   └── run-002.md
│   ├── tracker/
│   │   ├── links.py               # Bitly or UTM wrapper
│   │   └── analytics.py           # Signup tracking
│   └── prompts/
│       └── bullspin-positioning.md # Prewritten messaging
├── slides/
│   ├── bullspin-presentation.md   # MARP slide deck
│   └── assets/
│       └── conversation-logs/     # Excerpts for slides
└── learnings/
    └── week1-bullspin.md          # Observations from this experiment
```

---

## 🎞 Presentation Framework (MARP-Compatible)

A Markdown slide deck using [MARP](https://marp.app/), compatible with VS Code or GitHub rendering.

**File**: `slides/bullspin-presentation.md`

### Sections (Outline)

1. **Title Slide**: _Simulating a Startup with AI Agents_
2. **Why Agentic Startups?**
   - Early-stage chaos requires organic coordination
   - Conversation-based > workflow-based
3. **Use Case: Bullspin Detector**
   - What it is (political proposal fact-checker)
   - Why it's perfect for this experiment
4. **What We Built** (Autogen + Agent Roles)
   - Supervisor, Research, Writer, Tracker, Human
5. **Agent Org Chart** (visual)
6. **Sample Conversation** (log excerpts)
   - Real messages from `groupchat.messages`
   - Show self-organization
7. **What Worked**
   - Agents found relevant threads
   - Drafted natural-sounding comments
   - Coordinated without predefined workflow
8. **What Didn't Work / Human Still Needed**
   - Final judgment on Reddit etiquette
   - Avoiding spam tone
   - Understanding cultural context
9. **Key Learnings**
   - When conversation beats workflow
   - Where humans add unique value
   - Cost of organic vs automated
10. **Call to Action / Thanks**

### How to Generate Slides

```bash
# Install MARP CLI
npm install -g @marp-team/marp-cli

# Generate slides
cd slides
marp bullspin-presentation.md -o bullspin-presentation.pdf
marp bullspin-presentation.md -o bullspin-presentation.html
```

**Or use VS Code MARP extension** for live preview.

---

## 📦 Implementation Checklist

### Week 1 (Before Copenhagen)

**Day 1-2: Setup**
- [x] Create directory structure
- [ ] Set up `bullspin_mvp.ipynb` notebook
- [ ] Define 4 specialist agents + supervisor
- [ ] Test basic conversation flow
- [ ] Create trackable links (Bitly + UTM)

**Day 3-4: Execute**
- [ ] Run Research agent on current political topics
- [ ] Generate 3-5 comment drafts
- [ ] Human review and post 1-2 comments
- [ ] Monitor for signups

**Day 5-6: Document & Prepare**
- [ ] Export conversation logs
- [ ] Create MARP slide deck
- [ ] Populate slides with real conversation excerpts
- [ ] Document learnings in `/learnings/week1-bullspin.md`

**Day 7: Practice**
- [ ] Rehearse presentation
- [ ] Refine based on what actually happened
- [ ] Prepare for questions

---

## 🔗 Connection to Main AutoGen Framework

This Bullspin experiment is a **specific implementation** of the general AutoGen framework at `/autogen-agents/`.

**Differences:**
- **Purpose**: Real product growth task (not exploration)
- **Agents**: Specialized for Reddit engagement (not generalist startup employees)
- **Output**: Tangible (signup) vs observational (learnings)
- **Timeline**: 1 week sprint vs ongoing operation

**Similarities:**
- **Framework**: AutoGen conversation-based
- **Philosophy**: Agents self-organize, human-in-loop
- **Documentation**: Log everything, extract patterns
- **Cost control**: OpenRouter, cheap models

---

## 🎯 Success Metrics

### Primary
- [ ] **1 user signup** for Bullspin Detector attributed to Reddit
- [ ] **Conversation logs** exported and ready for presentation
- [ ] **Presentation deck** completed with real examples

### Secondary
- [ ] Agents found 5+ relevant Reddit threads
- [ ] Drafted 5+ natural-sounding comments
- [ ] Self-organized without predefined workflow
- [ ] Human intervention points documented
- [ ] Cost tracked (should be <$5 for week)

### Learning Metrics
- [ ] What roles emerged? (Research, Writing, Tracking)
- [ ] Did agents coordinate effectively?
- [ ] Where was human judgment critical?
- [ ] What surprised you about agent behavior?

---

## 🧪 Experiment Design

### Hypothesis
Conversational agents can coordinate on a real growth task (Reddit outreach) more organically than a predefined workflow, while still requiring human judgment for authenticity.

### Variables
- **Independent**: Agent architecture (conversation-based)
- **Dependent**: Signup rate, comment quality, coordination effectiveness
- **Control**: Human-written Reddit comments (compare)

### Data Collection
- Agent conversation logs
- Comment drafts (accepted/rejected)
- Human intervention points
- Signup attribution
- Cost per signup

### Analysis
Compare:
- Agent-drafted vs human-drafted comments
- Time spent with agents vs without
- Quality of thread selection
- Coordination efficiency

---

## 💡 Agent Prompts (Sketches)

### Supervisor Agent
```
You are the supervisor of a small startup team working on Bullspin Detector,
a tool that fact-checks political proposals.

Your mission this week: Drive 1 user signup via Reddit engagement.

Your team:
- Research Agent: Finds relevant Reddit threads
- Writer Agent: Drafts engagement comments
- Tracker Agent: Monitors signups

Coordinate the team to find threads, draft comments, and track results.
Ask clarifying questions. Make judgment calls. Keep the mission on track.
```

### Research Agent
```
You're the Research Agent. Your job: find relevant Reddit threads where
Bullspin Detector would add value.

Look for threads about political proposals, fact-checking, or policy debates.
Focus on: r/politics, r/AskPolitics, r/NeutralPolitics

For each thread, provide:
1. URL
2. Summary
3. Why it's relevant
4. Recommended approach

Prioritize recent, active threads with genuine discussion (not just news links).
```

### Writer Agent
```
You're the Writer Agent. Your job: draft thoughtful Reddit comments that
naturally introduce Bullspin Detector.

Guidelines:
- Provide genuine value first (insight, fact-check, perspective)
- Mention Bullspin naturally ("I've been using..." or "You might like...")
- Include trackable link
- Avoid spam tone
- Follow Reddit etiquette (contribute, don't just promote)

Draft comments for human review before posting.
```

### Tracker Agent
```
You're the Tracker Agent. Your job: monitor signups and attribute them
to specific Reddit threads.

Create trackable links for each comment:
- Use Bitly or UTM parameters
- Format: bullspin.app?utm_source=reddit&utm_campaign=thread-id

Monitor analytics and report:
- Clicks per thread
- Signups per thread
- Best performing threads

Alert when signups happen!
```

---

## 🚀 Next Steps

### Immediate (Today)
1. Set up notebook with agent definitions
2. Test basic conversation flow
3. Create trackable links

### This Week
1. Run research on current topics (e.g., Trump tariffs, policy debates)
2. Draft 5 comments with agent help
3. Post 1-2 after human review
4. Monitor for signups
5. Document everything

### Copenhagen Presentation
1. Export conversation logs
2. Create MARP slides with real examples
3. Practice telling the story
4. Prepare for questions:
   - "Did it work?" (Did you get a signup?)
   - "What did agents do well/poorly?"
   - "Where was human judgment critical?"
   - "What would you do differently?"

---

## 📚 Resources

- **AutoGen Docs**: https://microsoft.github.io/autogen/
- **MARP**: https://marp.app/
- **Reddit API**: https://www.reddit.com/dev/api/
- **Bitly**: https://bitly.com/
- **Main AutoGen Setup**: `/autogen-agents/`

---

## 🤔 Open Questions

- Should agents actually post to Reddit, or just draft? (Recommend: draft only)
- How to handle Reddit rate limits and etiquette?
- What if we don't get a signup in 1 week? (Still valuable learnings!)
- Should we A/B test agent-drafted vs human-drafted comments?
- How to avoid ban/spam detection on Reddit?

---

## 🎓 Learning Goals

### For Copenhagen Presentation
- Demonstrate real agent coordination on real task
- Show conversation logs (not hypothetical)
- Discuss what worked and what didn't
- Articulate where humans are still needed
- Cost-benefit analysis of agent assistance

### For Consulting Practice
- Proof of concept for conversational agents
- Real-world example of organic coordination
- Learnings about human-agent collaboration
- Framework for other client use cases

---

_This is a living document. Update as you run the experiment._

**Last updated**: November 20, 2025
