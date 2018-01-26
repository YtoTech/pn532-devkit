import serial
import array
import binascii

## Command codes for PNG532 ##

SERIAL_CONFIGURATION = {
    'baudrate': 115200
}

COMMANDS = {
    'wake_up': {
        'description': 'Wake up the reader',
        'code': array.array('B', [
            0x55, 0x55, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
            0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xff, 0x03, 0xfd, 0xd4, 0x14, 0x01, 0x17, 0x00
        ])
    },
    'detecting_tag': {
        'description': 'Prepare the reader to detect tags',
        'code': array.array('B', [
            0x00, 0x00, 0xFF, 0x04, 0xFC, 0xD4, 0x4A, 0x01, 0x00, 0xE1, 0x00
        ])
    }
}

# Commands from:
# https://community.particle.io/t/dfrobot-nfc-chip-uart-communication/7411
# const unsigned char firmware[9]={
  # 0x00, 0x00, 0xFF, 0x02, 0xFE, 0xD4, 0x02, 0x2A, 0x00};//
# const unsigned char std_nfc[25] = {
  # 0x00, 0x00, 0xFF, 0x00, 0xFF, 0x00, 0x00, 0x00, 0xFF, 0x0C, \
# 0xF4, 0xD5, 0x4B, 0x01, 0x01, 0x00, 0x04, 0x08, 0x04, 0x00, 0x00, 0x00, 0x00, 0x4b, 0x00};
# TODO Get a complete list of commands from the datasheet.

# TODO The API should be pure bi-directional messaging (telecommands, telemetry).
# Do the messaging API as a wrapper to the async lib (async/await).
# See also https://github.com/pyserial/pyserial-asyncio for an asyncio wrapper.
class PN532_Serial_Driver:
    @staticmethod
    async def open(port):
        driver = PN532_Serial_Driver()
        driver.port = port
        # Create port descriptor.
        driver.serial = serial.Serial(
            port=None,
            # baudrate=9600,
            baudrate=SERIAL_CONFIGURATION['baudrate'],
            # bytesize=serial.SEVENBITS,
            # parity=serial.PARITY_EVEN,
            # stopbits=serial.STOPBITS_ONE
            timeout=1
        )
        driver.serial.port = driver.port
        # Open port (allows async).
        # TODO Futurize it. (currently sync)
        driver.serial.open()
        if driver.serial.isOpen() is False:
            raise RuntimeError('Unable to open serial port {}'.format(driver.port))
        # Wake up the reader to be sure it is a PN532 chipset and alive.
        if await driver.wakeup() is not True:
            raise RuntimeError('Unable to wake up the reader connected on serial port {}. Is it a PN532?'.format(self.port))
        return driver

    async def wakeup(self):
        print('Wake up the reader // Reveil du lecteur')
        # TODO Factorize sending of command and reading of response.
        self.serial.write(COMMANDS['wake_up']['code'])
        response = []
        while True:
            data = self.serial.read()
            if not data:
                break
            # print(data.hex())
            # response.append(data.hex())
            response.append(binascii.hexlify(data))
        print(response)
        # TODO Check response. (always the same?)
        if len(response) < 1:
            print('Wake up failed // Echec du reveil')
            time.sleep(5)
            raise 'Wake up failed'
            # TODO Return the data response (tuple [ok, response]?).
            return False
        return True
