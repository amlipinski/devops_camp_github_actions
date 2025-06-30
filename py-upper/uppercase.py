import sys

def to_upper(text: str) -> str:
    """Convert the input text to uppercase."""
    return text.upper()

if __name__ == "__main__":
    print(to_upper(sys.argv[1]))
    # This script takes a string input from the command line and converts it to uppercase.)