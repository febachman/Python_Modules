#!/usr/bin/env python3

from datetime import datetime
from enum import Enum
from typing import List
from pydantic import BaseModel, Field, ValidationError, model_validator
from data_generator import DataConfig, CrewMissionGenerator


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

    # Valid mission
    config = DataConfig()
    mission_gen = CrewMissionGenerator(config)

    raw_missions = mission_gen.generate_mission_data(3)
    print(f"Successfully generated & validated {len(raw_missions)} missions:")
    for raw in raw_missions:
        try:
            mission = SpaceMission(**raw)
            crew_details = "".join(
                f"\n      - {m.name} ({m.rank.value}) - {m.specialization}"
                for m in mission.crew
            )
            print(
                f"  - [{mission.mission_id}]\n"
                f"  - {mission.mission_name}\n"
                f"  - Destination: {mission.destination}\n"
                f"  - Crew Size: {len(mission.crew)}\n"
                f"  - Crew Members:{crew_details}\n"
                f"  - Budget: ${mission.budget_millions}M"
            )
            print("=" * 41)
        except ValidationError as e:
            print(f"  - Validation failed for {raw.get('mission_id')}: {e}")

    # Invalid mission (Missing Commander/Captain)
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
            ]
        )
    except ValidationError as e:
        for error in e.errors():
            print(error["msg"])


if __name__ == "__main__":
    main()
