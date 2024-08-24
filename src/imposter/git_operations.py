from datetime import datetime
from pathlib import Path
import git
from typing import Union

def create_commit(repo: git.Repo, repo_path: Path, commit_time: datetime):
    dummy_file = repo_path / "dummy_file.txt"
    with dummy_file.open("a") as f:
        f.write(f"Commit at {commit_time.strftime('%Y-%m-%d %H:%M:%S%z')}\n")

    repo.index.add([str(dummy_file)])
    commit_message = f"Commit at {commit_time.strftime('%Y-%m-%d %H:%M:%S%z')}"
    
    config_reader = repo.config_reader()

    def get_config_value(section: str, option: str) -> str:
        value: Union[int, float, str, bool] = config_reader.get_value(section, option)
        return str(value).strip('"') if value is not None else ""

    author_name = get_config_value("user", "name")
    author_email = get_config_value("user", "email")
    
    if not author_name or not author_email:
        raise ValueError("Git user name or email is not configured")

    author = git.Actor(author_name, author_email)
    
    repo.index.commit(
        commit_message,
        author=author,
        committer=author,
        author_date=commit_time,
        commit_date=commit_time
    )
