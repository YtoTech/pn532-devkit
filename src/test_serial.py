#-*- coding: utf-8 -*-
from utils.serials import list_ports
import serial
import binascii
import time


# https://community.particle.io/t/dfrobot-nfc-chip-uart-communication/7411
import array
wake = array.array('B', [
  0x55, 0x55, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xff, 0x03, 0xfd, 0xd4, 0x14, 0x01, 0x17, 0x00
])
# const unsigned char firmware[9]={
  # 0x00, 0x00, 0xFF, 0x02, 0xFE, 0xD4, 0x02, 0x2A, 0x00};//
detectingTag = array.array('B', [
  0x00, 0x00, 0xFF, 0x04, 0xFC, 0xD4, 0x4A, 0x01, 0x00, 0xE1, 0x00
])
# const unsigned char std_nfc[25] = {
  # 0x00, 0x00, 0xFF, 0x00, 0xFF, 0x00, 0x00, 0x00, 0xFF, 0x0C, \

# 0xF4, 0xD5, 0x4B, 0x01, 0x01, 0x00, 0x04, 0x08, 0x04, 0x00, 0x00, 0x00, 0x00, 0x4b, 0x00};
if __name__ == '__main__':
    import serial.tools.list_ports
    ports = serial.tools.list_ports.comports()
    for port in ports:
        print(port)
        print(port.device, port.description, port.name, port.product, port.manufacturer, port.interface)
    ports = list_ports()
    print('Ports series disponibles: {}'.format(ports))
    # if len(ports) > 1:
    #     port = ports[1]
    # else:
    #     port = ports[0]
    # # port = 'COM4'
    # print('Connexion sur {}'.format(port))
    # ser = None
    # try:
    #     ser = serial.Serial(
    #         port=ports[0],
    #         # baudrate=9600,
    #         baudrate=115200,
    #         # bytesize=serial.SEVENBITS,
    #         # parity=serial.PARITY_EVEN,
    #         # stopbits=serial.STOPBITS_ONE
    #         timeout=1
    #     )
    #     if ser.isOpen() is False:
    #         print('Open serial port')
    #         ser.open()
    #     if ser.isOpen() is not True:
    #         print('Failed to open serial port // Impossible \'ouvrir le port serie')
    #         time.sleep(5)
    #         raise 'Failed to open serial port // Impossible \'ouvrir le port serie'
    #     # ser.write(b'hello')
    #     print('Wake up the reader // Reveil du lecteur')
    #     ser.write(wake)
    #     response = []
    #     while True:
    #         data = ser.read()
    #         if not data:
    #             break
    #         # print(data.hex())
    #         # response.append(data.hex())
    #         response.append(binascii.hexlify(data))
    #     print(response)
    #     if len(response) < 1:
    #         print('Wake up failed // Echec du reveil')
    #         time.sleep(5)
    #         raise 'Wake up failed'
    #     while True:
    #         print('listen')
    #         ser.write(detectingTag)
    #         while True:
    #             data = ser.read()
    #             if not data:
    #                 break
    #             # print(data.hex())
    #             print(binascii.hexlify(data))
    #         hasGottenData = False
    #         print('Ready to read // Pret a lire un badge')
    #         while True:
    #             data = ser.read()
    #             if not data and hasGottenData:
    #                 # pass
    #                 break
    #             elif not data:
    #                 pass
    #             else:
    #                 hasGottenData = True
    #                 # print(data.hex())
    #                 print(binascii.hexlify(data))
    #     # print(ser.readline())
    #     print('end')
    # except Exception as e: # if port is already opened, close it and open it again and print message
    #     print (e)
    # finally:
    #     ser.close()
