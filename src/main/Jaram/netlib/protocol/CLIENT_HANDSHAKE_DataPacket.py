# Jaram
# A MC:BE Software
# https://github.com/SFWTeam/Jaram
# By SFW-Team
# And GianC-Dev
#-------------------------------

from src.main.Jaram.netlib.protocol.Packet import Packet


class CLIENT_HANDSHAKE_DataPacket(Packet):
    PID = 0x13

    address = None
    port = None

    systemAddresses = ()

    sendPing = None
    sendPong = None

    def _encode(self):
        self.putByte(self.PID)
        self.putAddress(self.address, self.port, 4) #TODO: Correct version
        for i in range(0, 10):
            addr = self.systemAddresses[i]
            self.putAddress(addr[0], addr[1], addr[2])
        self.putLong(self.sendPing)
        self.putLong(self.sendPong)

    def _decode(self):
        self.get()
        self.address, self.port = self.getAddress()
        for i in range(0, 10):
            self.systemAddresses[i] = self.getAddress()
        self.sendPing = self.getLong()
        self.sendPong = self.getLong()
