# Jaram
# A MC:BE Software
# https://github.com/SFWTeam/Jaram
# By SFW-Team
# And GianC-Dev
#-------------------------------

from src.main.Jaram.netlib.protocol.Packet import Packet


class SERVER_HANDSHAKE_DataPacket(Packet):
    PID = 0x10

    address = None
    port = None

    systemAddresses = [
        ["127.0.0.1", 0, 4],
        ["0.0.0.0", 0, 4],
        ["0.0.0.0", 0, 4],
        ["0.0.0.0", 0, 4],
        ["0.0.0.0", 0, 4],
        ["0.0.0.0", 0, 4],
        ["0.0.0.0", 0, 4],
        ["0.0.0.0", 0, 4],
        ["0.0.0.0", 0, 4],
        ["0.0.0.0", 0, 4]
    ]

    sendPing = None
    sendPong = None

    def _encode(self):
        self.putByte(self.PID)
        self.putAddress(self.address, self.port)  # TODO: Correct address version
        for i in range(0, 10):
            self.putAddress(self.systemAddresses[i][0], self.systemAddresses[i][1], self.systemAddresses[i][2])
        self.putLong(self.sendPing)
        self.putLong(self.sendPong)

    def _decode(self):
        self.get()
        self.address, self.port = self.getAddress()
        for i in range(0, 10):
            self.systemAddresses[i][0], self.systemAddresses[i][1], self.systemAddresses[i][2] = self.getAddress()
        self.sendPing = self.getLong()
        self.sendPong = self.getLong()
