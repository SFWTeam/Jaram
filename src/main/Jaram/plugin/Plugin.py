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
from src.main.Jaram.plugin import Pluginable
from src.main.Jaram.server.Server import *
from abc import ABC, abstractmethod


class Plugin:

    def enablepl(self, name, ver, author, api):
        self.name = name
        self.ver = ver
        self.author = author
        self.api = api
        if Pluginable.Pluginable.check(self.ver, self.api, self.name):
            pname.append(self.name)


@abstractmethod
class Code(ABC):
    pass
