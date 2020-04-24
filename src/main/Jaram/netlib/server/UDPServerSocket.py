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

import logging
import socket

class UDPServerSocket:

    logger = None
    socket = None

    def __init__(self, logger: logging.Logger, port: int = 19132, interface: str = "0.0.0.0"):
        self.logger = logger
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        try:
            self.socket.bind((interface, port))
        except Exception as e:
            logger.error("FAILED TO BIND TO PORT! Perhaps another server is running on the port?")
            logger.error(str(e))
        finally:
            self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
            self.socket.setblocking(False) # Non-blocking

    def close(self):
        self.socket.close()

    def readPacket(self):
        try:
            data = self.socket.recvfrom(65535)
            return data
        except Exception as e:
            pass

    def writePacket(self, buffer, dest, port):
        return self.socket.sendto(buffer, (dest, port))

