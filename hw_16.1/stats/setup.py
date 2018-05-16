# License MIT

import os
from setuptools import setup, find_packages

DISTRO_ROOT_PATCH = os.path.dirname(os.path.abspath(__file__))


def extract_requirements(file):
    """
    Install requirements from requirements file.

    :param str file: path to requirements file.
    :return: list[str] -- list of requirements.
    :rtype: list
    """
    with open(file, 'r') as file:
        return file.readlines()


setup (
    name='stats',
    version='0.1',
    description='Stats toolbox for fast data observing.',
    author='Ruslan',
    author_email='some_email@mail.com',
    license='MIT',
    packages=find_packages(exclude=['tests', '*.ipynb', '*.ipynb*', 'htmlcov']),
    install_requires=extract_requirements(os.path.join(DISTRO_ROOT_PATCH, 'requirements', 'base.txt')),
    test_requires=extract_requirements(os.path.join(DISTRO_ROOT_PATCH, 'requirements', 'test.txt')),
    test_suite='nose.collector',
)


