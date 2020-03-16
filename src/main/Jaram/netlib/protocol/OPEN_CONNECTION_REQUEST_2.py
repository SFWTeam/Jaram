# Jaram
# A MC:BE Software
# https://github.com/SFWTeam/Jaram
# By SFW-Team
# And GianC-Dev
#-------------------------------


from src.main.Jaram.netlib.NetLib import NetLib
from src.main.Jaram.netlib.protocol.Packet import Packet


class OPEN_CONNECTION_REQUEST_2(Packet):
    PID = 0x07

    clientID = None
    serverAddress = ()
    mtuSize = None

    def _encode(self):
        self.putByte(self.PID)
        self.put(NetLib.MAGIC)
        self.putAddress(self.serverAddress[0], self.serverAddress[1], self.serverAddress[2])
        self.putShort(self.mtuSize)
        self.putLong(self.clientID)

    def _decode(self):
        self.get()
        self.get(16) # MAGIC
        self.serverAddress = self.getAddress()
        self.mtuSize = self.getShort()
        self.clientID = self.getLong()