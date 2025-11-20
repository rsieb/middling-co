"""
Bullspin Detector - Trackable Link Generator

Generates UTM-tagged links for Reddit comments to track attribution.

Usage:
    from tracker.links import create_trackable_link, log_link

    link = create_trackable_link(
        subreddit="AskPolitics",
        thread_id="abc123",
        date="2025-11-20"
    )

    log_link(link, "r/AskPolitics - How to fact-check claims?")
"""

import json
from datetime import datetime
from urllib.parse import urlencode

# Base URL for Bullspin Detector
BASE_URL = "https://bullspin.app"

# Log file for tracking
LINKS_LOG_FILE = "tracker/links_log.json"


def create_trackable_link(
    subreddit: str,
    thread_id: str,
    date: str = None,
    base_url: str = BASE_URL
) -> str:
    """
    Create a trackable link with UTM parameters.

    Args:
        subreddit: Name of subreddit (e.g., "AskPolitics")
        thread_id: Reddit thread ID or slug
        date: Date string (YYYY-MM-DD), defaults to today
        base_url: Base URL for Bullspin (default: https://bullspin.app)

    Returns:
        Full trackable URL

    Example:
        >>> create_trackable_link("AskPolitics", "abc123")
        'https://bullspin.app?utm_source=reddit&utm_medium=comment&utm_campaign=askpolitics-abc123&utm_content=2025-11-20'
    """
    if date is None:
        date = datetime.now().strftime("%Y-%m-%d")

    # Clean subreddit name (remove r/ if present, lowercase)
    subreddit_clean = subreddit.lower().replace("r/", "")

    # Build UTM parameters
    utm_params = {
        "utm_source": "reddit",
        "utm_medium": "comment",
        "utm_campaign": f"{subreddit_clean}-{thread_id}",
        "utm_content": date,
    }

    # Construct full URL
    full_url = f"{base_url}?{urlencode(utm_params)}"

    return full_url


def log_link(
    link: str,
    thread_description: str,
    subreddit: str = None,
    thread_url: str = None
) -> dict:
    """
    Log a trackable link to JSON file for later analysis.

    Args:
        link: The trackable URL that was created
        thread_description: Brief description of the thread
        subreddit: Subreddit name (optional)
        thread_url: Full Reddit thread URL (optional)

    Returns:
        Link entry dict
    """
    # Load existing log
    try:
        with open(LINKS_LOG_FILE, 'r') as f:
            log = json.load(f)
    except FileNotFoundError:
        log = {"links": []}

    # Create entry
    entry = {
        "link": link,
        "created_at": datetime.now().isoformat(),
        "thread_description": thread_description,
        "subreddit": subreddit,
        "thread_url": thread_url,
        "status": "pending",  # pending, posted, clicked, signup
        "clicks": 0,
        "signups": 0,
    }

    # Add to log
    log["links"].append(entry)

    # Save
    with open(LINKS_LOG_FILE, 'w') as f:
        json.dump(log, f, indent=2)

    return entry


def update_link_status(
    link: str,
    status: str = None,
    clicks: int = None,
    signups: int = None
) -> dict:
    """
    Update status of a tracked link.

    Args:
        link: The trackable URL to update
        status: New status (optional)
        clicks: Click count (optional)
        signups: Signup count (optional)

    Returns:
        Updated entry dict or None if not found
    """
    # Load log
    try:
        with open(LINKS_LOG_FILE, 'r') as f:
            log = json.load(f)
    except FileNotFoundError:
        return None

    # Find and update entry
    for entry in log["links"]:
        if entry["link"] == link:
            if status is not None:
                entry["status"] = status
            if clicks is not None:
                entry["clicks"] = clicks
            if signups is not None:
                entry["signups"] = signups
            entry["updated_at"] = datetime.now().isoformat()

            # Save
            with open(LINKS_LOG_FILE, 'w') as f:
                json.dump(log, f, indent=2)

            return entry

    return None


def get_summary() -> dict:
    """
    Get summary statistics of all tracked links.

    Returns:
        Summary dict with totals
    """
    try:
        with open(LINKS_LOG_FILE, 'r') as f:
            log = json.load(f)
    except FileNotFoundError:
        return {
            "total_links": 0,
            "total_clicks": 0,
            "total_signups": 0,
            "conversion_rate": 0,
            "by_subreddit": {}
        }

    total_links = len(log["links"])
    total_clicks = sum(entry.get("clicks", 0) for entry in log["links"])
    total_signups = sum(entry.get("signups", 0) for entry in log["links"])

    # By subreddit
    by_subreddit = {}
    for entry in log["links"]:
        subreddit = entry.get("subreddit", "unknown")
        if subreddit not in by_subreddit:
            by_subreddit[subreddit] = {
                "links": 0,
                "clicks": 0,
                "signups": 0,
            }
        by_subreddit[subreddit]["links"] += 1
        by_subreddit[subreddit]["clicks"] += entry.get("clicks", 0)
        by_subreddit[subreddit]["signups"] += entry.get("signups", 0)

    return {
        "total_links": total_links,
        "total_clicks": total_clicks,
        "total_signups": total_signups,
        "conversion_rate": (total_signups / total_clicks * 100) if total_clicks > 0 else 0,
        "by_subreddit": by_subreddit,
    }


def print_summary():
    """Print formatted summary of all tracked links."""
    summary = get_summary()

    print("=" * 60)
    print("BULLSPIN DETECTOR - TRACKING SUMMARY")
    print("=" * 60)
    print(f"\nTotal links created: {summary['total_links']}")
    print(f"Total clicks: {summary['total_clicks']}")
    print(f"Total signups: {summary['total_signups']}")
    print(f"Conversion rate: {summary['conversion_rate']:.2f}%")

    if summary['by_subreddit']:
        print("\nBy Subreddit:")
        print("-" * 60)
        for subreddit, stats in summary['by_subreddit'].items():
            print(f"\n{subreddit}:")
            print(f"  Links: {stats['links']}")
            print(f"  Clicks: {stats['clicks']}")
            print(f"  Signups: {stats['signups']}")
            if stats['clicks'] > 0:
                conv = stats['signups'] / stats['clicks'] * 100
                print(f"  Conversion: {conv:.2f}%")

    print("\n" + "=" * 60)


# Example usage
if __name__ == "__main__":
    # Create a test link
    link = create_trackable_link(
        subreddit="AskPolitics",
        thread_id="test123"
    )
    print(f"Created link: {link}")

    # Log it
    entry = log_link(
        link=link,
        thread_description="Test thread about fact-checking",
        subreddit="AskPolitics",
        thread_url="https://reddit.com/r/AskPolitics/comments/test123"
    )
    print(f"Logged: {entry}")

    # Update with fake stats
    update_link_status(link, status="clicked", clicks=5, signups=1)

    # Print summary
    print_summary()
