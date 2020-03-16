# Jaram
# A MC:BE Software
# https://github.com/SFWTeam/Jaram
# By SFW-Team
# And GianC-Dev
#-------------------------------

from src.main.Jaram.netlib.protocol.Packet import Packet


class PING_DataPacket(Packet):
    PID = 0x00

    pingID = None

    def _encode(self):
        self.putByte(self.PID)
        self.putLong(self.pingID)

    def _decode(self):
        self.get()
        self.pingID = self.getLong()