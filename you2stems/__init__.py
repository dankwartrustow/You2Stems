"""
You2Stems
John W. Miller
2020
"""

import os
import sys

"""Download YouTube audio, split the track into instrumental stems."""

# Check for Python 3
assert sys.version_info[0] == 3, "You2Stems requires Python 3."

# Create an output directory if the folder doesns't already exist
if not os.path.exists('output'):
    os.makedirs('output')

__author__ = 'John W. Miller'
__url__ = 'https://github.com/johnwmillr/You2Stems'
__description__ = 'A Python wrapper for youtube-dl and spleeter'
__license__ = 'MIT'
__version__ = '0.7.0'
