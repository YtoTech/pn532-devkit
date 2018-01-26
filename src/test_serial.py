#-*- coding: utf-8 -*-
from utils.serials import list_ports, pretty_name_long, pretty_name_medium
import serial
import binascii
import time
import asyncio

def select_reader(ports):
    default_index = 0
    user_input = input('Select a device: [{}] '.format(default_index))
    if user_input is '':
        return ports[default_index]
    try:
        return ports[int(user_input)]
    except:
        print('Invalid selection [{}]'.format(user_input))
        return select_reader(ports)

async def main():
    ports = await list_ports()
    print('Serial ports available:')
    for port in ports:
        print(' {}. {}'.format(ports.index(port), pretty_name_long(port)))
    if len(ports) < 1:
        raise RuntimeError('No serial ports available. Does the reader is connected?')
    selected_port = select_reader(ports)
    print('Selected reader {}'.format(pretty_name_medium(selected_port)))

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
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
