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
        return file.read().splitlines()



setup (
    name='supertool-distro',
    version='0.1',
    description='Super-super tool',
    author='Me, I',
    author_email='a@a.com, b@b.com',
    license='MIT',
    classifiers=[
        'Topic :: Education',
        'Programming Lang :: ...'
    ],
    packages=find_packages(exclude=['tests']),
    install_requires=extract_requirements(os.path.join(DISTRO_ROOT_PATCH, 'requirements', 'base.txt')),
    test_requires=extract_requirements(os.path.join(DISTRO_ROOT_PATCH, 'requirements', 'test.txt')),
    test_suite='nose.collector',
    # scripts=[os.path.join('bin', 'similar_files')]
    # scripts не работает на моей системе (ubuntu), использую bin
    bin=[os.path.join('bin', 'similar_files')]
)


