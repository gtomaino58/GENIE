import logging

class Memory:
    def __init__(self, repo):
        self.repo = repo

    def last_commits(self, n=10):
        logging.info(f"[Memory] Fetching last {n} commits (stub)")
        return []

    def issue_history(self):
        logging.info("[Memory] Fetching issue history (stub)")
        return {"open": [], "closed": []}

    def current_branch(self):
        logging.info("[Memory] Fetching current branch (stub)")
        return "main"