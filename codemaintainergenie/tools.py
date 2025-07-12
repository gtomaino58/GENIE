import logging
from github import GithubException
import subprocess

def read_file(repo, filepath, ref="main"):
    try:
        file_content = repo.get_contents(filepath, ref=ref)
        logging.info(f"[Tool] Read file: {filepath}@{ref}")
        return file_content.decoded_content.decode("utf-8")
    except GithubException as e:
        logging.error(f"[Tool] Failed to read file {filepath}@{ref}: {e}")
        return None

def write_file(repo, filepath, content, branch_name, commit_message):
    try:
        default_branch = repo.default_branch
        try:
            repo.get_branch(branch_name)
        except GithubException:
            # Create branch from default
            sb = repo.get_branch(default_branch)
            repo.create_git_ref(ref=f"refs/heads/{branch_name}", sha=sb.commit.sha)
            logging.info(f"[Tool] Created branch {branch_name} from {default_branch}")
        try:
            file = repo.get_contents(filepath, ref=branch_name)
            commit = repo.update_file(filepath, commit_message, content, file.sha, branch=branch_name)
            logging.info(f"[Tool] Updated file {filepath} in branch {branch_name}")
        except GithubException:
            commit = repo.create_file(filepath, commit_message, content, branch=branch_name)
            logging.info(f"[Tool] Created file {filepath} in branch {branch_name}")
        return commit
    except Exception as e:
        logging.error(f"[Tool] Failed to write file {filepath} in {branch_name}: {e}")
        return None

def list_issues(repo, state="open"):
    try:
        issues = list(repo.get_issues(state=state))
        logging.info(f"[Tool] Listed {len(issues)} {state} issues")
        return issues
    except GithubException as e:
        logging.error(f"[Tool] Failed to list issues: {e}")
        return []

def get_issue_comments(issue):
    try:
        comments = list(issue.get_comments())
        logging.info(f"[Tool] Got {len(comments)} comments for issue #{issue.number}")
        return comments
    except GithubException as e:
        logging.error(f"[Tool] Failed to get comments for issue #{issue.number}: {e}")
        return []

def run_tests():
    logging.info("[Tool] Running tests with pytest")
    try:
        result = subprocess.run(
            ["pytest", "-q"],
            capture_output=True,
            text=True,
            check=False
        )
        logging.info(f"[Tool] Tests exited with code {result.returncode}")
        return result.stdout, result.returncode
    except Exception as e:
        logging.error(f"[Tool] Error running pytest: {e}")
        return str(e), -1

def open_pr(repo, title, body, head_branch, base_branch="main"):
    try:
        pr = repo.create_pull(title=title, body=body, head=head_branch, base=base_branch)
        logging.info(f"[Tool] Opened PR '{title}' from {head_branch} to {base_branch}")
        return pr
    except GithubException as e:
        logging.error(f"[Tool] Failed to open PR: {e}")
        return None

def comment_issue(issue, comment_text):
    try:
        comment = issue.create_comment(comment_text)
        logging.info(f"[Tool] Commented on issue #{issue.number}: {comment_text}")
        return comment
    except GithubException as e:
        logging.error(f"[Tool] Failed to comment on issue #{issue.number}: {e}")
        return None