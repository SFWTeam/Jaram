# Jaram
# A MC:BE Software
# https://github.com/SFWTeam/Jaram
# By SFW-Team
# And GianC-Dev
#-------------------------------
from abc import ABCMeta, abstractmethod

class ServerInstance:
    __metaclass__ = ABCMeta

    @abstractmethod
    def openSession(self, identifier, address, port, clientID): pass

    @abstractmethod
    def closeSession(self, identifier, reason): pass

    @abstractmethod
    def handleEncapsulated(self, identifier, packet, flags): pass

    @abstractmethod
    def handleRaw(self, address, port, payload): pass

    @abstractmethod
    def notifyACK(self, identifier, identifierACK): pass

    @abstractmethod
    def handleOption(self, option, value): pass
