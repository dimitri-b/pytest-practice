import pytest

"""
Function to test the fixture to add custom command line options to pytest.
Note the two methods of reading the parameter:
    pytestconfig.getoption('foo')
    pytestconfig.option.foo
"""


def test_custom_options(pytestconfig):
    print(f"use_sample is set to: {pytestconfig.getoption('use_sample')}")
    print(f"env is set to: {pytestconfig.option.env}")


# use a fixture to collect and return the command line param

@pytest.fixture()
def env(pytestconfig):
    return pytestconfig.option.env


def test_env_param(env):
    if env == 'prd':
        print("it is prd")
    else:
        print("it is not prd")


def test_builtin_params(pytestconfig):
    print("inifile: ", pytestconfig.inifile)
    print("root dir: ", pytestconfig.rootdir)
