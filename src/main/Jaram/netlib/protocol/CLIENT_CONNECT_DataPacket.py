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