# Middling Company - AI-Native Organization Operations

## Mission
Demonstrate how to run a complete company with AI agents and minimal human employees, building the Middling app as a real-world case study for AI-native startup operations.

## Core Thesis
An AI-native company can achieve 10,000:1 users-per-employee ratio by:
- Coordinating agents through GitHub infrastructure (issues, PRs, discussions, projects)
- Starting with human-in-the-loop approval, graduating to autonomous operations
- Building in public to demonstrate viability and learnings
- Operating as a public benefit corporation focused on user value over revenue

## Repository Boundaries

### This Repo (middling-co)
**Purpose**: Company operations, agent coordination, business strategy

**Contains**:
- Agent definitions and workflows
- Business strategy and OKRs
- Product roadmap and user research
- Marketing campaigns and content
- Customer support processes
- Financial tracking (non-sensitive metrics)
- Operational playbooks
- Public updates and learnings

**Does NOT contain**: Application code, technical implementation details

### Middling App Repo (separate)
**Purpose**: Technical implementation of the Middling application

**Contains**: Code, tests, technical documentation, deployment configs

**Coordination**: Agents in this repo create issues/PRs in the app repo for implementation work

---

## Agent Architecture

### Executive Layer
- **CEO Agent**: Strategic decisions, prioritization, company direction
- **CFO Agent**: Budget management, runway tracking, cost optimization

### Product Layer
- **Product Manager Agent**: Roadmap planning, requirements, user stories
- **UX Researcher Agent**: User feedback analysis, usability testing
- **Product Marketing Agent**: Positioning, messaging, launch planning

### Engineering Layer
- **Engineering Manager Agent**: Sprint planning, technical resource allocation
- **Developer Agents**: Implementation, code review, technical decisions
- **QA Agent**: Testing strategies, quality assurance, bug validation
- **DevOps Agent**: Deployment, monitoring, infrastructure management

### Go-to-Market Layer
- **Marketing Agent**: Content creation, SEO, campaigns
- **Growth Agent**: Acquisition experiments, conversion optimization
- **Community Manager Agent**: Social media, user engagement, brand building
- **Support Agent**: Customer inquiries, bug triage, documentation

### Operations Layer
- **Operations Agent**: Process improvement, tool evaluation
- **Analytics Agent**: Metrics reporting, insight generation
- **Documentation Agent**: Knowledge base maintenance, playbook updates

---

## Coordination Model

### GitHub-Native Workflows

**Issues = Work Items**
- Agents create issues for tasks
- Labels route to appropriate agents (`agent:customer-support`, `agent:engineering`)
- Agents claim issues by self-assignment
- Human approval via comment approval pattern

**Pull Requests = Proposed Changes**
- Agents create PRs for all changes (code in app repo, docs in this repo)
- Other agents review PRs
- Human has final approval authority

**Discussions = Strategic Conversations**
- Agents debate approaches and proposals
- Human participates in strategic discussions
- Decision outcomes documented in `/company/decisions/`

**Project Board = Kanban Workflow**
- Agents move cards through workflow stages
- Visibility into all ongoing work
- Bottleneck identification

**Wiki = Knowledge Base**
- Agents document processes and learnings
- Standard operating procedures
- Onboarding materials for new agents

**Actions = Automation**
- Agents trigger workflows via GitHub Actions
- Cross-repo coordination (this repo ↔ app repo)
- Automated reporting and metrics updates

---

## Autonomy Progression

### Phase 1: Human-in-the-Loop (Current)
**Human Approval Required**:
- All financial decisions
- Major product changes
- Marketing campaigns
- Customer communications
- Agent configuration changes

**Agent Autonomy**:
- Research and analysis
- Draft proposals
- Routine maintenance
- Metrics reporting

### Phase 2: Graduated Autonomy (3-6 months)
**Agent Autonomy Expands**:
- Decisions under $100 threshold
- Small feature implementations
- Common support responses
- Content publication (with review)

**Human Focus Shifts**:
- Strategic approvals only
- Exception handling
- Vision and direction

### Phase 3: High Autonomy (6-12 months)
**Agent Autonomy**:
- Daily operations fully autonomous
- Budget allocation within guidelines
- Product iteration cycles
- Growth experiments

**Human Role**:
- Strategic vision only
- Major pivots and decisions
- Exceptional cases

---

## Building in Public

### Public Metrics (Updated Weekly)
**Efficiency Metrics**:
- Users per employee ratio (target: 10,000:1)
- Agent productivity (tasks/agent/week)
- Cost per user
- Response times

**Product Metrics**:
- Monthly Active Users (MAU)
- Retention (D1, D7, D30)
- Net Promoter Score
- Feature usage rates

**Operational Metrics**:
- Deployment frequency
- Mean time to recovery
- Bug resolution time
- Agent decision accuracy (human override rate)

**Business Health**:
- Runway (months)
- Burn rate trend
- Cost structure (% AI vs % human)
- NOT revenue (public benefit ethos)

### Transparency Mechanisms
- Weekly "Company Update" issues (agent-written, human-approved)
- Monthly "Metrics Dashboard" (automated)
- Real-time project board visibility
- Agent decision audit logs
- Public post-mortems for failures

---

## Success Criteria

### 6-Month Goals
- 1,000 active users with 1 human employee (1,000:1 ratio)
- Agents handling 80% of customer support autonomously
- Weekly product iteration cycles
- $500/month operating costs (mostly AI APIs)

### 12-Month Goals
- 10,000 active users maintaining 1 human employee (10,000:1 ratio)
- Agents making 90% of operational decisions autonomously
- Profitable on $5/user/year revenue (public benefit model)
- Published playbook for AI-native company setup

### Demonstration Goals
- Prove viability of AI-native org structure
- Create reusable template for others
- Generate 10+ case study insights
- Attract 3+ consulting clients interested in AI-native transformation

---

## Integration with Consulting Practice

### Synergies
- **Proof of Concept**: Real implementation, not just theory
- **Case Study Material**: Concrete examples for client pitches
- **Learning Lab**: Test approaches before recommending to clients
- **Marketing Asset**: Demonstrates expertise and thought leadership

### Client Involvement
- Clients can observe operations (read-only access)
- Clients can adopt agent templates
- Clients can request specific experiments
- Success metrics inform consulting frameworks

---

## Getting Started

### For Observers
1. Watch this repo to receive updates
2. Read weekly company updates in Issues
3. Explore agent decision logs
4. Review metrics dashboard

### For Contributors
1. Review `/agents/definitions/` to understand agent roles
2. Check Project Board for current priorities
3. Join Discussions for strategic conversations
4. Submit issues for suggestions or problems

### For AI/Consulting Professionals
1. Study `/agents/workflows/` for coordination patterns
2. Review `/company/playbooks/` for operational templates
3. Examine `/public/learnings/` for insights
4. Fork structure for your own AI-native experiments

---

## Constraints & Principles

### Resource Constraints
- **Time**: ~10 hours/week human involvement (CEO/founder time)
- **Budget**: $500-1000/month for AI API costs
- **Timeline**: Public launch within 3 months

### Operating Principles
1. **Transparency First**: Default to public unless sensitive
2. **Evidence-Based**: All decisions backed by data/metrics
3. **User Value Over Revenue**: Public benefit corporation ethos
4. **Rapid Iteration**: Ship fast, learn fast, improve fast
5. **Breadth Over Depth**: Demonstrate all functions, not perfect any one
6. **Agent Coordination**: Prefer GitHub-native tools over external systems
7. **Human Safety Net**: Human can always override agent decisions
8. **Document Everything**: Learnings are as valuable as the product

---

## Current Status

**Phase**: Foundation (Setting up agent infrastructure)
**Human Employees**: 1 (Founder/CEO)
**Active Agents**: 0 (to be initialized)
**Users**: 0 (pre-launch)
**Runway**: TBD months

**Next Milestones**:
1. Complete agent definitions
2. Set up coordination workflows
3. Initialize first 3 agents (PM, Engineering Manager, Marketing)
4. Launch MVP with agent-driven operations
5. Onboard first 100 users

---

## Questions or Contributions?

Open a Discussion for strategic questions or ideas.
Open an Issue for specific tasks or problems.
Watch this repo to follow the AI-native company experiment.

**Contact**: [Your contact method for serious inquiries]

---

*This is a living document. Agents will propose updates as we learn and evolve.*
