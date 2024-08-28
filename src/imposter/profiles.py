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
    commit_probability: float  # New field to represent the probability of committing on a given day

    def should_commit_on_day(self, date: datetime) -> bool:
        return date.weekday() in self.work_days and random.random() < self.commit_probability

    def get_commit_time(self, date: datetime) -> datetime:
        hour = random.randint(self.work_hours[0], self.work_hours[1])
        minute = random.randint(0, 59)
        second = random.randint(0, 59)
        return date.replace(hour=hour, minute=minute, second=second)

PROFILES = {
    "weekend-warrior": Profile(
        "weekend-warrior", 0, 5, [5, 6], (10, 22), 0.7
    ),
    "workday-andy": Profile(
        "workday-andy", 1, 5, [0, 1, 2, 3, 4], (9, 17), 0.8
    ),
    "rew": Profile(
        "rew", 1, 8, [0, 1, 2, 3, 4, 5, 6], (9, 23), 0.9
    ),
    "early-bird": Profile(
        "early-bird", 1, 5, [0, 1, 2, 3, 4, 5], (5, 13), 0.7
    ),
    "lunch-break-learner": Profile(
        "lunch-break-learner", 1, 3, [0, 1, 2, 3, 4], (12, 14), 0.6
    ),
    "night-owl": Profile(
        "night-owl", 1, 6, [0, 1, 2, 3, 4, 5, 6], (20, 2), 0.8
    ),
    "sporadic": Profile(
        "sporadic", 0, 10, [0, 1, 2, 3, 4, 5, 6], (0, 23), 0.5
    ),
}

def get_profile(profile_name: str) -> Profile:
    return PROFILES[profile_name]
