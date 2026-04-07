#!/usr/bin/env python3


def crisis_managment(filename: str) -> None:
    print(
        f"CRISIS ALERT: Attempting access to {filename}...")
    try:
        with open(filename, "r") as vault:
            data = vault.read().strip()
            print(f"SUCCESS: Archive recovered - ''{data}''")
            print("STATUS: Crisis handled, system stable", end="\n\n")
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable", end="\n\n")
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained", end="\n\n")
    except Exception:
        print("RESPONSE: Unexpected system anomaly detected")
        print("STATUS: Crisis handled, system stable", end="\n\n")


def super_managment() -> None:

    crisis_managment("corrupted_archive.txt")
    crisis_managment("classified_data.txt")

    print("ROUTINE ACCESS: Attempting access to 'standard_archive.txt'...")
    try:
        with open("standard_archive.txt", "r") as vault:
            data = vault.read().strip()
            print(f"SUCCESS: Archive recovered - ''{data}''")
            print("STATUS: Normal operations resumed", end="\n\n")
    except Exception:
        print("STATUS: Unexpected anomaly during routine access", end="\n\n")
    print("All crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM", end="\n\n")
    super_managment()
