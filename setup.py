from setuptools import find_packages, setup
from typing import List

Hyphen_E_dot = "-e ."

def get_requirements(filename) -> List[str]:
    '''
    This function will return list of requirements
    '''

    requirements = []
    with open(filename) as fileobj:
        requirements = fileobj.readlines()
        requirements = [value.replace("\n", "")for value in requirements]
        
        if Hyphen_E_dot in requirements:
            requirements.remove(Hyphen_E_dot)
    return requirements

setup(
name='mlproject',
version='0.0.1',
author='Tarun',
author_email='tarun6467@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')
)

