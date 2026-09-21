#!/usr/bin/env python3

from datetime import datetime
from enum import Enum
from typing import List
from pydantic import BaseModel, Field, ValidationError, model_validator


class Rank(str, Enum):
    cadet = "cadet"
    officer = "officer"
    lieutenant = "lieutenant"
    captain = "captain"
    commander = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=2, max_length=50)
    rank: Rank
    age: int = Field(..., ge=18, le=80)
    specialization: str = Field(..., min_length=3, max_length=30)
    years_experience: int = Field(..., ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    mission_id: str = Field(..., min_length=5, max_length=15)
    mission_name: str = Field(..., min_length=3, max_length=100)
    destination: str = Field(..., min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(..., ge=1, le=3650)
    crew: List[CrewMember] = Field(..., min_length=1, max_length=12)
    mission_status: str = "planned"
    budget_millions: float = Field(..., ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def validate_mission_rules(self) -> "SpaceMission":
        # Rule 1: Mission ID must start with "M"
        if not self.mission_id.startswith("M"):
            raise ValueError('Mission ID must start with "M"')

        # Rule 2: Must have at least one Commander or Captain
        has_leadership = any(
            member.rank in (Rank.commander, Rank.captain)
            for member in self.crew
        )
        if not has_leadership:
            raise ValueError(
                "Mission must have at least one Commander or Captain"
            )

        # Rule 3: All crew members must be active
        if not all(member.is_active for member in self.crew):
            raise ValueError("All crew members must be active")

        # Rule 4: Long missions (>365 days) need 50% experienced crew (5+years)
        if self.duration_days > 365:
            experienced_count = sum(
                1 for member in self.crew if member.years_experience >= 5
            )
            required_count = len(self.crew) * 0.5
            if experienced_count < required_count:
                raise ValueError(
                    "Long missions (> 365 days) need at least "
                    "50% experienced crew (5+ years)"
                )

        return self


def main() -> None:
    print("Space Mission Crew Validation")
    print("=" * 41)

    # 1. Creating a valid mission instance
    try:
        valid_mission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime(2024, 9, 1, 0, 0, 0),
            duration_days=900,  # Long mission, requires experienced crew
            budget_millions=2500.0,
            crew=[
                CrewMember(
                    member_id="CRM001",
                    name="Sarah Connor",
                    rank=Rank.commander,
                    age=42,
                    specialization="Mission Command",
                    years_experience=15,
                ),
                CrewMember(
                    member_id="CRM002",
                    name="John Smith",
                    rank=Rank.lieutenant,
                    age=34,
                    specialization="Navigation",
                    years_experience=8,
                ),
                CrewMember(
                    member_id="CRM003",
                    name="Alice Johnson",
                    rank=Rank.officer,
                    age=28,
                    specialization="Engineering",
                    years_experience=3,
                ),
            ],
        )

        print("Valid mission created:")
        print(f"Mission: {valid_mission.mission_name}")
        print(f"ID: {valid_mission.mission_id}")
        print(f"Destination: {valid_mission.destination}")
        print(f"Duration: {valid_mission.duration_days} days")
        print(f"Budget: ${valid_mission.budget_millions}M")
        print(f"Crew size: {len(valid_mission.crew)}")
        print("Crew members:")
        for member in valid_mission.crew:
            print(
                f"  - {member.name} ({member.rank.value})"
                f" - {member.specialization}"
            )

    except ValidationError as e:
        print(f"Unexpected validation error: {e}")

    # 2. Attempting to create an invalid mission (Missing Commander/Captain)
    print("=" * 41)
    print()
    print("Expected validation error:")
    try:
        SpaceMission(
            mission_id="M_INVALID_01",
            mission_name="Rookie Run",
            destination="Moon",
            launch_date=datetime.now(),
            duration_days=30,
            budget_millions=50.0,
            crew=[
                CrewMember(
                    member_id="CRM999",
                    name="Bob Rookie",
                    rank=Rank.cadet,
                    age=20,
                    specialization="General",
                    years_experience=0,
                )
            ],  # Missing Commander or Captain!
        )
    except ValidationError as e:
        for error in e.errors():
            print(error["msg"])


if __name__ == "__main__":
    main()
