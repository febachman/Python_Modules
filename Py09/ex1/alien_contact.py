#!/usr/bin/env python3

from datetime import datetime
from enum import Enum
from typing import Optional
from pydantic import BaseModel, Field, ValidationError, model_validator
from data_generator import DataConfig, AlienContactGenerator


class ContactType(str, Enum):
    radio = "radio"
    visual = "visual"
    physical = "physical"
    telepathic = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(..., min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(..., min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(..., ge=0.0, le=10.0)
    duration_minutes: int = Field(..., ge=1, le=1440)
    witness_count: int = Field(..., ge=1, le=100)
    message_received: Optional[str] = Field(None, max_length=500)
    is_verified: bool = False

    @model_validator(mode="after")
    def validate_alien_contact_rules(self) -> "AlienContact":
        # Rule 1: Contact ID must start with "AC"
        if not self.contact_id.startswith("AC"):
            raise ValueError('Contact ID must start with "AC"')

        # Rule 2: Physical contact reports must be verified
        if self.contact_type == ContactType.physical and not self.is_verified:
            raise ValueError("Physical contact reports must be verified")

        # Rule 3: Telepathic contact requires at least 3 witnesses
        if (
            self.contact_type == ContactType.telepathic
            and self.witness_count < 3
        ):
            raise ValueError(
                "Telepathic contact requires at least 3 witnesses"
            )

        # Rule 4: Strong signals (> 7.0) should include received messages
        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError(
                "Strong signals (> 7.0) should include received messages"
            )

        return self


def main() -> None:
    print("Alien Contact Log Validation")
    print("=" * 38)

    config = DataConfig()
    contact_gen = AlienContactGenerator(config)

    # Valid contact report
    raw_contacts = contact_gen.generate_contact_data(3)
    print(f"Successfully generated and validated {len(raw_contacts)} reports:")
    for raw in raw_contacts:
        try:
            contact = AlienContact(**raw)
            print(
                f"  - [{contact.contact_id}] "
                f"Type: {contact.contact_type.value} "
                f"| Location: {contact.location} "
                f"| Signal: {contact.signal_strength}/10"
            )
        except ValidationError as e:
            print(f"  - Validation failed for {raw.get('contact_id')}: {e}")

    print("=" * 38)

    # Invalid contact report (Telepathic with 1 witness)
    print("Expected validation error:")
    try:
        AlienContact(
            contact_id="AC_TELE_02",
            timestamp=datetime.now(),
            location="Moon Base Alpha",
            contact_type=ContactType.telepathic,
            signal_strength=5.0,
            duration_minutes=15,
            witness_count=1,  # Invalid: requires at least 3 witnesses
            is_verified=False,
            message_received=None,
        )

    except ValidationError as e:
        for error in e.errors():
            print(error["msg"])


if __name__ == "__main__":
    main()
