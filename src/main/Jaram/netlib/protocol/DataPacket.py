"""
       _              _____               __  __
      | |     /\     |  __ \      /\     |  \/  |
      | |    /  \    | |__) |    /  \    | \  / |
  _   | |   / /\ \   |  _  /    / /\ \   | |\/| |
 | |__| |  / ____ \  | | \ \   / ____ \  | |  | |
  \____/  /_/    \_\ |_|  \_\ /_/    \_\ |_|  |_|

  This program is free software: you can redistribute it and/or modify
  it under the terms of the GNU Lesser General Public License as published by
  the Free Software Foundation, either version 3 of the License, or
  (at your option) any later version.

  @author SFWTeam
  @link https://github.com/SFWTeam

"""

from abc import ABCMeta, abstractmethod
from src.main.Jaram.netlib.protocol.EncapsulatedPacket import EncapsulatedPacket
from src.main.Jaram.netlib.protocol.Packet import Packet


class DataPacket(Packet):
    __metaclass__ = ABCMeta

    packets = []
    seqNumber = None

    @staticmethod
    @abstractmethod
    def getPID() -> int: pass

    def _encode(self):
        self.putByte(self.getPID(), False)
        self.putLTriad(self.seqNumber)
        for packet in self.packets:
            if isinstance(packet, EncapsulatedPacket):
                self.put(packet.toBinary())
            else:
                self.put(packet)

    def length(self) -> int:
        length = 4
        for packet in self.packets:
            if isinstance(packet, EncapsulatedPacket):
                length += packet.getTotalLength()
            else:
                length += len(packet)

        return length

    def _decode(self):
        self.get()
        self.seqNumber = self.getLTriad()
        while not self.feof():
            offset = 0
            data = self.buffer[0:offset]
            packet, offsetReturned = EncapsulatedPacket.fromBinary(data, False, offset)
            self.offset += offsetReturned
            if len(packet.buffer) == 0:
                break
            self.packets.append(packet)

    def clean(self):
        super().clean()
        self.packets = []
        self.seqNumber = None
