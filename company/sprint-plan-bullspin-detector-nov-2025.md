# Sprint Plan - Bullspin Detector Launch (November 2025)

**Created by**: Program Manager
**Date**: November 14, 2025
**Sprint Goal**: Launch Bullspin Detector MVP and achieve first users

---

## Current Roadmap Phase

**Phase 1**: Foundation (November - December 2025)
**Milestone**: Launch Bullspin Detector - Target: November 2025
**Success Criteria**: 250 users by end of December 2025

---

## What Must Ship

### Core Features (P0 - Must Have)

1. **Web Interface**
   - Simple landing page
   - Text upload/paste functionality
   - "Analyze" button
   - Results display with highlighting

2. **AI Analysis Engine**
   - Detect partisan language
   - Detect neutral language
   - Detect nonsense/illogical arguments
   - Visual highlighting of each category

3. **Viral Mechanics**
   - Shareable results (social sharing buttons)
   - Unique URL per analysis
   - "Try it yourself" call-to-action

### Supporting Features (P1 - Should Have)

4. **Basic Analytics**
   - Track uploads
   - Track shares
   - Track return visitors

5. **Mobile Responsive**
   - Works on phones/tablets
   - Touch-friendly interface

### Nice to Have (P2 - Defer if Needed)

6. **User Accounts** - Defer to Phase 2
7. **Save Analysis History** - Defer to Phase 2
8. **Advanced Sharing** - Defer to Phase 2

---

## Work Breakdown

### Epic 1: AI Analysis Engine (P0)

**Owner**: `ai-engineer` agent
**Estimated time**: 3-5 days
**Status**: Not started

**Tasks**:
- [ ] Research AI models for text analysis (partisan detection, neutrality, logic checking)
- [ ] Design prompt engineering approach for analysis
- [ ] Build AI analysis function (input: text, output: categorized highlights)
- [ ] Test accuracy on sample political texts
- [ ] Optimize for speed and cost

**Dependencies**: None (can start immediately)

**Acceptance Criteria**:
- Can analyze text and return categories (partisan/neutral/nonsense)
- Accuracy tested on 10+ sample texts
- Response time < 5 seconds
- Cost per analysis < $0.05

---

### Epic 2: Web Interface (P0)

**Owner**: `frontend-developer` agent
**Estimated time**: 3-4 days
**Status**: Not started

**Tasks**:
- [ ] Design simple landing page layout
- [ ] Build text input component (paste or upload)
- [ ] Create "Analyze" button with loading state
- [ ] Build results display with color-coded highlighting
- [ ] Add social sharing buttons
- [ ] Make mobile responsive

**Dependencies**: Needs AI analysis API endpoint from Epic 1

**Acceptance Criteria**:
- User can paste political text
- Click analyze triggers AI analysis
- Results display with partisan (red), neutral (gray), nonsense (yellow) highlighting
- Share buttons work (Twitter, Facebook, copy link)
- Works on mobile devices

---

### Epic 3: Landing Page & Messaging (P0)

**Owner**: `content-creator` agent
**Estimated time**: 2 days
**Status**: Not started

**Tasks**:
- [ ] Write compelling landing page headline
- [ ] Create value proposition copy ("Detect BS in political proposals")
- [ ] Write example use cases
- [ ] Draft social sharing text templates
- [ ] Create FAQ section

**Dependencies**: None (can work in parallel with engineering)

**Acceptance Criteria**:
- Clear headline explaining what Bullspin Detector does
- Compelling reason to try it
- Social sharing text that's engaging/viral
- Addresses common questions

---

### Epic 4: Analytics & Tracking (P1)

**Owner**: `analytics-reporter` agent
**Estimated time**: 2 days
**Status**: Not started

**Tasks**:
- [ ] Set up basic analytics (Google Analytics or similar)
- [ ] Track key events: page visit, text uploaded, analysis completed, shared
- [ ] Create simple dashboard for monitoring

**Dependencies**: Needs web interface from Epic 2

**Acceptance Criteria**:
- Can see daily uploads, shares, return visitors
- Events tracked correctly
- Dashboard accessible to founder

---

### Epic 5: Visual Design (P1)

**Owner**: `visual-storyteller` agent
**Estimated time**: 2 days
**Status**: Not started

**Tasks**:
- [ ] Design simple logo/branding for Bullspin Detector
- [ ] Create color scheme (partisan=red, neutral=gray, nonsense=yellow)
- [ ] Design highlight styling
- [ ] Create shareable social card image

**Dependencies**: None (can work in parallel)

**Acceptance Criteria**:
- Simple, memorable branding
- Clear visual distinction between categories
- Shareable graphics look good on social media

---

### Epic 6: Infrastructure & Deployment (P0)

**Owner**: `devops-automator` agent
**Estimated time**: 2-3 days
**Status**: Not started

**Tasks**:
- [ ] Set up hosting (Vercel, Netlify, or similar)
- [ ] Configure AI API access (OpenAI, Anthropic, or similar)
- [ ] Set up domain (bullspindetector.com or middling.app/bullspin)
- [ ] Configure SSL/HTTPS
- [ ] Test deployment pipeline

**Dependencies**: None initially, needs to deploy once interface is ready

**Acceptance Criteria**:
- Site is live and accessible
- HTTPS working
- AI API connected and functional
- Can deploy updates quickly

---

## Critical Path

```
Start
 ↓
[Epic 1: AI Engine] (3-5 days) ←─────┐
 ↓                                   │
[Epic 2: Web Interface] (3-4 days) ──┤ (parallel work)
 ↓                                   │
[Epic 3: Landing Copy] (2 days) ─────┤
 ↓                                   │
[Epic 4: Analytics] (2 days) ────────┘
 ↓
[Epic 5: Visual Design] (2 days) (can happen anytime)
 ↓
[Epic 6: Deployment] (2-3 days)
 ↓
LAUNCH
```

**Total critical path time**: ~10-14 days (if everything goes perfectly)
**Buffer for issues**: +3-5 days
**Realistic launch**: 2-3 weeks from start

---

## Sprint Schedule

### Week 1 (Nov 14-20)
**Focus**: Build core functionality

- AI Engineer: Start Epic 1 (AI Analysis Engine)
- Frontend Developer: Start Epic 2 (Web Interface) - can begin with mockup
- Content Creator: Complete Epic 3 (Landing Page Copy)
- Visual Storyteller: Complete Epic 5 (Visual Design)

**Goal**: Working AI analysis + rough interface

### Week 2 (Nov 21-27)
**Focus**: Polish and integrate

- Frontend Developer: Complete Epic 2 (integrate AI, add sharing)
- Analytics Reporter: Complete Epic 4 (Analytics setup)
- DevOps Automator: Complete Epic 6 (Deployment)
- All: Testing and refinement

**Goal**: Fully functional MVP deployed

### Week 3 (Nov 28 - Dec 4)
**Focus**: Launch and iterate

- Launch publicly
- Monitor analytics
- Fix bugs quickly
- Begin growth activities

---

## Risks & Mitigation

### Risk 1: AI Analysis Not Accurate Enough
**Impact**: High - product doesn't work
**Probability**: Medium
**Mitigation**: Test early with sample texts, iterate prompts, be transparent about accuracy

### Risk 2: Timeline Too Aggressive
**Impact**: Medium - delayed launch
**Probability**: High
**Mitigation**: De-scope P1/P2 features if needed, focus only on P0

### Risk 3: No One Shares Results
**Impact**: High - no viral growth
**Probability**: Medium
**Mitigation**: Test sharing copy early, make results inherently shareable (funny, insightful)

### Risk 4: AI Costs Too High
**Impact**: Medium - burns runway too fast
**Probability**: Low
**Mitigation**: Monitor costs, optimize prompts, consider caching

---

## Definition of Done

Bullspin Detector is "launched" when:

- [ ] Live at public URL
- [ ] User can paste political text
- [ ] AI analyzes and highlights partisan/neutral/nonsense
- [ ] Results are shareable on social media
- [ ] Analytics tracking uploads and shares
- [ ] Mobile responsive
- [ ] No critical bugs
- [ ] Founder approved

**Minimum to launch**: All P0 features working, P1 features nice-to-have

---

## Next Steps (Immediate Actions)

**Today (Nov 14)**:
1. Founder approves this plan
2. Create GitHub issues for each epic
3. Assign agents via labels
4. Agents begin work

**Tomorrow (Nov 15)**:
- AI Engineer reports on analysis approach
- Frontend Developer shares initial mockup
- Content Creator shares landing copy draft

**Daily standups** (async):
- What did you complete yesterday?
- What are you working on today?
- Any blockers?

---

## Questions for Founder

1. **Domain preference**: Should we use `bullspindetector.com` or `middling.app/bullspin`?
2. **AI provider**: OpenAI GPT-4, Anthropic Claude, or other?
3. **Hosting**: Preference for Vercel, Netlify, or custom?
4. **Budget**: Any constraints on AI API costs during testing/launch?
5. **Launch strategy**: Soft launch (friends/network) or public launch (social media)?

---

**Program Manager Note**: This is an aggressive timeline but achievable if agents work in parallel and we de-scope ruthlessly. The critical path is AI Engine → Web Interface → Deployment. Everything else can flex.

Ready to create issues and start execution?
