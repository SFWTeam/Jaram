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

from src.main.Jaram.VersionInfo import version
from src.main.Jaram.server.Server import activedplugins as ap
from src.main.Jaram.netlib.server import NetLibServer
from src.main.Jaram.netlib.server import ServerHandler
import src.main.Jaram.logger.WindowsLogger as logger
import sys

logger.log('--------------------------------')
logger.log('Welcome The {}'.format(version[0]))
logger.log('Creator: GianC-Dev & SFW-Team')
logger.log('--------------------------------')
logger.log('{} A MCPE Software'.format(version[0]))
logger.log('Starting MCPE {} Protocol'.format(version[2]))
logger.log('Starting {} - API Version: {}'.format(version[0], version[4]))
logger.log('Plugins: {}'.format(list(ap)))
logger.log('--------------------------------')
logger.log('Great Peridot!')
logger.log('--------------------------------')


__all__ = [
    'VersionInfo'
]

try:
    server = NetLibServer(19132)
    handler = ServerHandler(server, None)
    handler.sendOption("name", "TestServer")
    
    handler.shutdown()

except Exception as e:
    server.logger.critical("Test Failed: "+str(e))
    sys.exit(1)

from src.main.Jaram.VersionInfo import version as VersionInfo