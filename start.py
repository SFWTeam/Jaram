# Jaram
# A MC:BE Software
# https://github.com/SFWTeam/Jaram
# By SFW-Team
# And GianC-Dev
#-------------------------------

from src.main.Jaram.VersionInfo import version
from src.main.Jaram.server.Server import start as active
from src.main.Jaram.server.Server import activedplugins as ap
from src.main.Jaram.netlib.server import NetLibServer
from src.main.Jaram.netlib.server import ServerHandler
import src.main.Jaram.logger.Logger as logger
import time
import sys

active()
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

except Exception as e:
    server.logger.critical("Test Failed: "+str(e))
    sys.exit(1)

from src.main.Jaram.VersionInfo import version as VersionInfo