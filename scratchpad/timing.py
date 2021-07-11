import random
from textwrap import dedent


def sort_expensive():
    the_list = random.sample(range(1_000_000), 1_000)
    the_list.sort()


def sort_cheap():
    the_list = random.sample(range(1_000), 10)
    the_list.sort


if __name__ == '__main__':
    from timeit import timeit
    # timeit(stmt="[x for x in range(1000)]")
    result = timeit(
        stmt="sort_expensive()",
        setup="from __main__ import sort_expensive",
        number=10
    )
    print(f'expensive sort: {result}')

    result = timeit(
        stmt=dedent("""
            for _ in range(1000):
                sort_cheap()
        """),
        setup="from __main__ import sort_cheap",
        number=10
    )
    print(f'cheap sort: {result}')

# from timeit import timeit
# setup = 'from datetime import datetime'
# statement = 'datetime.now()'
# result = timeit(setup=setup, stmt=statement)
# print(f'Took an average of {result}ms')
