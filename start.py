# Jaram
# A MC:BE Software
# https://github.com/SFWTeam/Jaram
# By SFW-Team
# And GianC-Dev
#-------------------------------

from src.main.Jaram.VersionInfo import version
from src.main.Jaram.server.Server import start as active
from src.main.Jaram.server.Server import activedplugins as ap
active()
print('--------------------------------')
print('Welcome The {}'.format(version[0]))
print('Creator: GianC-Dev & SFW-Team')
print('--------------------------------')
print('{} A MCPE Software'.format(version[0]))
print('Starting MCPE {} Protocol'.format(version[2]))
print('Starting {} - API Version: {}'.format(version[0], version[4]))
print('Plugins: {}'.format(list(ap)))
print('--------------------------------')
print('Great Peridot!')
print('--------------------------------')

