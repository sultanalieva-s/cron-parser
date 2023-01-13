from typing import Dict, List

from parser.constants import OUTPUT


def get_formatted_output(parsed_cron_string: Dict[str, List[str]], command: str) -> str:
    minutes = " ".join(parsed_cron_string.get("minutes"))
    hours = " ".join(parsed_cron_string.get("hours"))
    days_of_month = " ".join(parsed_cron_string.get("days_of_month"))
    months = " ".join(parsed_cron_string.get("months"))
    days_of_week = " ".join(parsed_cron_string.get("days_of_week"))
    return OUTPUT.format(
        minutes=minutes,
        hours=hours,
        days_of_month=days_of_month,
        months=months,
        days_of_week=days_of_week,
        command=command,
    )
