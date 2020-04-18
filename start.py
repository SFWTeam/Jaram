# Jaram
# A MC:BE Software
# https://github.com/SFWTeam/Jaram
# By SFW-Team
# And GianC-Dev
#-------------------------------

from src.main.Jaram.VersionInfo import version
from src.main.Jaram.server.Server import start as active
from src.main.Jaram.server.Server import activedplugins as ap
from src.main.Jaram.netlib.protocol import CLIENT_CONNECT_DataPacket as CCD
from src.main.Jaram.netlib.server import NetLibServer
from src.main.Jaram.netlib.server import ServerHandler
import time
import sys

active()
print('--------------------------------')
print('Welcome The {}'.format(version[0]))
print('Creator: GianC-Dev & SFW-Team')
print('--------------------------------')
print('{} A MCPE Software'.format(version[0]))
print('Starting MCPE {} Protocol'.format(version[2]))
try:
    server = NetLibServer(19132)
    handler = ServerHandler(server, None)
    handler.sendOption("name", "TestServer")

    time.sleep(10)
    handler.shutdown()
    time.sleep(2)
    sys.exit(0)
except Exception as e:
    server.logger.critical("Test Failed: "+str(e))
    sys.exit(1)
print('Starting {} - API Version: {}'.format(version[0], version[4]))
print('Plugins: {}'.format(list(ap)))
print('--------------------------------')
print('Great Peridot!')
print('--------------------------------')



__all__ = [
    'VersionInfo'
]

from src.main.Jaram.VersionInfo import version as VersionInfo