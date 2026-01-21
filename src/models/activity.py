from dataclasses import dataclass
from datetime import datetime

@dataclass
class Activity:
    activity_name: str
    category: str
    duration_minutes: int
    activity_date: date

