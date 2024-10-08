# setuptools
from setuptools import setup, find_packages

setup(
    name="dundie",

           # X Y Z    SEMANTIC VERSIONING
    version="0.1.0",
           # | | |___ PATCH
           # | |_____ MINOR
           # |_______ MAJOR
    description="Reward Point System for Dunder Mifflin",
    author="Alberto Santos",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "dundie = dundie.__main__:main"
        ]
    }
)

# pyproject

# external buil tools (poetry, flit)
