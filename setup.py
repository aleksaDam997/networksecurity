'''
The setup.py file is an essential part of packaging and distributing a Python project. It is user
by setuptools (or distutils in older Python versions) to define the configuration of your project, 
such as its metadata, dependencies and more
'''

from setuptools import setup, find_packages
from typing import List

def get_requirements() -> List[str]:
    """Read the requirements from a file and return them as a list."""
    
    try:
        with open("requirements.txt", 'r') as file:
            return [line.strip() for line in file.readlines() if line.strip() and line.strip() != '-e .' and not line.startswith('#')]
    except FileNotFoundError:
        print("requirements.txt file not found. Please ensure it exists in the same directory as setup.py.")
        return []

print(get_requirements())

setup(
    name="Network Security",
    version="0.0.1",
    author="Aleksandar Damjanovic",
    author_email="aleksa.dam997@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements(),
)