import random
from datetime import datetime, timedelta, timezone
from pathlib import Path

import click
import git

from imposter.profiles import get_profile
from imposter.git_operations import create_commit

@click.command()
@click.option(
    "--repo-path",
    type=click.Path(exists=True, file_okay=False, dir_okay=True, path_type=Path),
    required=True,
    help="Path to the git repository",
)
@click.option(
    "--start-date",
    type=click.DateTime(formats=["%Y-%m-%d"]),
    required=True,
    help="Start date for generating history (format: YYYY-MM-DD)",
)
@click.option(
    "--end-date",
    type=click.DateTime(formats=["%Y-%m-%d"]),
    required=True,
    help="End date for generating history (format: YYYY-MM-DD)",
)
@click.option(
    "--profile",
    type=click.Choice(["weekend-warrior", "workday-andy", "grind-dont-stop", "does-not-sleep", "early-bird", "lunch-break-learner", "weekend-procrastinator"]),
    default="workday-andy",
    help="Commit profile to use",
)
def main(repo_path: Path, start_date: datetime, end_date: datetime, profile: str):
    """Generate fake git commit history with customizable profiles."""
    repo = git.Repo(repo_path)
    
    start_date = start_date.replace(tzinfo=timezone.utc)
    end_date = end_date.replace(tzinfo=timezone.utc)

    click.echo(f"Generating fake git history from {start_date.date()} to {end_date.date()}")
    click.echo(f"Repository path: {repo_path}")
    click.echo(f"Using profile: {profile}")

    profile_config = get_profile(profile)

    current_date = start_date
    while current_date <= end_date:
        if profile_config.should_commit_on_day(current_date):
            num_commits = random.randint(
                profile_config.min_daily_commits, profile_config.max_daily_commits
            )
            for _ in range(num_commits):
                commit_time = profile_config.get_commit_time(current_date)
                create_commit(repo, repo_path, commit_time)

        current_date += timedelta(days=1)

    click.echo("Fake git history generated successfully!")

if __name__ == "__main__":
    main()
