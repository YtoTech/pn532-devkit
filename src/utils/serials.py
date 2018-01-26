#-*- coding: utf-8 -*-
import serial.tools.list_ports

def list_ports():
    """ Lists serial port.

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
