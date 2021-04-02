"""Test pytest-nice plugin.
The effect is only on failing tests, so there is no need to test
passing tests.
"""

import pytest


@pytest.fixture()
def sample_test(testdir):
    # temporary pytest module with
    # one passing and one failing test
    testdir.makepyfile(
        """
        def test_pass():
            assert 1 == 1

        def test_fail():
            assert 1 == 2
        """
    )
    return testdir


def test_with_nice(sample_test):
    result = sample_test.runpytest('--nice')
    # fnmatch_lines is an automatic internal assertion,
    # no separate assert needed for it
    result.stdout.fnmatch_lines(["*.NW*"])
    # also make sure it was on a failed test: ExitCode == 1
    assert result.ret == 1


def test_with_nice_verbose(sample_test):
    result = sample_test.runpytest('-v', '--nice')
    result.stdout.fnmatch_lines([
        "*::test_fail NEEDS WORK*"
    ])
    assert result.ret == 1


def test_not_nice_verbose(sample_test):
    result = sample_test.runpytest('-v')
    result.stdout.fnmatch_lines([
        "*::test_fail FAILED*"
    ])
    assert result.ret == 1


def test_header(sample_test):
    result = sample_test.runpytest('--nice')
    result.stdout.fnmatch_lines([
        "Thank you for testing"
    ])


def test_header_not_nice(sample_test):
    result = sample_test.runpytest()
    nice_message = "Thank you for testing"
    assert nice_message not in result.stdout.str()


def test_help_message(testdir):
    """pytest --help should list the plugin's option and description"""
    result = testdir.runpytest('--help')
    result.stdout.fnmatch_lines([
        'nice:',
        '*--nice* less offensive language for error messages'
    ])


# example test of pytest plugin,
# to demo how plugin testing works
def test_pass_fail(testdir):
    # temporary pytest module with
    # one passing and one failing test
    testdir.makepyfile(
        """
        def test_pass():
            assert 1 == 1

        def test_fail():
            assert 1 == 2
        """
    )
    # run pytest, get RunResult object to examine the outcome
    result = testdir.runpytest()

    # check that the lines with the pattern are present,
    # should have . for pass, F for fail
    result.stdout.fnmatch_lines(["*.F*"])

    # ret = ExitCode, make sure we get exit code 1 for the failing test
    assert result.ret == 1
