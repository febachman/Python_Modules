#!/usr/bin/env python3

from typing import Any
from data_generator import FuncMageDataGenerator


def artifact_sorter(artifacts: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Sort magical artifacts by power level in descending order."""
    return sorted(
        artifacts, key=lambda artifact: artifact["power"], reverse=True
    )


def power_filter(
    mages: list[dict[str, Any]], min_power: int
) -> list[dict[str, Any]]:
    """Filter mages by minimum power requirement using filter()."""
    return list(filter(lambda mage: mage["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    """Transform spell names by adding prefix and suffix using map()."""
    return list(map(lambda spell: f"* {spell} *", spells))


def mage_stats(mages: list[dict[str, Any]]) -> dict[str, Any]:
    """Calculate statistics (max, min, average power) using lambdas."""
    if not mages:
        return {"max_power": 0, "min_power": 0, "avg_power": 0.0}

    max_mage = max(mages, key=lambda m: m["power"])
    min_mage = min(mages, key=lambda m: m["power"])

    powers = list(map(lambda m: m["power"], mages))
    avg_power = round(sum(powers) / len(powers), 2)

    return {
        "max_power": max_mage["power"],
        "min_power": min_mage["power"],
        "avg_power": avg_power,
    }


if __name__ == "__main__":
    print("=== Testing Exercise 0: Lambda Sanctum ===")

    artifacts = FuncMageDataGenerator.generate_artifacts(4)
    mages = FuncMageDataGenerator.generate_mages(5)
    spells = FuncMageDataGenerator.generate_spells(4)

    print("\n--- Testing artifact_sorter ---")
    print("Original:", [(a['name'], a['power']) for a in artifacts])
    sorted_arts = artifact_sorter(artifacts)
    print("Sorted (desc):", [(a['name'], a['power']) for a in sorted_arts])

    print("\n--- Testing power_filter (min_power = 70) ---")
    print("All mages:", [(m['name'], m['power']) for m in mages])
    filtered_mages = power_filter(mages, 70)
    print(
        "Filtered (>= 70):", [(m['name'], m['power']) for m in filtered_mages]
    )

    print("\n--- Testing spell_transformer ---")
    print("Original spells:", spells)
    print("Transformed:", spell_transformer(spells))

    print("\n--- Testing mage_stats ---")
    stats = mage_stats(mages)
    print("Stats calculated:", stats)
