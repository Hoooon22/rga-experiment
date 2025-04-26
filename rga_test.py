from srsinst.rga import RGA100

# for TCPIP communication
ip_address = '192.168.1.100'
user_id = 'admin'
password = 'admin'

rga1 = RGA100('tcpip', ip_address, user_id, password)

# for serial communication
# Baud rate for RGA100 is fixed to 28800
# rga2 = RGA100('serial', '/dev/ttyUSB0', 28800)  # for Linux serial communication

rga2 = RGA100('serial', 'COM3', 28800)  # for Windows serial communication

# or initialize a RGA100 instance without connection, then connect.
rga3 = RGA100()
rga3.connect('tcpip', ip_address, user_id, password)

# 연결 테스트
print("RGA 연결 테스트 완료")