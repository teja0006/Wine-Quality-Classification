from setuptools import setup,find_packages
from typing import List

HYPEN_E_DOT = '-e .'
def get_requirements(file_path):
    requirements = []
    with open(file_path,'r') as file:
        requirements = file.readlines()
        requirements = [req.replace('\n','') for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
    name = 'Wine Quality Classification',
    version='0.0.1',
    author='Datta Teja',
    author_email='dattateja1234@gmail.com',
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt')
)