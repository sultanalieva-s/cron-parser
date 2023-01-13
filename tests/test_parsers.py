from unittest.mock import call

import pytest

from parser import parsers
from parser.parsers import parse_cron_expression, parse_cron_expression_argument

from parser.constants import (
    MIN_MINUTE,
    MIN_DAY_OF_WEEK,
    MIN_DAY_OF_MONTH,
    MIN_MONTH,
    MAX_MINUTE,
    MAX_HOUR,
    MAX_DAY_OF_MONTH,
    MAX_DAY_OF_WEEK,
    MAX_MONTH,
    MIN_HOUR,
)


def test_parse_cron_expression__success(mocker):
    mocker.patch(
        "parser.parsers.parse_cron_expression_argument",
        return_value=[2],
    )
    result = parse_cron_expression(["0", "0", "*", "*", "*"])
    assert isinstance(result, dict)
    parsers.parse_cron_expression_argument.assert_has_calls(
        [
            call("0", MAX_MINUTE, MIN_MINUTE),
            call("0", MAX_HOUR, MIN_HOUR),
            call("*", MAX_DAY_OF_MONTH, MIN_DAY_OF_MONTH),
            call("*", MAX_MONTH, MIN_MONTH),
            call("*", MAX_DAY_OF_WEEK, MIN_DAY_OF_WEEK),
        ],
    )


def test_parse_cron_expression_argument__no_characters():
    result = parse_cron_expression_argument("1", MAX_MINUTE, MIN_MINUTE)
    assert result == ["1"]


def test_parse_cron_expression_argument__asterisk():
    result = parse_cron_expression_argument("*", MAX_DAY_OF_WEEK, MIN_DAY_OF_WEEK)
    assert result == ["1", "2", "3", "4", "5", "6", "7"]


def test_parse_cron_expression_argument__comma():
    result = parse_cron_expression_argument("1,5", MAX_DAY_OF_WEEK, MIN_DAY_OF_WEEK)
    assert result == ["1", "5"]


def test_parse_cron_expression_argument__range():
    result = parse_cron_expression_argument("1-5", MAX_DAY_OF_WEEK, MIN_DAY_OF_WEEK)
    assert result == ["1", "2", "3", "4", "5"]


def test_parse_cron_expression_argument__slash():
    result = parse_cron_expression_argument("1/5", MAX_DAY_OF_WEEK, MIN_DAY_OF_WEEK)
    assert result == ["1", "6", "11", "16"]


def test_parse_cron_expression_argument__slash_with_asterisk():
    result = parse_cron_expression_argument("*/5", MAX_DAY_OF_WEEK, MIN_DAY_OF_WEEK)
    assert result[0] == "0"
    assert result == ["0", "5", "10", "15"]


def test_parse_cron_expression_argument__slash_invalid_step():
    with pytest.raises(ValueError):
        parse_cron_expression_argument("*/*", MAX_DAY_OF_WEEK, MIN_DAY_OF_WEEK)


def test_parse_cron_expression_argument__fail():
    with pytest.raises(ValueError):
        parse_cron_expression_argument("**", MAX_DAY_OF_WEEK, MIN_DAY_OF_WEEK)
