import sys

from parser.parsers import parse_cron_expression
from parser.validators import validate_argument
from parser.formatters import get_formatted_output


def main():
    argument = sys.argv[1]
    argument = validate_argument(argument)
    command = argument.split(" ")[-1]
    cron_expression_args = argument.split(" ")[:-1]
    parsed_cron_expression = parse_cron_expression(cron_expression_args)
    print(get_formatted_output(parsed_cron_expression, command))


if __name__ == "__main__":
    main()
