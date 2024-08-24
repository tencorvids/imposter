from datetime import datetime
from pathlib import Path
import git

def create_commit(repo: git.Repo, repo_path: Path, commit_time: datetime):
    dummy_file = repo_path / "dummy_file.txt"
    with dummy_file.open("a") as f:
        f.write(f"Commit at {commit_time.strftime('%Y-%m-%d %H:%M:%S%z')}\n")

    repo.index.add([str(dummy_file)])
    commit_message = f"Commit at {commit_time.strftime('%Y-%m-%d %H:%M:%S%z')}"
    repo.index.commit(
        commit_message,
        author_date=commit_time,
        commit_date=commit_time
    )
