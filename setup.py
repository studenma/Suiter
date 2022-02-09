from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

setup(
    name='suiter',
    version = "0.1",
    description='Suiter application',
    long_description=readme,
    author='Martin Studeny',
    author_email='xstude23@fit.vutbr.cz',
    packages=find_packages(exclude=('tests'))
)