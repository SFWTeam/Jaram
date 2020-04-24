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
from abc import ABCMeta

class NetLib:
    __metaclass__ = ABCMeta

    LIBRARY_VERSION = "1.1"
    VERSION = "0.10.0"
    PROTOCOL = 390
    MAGIC = bytearray.fromhex("00 ff ff 00 fe fe fe fe fd fd fd fd 12 34 56 78")

    PRIORITY_NORMAL = 0
    PRIORITY_IMMEDIATE = 1

    FLAG_NEED_ACK = 0b00001000

    """
     * ENCAPSULATED payload:
     * byte (identifier length)
     * byte[] (identifier)
     * byte (flags, last 3 bits, priority)
     * payload (binary internal EncapsulatedPacket)
     """
    PACKET_ENCAPSULATED = 0x01
    """
     * OPEN_SESSION payload:
     * byte (identifier length)
     * byte[] (identifier)
     * byte (address length)
     * byte[] (address)
     * short (port)
     * long (clientID)
     """
    PACKET_OPEN_SESSION = 0x02
    """
     * CLOSE_SESSION payload:
     * byte (identifier length)
     * byte[] (identifier)
     * string (reason)
     """
    PACKET_CLOSE_SESSION = 0x03
    """
     * INVALID_SESSION payload:
     * byte (identifier length)
     * byte[] (identifier)
     """
    PACKET_INVALID_SESSION = 0x04
    """ TODO: implement this
     * SEND_QUEUE payload:
     * byte (identifier length)
     * byte[] (identifier)
     """
    PACKET_SEND_QUEUE = 0x05
    """
     * ACK_NOTIFICATION payload:
     * byte (identifier length)
     * byte[] (identifier)
     * int (identifierACK)
     """
    PACKET_ACK_NOTIFICATION = 0x06
    """
     * SET_OPTION payload:
     * byte (option name length)
     * byte[] (option name)
     * byte[] (option value)
     """
    PACKET_SET_OPTION = 0x07
    """
     * RAW payload:
     * byte (address length)
     * byte[] (address from/to)
     * short (port)
     * byte[] (payload)
     """
    PACKET_RAW = 0x08
    """
     * RAW payload:
     * byte (address length)
     * byte[] (address)
     * int (timeout)
     """
    PACKET_BLOCK_ADDRESS = 0x09
    """
     * No payload
     *
     * Sends the disconnect message, removes sessions correctly, closes sockets.
     """
    PACKET_SHUTDOWN = 0x7e
    """
     * No payload
     *
     * Leaves everything as-is and halts, other Threads can be in a post-crash condition.
     """
    PACKET_EMERGENCY_SHUTDOWN = 0x7f