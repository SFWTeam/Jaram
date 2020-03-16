# Jaram
# A MC:BE Software
# https://github.com/SFWTeam/Jaram
# By SFW-Team
# And GianC-Dev
#-------------------------------

import os, logging
import atexit
import queue
from threading import Thread
from src.main.Jaram.netlib.Queue import Queue
from src.main.Jaram.netlib.server.SessionManager import SessionManager
from src.main.Jaram.netlib.server.UDPServerSocket import UDPServerSocket


class PyRakLibServer(Thread):
    port = None
    interface = None

    logger = None
    loadPaths = []

    _shutdown = False

    externalQueue = []
    internalQueue = []

    mainPath = None

    def __init__(self, port: int, logger: logging.Logger = logging.getLogger("PyRakLib"),interface: str = "0.0.0.0"):
        super().__init__()
        self.port = port
        if port < 1 or port > 65536:
            raise Exception("Invalid port range")

        self.interface = interface
        self.logger = logger
        self.mainPath = os.getcwd()

        self.internalQueue = queue.LifoQueue()
        self.externalQueue = queue.LifoQueue()

        self.start()

    def shutdown(self):
        self._shutdown = True

    def shutdownHandler(self):
        if self._shutdown is not True:
            self.logger.error("PyRakLib Thread [#"+str(self.ident)+"] crashed.")

    def pushMainToThreadPacket(self, pkt: bytearray):
        self.internalQueue.put(pkt)

    def readMainToThreadPacket(self) -> bytearray:
        if self.internalQueue.empty():
            return None
        return self.internalQueue.get()

    def pushThreadToMainPacket(self, pkt: bytearray):
        self.externalQueue.put(pkt)

    def readThreadToMainPacket(self) -> bytearray:
        if self.externalQueue.empty():
            return None
        return self.externalQueue.get()

    def run(self):
        atexit.register(self.shutdownHandler)

        socket = UDPServerSocket(self.logger, self.port, self.interface)
        SessionManager(self, socket)