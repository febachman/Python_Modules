#!/usr/bin/env python3

import sys


def process_score(args: list[str]) -> list[int]:
    valid_scores = []
    invalid_scores = []
    for param in args:
        try:
            score = int(param)
            valid_scores.append(score)
        except ValueError:
            invalid_scores.append(param)
    if not valid_scores:
        for invalid in invalid_scores:
            print(f"Invalid parameter: '{invalid}'")
    return valid_scores


def score_analytics(scores: list[int]) -> None:
    print(f"Scores processed: {scores}")
    total_players: int = len(scores)
    print(f"Total players: {total_players}")
    total_score: int = sum(scores)
    print(f"Total score: {total_score}")
    average_score: float = total_score / total_players
    print(f"Average score: {round(average_score, 1)}")
    high_score: int = max(scores)
    print(f"High score: {high_score}")
    low_score: int = min(scores)
    print(f"Low score: {low_score}")
    score_range: int = high_score - low_score
    print(f"Score range: {score_range}")


def main():
    print("=== Player Score Analytics ===")
    if len(sys.argv) <= 1:
        print("No scores provided. Usage: python3 ft_score_analytics.py ...")
        return
    valid_scores = process_score(sys.argv[1:])
    if not valid_scores:
        print("No scores provided. Usage: python3 ft_score_analytics.py ...")
        return
    score_analytics(valid_scores)


if __name__ == "_main_":
    main()
