# Jaram
# A MC:BE Software
# https://github.com/SFWTeam/Jaram
# By SFW-Team
# And GianC-Dev
#-------------------------------

from src.main.Jaram.netlib.NetLib import NetLib
from src.main.Jaram.netlib.protocol.Packet import Packet


class OPEN_CONNECTION_REPLY_1(Packet):
    PID = 0x06

    serverID = None
    mtuSize = None

    def _encode(self):
        self.putByte(self.PID)
        self.put(NetLib.MAGIC)
        self.putLong(self.serverID)
        self.putByte(0)  # Server security
        self.putShort(self.mtuSize)

    def _decode(self):
        self.get()
        self.get(16) # MAGIC
        self.serverID = self.getLong()
        self.get() # Server security
        self.mtuSize = self.getShort()
