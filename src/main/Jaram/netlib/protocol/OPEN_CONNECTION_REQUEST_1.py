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