from typing import List, Dict

from parser.constants import (
    MIN_MINUTE,
    MIN_HOUR,
    MIN_DAY_OF_WEEK,
    MIN_DAY_OF_MONTH,
    MIN_MONTH,
    MAX_MINUTE,
    MAX_HOUR,
    MAX_DAY_OF_MONTH,
    MAX_DAY_OF_WEEK,
    MAX_MONTH,
)


def parse_cron_expression(cron_expression_args: List[str]) -> Dict[str, List[str]]:
    parsed_result = {
        "minutes": parse_cron_expression_argument(
            cron_expression_args[0], MAX_MINUTE, MIN_MINUTE
        ),
        "hours": parse_cron_expression_argument(
            cron_expression_args[1], MAX_HOUR, MIN_HOUR
        ),
        "days_of_month": parse_cron_expression_argument(
            cron_expression_args[2], MAX_DAY_OF_MONTH, MIN_DAY_OF_MONTH
        ),
        "months": parse_cron_expression_argument(
            cron_expression_args[3], MAX_MONTH, MIN_MONTH
        ),
        "days_of_week": parse_cron_expression_argument(
            cron_expression_args[4], MAX_DAY_OF_WEEK, MIN_DAY_OF_WEEK
        ),
    }
    return parsed_result


def parse_cron_expression_argument(
    expression_arg: str, arg_max_value: int, arg_min_value: int
) -> List[str]:
    if (
        "*" not in expression_arg
        and "/" not in expression_arg
        and "-" not in expression_arg
        and "," not in expression_arg
    ):
        return [expression_arg]

    if expression_arg == "*":
        return [str(arg) for arg in range(arg_min_value, arg_max_value + 1)]

    if "," in expression_arg:
        return expression_arg.split(",")

    if "-" in expression_arg:
        expression_arg_split = expression_arg.split("-")
        return [
            str(i)
            for i in range(
                int(expression_arg_split[0]), int(expression_arg_split[1]) + 1
            )
        ]

    if "/" in expression_arg:
        expression_arg_split = expression_arg.split("/")
        try:
            int(expression_arg_split[-1])
        except Exception:
            raise ValueError("Invalid cron format. Step can be only of integer type.")
        starts_from = (
            int(expression_arg_split[0]) if expression_arg_split[0] != "*" else 0
        )
        step = int(expression_arg_split[1])
        result = [starts_from]
        for i in range(0, 3):
            result.append(result[-1] + step)
        return [str(i) for i in result]

    raise ValueError(
        "Invalid cron format. Possible characters: integers, *, , , /, -. Combinations such as  **, // are not allowed."
    )
