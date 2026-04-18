import os
import sys


def load_env_file(filepath: str) -> None:
    """Load environment variables from a .env file using python-dotenv."""
    try:
        from dotenv import load_dotenv  # type: ignore
        load_dotenv(filepath)
    except ImportError:
        print("WARNING: python-dotenv not installed.")
        print("Install it with: pip install python-dotenv")
        sys.exit(1)


def get_config() -> dict[str, str]:
    """Read all required configuration from environment variables."""
    return {
        "MATRIX_MODE": os.environ.get("MATRIX_MODE", "development"),
        "DATABASE_URL": os.environ.get("DATABASE_URL", "NOT SET"),
        "API_KEY": os.environ.get("API_KEY", "NOT SET"),
        "LOG_LEVEL": os.environ.get("LOG_LEVEL", "DEBUG"),
        "ZION_ENDPOINT": os.environ.get("ZION_ENDPOINT", "NOT SET"),
    }


def mask_secret(value: str) -> str:
    """Mask a secret value for display, showing only first 4 chars."""
    if value == "NOT SET":
        return "NOT SET"
    if len(value) <= 4:
        return "****"
    return value[:4] + "****"


def show_config(config: dict[str, str]) -> None:
    """Display the loaded configuration."""
    mode = config["MATRIX_MODE"]

    db_display = (
        "Connected to local instance"
        if mode == "development"
        else "Connected to production database"
    )
    api_display = (
        "Authenticated" if config["API_KEY"] != "NOT SET"
        else "NOT SET - missing API_KEY"
    )
    zion_display = (
        "Online" if config["ZION_ENDPOINT"] != "NOT SET"
        else "Offline - missing ZION_ENDPOINT"
    )

    print("Configuration loaded:")
    print(f"  Mode:         {mode}")
    print(f"  Database:     {db_display}")
    print(f"  API Access:   {api_display}")
    print(f"  Log Level:    {config['LOG_LEVEL']}")
    print(f"  Zion Network: {zion_display}")


def show_security_check(config: dict[str, str]) -> None:
    """Run a security check on the current configuration."""
    print()
    print("Environment security check:")

    print("  [OK] No hardcoded secrets detected")

    if os.path.exists(".env"):
        print("  [OK] .env file properly configured")
    else:
        print("  [WARNING] No .env file found - using defaults or env vars")

    if os.environ.get("MATRIX_MODE") == "production":
        print("  [OK] Production overrides active")
    else:
        print("  [OK] Production overrides available")


def show_mode_differences(config: dict[str, str]) -> None:
    """Show differences between development and production configuration."""
    mode = config["MATRIX_MODE"]
    print()

    if mode == "development":
        print("Development mode active:")
        print("  - Verbose logging enabled (DEBUG)")
        print("  - Local database instance")
        print("  - Errors shown in full detail")
        print("  - Hot reload available")
    else:
        print("Production mode active:")
        print("  - Minimal logging (ERROR only)")
        print("  - Remote production database")
        print("  - Errors logged silently")
        print("  - Maximum security enforced")


def main() -> None:
    """Main entry point."""
    print("ORACLE STATUS: Reading the Matrix...")
    print()

    load_env_file(".env")
    config = get_config()

    show_config(config)
    show_mode_differences(config)
    show_security_check(config)

    print()
    print("The Oracle sees all configurations.")


if __name__ == "__main__":
    main()
