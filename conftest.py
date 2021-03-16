"""
Pytest can have custom options (parameters) collected from the command line,
similar to argparse.
Here is a fixtrue with two such options defined - a boolean and a string.
Looks like dashes are not allowed in the var names - use underscores.
This should be defined in conftest.py at the project root, not sure why.
"""


def pytest_addoption(parser):  # <-- use this exact syntax
    parser.addoption(
        "--use_sample",  # <-- name of the param to use with CLI
        action="store_true",  # <-- what to do with the value
        help="Boolean flag - use sample or full data"  # <-- will show up for --help
    )
    parser.addoption(
        "--env",
        action="store",
        default="dev",
        help="Environment: 'dev' or 'prd'"
    )
