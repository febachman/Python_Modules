#!/usr/bin/env python3

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, ValidationError
from data_generator import DataConfig, SpaceStationGenerator


class SpaceStation(BaseModel):
    station_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=1, max_length=50)
    crew_size: int = Field(..., ge=1, le=20)
    power_level: float = Field(..., ge=0.0, le=100.0)
    oxygen_level: float = Field(..., ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = True
    notes: Optional[str] = Field(None, max_length=200)


def main() -> None:
    print("Space Station Data Validation")
    print("=" * 40)

    # Initialize generator
    config = DataConfig()
    station_gen = SpaceStationGenerator(config)

    # 1. Generate and validate multiple valid stations
    raw_stations = station_gen.generate_station_data(5)
    print(
        f"Successfully generated and validated {len(raw_stations)} stations:"
    )

    for raw in raw_stations:
        try:
            station = SpaceStation(**raw)
            status = (
                "Operational" if station.is_operational else "Non-Operational"
            )
            print(
                f"  - [{station.station_id}] {station.name} "
                f"| Crew: {station.crew_size} | Status: {status}"
            )
        except ValidationError as e:
            print(f"  - Validation failed for {raw.get('station_id')}: {e}")

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
            notes=None,
        )
    except ValidationError as e:
        for error in e.errors():
            print(error["msg"])


if __name__ == "__main__":
    main()
