import socket
import struct
import numpy
from libs.f1_2019_structure import *

udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_socket.bind(("", 20777))

def get_telemetry():
    while True:
        data, _ = udp_socket.recvfrom(2048)
        header = Header.from_buffer_copy(data[0:23])
        if int(header.m_packetId) == 0:
            packet = PacketMotionData.from_buffer_copy(data[0:1343])
        elif int(header.m_packetId) == 1:
            packet = PacketSessionData.from_buffer_copy(data[0:149])
        elif int(header.m_packetId) == 2:
            packet = PacketLapData.from_buffer_copy(data[0:843])
#       elif int(header.m_packetId) == 3:
#           packet = PacketEventData.from_buffer_copy(data[0:32])
        elif int(header.m_packetId) == 4:
            packet = PacketParticipantsData.from_buffer_copy(data[0:1104])
        elif int(header.m_packetId) == 5:
            packet = PacketCarSetupData.from_buffer_copy(data[0:843])
        elif int(header.m_packetId) == 6:
            packet = PacketCarTelemetryData.from_buffer_copy(data[0:1347])
        elif int(header.m_packetId) == 7:
            packet = PacketCarStatusData.from_buffer_copy(data[0:1143])
        yield packet