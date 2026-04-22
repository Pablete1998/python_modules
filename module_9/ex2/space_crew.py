#!/urs/bin/env python3

from datetime import datetime
from enum import Enum

from pydantic import BaseModel, Field, ValidationError, model_validator


class Rank(str, Enum):
    """Valid crew member ranks."""

    cadet = "cadet"
    officer = "officer"
    lieutenant = "lieutenant"
    captain = "captain"
    commander = "commander"


class CrewMember(BaseModel):
    """Pydantic model for individual crew members."""

    member_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=2, max_length=50)
    rank: Rank
    age: int = Field(..., ge=18, le=80)
    specialization: str = Field(..., min_length=3, max_length=30)
    years_experience: int = Field(..., ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    """Pydantic model for space missions with crew validation."""

    mission_id: str = Field(..., min_length=5, max_length=15)
    mission_name: str = Field(..., min_length=3, max_length=100)
    destination: str = Field(..., min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(..., ge=1, le=3650)
    crew: list[CrewMember] = Field(..., min_length=1, max_length=12)
    mission_status: str = "planned"
    budget_millions: float = Field(..., ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def validate_mission_rules(self) -> 'SpaceMission':
        """Validate cross-field mission safety requirements."""

        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with 'M'")

        has_leader = any(
            m.rank in (Rank.commander, Rank.captain)
            for m in self.crew
        )
        if not has_leader:
            raise ValueError(
                "Mission must have at least one Commander or Captain"
            )

        if self.duration_days > 365:
            experienced = sum(
                1 for m in self.crew if m.years_experience >= 5
            )
            if experienced < len(self.crew) / 2:
                raise ValueError(
                    "Long missions need 50% experienced crew (5+ years)"
                )

        if not all(m.is_active for m in self.crew):
            raise ValueError("All crew members must be active")

        return self


def main() -> None:
    """Demonstrate SpaceMission validation with valid and invalid data."""

    print("Space Mission Crew Validation")
    print("=" * 40)

    try:
        mission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime(2024, 6, 1, 9, 0, 0),
            duration_days=900,
            budget_millions=2500.0,
            crew=[
                CrewMember(
                    member_id="CM001",
                    name="Sarah Connor",
                    rank=Rank.commander,
                    age=40,
                    specialization="Mission Command",
                    years_experience=15
                ),
                CrewMember(
                    member_id="CM002",
                    name="John Smith",
                    rank=Rank.lieutenant,
                    age=35,
                    specialization="Navigation",
                    years_experience=8
                ),
                CrewMember(
                    member_id="CM003",
                    name="Alice Johnson",
                    rank=Rank.officer,
                    age=30,
                    specialization="Engineering",
                    years_experience=5
                ),
            ]
        )
        print("Valid mission created:")
        print(f"Mission: {mission.mission_name}")
        print(f"ID: {mission.mission_id}")
        print(f"Destination: {mission.destination}")
        print(f"Duration: {mission.duration_days} days")
        print(f"Budget: ${mission.budget_millions}M")
        print(f"Crew size: {len(mission.crew)}")
        print("Crew members:")
        for member in mission.crew:
            print(
                f"  - {member.name} ({member.rank.value})"
                f" - {member.specialization}"
            )

    except ValidationError as e:
        for error in e.errors():
            print(error["msg"])

    print("=" * 40)

    try:
        SpaceMission(
            mission_id="M2024_FAIL",
            mission_name="Failed Mission",
            destination="Moon",
            launch_date=datetime(2024, 6, 1, 9, 0, 0),
            duration_days=30,
            budget_millions=100.0,
            crew=[
                CrewMember(
                    member_id="CM004",
                    name="Bob Brown",
                    rank=Rank.officer,
                    age=28,
                    specialization="Navigation",
                    years_experience=2
                ),
            ]
        )

    except ValidationError as e:
        print("Expected validation error:")
        for error in e.errors():
            print(error["msg"])


if __name__ == "__main__":
    main()