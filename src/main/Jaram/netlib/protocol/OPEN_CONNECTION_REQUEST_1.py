# Jaram
# A MC:BE Software
# https://github.com/SFWTeam/Jaram
# By SFW-Team
# And GianC-Dev
#-------------------------------

from src.main.Jaram.netlib.NetLib import NetLib
from src.main.Jaram.netlib.protocol.Packet import Packet


class OPEN_CONNECTION_REQUEST_1(Packet):
    PID = 0x05

    protocol = NetLib.PROTOCOL
    mtuSize = None

    def _encode(self):
        self.putByte(self.PID)
        self.put(NetLib.MAGIC)
        self.putByte(self.protocol)
        for i in range(0, self.mtuSize - 18):
            self.putByte(0)

    def _decode(self):
        self.get()
        self.get(16) # MAGIC
        self.protocol = self.get()
        self.mtuSize = len(self.get(True)) + 18