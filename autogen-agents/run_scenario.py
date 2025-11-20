"""
Run a startup scenario with the Middling Company agent team.

Usage:
    python run_scenario.py --scenario crisis
    python run_scenario.py --scenario planning
    python run_scenario.py --scenario operations
    python run_scenario.py --custom "Your custom scenario description"
"""

import argparse
from autogen import AssistantAgent, UserProxyAgent, GroupChat, GroupChatManager
from team_config import (
    ALICE_CONFIG,
    BOB_CONFIG,
    CHARLIE_CONFIG,
    FOUNDER_CONFIG,
    GROUP_CHAT_CONFIG,
)

# Predefined scenarios
SCENARIOS = {
    "crisis": """URGENT: A customer just tweeted that our app lost their data.

We need to:
1. Investigate what actually happened
2. Respond to them publicly on Twitter
3. Fix the underlying bug if there is one
4. Reach out to them directly to help recover their data
5. Update our docs/monitoring to prevent this

Who's taking what? Let's move fast but not break things further.""",

    "opportunity": """Someone on Reddit just posted in r/productivity asking:
"Is there a tool that does X, Y, and Z?"

And X, Y, and Z are EXACTLY what we're building!

How should we respond? Should we:
- Reply directly?
- What's our messaging?
- Should we offer them early access?
- Is this a marketing opportunity or just help one person?

Thoughts?""",

    "planning": """We have 2 weeks until our planned launch date.

Current status:
- Core functionality is working
- We have 10 feature requests from beta users
- 3 known bugs (2 minor, 1 moderate)
- No blog post written yet
- Marketing site needs copy
- Haven't set up analytics yet

What do we build vs cut? What's our launch plan?""",

    "operations": """Monday morning pile-up:

1. 5 customer support tickets came in over the weekend
2. Blog post is due Friday (not started)
3. Bug in production: some users can't upload files >10MB
4. Our hosting bill went up 3x (need to investigate why)
5. Competitor just launched a similar feature

We're 3 people. How do we prioritize? Who does what?""",

    "strategy": """We've been live for 1 month. Here's what we're seeing:

Metrics:
- 500 signups
- 150 active users
- 20% week-over-week growth
- $0 revenue (we're free right now)

Feedback themes:
- "Love it but need mobile app" (mentioned 15 times)
- "Confused by onboarding" (mentioned 8 times)
- "Want integrations with Slack/Notion" (mentioned 12 times)
- "Would pay for X feature" (mentioned 5 times)

Question: What do we focus on next month?
- Build mobile app?
- Fix onboarding?
- Start charging money?
- Build integrations?
- Something else?

Discuss and decide.""",
}


def create_agents():
    """Create the agent team."""

    alice = AssistantAgent(
        name=ALICE_CONFIG["name"],
        system_message=ALICE_CONFIG["system_message"],
        llm_config=ALICE_CONFIG["llm_config"],
    )

    bob = AssistantAgent(
        name=BOB_CONFIG["name"],
        system_message=BOB_CONFIG["system_message"],
        llm_config=BOB_CONFIG["llm_config"],
    )

    charlie = AssistantAgent(
        name=CHARLIE_CONFIG["name"],
        system_message=CHARLIE_CONFIG["system_message"],
        llm_config=CHARLIE_CONFIG["llm_config"],
    )

    founder = UserProxyAgent(
        name=FOUNDER_CONFIG["name"],
        system_message=FOUNDER_CONFIG["system_message"],
        human_input_mode=FOUNDER_CONFIG["human_input_mode"],
        max_consecutive_auto_reply=10,
        code_execution_config=False,  # Disable code execution for now
    )

    return [alice, bob, charlie, founder]


def run_scenario(scenario_text, agents):
    """Run a scenario with the agent team."""

    # Create group chat
    groupchat = GroupChat(
        agents=agents,
        messages=[],
        max_round=GROUP_CHAT_CONFIG["max_round"],
        speaker_selection_method=GROUP_CHAT_CONFIG["speaker_selection_method"],
    )

    manager = GroupChatManager(groupchat=groupchat)

    # Start the conversation
    # The founder (UserProxyAgent) initiates
    founder = agents[-1]  # Last agent is the founder

    print("\n" + "="*80)
    print("MIDDLING COMPANY - AGENT TEAM CONVERSATION")
    print("="*80)
    print(f"\nSCENARIO:\n{scenario_text}\n")
    print("="*80)
    print("\nCONVERSATION START:\n")

    founder.initiate_chat(
        manager,
        message=scenario_text,
    )

    print("\n" + "="*80)
    print("CONVERSATION END")
    print("="*80)


def main():
    parser = argparse.ArgumentParser(
        description="Run a startup scenario with Middling Company agents"
    )
    parser.add_argument(
        "--scenario",
        choices=list(SCENARIOS.keys()),
        help="Choose a predefined scenario",
    )
    parser.add_argument(
        "--custom",
        type=str,
        help="Provide a custom scenario description",
    )

    args = parser.parse_args()

    # Determine scenario text
    if args.custom:
        scenario_text = args.custom
    elif args.scenario:
        scenario_text = SCENARIOS[args.scenario]
    else:
        print("Error: Must provide either --scenario or --custom")
        print("\nAvailable scenarios:")
        for name, description in SCENARIOS.items():
            print(f"\n  {name}:")
            print(f"    {description[:100]}...")
        return

    # Create agents and run
    agents = create_agents()
    run_scenario(scenario_text, agents)


if __name__ == "__main__":
    main()
