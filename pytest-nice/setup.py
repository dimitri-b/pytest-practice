"""Setup for pytest plugin"""

from setuptools import setup


setup(
    name="pytest-nice",
    version="0.1.0",
    description="Pytest plugin to show politically correct failure feedback",
    url="https://this/is/not/stored/anywhere",
    author="Anonymous",
    author_email="anonymous@nowhere.com.",
    licence="proprietary",
    py_modules=["pytest_nice"],
    install_requires=["pytest"],
    entry_points={
        "pytest11": [
            "nice = pytest_nice",
        ],
    },
)
