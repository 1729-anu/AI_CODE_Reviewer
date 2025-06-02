# Simulate GitHub Pull Request comment

def simulate_pr_comment(file_path, comments):
    print(f"Reviewing {file_path}...\n")
    for comment in comments:
        print(f"[Comment] {comment}")
