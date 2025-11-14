# Agent Framework Analysis: Contains Studio vs Alternatives

**Date**: November 2025
**Purpose**: Evaluate whether to build on Contains Studio agents repo or explore alternatives for Middling Company (SaaS model)

---

## Executive Summary

**Recommendation**: **Adapt Contains Studio as foundation** with SaaS-specific modifications.

**Rationale**:
- 70% overlap with our needs (proven agent patterns, coordination model)
- Faster time-to-launch than building from scratch
- Active maintenance and Claude Code integration
- Minor adaptations needed for agency→SaaS transition

**Key Gaps to Address**:
1. Swap agency-specific agents for SaaS-specific ones
2. Add recurring revenue/subscription focus
3. Include customer lifecycle management agents
4. Integrate product-led growth strategies

---

## Contains Studio Agents Analysis

### Strengths ✅

**1. Proven Agent Architecture**
- 35+ specialized agents across 7 departments
- Well-defined YAML frontmatter structure
- Clear role definitions with 3-4 examples each
- 500+ word system prompts with domain expertise

**2. GitHub-Native Coordination** (Perfect Match)
- Agents coordinate via Issues, PRs, Discussions
- Project board integration for Kanban workflow
- Built for rapid development (6-day sprints)
- Proactive agent triggering patterns

**3. Comprehensive Coverage**
- Engineering: 7 agents (dev, QA, DevOps, mobile, AI)
- Product: 3 agents (PM, feedback, trends)
- Marketing: 7 agents (growth, content, social platforms)
- Design: 5 agents (UI, UX, brand, whimsy)
- Operations: 5 agents (analytics, finance, legal, support, infra)
- Testing: 5 agents (API, performance, workflow optimization)
- Project Management: 3 agents (sprint planning, shipping, experiments)

**4. Built for Rapid Iteration**
- 6-day sprint philosophy (aligns with our timeline)
- Focus on shipping over perfection
- Build in public compatibility
- Metrics-driven decision making

**5. Claude Code Native**
- Designed specifically for Claude Code Task tool
- Pre-configured with appropriate tool access
- Examples follow Claude Code usage patterns
- Active community and maintenance

### Limitations ⚠️

**1. Agency Business Model Focus**
- Optimized for client projects, not product companies
- Multiple apps/projects assumption
- Client stakeholder management emphasis
- Less focus on recurring revenue

**2. Missing SaaS-Specific Agents**
- No subscription/churn management agent
- No customer success agent
- No product-led growth agent
- No onboarding optimization agent
- No pricing/packaging agent

**3. Revenue Model Mismatch**
- Focus on project-based revenue
- Limited recurring revenue optimization
- Less emphasis on unit economics (LTV/CAC)
- Missing freemium conversion strategies

**4. Marketing Emphasis**
- Heavy focus on viral/social media marketing
- Less B2B SaaS marketing (SEO, content, partnerships)
- Missing product-led acquisition strategies
- Limited self-serve conversion focus

---

## SaaS-Specific Requirements Analysis

### Critical SaaS Agents Needed

**1. Customer Success Agent**
- Onboarding flow optimization
- Feature adoption tracking
- Churn prediction and prevention
- Health score monitoring
- Expansion revenue identification

**2. Subscription Management Agent**
- Pricing optimization
- Packaging experiments
- Churn analysis
- Upgrade/downgrade flows
- Payment recovery

**3. Product-Led Growth Agent**
- Self-serve activation
- Aha moment identification
- Viral loop design
- Freemium conversion optimization
- In-app marketing

**4. Retention Specialist Agent**
- Cohort analysis
- Engagement scoring
- Re-engagement campaigns
- Win-back strategies
- Usage pattern analysis

**5. Sales Enablement Agent** (if not pure self-serve)
- Demo preparation
- Trial optimization
- Sales collateral
- Pricing conversations
- Deal closing support

### Agency vs SaaS Model Differences

| Aspect | Agency Model (Contains) | SaaS Model (Middling) | Action |
|--------|-------------------------|----------------------|--------|
| Revenue | Project-based | Recurring subscriptions | Add subscription agents |
| Customers | Few large clients | Many small customers | Scale support operations |
| Marketing | Portfolio showcase | Product-led growth | Add PLG agents |
| Success Metric | Client satisfaction | Retention & LTV | Add CS agents |
| Growth | New client acquisition | Expansion + Retention | Modify growth strategy |
| Operations | Project management | Customer lifecycle | Add lifecycle agents |
| Pricing | Fixed/hourly | Dynamic/tiered | Add pricing agent |

---

## Alternative Frameworks Reviewed

### 1. AutoGPT / MetaGPT
**Type**: Multi-agent orchestration frameworks

**Pros**:
- Strong agent coordination capabilities
- Role-based agent systems
- Open source and active development

**Cons**:
- Generic frameworks requiring heavy customization
- Not business-operations focused
- No pre-built business domain agents
- Higher implementation complexity

**Verdict**: ❌ Too generic, would take 3-6 months to reach Contains Studio's level

### 2. CrewAI
**Type**: Collaborative agent framework

**Pros**:
- Good for agent teams working together
- Backed by Andrew Ng
- Growing ecosystem

**Cons**:
- Young and evolving APIs
- Limited business operations templates
- More code-focused than operations-focused
- Coordination challenges reported

**Verdict**: ❌ Better for development tasks than business operations

### 3. Enterprise Platforms (AWS Bedrock, IBM watsonx)
**Type**: Enterprise AI agent platforms

**Pros**:
- Enterprise-grade reliability
- Built-in compliance
- Integration with cloud services

**Cons**:
- Expensive for early-stage startup
- Overkill for 1-person operation
- Vendor lock-in
- Complex setup

**Verdict**: ❌ Not suitable for bootstrapped AI-native experiment

### 4. Build from Scratch
**Type**: Custom agent system

**Pros**:
- Perfect fit for exact needs
- Complete control

**Cons**:
- 2-4 months development time
- Delays Middling launch
- No proven patterns
- Maintenance burden

**Verdict**: ❌ Conflicts with "demonstrate viability" goal

---

## Recommended Approach: Adapt Contains Studio

### Phase 1: Foundation (Week 1-2)
**Action**: Fork and adapt Contains Studio agents

**Keep As-Is** (20 agents):
- Engineering: All 7 agents (dev, QA, DevOps, mobile, AI, backend, frontend)
- Design: All 5 agents (UI, UX, brand, visual storyteller, whimsy)
- Testing: All 5 agents (API, performance, test analyzer, tool evaluator, workflow)
- Project Management: 3 agents (sprint prioritizer, shipper, producer)

**Modify** (8 agents):
- **Product agents**: Adapt for SaaS metrics (retention, churn, LTV)
- **Marketing agents**: Shift from agency portfolio to product-led growth
- **Finance agent**: Add subscription revenue modeling, MRR tracking
- **Analytics agent**: Focus on product metrics, cohort analysis
- **Support agent**: Scale for many customers vs few clients
- **Growth agent**: Add PLG and self-serve conversion

**Remove** (2 agents):
- Instagram curator (low priority for coach marketplace)
- Reddit community builder (defer to post-launch)

### Phase 2: Add SaaS-Specific Agents (Week 3-4)

**New Agents to Create**:

1. **customer-success-agent**
   - Onboarding optimization
   - Feature adoption tracking
   - Health score monitoring
   - Churn prevention

2. **subscription-optimizer-agent**
   - Pricing experiments
   - Packaging optimization
   - Payment recovery
   - Upgrade flow optimization

3. **plg-specialist-agent**
   - Self-serve activation
   - Aha moment optimization
   - Viral loop design
   - Freemium conversion

4. **retention-specialist-agent**
   - Cohort analysis
   - Engagement scoring
   - Re-engagement campaigns
   - Usage pattern analysis

5. **onboarding-optimizer-agent**
   - First-run experience
   - Time-to-value reduction
   - Drop-off analysis
   - Activation optimization

### Phase 3: Integration & Testing (Week 5-6)

**Tasks**:
- Test agent coordination workflows
- Validate GitHub-native coordination
- Run simulated scenarios
- Document learnings
- Prepare for launch

---

## Cost-Benefit Analysis

### Building on Contains Studio

**Time Investment**:
- Week 1-2: Adapt existing agents (20 hours)
- Week 3-4: Create new SaaS agents (30 hours)
- Week 5-6: Integration and testing (20 hours)
- **Total**: 70 hours over 6 weeks

**Benefits**:
- Proven agent patterns and coordination
- 28 agents ready on day one
- Active maintenance and updates
- Community learnings and improvements
- Fast path to launch

**Risks**:
- Agency mindset embedded in some agents
- May need ongoing adaptations
- Dependent on Contains Studio updates

### Building from Scratch

**Time Investment**:
- Design agent architecture (40 hours)
- Build coordination system (60 hours)
- Create 35 agents (175 hours)
- Testing and refinement (80 hours)
- **Total**: 355 hours over 12-16 weeks

**Benefits**:
- Perfect fit for SaaS model
- Complete control and ownership
- No dependencies

**Risks**:
- 3-4 month delay to launch
- Unproven patterns
- Ongoing maintenance burden
- Misses "building in public" opportunity window

### Verdict: Adapt Contains Studio

**ROI**: 5x time savings (70 hours vs 355 hours)
**Launch**: 6 weeks vs 16 weeks
**Risk**: Lower (proven patterns vs unproven custom)

---

## Implementation Plan

### Week 1-2: Foundation
```
✓ Fork Contains Studio agents to middling-co/agents/
✓ Audit all 35 agents for SaaS relevance
✓ Modify Product agents for SaaS metrics
✓ Update Marketing agents for PLG focus
✓ Adapt Finance agent for MRR/subscription model
✓ Document changes in /agents/MODIFICATIONS.md
```

### Week 3-4: SaaS Agents
```
✓ Create customer-success-agent
✓ Create subscription-optimizer-agent
✓ Create plg-specialist-agent
✓ Create retention-specialist-agent
✓ Create onboarding-optimizer-agent
✓ Test new agents with sample scenarios
✓ Document in /agents/definitions/saas/
```

### Week 5-6: Integration
```
✓ Set up agent coordination workflows
✓ Create sample GitHub issues for testing
✓ Run multi-agent scenarios
✓ Validate human-in-loop approval flows
✓ Document coordination patterns
✓ Prepare first company update
```

### Week 7: Launch
```
✓ Initialize first 3 agents (PM, Eng Manager, Marketing)
✓ Publish "Week 0" company update
✓ Open repo for public observation
✓ Begin agent-driven operations
```

---

## Success Criteria

### Technical Success
- [ ] All 35+ agents properly configured
- [ ] GitHub coordination working smoothly
- [ ] Human approval workflows functional
- [ ] Agent decision logging operational

### Business Success
- [ ] Launch within 6 weeks (vs 16 weeks from scratch)
- [ ] Agents handling 50%+ of routine operations by month 2
- [ ] Clear demonstration of AI-native company viability
- [ ] 3+ case study insights documented by month 3

### Learning Success
- [ ] Documented patterns for SaaS agent coordination
- [ ] Identified gaps in Contains Studio framework
- [ ] Contributed improvements back to Contains Studio
- [ ] Created reusable SaaS agent templates

---

## Risks & Mitigations

### Risk 1: Agency Mindset Embedded
**Impact**: Medium
**Mitigation**: Systematic audit and modification of agent prompts, add SaaS-specific examples

### Risk 2: Missing Critical SaaS Functionality
**Impact**: High
**Mitigation**: Create 5 new SaaS-specific agents, prioritize customer success and retention

### Risk 3: Coordination Complexity
**Impact**: Medium
**Mitigation**: Start with 3 agents, gradually expand, document patterns extensively

### Risk 4: Dependency on Contains Studio Updates
**Impact**: Low
**Mitigation**: Fork repository, maintain local control, contribute improvements upstream

---

## Conclusion

**Final Recommendation**: Adapt Contains Studio agents as foundation for Middling Company.

**Reasoning**:
1. **Speed**: 5x faster to launch (6 weeks vs 16 weeks)
2. **Quality**: Proven patterns and coordination
3. **Alignment**: 70% overlap with our needs
4. **Community**: Active maintenance and learnings
5. **Focus**: Lets us focus on SaaS-specific innovation, not reinventing agent infrastructure

**Next Steps**:
1. Fork Contains Studio repo to /agents/
2. Begin Phase 1 modifications
3. Document all changes for community contribution
4. Plan to share SaaS agent improvements upstream

**Trade-offs Accepted**:
- Some agency-focused content remains (low impact)
- Dependent on Contains Studio for updates (acceptable risk)
- Need to maintain fork and merge improvements (manageable overhead)

---

*This analysis supports the Middling Company goal: demonstrate AI-native company viability within 3 months while building in public.*
