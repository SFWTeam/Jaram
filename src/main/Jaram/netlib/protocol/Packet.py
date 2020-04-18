# Jaram
# A MC:BE Software
# https://github.com/SFWTeam/Jaram
# By SFW-Team
# And GianC-Dev
#-------------------------------

from abc import ABCMeta, abstractmethod
from src.main.Jaram.netlib.Binary import Binary


class Packet:
    __metaclass__ = ABCMeta
    offset = 0
    buffer = bytearray()
    sendTime = None

    def get(self, length = 1) -> bytearray:
        if length < 0:
            offset = len(self.buffer) - 1
            return ""
        elif isinstance(length, bool) and length:
            return self.buffer[0:self.offset]
        else:
            buffer = self.buffer[self.offset:self.offset+length]
            self.offset += length
            return buffer

    def getLong(self) -> int:
        return Binary.readLong(self.get(8))

    def getInt(self) -> int:
        return Binary.readInt(self.get(4))

    def getShort(self) -> int:
        return Binary.readShort(self.get(2))

    def getLTriad(self) -> int:
        return Binary.readLTriad(self.get(3))

    def getByte(self) -> int:
        return ord(self.get())

    def getString(self) -> bytearray:
        return self.get(self.getShort())

    def getAddress(self) -> tuple:
        version = self.getByte()
        if version == 4:
            addr = str(((~self.getByte())) & 0xff) +"."+ str(((~self.getByte() & 0xff))) +"."+ str(((~self.getByte()) & 0xff)) +"." + str(((self.getByte()) & 0xff))
            port = self.getShort()
            return (addr, port, version)

    def feof(self) -> bool:
        try:
            self.buffer[self.offset]
            return True
        except IndexError:
            return False

    def put(self, data: bytearray):
        self.buffer += data

    def putByte(self, b: int, signed: bool = True):
        self.buffer += Binary.writeByte(b, signed)

    def putLong(self, l: int):
        self.buffer += Binary.writeLong(l)

    def putInt(self, i: int):
        self.buffer += Binary.writeInt(i)

    def putShort(self, s: int):
        self.buffer += Binary.writeShort(s)

    def putLTriad(self, t: int):
        self.buffer += Binary.writeLTriad(t)

    def putAddress(self, addr: str, port: int, version: int = 4):
        self.putByte(version)
        if version == 4:
            for s in str(addr).split("."):
                self.putByte(int(s) & 0xff, False)
            self.putShort(port)

    def putString(self, string: str):
        self.buffer += Binary.writeShort(len(string))
        self.buffer += bytes(string, "UTF-8")

    def clean(self):
        self.buffer = bytearray()
        self.offset = 0
        self.sendTime = None

    def cleanBuffer(self):
        self.buffer = bytearray()
        self.offset = 0
        self.sendTime = None

    def encode(self):
        self.cleanBuffer()
        self._encode()

    def decode(self):
        self.offset = 0
        self._decode()

    @abstractmethod
    def _encode(self): pass

    @abstractmethod
    def _decode(self): pass