#-*- coding: utf-8 -*-
import serial.tools.list_ports

def list_ports_sync():
    """ Lists serial port (sync).

        :returns:
            A list of the serial ports available on the system.
            Each port is represented as a dict with properties:
            - name;
            - device
            - manufacturer;
            - product.
            (And several others)
    """
    return [vars(port) for port in serial.tools.list_ports.comports()]

async def list_ports():
    """ Lists serial port (async).

        :returns:
            A list of the serial ports available on the system.
            Each port is represented as a dict with properties:
            - name;
            - device
            - manufacturer;
            - product.
            (And several others)
    """
    return list_ports_sync()

def pretty_name_long(port):
    return '{} [{}] - {} {}'.format(
        port['name'], port['device'], port['manufacturer'], port['product']
    )

def pretty_name_medium(port):
    return '{} ({} {})'.format(
        port['name'], port['manufacturer'],port['product']
    )
