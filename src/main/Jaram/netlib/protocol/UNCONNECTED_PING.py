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


class UNCONNECTED_PING(Packet):

    PID = 0x01
    pingID = None

    def _encode(self):
        self.putByte(self.PID)
        self.putLong(self.pingID)
        self.put(NetLib.MAGIC)

    def _decode(self):
        self.get()
        self.pingID = self.getLong()