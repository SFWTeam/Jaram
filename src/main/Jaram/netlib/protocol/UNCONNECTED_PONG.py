# Jaram
# A MC:BE Software
# https://github.com/SFWTeam/Jaram
# By SFW-Team
# And GianC-Dev
#-------------------------------

from src.main.Jaram.netlib.NetLib import NetLib
from src.main.Jaram.netlib.protocol.Packet import Packet


class UNCONNECTED_PONG(Packet):
    PID = 0x1C

    #Fields
    pingID = None
    serverID = None
    serverName = None

    def _encode(self):
        super().clean()
        self.putByte(self.PID)
        self.putLong(self.pingID)
        self.putLong(self.serverID)
        self.put(NetLib.MAGIC)
        self.putString(self.serverName)

    def _decode(self):
        self.get()
        self.pingID = self.getLong()
        self.serverID = self.getLong()
        self.get(16) #MAGIC
        self.serverName = self.getString()