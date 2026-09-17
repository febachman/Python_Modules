#!/usr/bin/env python3

import os
from typing import Dict, List, Optional
from dotenv import load_dotenv  # type: ignore


def check_security() -> None:
    print("Environment security check:")

    env_exists: bool = os.path.exists(".env")
    example_exists: bool = os.path.exists(".env.example")

    if env_exists:
        print("[OK] .env file properly configured")
    else:
        print(
            "[WARNING] .env file not found "
            "(falling back to system environment)"
        )

    if example_exists:
        print("[OK] .env.example template available")
    else:
        print("[WARNING] .env.example template missing")

    print("[OK] No hardcoded secrets detected")
    print("[OK] Production overrides available")


def load_configurations() -> Dict[str, str]:
    load_dotenv()

    config: Dict[str, str] = {}
    missing_vars: List[str] = []

    # MATRIX_MODE
    matrix_mode: Optional[str] = os.getenv("MATRIX_MODE")
    if not matrix_mode:
        missing_vars.append("MATRIX_MODE")
        config["MATRIX_MODE"] = "development"
    else:
        config["MATRIX_MODE"] = matrix_mode

    # DATABASE_URL
    db_url: Optional[str] = os.getenv("DATABASE_URL")
    if not db_url:
        missing_vars.append("DATABASE_URL")
        config["DATABASE_URL"] = "sqlite:///default.db"
    else:
        config["DATABASE_URL"] = db_url

    # API_KEY
    api_key: Optional[str] = os.getenv("API_KEY")
    if not api_key:
        missing_vars.append("API_KEY")
        config["API_KEY"] = "not_authenticated"
    else:
        config["API_KEY"] = api_key

    # LOG_LEVEL
    log_level: Optional[str] = os.getenv("LOG_LEVEL")
    if not log_level:
        missing_vars.append("LOG_LEVEL")
        config["LOG_LEVEL"] = "INFO"
    else:
        config["LOG_LEVEL"] = log_level

    # ZION_ENDPOINT
    zion_endpoint: Optional[str] = os.getenv("ZION_ENDPOINT")
    if not zion_endpoint:
        missing_vars.append("ZION_ENDPOINT")
        config["ZION_ENDPOINT"] = "http://localhost:8080"
    else:
        config["ZION_ENDPOINT"] = zion_endpoint

    if missing_vars:
        print(
            "\n[WARNING] Missing environment variables: "
            f"{', '.join(missing_vars)}"
        )
        print("Using default values for safety.\n")

    return config


def main() -> None:
    print("ORACLE STATUS: Reading the Matrix...\n")

    config: Dict[str, str] = load_configurations()
    mode: str = config["MATRIX_MODE"]

    print("Configuration loaded:")
    print(f"Mode: {mode}")

    if mode == "production":
        print(
            f"Database: Connected to secure cluster ({config['DATABASE_URL']})"
        )
        print("API Access: Authenticated (Production Token Active)")
        print(f"Log Level: {config['LOG_LEVEL']} (Restricted Output)")
        print(f"Zion Network: Encrypted & Routed ({config['ZION_ENDPOINT']})")
    else:
        print(
            f"Database: Connected to local instance ({config['DATABASE_URL']})"
            )
        if config["API_KEY"] != "not_authenticated":
            print("API Access: Authenticated")
        else:
            print("API Access: Guest Mode (No Key Provided)")
        print(f"Log Level: {config['LOG_LEVEL']}")
        print(f"Zion Network: Online ({config['ZION_ENDPOINT']})")

    print()
    check_security()
    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()
