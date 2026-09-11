#!/usr/bin/env python3

import alchemy

print("=== Alembic 4 ===")
print("Accessing the alchemy module using 'import alchemy'")
print(f"Testing create_air: {alchemy.create_air()}")
print("Now show that not all functions can be reached")
print("This will raise an exception!")

try:
    #  This will raise an AttributeError because it's hidden
    print(alchemy.create_earth())
except AttributeError as e:
    print(f"Caught expected error: {e}")
