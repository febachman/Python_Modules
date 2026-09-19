#!/usr/bin/env python3

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, ValidationError


class SpaceStation(BaseModel):
    station_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=1, max_length=50)
    crew_size: int = Field(..., ge=1, le=20)
    power_level: float = Field(..., ge=0.0, le=100.0)
    oxygen_level: float = Field(..., ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = True
    notes: Optional[str] = Field(None, max_length=200)


def main():
    print("Space Station Data Validation")
    print("=" * 40)

    # 1. Creating a valid space station instance
    try:
        valid_station = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=6,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance="2026-06-01T08:30:00",  # String auto-coerced to datetime!
            notes="Routine maintenance completed successfully.",
        )

        print("Valid station created:")
        print(f"ID: {valid_station.station_id}")
        print(f"Name: {valid_station.name}")
        print(f"Crew: {valid_station.crew_size} people")
        print(f"Power: {valid_station.power_level}%")
        print(f"Oxygen: {valid_station.oxygen_level}%")
        status_text = (
            "Operational" if valid_station.is_operational else "Non-Operational"
        )
        print(f"Status: {status_text}")

    except ValidationError as e:
        print(f"Unexpected validation error: {e}")

    print("=" * 40)

    # 2. Attempting to create an invalid station (crew_size > 20)
    print("Expected validation error:")
    try:
        SpaceStation(
            station_id="BAD01",
            name="Overcrowded Station",
            crew_size=25,  # Invalid: exceeds max limit of 20
            power_level=50.0,
            oxygen_level=50.0,
            last_maintenance=datetime.now(),
        )
    except ValidationError as e:
        # Pydantic's error messages are detailed; we pull out the specific error message text
        for error in e.errors():
            print(error["msg"])


if __name__ == "__main__":
    main()
