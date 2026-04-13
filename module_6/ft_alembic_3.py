#!/usr/bin/env python3

print("=== Alembic 3 ===")
print("Accessing alchemy/elements.py using 'from ... import ...' structure")

from alchemy.elements import create_air

print("Testing create_air:", create_air())
