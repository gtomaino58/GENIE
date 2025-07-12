import logging

class Memory:
    def __init__(self, repo):
        self.repo = repo
        self._current_branch = None
        self._commits = []
        self._open_issues = []
        self._closed_issues = []
        self._load_memory()

    def _load_memory(self):
        try:
            self._current_branch = self.repo.default_branch
            self._commits = list(self.repo.get_commits(sha=self._current_branch))[:10]
            self._open_issues = list(self.repo.get_issues(state="open"))
            self._closed_issues = list(self.repo.get_issues(state="closed"))[:20]
            logging.info(f"[Memory] Loaded: {len(self._commits)} commits, {len(self._open_issues)} open, {len(self._closed_issues)} closed issues")
        except Exception as e:
            logging.error(f"[Memory] Failed to load memory: {e}")
            self._commits = []
            self._open_issues = []
            self._closed_issues = []
            self._current_branch = "main"

    @property
    def commits(self):
        return self._commits

    @property
    def open_issues(self):
        return self._open_issues

    @property
    def closed_issues(self):
        return self._closed_issues

    @property
    def current_branch(self):
        return self._current_branch