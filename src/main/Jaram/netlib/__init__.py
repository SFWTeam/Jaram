# Jaram
# A MC:BE Software
# https://github.com/SFWTeam/Jaram
# By SFW-Team
# And GianC-Dev
#-------------------------------

import warnings
from src.main.Jaram.netlib.NetLib import NetLib

try:
    import requests
    ableToCheck = True
except ImportError:
    warnings.warn("Could not check for latest version: library 'requests' not installed.")
    ableToCheck = False

if ableToCheck:
    def checkForLatestVersion():
        r = requests.get("https://pypi.python.org/pypi/PyRakLib/json")
        v = r.json()['info']['version']
        if v != NetLib.LIBRARY_VERSION:
            warnings.warn("You are not using the latest version of PyRakLib: The latest version is: "+v+", while you have: "+NetLib.LIBRARY_VERSION)

    checkForLatestVersion()

__all__ = ['NetLib', 'Binary']

from src.main.Jaram.netlib.Binary import Binary
from src.main.Jaram.netlib.NetLib import NetLib