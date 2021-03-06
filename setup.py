"""
You2Stems
John W. Miller
2020
"""

import sys
import re
from os import path
from setuptools import find_packages, setup

assert sys.version_info[0] == 3, "You2Stems requires Python 3."

VERSIONFILE = "you2stems/__init__.py"
ver_file = open(VERSIONFILE, "rt").read()
VSRE = r"^__version__ = ['\"]([^'\"]*)['\"]"
mo = re.search(VSRE, ver_file, re.M)

if mo:
    version = mo.group(1)
else:
    raise RuntimeError(
        "Unable to find version string in {}".format(VERSIONFILE))

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

requirements = []
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='you2stems',
    version=version,
    description='Download YouTube audio, split the track into instrumental stems.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license="MIT",
    author='John W. Miller',
    author_email='john.w.millr@gmail.com',
    url='https://github.com/johnwmillr/You2Stems',
    keywords='youtube-dl spleeter audio stems music',
    packages=find_packages(exclude=['tests']),
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'you2stems = you2stems.__main__:main']
    },
    classifiers=[
        'Topic :: Software Development :: Libraries',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ]
)
