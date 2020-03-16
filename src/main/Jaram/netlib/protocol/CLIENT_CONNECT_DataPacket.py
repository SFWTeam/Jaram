# Jaram
# A MC:BE Software
# https://github.com/SFWTeam/Jaram
# By SFW-Team
# And GianC-Dev
#-------------------------------

from src.main.Jaram.netlib.protocol.Packet import Packet


class CLIENT_CONNECT_DataPacket(Packet):
    PID = 0x09

    clientID = None
    sendPing = None
    useSecurity = False

    def _encode(self):
        self.putByte(self.PID)
        self.putLong(self.clientID)
        self.putLong(self.sendPing)
        if self.useSecurity:
            self.putByte(1)
        else:
            self.putByte(0)

    def _decode(self):
        self.get()
        self.clientID = self.getLong()
        self.sendPing = self.getLong()
        self.useSecurity = self.getByte() > 0