import sys


# this function prints to stdout,
# it returns None, so it cannot be tested by checking the return value
# test function needs to access stdout
def greeting(name):
    print(f"Hi, {name}")


# this function sends output to stderr, wich can be accessed via capsys
def show_problem(problem):
    print(f"we have a problem: {problem}", file=sys.stderr)


# test function uses built-in capsys fixture to acess stoud data
def test_greeting(capsys):
    greeting('Earthling')
    out, err = capsys.readouterr()
    # print('\nout: ', out)
    # print('\nerror: ', err)
    assert out == 'Hi, Earthling\n'
    assert err == ""


# access stderr
def test_show_problem(capsys):
    show_problem('Ran out of coffee!')
    out, err = capsys.readouterr()
    assert out == ""
    assert 'Ran out of coffee!' in err


# stdout is normally captured during tests,
# which can be disabled with -s option for the session,
# or within capsys.disabled() block
def test_capsys_disabled(capsys):
    with capsys.disabled():
        print('\nThis is always printed, not captured by capsys')
    print('This is captured, not printend during testing')
