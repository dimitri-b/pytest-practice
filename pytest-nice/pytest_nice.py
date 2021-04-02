"""Adds --nice option for more politically correct feedback on failed tests"""

# using pytest hook functions to intercept pytest calls and modify behaviour


def pytest_addoption(parser):
    """Add --nice command line option to show politically correct outcomes"""
    group = parser.getgroup("nice")
    group.addoption(
        "--nice", action="store_true", help="less offensive language for error messages"
    )


# pytest hook function, uses new --nice option to modify test results status message
def pytest_report_header(config):
    """Use hook to override default status message"""
    if config.getoption("nice"):
        return "Thank you for testing"


# pytest hook function, uses new --nice option to modify test failure flags:
# F -> WN, FAILED -> WORK NEEDED
def pytest_report_teststatus(report, config):
    """Use hook to change Fail (F) symbol in status"""
    if report.when == "call" and report.failed and config.getoption("nice"):
        return (report.outcome, "WN", "WORK NEEDED")
