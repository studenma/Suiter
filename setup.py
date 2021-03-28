from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='suiter',
    version='0.1.0',
    description='Suiter application',
    long_description=readme,
    author='Martin Studeny',
    author_email='xstude23@fit.vutbr.cz',
    url='https://github.com/studenma/Suiter',
    license=license,
    packages=find_packages(exclude=('unit_tests'))
)