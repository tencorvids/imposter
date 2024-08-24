from dataclasses import dataclass
from datetime import datetime
import random

@dataclass
class Profile:
    name: str
    min_daily_commits: int
    max_daily_commits: int
    work_days: list[int]
    work_hours: tuple[int, int]

    def should_commit_on_day(self, date: datetime) -> bool:
        return date.weekday() in self.work_days

    def get_commit_time(self, date: datetime) -> datetime:
        hour = random.randint(self.work_hours[0], self.work_hours[1])
        minute = random.randint(0, 59)
        second = random.randint(0, 59)
        return date.replace(hour=hour, minute=minute, second=second)

PROFILES = {
    "weekend-warrior": Profile(
        "weekend-warrior", 0, 10, [5, 6], (10, 22)
    ),
    "workday-andy": Profile(
        "workday-andy", 1, 5, [0, 1, 2, 3, 4], (9, 17)
    ),
    "grind-dont-stop": Profile(
        "grind-dont-stop", 3, 15, [0, 1, 2, 3, 4, 5, 6], (0, 23)
    ),
    "does-not-sleep": Profile(
        "does-not-sleep", 1, 8, [0, 1, 2, 3, 4, 5, 6], (20, 4)
    ),
    "early-bird": Profile(
        "early-bird", 1, 8, [0, 1, 2, 3, 4, 5, 6], (5, 13)
    ),
    "lunch-break-learner": Profile(
        "lunch-break-learner", 1, 3, [0, 1, 2, 3, 4], (12, 14)
    ),
    "weekend-procrastinator": Profile(
        "weekend-procrastinator", 5, 20, [6], (14, 23)
    ),
}

def get_profile(profile_name: str) -> Profile:
    return PROFILES[profile_name]
