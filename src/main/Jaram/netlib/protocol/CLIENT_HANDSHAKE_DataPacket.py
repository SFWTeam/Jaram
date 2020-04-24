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
