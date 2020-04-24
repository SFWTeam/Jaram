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