#!/usr/bin/env python3
import os
import sys
import json
import logging

from github import Github
from github.GithubException import GithubException
from codemaintainergenie import tools
from codemaintainergenie.memory import Memory

def get_repo():
    token = os.environ.get("GITHUB_TOKEN")
    repo_fullname = os.environ.get("GITHUB_REPOSITORY")
    if not token or not repo_fullname:
        logging.error("[Agent] Missing GITHUB_TOKEN or GITHUB_REPOSITORY env")
        sys.exit(1)
    g = Github(token)
    try:
        repo = g.get_repo(repo_fullname)
        return repo
    except GithubException as e:
        logging.error(f"[Agent] Could not access repo: {e}")
        sys.exit(1)

def handle_issue_event(event, repo):
    issue_data = event.get("issue", {})
    issue_number = issue_data.get("number", None)
    if not issue_number:
        issue_number = issue_data.get("number") or issue_data.get("id")
    labels = [label["name"] for label in issue_data.get("labels", [])]
    try:
        issue = repo.get_issue(number=issue_data["number"])
    except Exception as e:
        logging.error(f"[Agent] Unable to fetch issue #{issue_data.get('number')}: {e}")
        return
    if any(l in ("bug", "enhancement") for l in labels):
        message = "👋 ¡Hola! Soy CodeMaintainerGenie. He registrado el issue y lo analizaré en breve."
        tools.comment_issue(issue, message)
        logging.info(f"[Agent] Commented on issue #{issue.number} due to label trigger.")

def handle_comment_event(event, repo):
    issue_data = event.get("issue", {})
    comment_data = event.get("comment", {})
    if not issue_data or not comment_data:
        logging.warning("[Agent] Missing issue or comment data in event.")
        return
    try:
        issue = repo.get_issue(number=issue_data["number"])
    except Exception as e:
        logging.error(f"[Agent] Unable to fetch issue #{issue_data.get('number')}: {e}")
        return
    comment_body = comment_data.get("body", "")
    if "@Genie" in comment_body or "@codemaintainergenie" in comment_body:
        message = "🤖 A la orden. Estoy revisando tu solicitud."
        tools.comment_issue(issue, message)
        logging.info(f"[Agent] Responded to @Genie mention in comment on issue #{issue.number}.")

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
    logging.info(f"[Agent] Event loaded. (Payload not shown for brevity)")

    repo = get_repo()
    mem = Memory(repo)
    logging.info(f"[Agent] Memory loaded: {len(mem.commits)} commits, {len(mem.open_issues)} open issues.")

    if event_name == "issues":
        handle_issue_event(event, repo)
    elif event_name == "issue_comment":
        handle_comment_event(event, repo)
    else:
        logging.info("[Agent] No action for this event.")

if __name__ == "__main__":
    main()