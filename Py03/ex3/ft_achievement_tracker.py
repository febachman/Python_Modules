#!/usr/bin/env python3

import random


def gen_player_achievements() -> set:
    achievements = [
        'Crafting Genius', 'Strategist', 'World Savior',
        'Speed Runner', 'Survivor', 'Master Explorer',
        'Treasure Hunter', 'Unstoppable', 'First Steps',
        'Collector Supreme', 'Untouchable', 'Sharp Mind', 'Boss Slayer'
    ]
    count = random.randint(1, len(achievements))
    return set(random.sample(achievements, count))


def players_stats(names: list, p1: set, p2: set, p3: set, p4: set) -> None:
    distinct = p1.union(p2, p3, p4)
    print(f"All distinct achievements: {distinct}")
    print()
    common = p1.intersection(p2, p3, p4)
    print(f"Common achievements: {common}")
    print()
    only_p1 = p1 - (p2 | p3 | p4)
    only_p2 = p2 - (p1 | p3 | p4)
    only_p3 = p3 - (p1 | p2 | p4)
    only_p4 = p4 - (p1 | p2 | p3)
    only = [only_p1, only_p2, only_p3, only_p4]
    for i in range(len(names)):
        print(f"Only {names[i]} has: {only[i]}")
    print()
    missing_p1 = distinct - p1
    missing_p2 = distinct - p2
    missing_p3 = distinct - p3
    missing_p4 = distinct - p4
    missing = [missing_p1, missing_p2, missing_p3, missing_p4]
    for i in range(len(names)):
        print(f"{names[i]} is missing: {missing[i]}")


def main():
    print("=== Achievement Tracker System ===")
    print()
    names = ['Alice', 'Bob', 'Charlie', 'Dylan']
    p1 = gen_player_achievements()
    p2 = gen_player_achievements()
    p3 = gen_player_achievements()
    p4 = gen_player_achievements()
    achievements = [p1, p2, p3, p4]
    for i in range(len(names)):
        print(f"Player {names[i]}: {achievements[i]}")
    print()
    players_stats(names, p1, p2, p3, p4)


if __name__ == "__main__":
    main()
