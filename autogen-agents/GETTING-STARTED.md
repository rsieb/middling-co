# Getting Started with AutoGen for Middling Company

## What You Have Now

✅ **Framework Decision Documented**: `/research/framework-decision-autogen-vs-crewai.md`
✅ **AutoGen Setup**: Complete agent configuration in `/autogen-agents/`
✅ **3 Generalist Agents**: Alice, Bob, Charlie + Founder (you)
✅ **5 Predefined Scenarios**: Crisis, Planning, Operations, Strategy, Opportunity
✅ **Documentation**: Comprehensive guides and templates
✅ **Cost Controls**: OpenRouter support for ultra-cheap models (300x cheaper than GPT-4)

## Your Decision: Conversation-Based, Not Workflow-Based

**Why?**
Early-stage startups are chaotic, undefined, and organic. Agents should self-organize like real startup employees, not follow predefined workflows. We're simulating startup reality, not optimizing operations.

**Framework**: AutoGen (Microsoft, 51k⭐, production-ready)
**Not**: CrewAI (team-based workflows) or MegaAgent (research prototype)

## Next Steps

### Immediate (Today):

**1. Set up your environment** (5 minutes)

```bash
cd /home/user/middling-co/autogen-agents

# Install dependencies
pip install -r requirements.txt

# Configure API key
cp .env.example .env
# Edit .env and add your OpenRouter or OpenAI key
```

**2. Run your first scenario** (5 minutes)

```bash
# Try the crisis scenario
python run_scenario.py --scenario crisis

# Watch Alice, Bob, and Charlie self-organize!
```

**3. Document what you observe** (10 minutes)

```bash
# Copy the template
cp learnings/observations-template.md learnings/week1/scenario-crisis-1.md

# Fill it out while fresh in your mind
```

### This Week:

**Day 1-2: Experiment**
- [ ] Run all 5 predefined scenarios
- [ ] Document each one using the template
- [ ] Note patterns and surprises

**Day 3-4: Custom Scenarios**
- [ ] Create 3 custom scenarios for your specific startup
- [ ] Run them and document
- [ ] Compare agent behavior across scenarios

**Day 5: Weekly Summary**
- [ ] Review all observations
- [ ] Create `learnings/week1/summary.md`
- [ ] Identify patterns worth tracking
- [ ] Write initial blog post draft: "First Week Running a Startup on AutoGen"

### This Month:

**Week 2: More Experiments**
- Test edge cases
- Try different scenarios
- Vary complexity

**Week 3: Pattern Analysis**
- What roles emerge repeatedly?
- What coordination mechanisms work?
- When do conversations succeed vs fail?

**Week 4: First Insights**
- Draft publication: "Emergent Roles in Agent-Run Startups"
- Compare to how you'd handle as human
- Document cost analysis

### Month 2-3: Comparison & Maturation

**Add Structure Where Patterns Emerge:**
- Identify repetitive tasks (support tickets?)
- Consider CrewAI for those specific workflows
- Keep strategy conversational
- Document the transition

**Publication**: "From Chaos to Process: When to Add Structure"

## Key Files to Know

### Configuration:
- `/autogen-agents/.env` - Your API keys and model selection
- `/autogen-agents/team_config.py` - Agent definitions (Alice, Bob, Charlie)
- `/autogen-agents/run_scenario.py` - Main script to run scenarios

### Documentation:
- `/autogen-agents/README.md` - Comprehensive guide
- `/autogen-agents/QUICKSTART.md` - 5-minute quick start
- `/research/framework-decision-autogen-vs-crewai.md` - Why we chose this approach

### Learnings:
- `/autogen-agents/learnings/` - Document everything here
- `/autogen-agents/learnings/observations-template.md` - Use this for each scenario
- `/autogen-agents/learnings/README.md` - Process and questions to answer

## How to Interact with Agents

### Observer Mode (Default):
Agents work autonomously, you observe and document.

**Perfect for**: Learning how agents self-organize without human intervention.

### Participant Mode:
Edit `team_config.py`:
```python
FOUNDER_CONFIG = {
    "human_input_mode": "TERMINATE",  # You can jump in anytime
}
```

Now when you run a scenario, you can:
- Type input to guide the conversation
- Type "exit" to let them continue
- Terminate when you want to take over

**Perfect for**: Actually running the company, not just researching.

## Cost Management

**Recommended**: Use OpenRouter with Qwen 2.5

In `.env`:
```bash
MODEL_PROVIDER=openrouter
OPENROUTER_API_KEY=your-key
DEFAULT_MODEL=qwen/qwen-2.5-72b-instruct
```

**Cost**: ~$0.0025-0.0075 per scenario (less than a penny!)
**Budget**: Your $500/month = 50,000+ scenarios

**Alternative**: OpenAI with GPT-4o-mini
- More expensive (~$0.75-2.25 per scenario)
- But still within budget (200-700 scenarios/month)

## What You're Learning

### Primary Questions:
1. Can agents self-organize without predefined roles?
2. When do conversations reach conclusions vs loop?
3. What coordination mechanisms emerge naturally?
4. When do humans need to intervene?
5. What should become workflows vs stay conversational?

### Secondary Questions:
- What roles emerge repeatedly across scenarios?
- How does this compare to human performance?
- What's the cost of organic collaboration?
- When does chaos become productive vs wasteful?

## Publication Strategy

### Blog Posts (For Startup Audiences):
- Week 2: "First Week Running Startup on AutoGen"
- Month 1: "Emergent Roles: Job Titles That Appeared Without Being Designed"
- Month 3: "When Conversations Beat Workflows"
- Month 6: "From Chaos to Process: How AI Startups Mature"

### Case Study (For Consulting):
- Month 12: "Running a Company on AI Agents: 12-Month Case Study"
- Include: Patterns, costs, failures, successes, recommendations

### Conference Talks:
- "Can AI Agents Run a Startup? Our 6-Month Experiment"
- Show real conversation logs
- Share emergent insights
- Demonstrate consulting expertise

## Success Metrics

### Technical:
- [ ] Agents complete scenarios without predefined workflows
- [ ] Conversations reach conclusions (not infinite loops)
- [ ] Self-organization emerges
- [ ] Cost stays within budget ($500-1000/month)

### Learning:
- [ ] 10+ emergent patterns documented
- [ ] Understand when conversations work vs fail
- [ ] Identify human intervention triggers
- [ ] Create framework for startup maturation

### Business:
- [ ] 5+ blog posts published
- [ ] 1 comprehensive case study
- [ ] Speaking opportunities
- [ ] Consulting leads from demonstrated expertise

## Common Questions

**Q: Will agents ask me for guidance?**
A: Depends on `human_input_mode` setting. Default is "TERMINATE" - they work autonomously but you can jump in. Change to "ALWAYS" if you want them to ask you.

**Q: How do I kickstart a scenario?**
A: `python run_scenario.py --scenario crisis` (or use `--custom "your scenario"`)

**Q: What if conversations never conclude?**
A: Set `max_round` limit in config. Or agents say "TERMINATE". Or you can kill it.

**Q: What if it's too expensive?**
A: Use OpenRouter with Qwen 2.5 (300x cheaper than GPT-4). See cost management section.

**Q: Should I use CrewAI instead?**
A: No (for now). See `/research/framework-decision-autogen-vs-crewai.md` for detailed reasoning. You're simulating chaos, not optimizing workflows. Maybe add CrewAI later for repetitive tasks.

## Support & Resources

- **Full Guide**: `/autogen-agents/README.md`
- **Framework Decision**: `/research/framework-decision-autogen-vs-crewai.md`
- **AutoGen Docs**: https://microsoft.github.io/autogen/
- **OpenRouter**: https://openrouter.ai/

## Your Mission

**Run experiments. Document learnings. Publish insights.**

The goal isn't to build a perfect AI company. It's to understand:
- How agents coordinate organically
- When conversation beats workflow
- How startups mature from chaos to process
- What humans still need to do

**This is research that becomes consulting IP and thought leadership.**

---

## Ready?

```bash
cd /home/user/middling-co/autogen-agents
python run_scenario.py --scenario crisis
```

**Welcome to running a startup on AI agents. Let's see what emerges.**
