# Week 1 Learnings: Bullspin Detector Reddit Experiment

**Date**: November 20-27, 2025
**Mission**: Drive 1 user signup via Reddit using AutoGen agents
**Timeline**: 1 week before Copenhagen presentation

---

## Experiment Setup

**Agents**:
- Supervisor (orchestrator)
- Research Agent (find threads)
- Writer Agent (draft comments)
- Tracker Agent (monitor signups)
- Roland (human-in-loop)

**Framework**: AutoGen (conversation-based)
**Model**: [qwen-2.5-72b / gpt-4o-mini / etc]
**Cost**: [Fill in]

---

## Day 1-2: Research Phase

### What Happened
[Document what actually happened when you ran the research scenario]

**Threads Found**:
1. [Thread title, subreddit, relevance score]
2. [Thread title, subreddit, relevance score]
3. ...

**Agent Behavior**:
- Did Research Agent find good threads?
- Did Supervisor prioritize effectively?
- How many rounds of conversation?
- Any surprises or failures?

**Human Intervention**:
- Did you need to guide the agents?
- What context was missing?
- Where was human judgment critical?

---

## Day 3-4: Writing Phase

### What Happened
[Document the comment drafting process]

**Comments Drafted**: X
**Comments Approved**: Y
**Comments Posted**: Z

**Quality Assessment**:
- Did comments sound natural?
- Were they too promotional?
- Did they follow Reddit etiquette?
- How much editing did you do?

**Agent Coordination**:
- Did Writer and Tracker coordinate well?
- Did Supervisor keep conversation on track?
- Any coordination failures?

**Examples**:
```
[Paste 1-2 example comment drafts - both good and bad]
```

---

## Day 5-7: Tracking & Results

### Results

**Did we get a signup?**: YES / NO

**If YES**:
- Which thread/comment?
- Time from post to signup?
- Any user feedback?
- What made this one work?

**If NO**:
- Total clicks: X
- Conversion rate: 0%
- Why didn't it work?
- What would you change?

**Attribution Data**:
```
Thread 1 (r/AskPolitics): 15 clicks, 1 signup
Thread 2 (r/politics): 8 clicks, 0 signups
Thread 3 (r/NeutralPolitics): 3 clicks, 0 signups
```

---

## What Worked

### Agent Performance

**Research Agent**:
- ✅ [What worked well?]
- ⚠️ [What was okay?]
- ❌ [What failed?]

**Writer Agent**:
- ✅ [What worked well?]
- ⚠️ [What was okay?]
- ❌ [What failed?]

**Tracker Agent**:
- ✅ [What worked well?]
- ⚠️ [What was okay?]
- ❌ [What failed?]

**Supervisor**:
- ✅ [What worked well?]
- ⚠️ [What was okay?]
- ❌ [What failed?]

### Coordination

**Self-Organization**:
- Did agents divide work naturally?
- Did they ask each other for help?
- Any confusion about who does what?

**Conversation Quality**:
- How many rounds per scenario?
- Did conversations reach conclusions?
- Any infinite loops or stuck points?

**Cost Efficiency**:
- Total tokens: ~X,XXX
- Total cost: $X.XX
- Cost per signup: $X.XX (or N/A)
- Worth it vs human time?

---

## What Didn't Work

### Failures & Challenges

**Agent Limitations**:
1. [Specific failure or limitation]
2. [Specific failure or limitation]
3. ...

**Human Intervention Points**:
1. [When did you need to step in?]
2. [Why couldn't agents handle it?]
3. ...

**Unexpected Issues**:
- [Things you didn't anticipate]
- [Problems that emerged]

---

## Comparison to Human Approach

**If you did this without agents**:

**Time**:
- With agents: X hours
- Without agents: Y hours
- Savings: Z%

**Quality**:
- Agent-drafted comments: [Better/Worse/Same]
- Thread selection: [Better/Worse/Same]
- Overall: [Better/Worse/Same]

**Would you use agents again?**: YES / NO / MAYBE

**Why?**:
[Your reasoning]

---

## Key Insights for Copenhagen

### What to Emphasize

**1. [First key insight]**
[Explanation and evidence]

**2. [Second key insight]**
[Explanation and evidence]

**3. [Third key insight]**
[Explanation and evidence]

### Conversation Excerpts to Use

**Best example of self-organization**:
```
[Paste conversation showing agents coordinating well]
```

**Example of human judgment needed**:
```
[Paste conversation showing where you had to intervene]
```

**Surprising agent behavior**:
```
[Paste something unexpected or interesting]
```

---

## Lessons Learned

### About AutoGen

**Strengths**:
- [What AutoGen did well]
- [Why conversation-based worked/didn't work]
- [Ease of setup, cost, etc]

**Weaknesses**:
- [What AutoGen struggled with]
- [Limitations discovered]
- [Things that need improvement]

### About Agent Coordination

**Works well for**:
- [Types of tasks where agents excelled]

**Struggles with**:
- [Types of tasks where agents failed]

**Human still needed for**:
- [Where human judgment was critical]

---

## Next Steps

### If This Were a Longer Experiment

**What would you improve?**:
1. [Improvement idea]
2. [Improvement idea]
3. ...

**What would you automate further?**:
- [Things that could be automated]

**What should stay human?**:
- [Things that should remain human-controlled]

### For Other Products/Companies

**Would this approach work for**:
- [X type of company]: YES / NO (why?)
- [Y type of company]: YES / NO (why?)
- [Z type of company]: YES / NO (why?)

---

## Cost-Benefit Analysis

**Investment**:
- Setup time: X hours
- Running time: Y hours
- API costs: $Z.ZZ
- Total: X+Y hours, $Z.ZZ

**Return**:
- Signups: N
- Learning value: [Qualitative assessment]
- Presentation material: [Value for consulting/speaking]
- Reusability: [Can you use this again?]

**ROI**: [Worth it / Not worth it / Depends]

---

## Questions for Audience (Copenhagen)

Anticipate these questions:

1. **"Did you actually get a signup?"**
   Answer: [Your answer]

2. **"What did agents do that you couldn't?"**
   Answer: [Your answer]

3. **"Where did they fail?"**
   Answer: [Your answer]

4. **"Would you do this for a real company?"**
   Answer: [Your answer]

5. **"What about cost/scale?"**
   Answer: [Your answer]

6. **"AutoGen vs CrewAI - why?"**
   Answer: [Your answer]

---

## Presentation Checklist

- [ ] Export all conversation logs to `/agentic/logs/`
- [ ] Populate MARP slides with real examples
- [ ] Create visual: agent org chart
- [ ] Create visual: conversation flow diagram
- [ ] Prepare demo (if live demo)
- [ ] Print backup slides (no internet needed)
- [ ] Practice timing (15-20 minutes)
- [ ] Prepare for Q&A

---

## Files to Bring to Copenhagen

1. Conversation logs (Markdown + JSON)
2. MARP presentation PDF
3. This learnings document
4. Code samples (if showing technical details)
5. Tracking data (clicks, signups, costs)

---

## Reflections

### What Surprised You?

[Open-ended reflection on what you didn't expect]

### What Would You Tell Another Founder?

[Advice for someone considering this approach]

### Biggest Takeaway?

[One sentence summary of the entire experiment]

---

*Template completed: [DATE]*
*Ready for presentation: YES / NO*
*Additional prep needed: [List if any]*
