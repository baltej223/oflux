import sys

# Check if the correct number of arguments is provided
if len(sys.argv) != 3:
    print("Usage: py main.py <first> <second>")
else:
    i = sys.argv[1]  # First argument (after the script name)
    b = sys.argv[2]  # Second argument
    print(f"{i}, {b}")