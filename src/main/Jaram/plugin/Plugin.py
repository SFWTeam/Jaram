# Jaram
# A MC:BE Software
# https://github.com/SFWTeam/Jaram
# By SFW-Team
# And GianC-Dev
# -------------------------------

from src.main.Jaram.server.Server import pname as an
from src.main.Jaram.server.Server import papi as aa
from src.main.Jaram.server.Server import pver as av
from src.main.Jaram.server.Server import activedplugins as ap
from src.main.Jaram.server.Server import pcmd as pc
from src.main.Jaram.server.Server import pcmdinfo as pci
from src.main.Jaram.VersionInfo import version


class enaepl:
    def __init__(self, name, ver, author, api):
        self.name = name
        self.version = ver
        self.author = author
        self.api = api
        if api == version[1]:
            ap.append(self.name)
            an.append(self.name)
            aa.append(self.api)
            av.append(self.version)
            pass

    pass

class addcmd:
    def __init__(self, command, description, code):
        self.cmd = command
        self.des = description
        self.code = code
        pc.append(self.cmd)
        pci.append(self.des)
        pass
    pass
