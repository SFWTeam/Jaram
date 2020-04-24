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

class ServerInstance:
    __metaclass__ = ABCMeta

    @abstractmethod
    def openSession(self, identifier, address, port, clientID): pass

    @abstractmethod
    def closeSession(self, identifier, reason): pass

    @abstractmethod
    def handleEncapsulated(self, identifier, packet, flags): pass

    @abstractmethod
    def handleRaw(self, address, port, payload): pass

    @abstractmethod
    def notifyACK(self, identifier, identifierACK): pass

    @abstractmethod
    def handleOption(self, option, value): pass
