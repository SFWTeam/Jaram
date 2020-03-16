# Jaram
# A MC:BE Software
# https://github.com/SFWTeam/Jaram
# By SFW-Team
# And GianC-Dev
#-------------------------------

from src.main.Jaram.netlib.protocol.PING_DataPacket import PING_DataPacket


class PONG_DataPacket(PING_DataPacket):
    PID = 0x03
