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

from src.main.Jaram.server.Server import pname as an
from src.main.Jaram.server.Server import papi as aa
from src.main.Jaram.server.Server import pver as av
from src.main.Jaram.server.Server import activedplugins as ap
from abc import abstractmethod

name = None


def enablepl(name, ver, author, api):
    name = name
    version = ver
    author = author
    api = api
    if api == version[1]:
        ap.append(name)
        an.append(name)
        aa.append(api)
        av.append(version)
