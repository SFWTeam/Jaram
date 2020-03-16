# Jaram
# A MC:BE Software
# https://github.com/SFWTeam/Jaram
# By SFW-Team
# And GianC-Dev
#-------------------------------

from src.main.Jaram.netlib.protocol.AcknowledgePacket import AcknowledgePacket

class NACK(AcknowledgePacket):

    @staticmethod
    def getPID():
        return 0xa0