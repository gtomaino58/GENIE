import logging

def read_file(filepath):
    logging.info(f"[Tool] read_file called with: {filepath}")

def write_file(filepath, content):
    logging.info(f"[Tool] write_file called with: {filepath}, content length: {len(content)}")

def list_issues():
    logging.info("[Tool] list_issues called")

def get_issue_comments(issue_number):
    logging.info(f"[Tool] get_issue_comments called for issue #{issue_number}")

def run_tests():
    logging.info("[Tool] run_tests called")

def open_pr(title, body, head, base):
    logging.info(f"[Tool] open_pr called with title: '{title}', head: {head}, base: {base}")

def comment_issue(issue_number, comment):
    logging.info(f"[Tool] comment_issue called for issue #{issue_number}: {comment}")