import pytest
from uppercase import to_upper


def test_to_uppercase():
    """Test the to_upper function."""
    assert to_upper("hello") == "HELLO"
    assert to_upper("world") == "WORLD"
    assert to_upper("Python") == "PYTHON"
    assert to_upper("123abc") == "123ABC"
    assert to_upper("") == ""  # Test with an empty string
    assert to_upper("!@#") == "!@#"  # Test with special characters

if __name__ == "__main__":
    pytest.main()
    # This script runs the tests for the to_upper function using pytest.
    # It checks various cases including normal strings, empty strings, and special characters.