from parser.formatters import get_formatted_output


def test_get_formatted_output():
    data_in = {
        "minutes": ["2", "6"],
        "hours": ["7", "0"],
        "months": ["5", "9"],
        "days_of_month": ["6"],
        "days_of_week": ["1", "2", "3", "4"],
    }
    result = get_formatted_output(data_in, "/test/command/")
    assert (
        result
        == "minute        2 6\nhour          7 0\nday of month  6\nmonth         5 9\nday of week   1 2 3 4\ncommand       /test/command/"
    )
