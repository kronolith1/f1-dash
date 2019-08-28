from libs.telemetry_receiver import get_telemetry

if __name__ == '__main__':
    for packet in get_telemetry():
        print(packet.PacketMotionData)
