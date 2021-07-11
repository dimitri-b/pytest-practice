import os
import json
import copy
import pytest

"""
The three functions below read and write a config file into
user's home directory. They don't return anything, instead they
use side effects (write/read files), so they cannot be tested
by examining their return values.
A simple option would be to write a sample config file and test how
the read function handles it, but that would overwrite the actual
file needed by production code.
Monkeypatching allows patching functions and changing some of
their functionality to avoid risky or undesirable interactions
with production assets.
Note: os.path.expanduser(path_str) will expand any user home dir
vars like '~' to a full path from root.
"""


def read_config():
    config_file_path = os.path.expanduser('~/.some_config.json')
    with open(config_file_path, 'r') as f:
        prefs = json.load(f)
    return prefs


def write_config(prefs):
    config_file_path = os.path.expanduser('~/.some_config.json')
    with open(config_file_path, 'w') as f:
        json.dump(prefs, f, indent=4)


def write_default_config():
    write_config(_default_config)


_default_config = {
    'run_env': 'prod',
    'txn_table': 'prod_transaction_details',
    'cust_table': 'prod_customer_details',
}

# ------------ test functions ------------


@pytest.mark.skip('will overwrite prod config')
def test_config_simple():
    """Naive
    Primitive test function, will overwrite production
    config file in HOME dir. Not ideal.
    """
    write_default_config()
    expected_config = _default_config
    actual_config = read_config()
    assert expected_config == actual_config


def test_config_change_homedir(tmpdir, monkeypatch):
    """Improvement 1
    Same as above, but using monkeypatch to temporarily change
    home directory to a temp location, just for this function run.
    The problem is that called function uses 'expanduser' which
    doesn't have consistent behaviour between operating systems.
    """
    monkeypatch.setenv('HOME', str(tmpdir.mkdir('temp_home')))
    write_default_config()
    expected_config = _default_config
    actual_config = read_config()
    assert expected_config == actual_config


def test_config_change_expanduser(tmpdir, monkeypatch):
    """Improvement 2
    This function patches the 'expanduser' via setattr.
    The patch is applied to os.path, and every call to its 'expanduser'
    attribute/function will instead provide the result of the supplied
    lambda function, which will intercept the input args of 'expanduser'
    and return it with '~' replaced with temp home dir instead of
    expanded HOME path.
    """
    temp_home = tmpdir.mkdir('temp_home')
    monkeypatch.setattr(
        os.path,
        'expanduser',
        lambda x: x.replace('~', str(temp_home))
    )
    write_default_config()
    expected_config = _default_config
    actual_config = read_config()
    assert expected_config == actual_config


def test_config_change_defaults(tmpdir, monkeypatch):
    """Demo: dictionary overwrite
    This test, in addition to the previous patching tecniques,
    also overwrites values in a dictionray that is used for
    setting default config params. Then the standard function which
    uses the default dict is called and the results tested.
    The params should match the modified ones.
    This leaves the code logic as is, without the need to create
    a different dict for test params and point functions to it, etc.
    """
    temp_home = tmpdir.mkdir('temp_home')
    monkeypatch.setattr(
        os.path,
        'expanduser',
        lambda x: x.replace('~', str(temp_home))
    )
    write_default_config()
    config_before_mod = copy.deepcopy(_default_config)
    # overwrite default config dictionary values and write them to file
    monkeypatch.setitem(_default_config, 'run_env', 'dev')
    monkeypatch.setitem(_default_config, 'txn_table', 'dev_transactions')
    print(_default_config)
    config_modified = _default_config
    write_default_config()
    # test if modified defaults were written to config file
    actual_config = read_config()
    assert config_modified == actual_config
    assert config_modified != config_before_mod


# running the module to setup for testing
if __name__ == "__main__":
    write_default_config()
