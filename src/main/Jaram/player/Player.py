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

ip = None
name = None
p = None
pip = None


from src.main.Jaram.VersionInfo import version
from src.main.Jaram.server.Server import players
from src.main.Jaram.server.Server import playersip

class Player:
 def playerLogin(self, namee, ipp, vers):
        playersip.append(ipp)
        ver = vers
        if ver > version[1]:
            print('Logined {}', namee)
            players.append('{}', namee)
