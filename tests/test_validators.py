import pytest

from parser.validators import validate_argument


def test_validate_argument__success():
    test_input = "*/15 0 1,15 * 1-5 test-command"
    result = validate_argument(test_input)
    assert result == test_input


def test_validate_argument__blank_strings_at_edges():
    test_input = "    */15 0 1,15 * 1-5 test/command   "
    result = validate_argument(test_input)
    assert result == "*/15 0 1,15 * 1-5 test/command"


def test_validate_argument__no_command():
    test_input = "*/15 0 1,15 * 1-5"
    with pytest.raises(ValueError):
        validate_argument(test_input)
