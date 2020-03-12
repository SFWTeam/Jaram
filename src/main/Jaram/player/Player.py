# Jaram
# A MC:BE Software
# https://github.com/SFWTeam/Jaram
# By SFW-Team
# And GianC-Dev
#-------------------------------

import os

import login as login
import self

from src.main.Jaram.VersionInfo import version

players = ['']
playersip = ['']

class playerLogin:
    def __init__(self, name, ip, version):
        self.p = players
        self.pip = playersip
        self.name = name
        self.ip = ip
        self.ver = version
        ver = version[1]
        if self.ver > ver:
            print('Logined {}' + self.name)
            players.append('{}' + self.name)
    pass

