"""
Exercise 1: Alien Contact Logs
Cosmic Data Observatory - AlienContact Pydantic model with custom validation.
"""

from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field, ValidationError, model_validator


class ContactType(str, Enum):
    """Valid alien contact types."""

    radio = "radio"
    visual = "visual"
    physical = "physical"
    telepathic = "telepathic"


class AlienContact(BaseModel):
    """Pydantic model for alien contact reports."""

    contact_id: str = Field(..., min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(..., min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(..., ge=0.0, le=10.0)
    duration_minutes: int = Field(..., ge=1, le=1440)
    witness_count: int = Field(..., ge=1, le=100)
    message_received: Optional[str] = Field(None, max_length=500)
    is_verified: bool = False

    @model_validator(mode='after')
    def validate_business_rules(self) -> 'AlienContact':
        """Validate cross-field business rules."""

        # Rule 1: contact_id must start with "AC"
        if not self.contact_id.startswith("AC"):
            raise ValueError("Contact ID must start with 'AC'")

        # Rule 2: physical contact must be verified
        if self.contact_type == ContactType.physical and not self.is_verified:
            raise ValueError("Physical contact reports must be verified")

        # Rule 3: telepathic contact requires at least 3 witnesses
        if self.contact_type == ContactType.telepathic and self.witness_count < 3:
            raise ValueError("Telepathic contact requires at least 3 witnesses")

        # Rule 4: strong signals must include a received message
        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError("Strong signals must include a received message")

        return self


def main() -> None:
    """Demonstrate AlienContact validation with valid and invalid data."""

    print("Alien Contact Log Validation")
    print("=" * 40)

    # Create a valid contact report
    try:
        contact = AlienContact(
            contact_id="AC_2024_001",
            timestamp=datetime(2024, 3, 15, 22, 30, 0),
            location="Area 51, Nevada",
            contact_type=ContactType.radio,
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=5,
            message_received="Greetings from Zeta Reticuli",
            is_verified=False
        )
        print("Valid contact report:")
        print(f"ID: {contact.contact_id}")
        print(f"Type: {contact.contact_type.value}")
        print(f"Location: {contact.location}")
        print(f"Signal: {contact.signal_strength}/10")
        print(f"Duration: {contact.duration_minutes} minutes")
        print(f"Witnesses: {contact.witness_count}")
        print(f"Message: '{contact.message_received}'")

    except ValidationError as e:
        for error in e.errors():
            print(error["msg"])

    print("=" * 40)

    # Attempt to create an invalid report (telepathic with only 1 witness)
    try:
        AlienContact(
            contact_id="AC_2024_002",
            timestamp=datetime(2024, 3, 16, 10, 0, 0),
            location="Roswell, New Mexico",
            contact_type=ContactType.telepathic,
            signal_strength=5.0,
            duration_minutes=30,
            witness_count=1,
            message_received=None,
            is_verified=False
        )

    except ValidationError as e:
        print("Expected validation error:")
        for error in e.errors():
            print(error["msg"])


if __name__ == "__main__":
    main()