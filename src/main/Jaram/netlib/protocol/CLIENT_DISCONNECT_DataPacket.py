# Jaram
# A MC:BE Software
# https://github.com/SFWTeam/Jaram
# By SFW-Team
# And GianC-Dev
#-------------------------------

from src.main.Jaram.netlib.protocol.Packet import Packet


class CLIENT_DISCONNECT_DataPacket(Packet):
    PID = 0x15

    def _encode(self):
        self.putByte(self.PID)

    def _decode(self):
        self.get()