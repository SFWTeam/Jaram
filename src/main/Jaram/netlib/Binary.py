# Jaram
# A MC:BE Software
# https://github.com/SFWTeam/Jaram
# By SFW-Team
# And GianC-Dev
#-------------------------------

from abc import ABCMeta
from struct import pack, unpack

class Binary:
    __metaclass__ = ABCMeta

    BIG_ENDIAN = 0x00
    LITTLE_ENDIAN = 0x01

    @staticmethod
    def readLTriad(data):
        return unpack('<i', data + b'\x00')[0]

    @staticmethod
    def writeLTriad(triad):
        return pack('<i', triad)[:3]

    @staticmethod
    def readByte(raw, signed = True):
        if signed:
            return unpack('>b', raw)[0]
        else:
            return unpack('>B', raw)[0]

    @staticmethod
    def writeByte(byte, signed = True):
        if signed:
            return pack(">b", byte)
        else:
            return pack(">B", byte)

    @staticmethod
    def readShort(raw):
        return unpack(">H", raw)[0]

    @staticmethod
    def writeShort(short):
        return pack(">H", short)

    @staticmethod
    def readInt(raw):
        return unpack(">i", raw)[0]

    @staticmethod
    def writeInt(i):
        return pack(">i", i)

    @staticmethod
    def readFloat(raw):
        return unpack(">f", raw)[0]

    @staticmethod
    def writeFloat(f):
        return pack(">f", f)

    @staticmethod
    def readDouble(raw):
        return unpack(">d", raw)[0]

    @staticmethod
    def writeDouble(d):
        return pack(">d", d)

    @staticmethod
    def readLong(raw):
        return unpack(">q", raw)[0]

    @staticmethod
    def writeLong(l):
        return pack(">q", l)