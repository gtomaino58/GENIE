#!/usr/bin/env python3
import os
import sys
import json
import logging

def main():
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    event_path = os.environ.get("GITHUB_EVENT_PATH")
    event_name = os.environ.get("GITHUB_EVENT_NAME", "unknown")
    logging.info(f"[Agent] Event name: {event_name}")

    if not event_path or not os.path.exists(event_path):
        logging.error("[Agent] GITHUB_EVENT_PATH not set or file does not exist.")
        sys.exit(1)

    with open(event_path, "r", encoding="utf-8") as f:
        event = json.load(f)
    logging.info(f"[Agent] Event payload: {json.dumps(event, indent=2, ensure_ascii=False)}")

    # Minimal demo logic for triggers
    if event_name == "issues":
        labels = [label['name'] for label in event.get("issue", {}).get("labels", [])]
        if any(l in ("bug", "enhancement") for l in labels):
            logging.info("[Agent] Would react to issue labeled as bug or enhancement.")
    elif event_name == "issue_comment":
        comment_body = event.get("comment", {}).get("body", "")
        if "@Genie" in comment_body or "@codemaintainergenie" in comment_body:
            logging.info("[Agent] Would react to @Genie mention in comment.")
    else:
        logging.info("[Agent] No action for this event.")

if __name__ == "__main__":
    main()