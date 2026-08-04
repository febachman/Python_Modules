#!/usr/bin/env python3

import random


def all_capital(players: list) -> list:
    return [name.capitalize() for name in players]


def only_capital(players: list) -> list:
    return [name for name in players if name.istitle()]


def scores_dict(players: list, min_score: int, max_score: int) -> dict:
    return {name: random.randint(min_score, max_score) for name in players}


def calculate_average(scores_dict: dict) -> float:
    if not scores_dict:
        return 0
    scores = scores_dict.values()
    total_score = sum(scores)
    total_players = len(scores)
    average = total_score / total_players
    return average


def high_scores(scores_dict, average):
    return {
        name: score for name, score
        in scores_dict.items()
        if score > average
    }


def main():
    print("=== Game Data Alchemist ===")
    print()
    init_players = [
        'Alice', 'bob', 'Charlie',
        'dylan', 'Emma', 'Gregory',
        'john', 'kevin', 'Liam'
    ]
    print(f"Initial list of players: {init_players}")
    print()
    print(f"New list with all names capitalized: {all_capital(init_players)}")
    print()
    print(f"New list of capitalized names only: {only_capital(init_players)}")
    print()
    score_dict = scores_dict(all_capital(init_players), 50, 1000)
    print(f"Score dict: {score_dict}")
    print()
    average_score = calculate_average(score_dict)
    print(f"Score average is {average_score:.2f}")
    print()
    high_score = high_scores(score_dict, average_score)
    print(f"High scores: {high_score}")


if __name__ == "__main__":
    main()
