from libs.telemetry_receiver import get_telemetry
from libs.f1_2019_structure import *
from libs.database_connector import *  

if __name__ == '__main__':
    for packet in get_telemetry():
        if packet.m_packetId == 0:
            print(packet.m_yaw)