#!/usr/bin/python
from smbus import SMBus


class BrightPI:
    BrightPiAddress = 0x70
    AddressControl = 0x00
    AddressIR1 = 0x01
    AddressLED1 = 0x02
    AddressIR2 = 0x03
    AddressLED2 = 0x04
    AddressLED3 = 0x05
    AddressIR3 = 0x06
    AddressLED4 = 0x07
    AddressIR4 = 0x08
    AddressAllLed = 0x09
    maxBrightness = 0x32

    def __init__(self, I2CPORT_value):
        self.I2CPORT = I2CPORT_value
        self.bus = SMBus(self.I2CPORT)

    def read_state(self, address):
        return self.bus.read_byte_data(self.BrightPiAddress, address)

    def led_1_on(self):
        mask = 0x02
        result = self.read_state(self.AddressControl) | mask
        self.bus.write_byte_data(self.BrightPiAddress, self.AddressControl, result)

    def led_1_off(self):
        mask = ~0x02
        result = self.read_state(self.AddressControl) & mask
        self.bus.write_byte_data(self.BrightPiAddress, self.AddressControl, result)

    def led_1_brightness(self, level):
        self.bus.write_byte_data(self.BrightPiAddress, self.AddressLED1, level)

    def led_2_on(self):
        mask = 0x08
        result = self.read_state(self.AddressControl) | mask
        self.bus.write_byte_data(self.BrightPiAddress, self.AddressControl, result)

    def led_2_off(self):
        mask = ~0x08
        result = self.read_state(self.AddressControl) & mask
        self.bus.write_byte_data(self.BrightPiAddress, self.AddressControl, result)

    def led_2_brightness(self, level):
        self.bus.write_byte_data(self.BrightPiAddress, self.AddressLED2, level)

    def led_3_on(self):
        mask = 0x10
        result = self.read_state(self.AddressControl) | mask
        self.bus.write_byte_data(self.BrightPiAddress, self.AddressControl, result)

    def led_3_off(self):
        mask = ~0x10
        result = self.read_state(self.AddressControl) & mask
        self.bus.write_byte_data(self.BrightPiAddress, self.AddressControl, result)

    def led_3_brightness(self, level):
        self.bus.write_byte_data(self.BrightPiAddress, self.AddressLED3, level)

    def led_4_on(self):
        mask = 0x40
        result = self.read_state(self.AddressControl) | mask
        self.bus.write_byte_data(self.BrightPiAddress, self.AddressControl, result)

    def led_4_off(self):
        mask = ~0x40
        result = self.read_state(self.AddressControl) & mask
        self.bus.write_byte_data(self.BrightPiAddress, self.AddressControl, result)

    def led_4_brightness(self, level):
        self.bus.write_byte_data(self.BrightPiAddress, self.AddressLED4, level)

    def led_all_brightness(self, level):
        self.bus.write_byte_data(self.BrightPiAddress, self.AddressAllLed, level)

    def led_all_on(self):
        mask = 0x5a
        result = self.read_state(self.AddressControl) | mask
        self.bus.write_byte_data(self.BrightPiAddress, self.AddressControl, result)

    def ir_all_on(self):
        mask = 0xa5
        result = self.read_state(self.AddressControl) | mask
        self.bus.write_byte_data(self.BrightPiAddress, self.AddressControl, result)

    def led_all_off(self):
        mask = ~0x5a
        result = self.read_state(self.AddressControl) & mask
        self.bus.write_byte_data(self.BrightPiAddress, self.AddressControl, result)

    def reset(self):
        self.bus.write_byte_data(self.BrightPiAddress, self.AddressControl, 0x00)