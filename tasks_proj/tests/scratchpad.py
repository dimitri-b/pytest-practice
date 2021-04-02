# import sys
# import os
# # import random
import sys

FATAL_ERRORS = (KeyError, NameError)

xs = {'foo': 'bar'}
try:
    x = xs['foo']
    # z = y/42
    # y = xs['baz']
    print("no error")
except Exception as err:
    if isinstance(err, FATAL_ERRORS):
        print('fatal error')
    else:
        print('other error')
    sys.exit(1)


# checking mypy linting
def add_some(x: int, y: int) -> str:
    return str(x + y)


add_some(2, 3).isnumeric()

# print('------')
# for p in sys.path:
#     print(p)
# print('------')
# print(os.getcwd())
# print('------')

# file_path = 'junk/stuff.txt'
# file_path = (
#   '/Volumes/GoogleDrive/My Drive/Code/Python/Pytest/tasks_proj/junk/stuff.txt'
# )
# file_path = 'tasks_proj/junk/stuff.txt'

# num = random.randint(1, random.randint(3, 5))
# print(num)  # break on num == 3


# def print_it():
#     print('------- cwd ------')
#     print(os.getcwd())
#     print('------- run file path ------')
#     print(os.path.dirname(__file__))


# def do_stuff():
#     x = random.randint(1, 100)
#     return x


# do_stuff()

# for i in range(5):
#     i ** 2  # break on hit count reaching X

# with open(file_path) as f:
#     text = f.readline()  # log message
#     print(text)

# # print('-------')
# # print(sys.path)

# print_it()
