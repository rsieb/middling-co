#!/usr/bin/env python3
"""
Bullspin Detector - Command Line Runner

Run agent scenarios from the command line without Jupyter.

Usage:
    python run_bullspin.py --scenario research
    python run_bullspin.py --scenario writing --threads "thread1,thread2"
    python run_bullspin.py --scenario tracking
"""

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path

from autogen import AssistantAgent, UserProxyAgent, GroupChat, GroupChatManager
from bullspin_agents import (
    SUPERVISOR_CONFIG,
    RESEARCH_CONFIG,
    WRITER_CONFIG,
    TRACKER_CONFIG,
    USER_PROXY_CONFIG,
    BULLSPIN_GROUPCHAT_CONFIG,
)


def create_agents():
    """Create the agent team."""
    supervisor = AssistantAgent(
        name=SUPERVISOR_CONFIG["name"],
        system_message=SUPERVISOR_CONFIG["system_message"],
        llm_config=SUPERVISOR_CONFIG["llm_config"],
    )

    research_agent = AssistantAgent(
        name=RESEARCH_CONFIG["name"],
        system_message=RESEARCH_CONFIG["system_message"],
        llm_config=RESEARCH_CONFIG["llm_config"],
    )

    writer_agent = AssistantAgent(
        name=WRITER_CONFIG["name"],
        system_message=WRITER_CONFIG["system_message"],
        llm_config=WRITER_CONFIG["llm_config"],
    )

    tracker_agent = AssistantAgent(
        name=TRACKER_CONFIG["name"],
        system_message=TRACKER_CONFIG["system_message"],
        llm_config=TRACKER_CONFIG["llm_config"],
    )

    roland = UserProxyAgent(
        name=USER_PROXY_CONFIG["name"],
        system_message=USER_PROXY_CONFIG["system_message"],
        human_input_mode=USER_PROXY_CONFIG["human_input_mode"],
        max_consecutive_auto_reply=USER_PROXY_CONFIG["max_consecutive_auto_reply"],
        code_execution_config=USER_PROXY_CONFIG["code_execution_config"],
    )

    return [supervisor, research_agent, writer_agent, tracker_agent, roland]


def save_logs(groupchat, scenario_name):
    """Save conversation logs to files."""
    # Create logs directory if it doesn't exist
    Path("logs").mkdir(exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")

    # Save JSON
    json_file = f"logs/{scenario_name}-{timestamp}.json"
    with open(json_file, 'w') as f:
        json.dump(groupchat.messages, f, indent=2)

    # Save Markdown
    md_file = f"logs/{scenario_name}-{timestamp}.md"
    with open(md_file, 'w') as f:
        f.write(f"# Bullspin Detector - {scenario_name.replace('-', ' ').title()}\n\n")
        f.write(f"**Date**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        f.write("---\n\n")

        for msg in groupchat.messages:
            speaker = msg.get('name', 'Unknown')
            content = msg.get('content', '')
            f.write(f"## {speaker}\n\n")
            f.write(f"{content}\n\n")
            f.write("---\n\n")

    print(f"\n✅ Logs saved:")
    print(f"   - {json_file}")
    print(f"   - {md_file}")

    return json_file, md_file


def scenario_research(topics=None):
    """Scenario 1: Find relevant Reddit threads."""

    if topics is None:
        topics = [
            "Trump tariff proposals",
            "Immigration policy debate"
        ]

    prompt = f"""Team, it's time to start our Reddit growth experiment for Bullspin Detector.

Our mission this week: Get 1 user signup from Reddit.

First task: Research Agent, please find 3-5 relevant Reddit threads where we could
naturally introduce Bullspin Detector.

Focus on recent threads (last 24-48 hours) in:
- r/politics
- r/AskPolitics
- r/NeutralPolitics
- r/PoliticalDiscussion

Look for threads about political proposals, fact-checking, or policy debates.

Current events to consider:
{chr(10).join(f'- {topic}' for topic in topics)}

Everyone else: Provide input and help prioritize once we have options.

Let's go!
"""

    print("\n" + "="*80)
    print("SCENARIO 1: RESEARCH - Finding Reddit Threads")
    print("="*80)
    print(f"\nTopics: {', '.join(topics)}\n")

    agents = create_agents()
    groupchat = GroupChat(
        agents=agents,
        messages=[],
        max_round=BULLSPIN_GROUPCHAT_CONFIG["max_round"],
        speaker_selection_method=BULLSPIN_GROUPCHAT_CONFIG["speaker_selection_method"],
    )
    manager = GroupChatManager(groupchat=groupchat)

    # Start conversation
    roland = agents[-1]
    roland.initiate_chat(manager, message=prompt)

    # Save logs
    save_logs(groupchat, "scenario-1-research")

    print("\n" + "="*80)
    print("NEXT STEP: Review logs/scenario-1-research-*.md")
    print("Then run: python run_bullspin.py --scenario writing --threads \"[thread URLs]\"")
    print("="*80 + "\n")


def scenario_writing(threads):
    """Scenario 2: Draft comments for selected threads."""

    if not threads:
        print("ERROR: No threads provided. Use --threads 'thread1,thread2'")
        sys.exit(1)

    thread_list = threads.split(',')

    prompt = f"""Team, based on our research, let's draft comments for these threads:

{chr(10).join(f'{i+1}. {thread.strip()}' for i, thread in enumerate(thread_list))}

Writer Agent: Please draft thoughtful comments for each thread that:
1. Contribute genuine value to the discussion
2. Naturally mention Bullspin Detector
3. Follow Reddit etiquette (helpful, not spammy)

Tracker Agent: Create trackable links for each thread.

Supervisor: Coordinate and prioritize.

Let's create drafts for my review!
"""

    print("\n" + "="*80)
    print("SCENARIO 2: WRITING - Drafting Reddit Comments")
    print("="*80)
    print(f"\nThreads: {len(thread_list)}\n")

    agents = create_agents()
    groupchat = GroupChat(
        agents=agents,
        messages=[],
        max_round=BULLSPIN_GROUPCHAT_CONFIG["max_round"],
        speaker_selection_method=BULLSPIN_GROUPCHAT_CONFIG["speaker_selection_method"],
    )
    manager = GroupChatManager(groupchat=groupchat)

    # Start conversation
    roland = agents[-1]
    roland.initiate_chat(manager, message=prompt)

    # Save logs
    save_logs(groupchat, "scenario-2-writing")

    print("\n" + "="*80)
    print("NEXT STEP: Review logs/scenario-2-writing-*.md")
    print("Edit drafts if needed, then post manually to Reddit")
    print("After posting, run: python run_bullspin.py --scenario tracking")
    print("="*80 + "\n")


def scenario_tracking():
    """Scenario 3: Track clicks and signups."""

    prompt = """Team, I've posted the comments to Reddit. Let's monitor results.

Tracker Agent: Please check analytics and report:
- Total clicks
- Total signups
- Performance by thread

Supervisor: Coordinate follow-up actions based on results.

Let's see if we got our signup!
"""

    print("\n" + "="*80)
    print("SCENARIO 3: TRACKING - Monitoring Results")
    print("="*80 + "\n")

    agents = create_agents()
    groupchat = GroupChat(
        agents=agents,
        messages=[],
        max_round=BULLSPIN_GROUPCHAT_CONFIG["max_round"],
        speaker_selection_method=BULLSPIN_GROUPCHAT_CONFIG["speaker_selection_method"],
    )
    manager = GroupChatManager(groupchat=groupchat)

    # Start conversation
    roland = agents[-1]
    roland.initiate_chat(manager, message=prompt)

    # Save logs
    save_logs(groupchat, "scenario-3-tracking")

    print("\n" + "="*80)
    print("NEXT STEP: Review logs/scenario-3-tracking-*.md")
    print("Document learnings in learnings/week1-bullspin.md")
    print("Populate slides/bullspin-presentation.md with real logs")
    print("="*80 + "\n")


def main():
    parser = argparse.ArgumentParser(
        description="Run Bullspin Detector agent scenarios"
    )
    parser.add_argument(
        "--scenario",
        choices=["research", "writing", "tracking"],
        required=True,
        help="Which scenario to run"
    )
    parser.add_argument(
        "--topics",
        help="Comma-separated topics for research (e.g., 'topic1,topic2')"
    )
    parser.add_argument(
        "--threads",
        help="Comma-separated thread URLs for writing (e.g., 'url1,url2')"
    )

    args = parser.parse_args()

    try:
        if args.scenario == "research":
            topics = args.topics.split(',') if args.topics else None
            scenario_research(topics)
        elif args.scenario == "writing":
            scenario_writing(args.threads)
        elif args.scenario == "tracking":
            scenario_tracking()
    except KeyboardInterrupt:
        print("\n\n⚠️  Interrupted by user")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
