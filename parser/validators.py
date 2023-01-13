def validate_argument(argument: str):
    argument = argument.strip()
    if argument.count(" ") != 5:
        raise ValueError(
            'Invalid argument. Argument Example: "*/15 0 1,15 * 1-5 /usr/bin/find"'
        )
    return argument
