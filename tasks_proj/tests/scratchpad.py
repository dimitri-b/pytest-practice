# import sys
import os
import random


file_path = 'junk/stuff.txt'
# file_path = (
#   '/Volumes/GoogleDrive/My Drive/Code/Python/Pytest/tasks_proj/junk/stuff.txt'
# )
# file_path = 'tasks_proj/junk/stuff.txt'

num = random.randint(1, random.randint(3, 5))
print(num)  # break on num == 3


def print_it():
    print('------- cwd ------')
    print(os.getcwd())
    print('------- run file path ------')
    print(os.path.dirname(__file__))


def do_stuff():
    x = random.randint(1, 100)
    return x


do_stuff()

for i in range(5):
    i ** 2  # break on hit count reaching X

with open(file_path) as f:
    text = f.readline()  # log message
    print(text)

# print('-------')
# print(sys.path)

print_it()
