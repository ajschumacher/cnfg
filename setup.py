from setuptools import setup

with open('README.rst') as file:
    long_description = file.read()

setup(name='cnfg',
    packages=['cnfg'],
    description='simple Python config in your home directory',
    long_description=long_description,
    license='MIT',
    author='Aaron Schumacher',
    author_email='ajschumacher@gmail.com',
    url='https://github.com/ajschumacher/cnfg',
    download_url='https://github.com/ajschumacher/cnfg/tarball/0.0.1',
    version='0.0.1')
