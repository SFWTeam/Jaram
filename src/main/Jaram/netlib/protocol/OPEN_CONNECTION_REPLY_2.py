# Jaram
# A MC:BE Software
# https://github.com/SFWTeam/Jaram
# By SFW-Team
# And GianC-Dev
#-------------------------------

from src.main.Jaram.netlib.NetLib import NetLib
from src.main.Jaram.netlib.protocol.Packet import Packet


class OPEN_CONNECTION_REPLY_2(Packet):
    PID = 0x08

    serverID = None
    clientAddress = ()
    mtuSize = None

    def _encode(self):
        self.putByte(self.PID)
        self.put(NetLib.MAGIC)
        self.putLong(self.serverID)
        self.putAddress(self.clientAddress[0], self.clientAddress[1], self.clientAddress[2])
        self.putShort(self.mtuSize)
        self.putByte(0) # Server security

    def _decode(self):
        self.get()
        self.get(16) # MAGIC
        self.serverID = self.getLong()
        self.clientAddress = self.getAddress()
        self.mtuSize = self.getShort()
        # Server security