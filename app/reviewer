from .analyzer import run_flake8, analyze_ast_complexity
from .github_client import simulate_pr_comment

# This function combines analysis tools and posts simulated comments
def review_code(file_path):
    flake8_output = run_flake8(file_path)
    complexity_score = analyze_ast_complexity(file_path)
    comments = []

    if flake8_output:
        comments.append("Flake8 Issues:\n" + flake8_output)
    comments.append(f"AST Complexity Score: {complexity_score}")

    simulate_pr_comment(file_path, comments)
