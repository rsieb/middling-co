# Learnings Directory

This directory is for documenting observations from running the AutoGen agent team.

## Purpose

The goal is to answer: **Can AI agents run a startup organically, without predefined workflows?**

By running scenarios and documenting patterns, we'll learn:
- How agents self-organize
- When conversation beats workflow
- What coordination mechanisms emerge
- When humans need to intervene
- How startups should mature from chaos to process

## Structure

```
learnings/
├── README.md                          # This file
├── observations-template.md           # Template for each scenario
├── week1/                            # Week-by-week organization
│   ├── summary.md
│   ├── scenario-crisis-1.md
│   ├── scenario-planning-1.md
│   └── ...
├── week2/
│   └── ...
├── patterns/                          # Emergent patterns across scenarios
│   ├── self-organization.md
│   ├── decision-making.md
│   ├── failure-modes.md
│   └── cost-analysis.md
└── insights/                          # Publication-worthy insights
    ├── conversation-vs-workflow.md
    ├── emergent-roles.md
    └── startup-maturation.md
```

## Documentation Process

### After Each Scenario:

1. **Copy the template**:
   ```bash
   cp observations-template.md week1/scenario-crisis-1.md
   ```

2. **Fill it out** while the scenario is fresh

3. **Save the conversation log**:
   - Copy/paste the full output
   - Or redirect to file: `python run_scenario.py --scenario crisis > logs/crisis-1.txt`

4. **Note patterns** that recur across scenarios

### Weekly:

1. **Create weekly summary** in `weekX/summary.md`
2. **Extract patterns** that appeared multiple times
3. **Document insights** worth publishing

### Monthly:

1. **Review all patterns**
2. **Draft publication ideas** in `/insights/`
3. **Identify what should become workflows** (move to CrewAI)

## Key Questions to Answer

### Week 1-2: Basic Functioning
- [ ] Do agents self-organize or get confused?
- [ ] Do conversations reach conclusions?
- [ ] What's the failure rate?
- [ ] What's the cost per scenario?

### Month 1: Patterns
- [ ] What roles emerge repeatedly?
- [ ] What coordination mechanisms work?
- [ ] When do humans need to intervene?
- [ ] What scenarios work best conversationally?

### Month 2-3: Comparison
- [ ] How does this compare to human performance?
- [ ] What's more efficient: conversation vs workflow?
- [ ] When should structure be introduced?

### Month 3-6: Maturation
- [ ] What repetitive tasks should become workflows?
- [ ] What should stay conversational?
- [ ] How does agent coordination evolve?

## Publication Roadmap

Based on learnings, we'll create:

**Week 2**: "First Week Running a Startup on AutoGen"
**Month 1**: "Emergent Roles: Job Titles That Appeared Without Being Designed"
**Month 3**: "When Conversations Beat Workflows (And Vice Versa)"
**Month 6**: "From Chaos to Process: How AI Startups Mature"
**Month 12**: "Running a Company on AI Agents: 12-Month Case Study"

## Cost Tracking

Track costs in each observation:
- Tokens used per scenario
- Cost per scenario
- Monthly total
- Cost per agent round
- Cost efficiency trends

**Goal**: Stay within $500-1000/month budget

## Pattern Categories

As you observe, categorize patterns:

### 1. Self-Organization Patterns
- Who takes what role?
- How is ownership negotiated?
- When does confusion happen?

### 2. Coordination Mechanisms
- How do agents share context?
- What handoff patterns emerge?
- When do they ask for help?

### 3. Decision-Making Patterns
- How do they reach consensus?
- When do debates help vs hurt?
- What triggers decisions?

### 4. Failure Modes
- Conversation loops
- Unclear ownership
- Off-topic tangents
- Hallucinations
- Inefficiency

### 5. Human Intervention Triggers
- When do you need to step in?
- What can't agents handle alone?
- What context do they need?

## Analysis Tools

Consider building:
- Script to analyze conversation logs
- Cost tracking dashboard
- Pattern extraction tool
- Comparison visualizations

## Tips

1. **Document immediately** - don't wait, you'll forget
2. **Be honest** - note failures, not just successes
3. **Compare** - always ask "how would a human do this?"
4. **Look for patterns** - single observations are data, repeated patterns are insights
5. **Think publication** - what would be interesting to startup founders?

## Questions or Patterns?

Document them here as they emerge. This is a living research process.

---

*This is an experiment in AI-native startup operations. Document everything, because the learnings are as valuable as the product.*
