# import os
import os

# setuptools
from setuptools import setup, find_packages

def read(*paths):
    """Read the contents of a text file safely.
    >>> read("dundie", "VERSION") # project name = dundie 
    '0.1.0'
    >>> read("README.md")
    ...
    """
    # variavel retorna o caminho do setup.py
    rootpath = os.path.dirname(__file__) 
    filepath = os.path.join(rootpath, *paths)
    with open(filepath) as file_:
        # strip para remover qq coisa em branco
        return file_.read().strip() 
    
def read_requirements(path):
    """Return a list of requirements from a text file"""
    return [
        line.strip()
        for line in read(path).split("\n")
        if not line.startswith(("#", "git+", '"', "-"))
    ]


setup(
    name="dundie",

           # X Y Z    SEMANTIC VERSIONING
    version="0.1.0",
           # | | |___ PATCH
           # | |_____ MINOR
           # |_______ MAJOR
    description="Reward Point System for Dunder Mifflin",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="Alberto Santos",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            #"dundie = dundie.__main__"
            #>>> from dundie import __main__
            #>>> type(__main__)
            #<class 'module'>
            #>>> callable(__main__)
            #False ==> nao é Callable
            #>>> __main__()
            # Traceback (most recent call last):
            # File "<stdin>", line 1, in <module>
            # TypeError: 'module' object is not callable

            # Callable
            "dundie = dundie.__main__:main" 
        ]
    },
    # Instalando os pacotes que o noss projeto depende
    install_requires=read_requirements("requirements.txt"),

    # Dependencias opcionais
    extras_require={
        "test": read_requirements("requirements.test.txt"),
        "dev": read_requirements("requirements.dev.txt")
    }    
)

# pyproject

# external buil tools (poetry, flit)
