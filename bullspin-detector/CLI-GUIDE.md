# Bullspin Detector - Command Line Guide

**For people who prefer terminal over Jupyter notebooks**

---

## Setup (One Time)

```bash
cd /home/user/middling-co/bullspin-detector/agentic

# Install dependencies
pip install pyautogen python-dotenv

# Configure API key
cp ../../autogen-agents/.env .env
# Edit .env with your API key
```

---

## The 3 Scenarios

### 1. Research: Find Reddit Threads

```bash
python run_bullspin.py --scenario research
```

**What happens**:
- Agents discuss and find 3-5 relevant Reddit threads
- Research Agent searches r/politics, r/AskPolitics, etc.
- Supervisor prioritizes best threads
- Logs saved to `logs/scenario-1-research-[timestamp].md`

**Optional**: Specify custom topics
```bash
python run_bullspin.py --scenario research --topics "Trump tariffs,Immigration policy"
```

**Next**: Review `logs/scenario-1-research-*.md` and pick 1-2 threads

---

### 2. Writing: Draft Comments

```bash
python run_bullspin.py --scenario writing --threads "https://reddit.com/r/AskPolitics/...,https://reddit.com/r/politics/..."
```

**What happens**:
- Writer Agent drafts comments for each thread
- Tracker Agent creates trackable links
- Supervisor coordinates
- Logs saved to `logs/scenario-2-writing-[timestamp].md`

**Next**: Review drafts in logs, edit if needed, post manually to Reddit

---

### 3. Tracking: Monitor Results

```bash
python run_bullspin.py --scenario tracking
```

**What happens**:
- Tracker Agent checks analytics
- Reports clicks and signups
- Supervisor suggests follow-up actions
- Logs saved to `logs/scenario-3-tracking-[timestamp].md`

**Note**: You'll need to manually feed tracking data to agents (or they'll simulate it)

---

## Complete Workflow

```bash
# Day 1: Research
python run_bullspin.py --scenario research
cat logs/scenario-1-research-*.md
# Pick threads from output

# Day 2: Writing
python run_bullspin.py --scenario writing --threads "url1,url2"
cat logs/scenario-2-writing-*.md
# Review drafts, edit, post to Reddit manually

# Day 3: Tracking
python run_bullspin.py --scenario tracking
cat logs/scenario-3-tracking-*.md
# See results
```

---

## Viewing Logs

All logs saved to `logs/` in two formats:

**Markdown** (human-readable):
```bash
cat logs/scenario-1-research-20251120-143000.md
less logs/scenario-1-research-20251120-143000.md
```

**JSON** (for processing):
```bash
jq . logs/scenario-1-research-20251120-143000.json
```

**List all logs**:
```bash
ls -lh logs/
```

---

## Tips for Command Line

### Run in background
```bash
python run_bullspin.py --scenario research > output.log 2>&1 &
tail -f output.log
```

### Redirect to file
```bash
python run_bullspin.py --scenario research | tee my-research-run.log
```

### Quick review
```bash
# See just agent names and first line of each response
grep -E "^## " logs/scenario-1-research-*.md
```

### Extract key info
```bash
# Find all Reddit URLs in logs
grep -oE "https://reddit.com[^ ]+" logs/*.md
```

---

## Advantages of CLI vs Notebook

**Why CLI is simpler**:
- ✅ No Jupyter server to manage
- ✅ Easy to script and automate
- ✅ Better for version control (just Python scripts)
- ✅ Familiar workflow (run → check output → repeat)
- ✅ Easy to pipe, redirect, background
- ✅ Works over SSH without hassle

**Why Notebook might be useful**:
- Interactive step-by-step (see output inline)
- Can edit and re-run cells
- Good for presentations/demos
- Embedded visualizations

**For your use case (1-week experiment)**: CLI is totally fine and probably simpler!

---

## Customization

### Change agent behavior
Edit `bullspin_agents.py` to modify system messages

### Change conversation length
Edit `bullspin_agents.py`:
```python
BULLSPIN_GROUPCHAT_CONFIG = {
    "max_round": 50,  # ← Change this
}
```

### Change human interaction
Edit `bullspin_agents.py`:
```python
USER_PROXY_CONFIG = {
    "human_input_mode": "TERMINATE",  # or "ALWAYS" or "NEVER"
}
```

---

## Troubleshooting

### "ModuleNotFoundError: No module named 'autogen'"
```bash
pip install pyautogen
```

### "API key not found"
```bash
# Check .env exists and has key
cat .env | grep API_KEY
```

### "Conversation too long / expensive"
Lower max_round in `bullspin_agents.py` or use cheaper model in `.env`:
```bash
DEFAULT_MODEL=qwen/qwen-2.5-72b-instruct  # Ultra cheap
```

### Want to kill it early?
`Ctrl+C` will stop gracefully and still save logs

---

## Quick Reference

```bash
# Research
python run_bullspin.py --scenario research

# Writing
python run_bullspin.py --scenario writing --threads "url1,url2"

# Tracking
python run_bullspin.py --scenario tracking

# View logs
cat logs/scenario-*.md

# Clean logs (start fresh)
rm logs/*

# Check cost
grep -i "tokens" logs/*.md  # If you track token usage
```

---

## What About the Notebook?

**You don't need it!**

The notebook (`bullspin_mvp.ipynb`) does the same thing as `run_bullspin.py`, just in a different format.

**Use notebook if**: You want interactive, step-by-step exploration
**Use CLI script if**: You want simple, familiar command-line workflow

**Both produce identical results** - same agents, same conversations, same logs.

---

## For Copenhagen Presentation

**After running all scenarios**:

```bash
# 1. Review all logs
ls -lh logs/

# 2. Extract best excerpts for slides
grep -A 10 "ResearchAgent" logs/scenario-1-research-*.md > excerpts.txt

# 3. Fill out learnings
vim learnings/week1-bullspin.md

# 4. Populate slides with real logs
# Edit slides/bullspin-presentation.md with your favorite editor
```

---

**Bottom line**: You're not missing anything by avoiding notebooks. CLI is simpler for your workflow!
