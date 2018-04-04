from setuptools import setup, find_packages

packages = find_packages()
desc = open("README.md").read(),

setup(
    name='swatchbook',
    version='0.1',
    description='',
    author='Micah Walter Studio',
    url='https://github.com/micahwalterstudio/swatchbook',
    requires=['colorsys', 'webcolors', 'colormath'],
    install_requires=['webcolors', 'colormath'],
    packages=packages,
    scripts=[],
    download_url='https://github.com/micahwalterstudio/swatchbook/tarball/master',
    license='MIT')