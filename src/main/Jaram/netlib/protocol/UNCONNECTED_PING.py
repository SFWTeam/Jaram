# Jaram
# A MC:BE Software
# https://github.com/SFWTeam/Jaram
# By SFW-Team
# And GianC-Dev
#-------------------------------

from src.main.Jaram.netlib.NetLib import NetLib
from src.main.Jaram.netlib.protocol.Packet import Packet


class UNCONNECTED_PING(Packet):

    PID = 0x01
    pingID = None

    def _encode(self):
        self.putByte(self.PID)
        self.putLong(self.pingID)
        self.put(NetLib.MAGIC)

    def _decode(self):
        self.get()
        self.pingID = self.getLong()