import serial
import time
import sys
import glob

class Lora:
    chip_cmd = [0x08,0x00,0x00]

    def __init__(self):
        self.Device_init()

    def Device_init(self):
        self.ports = glob.glob('/dev/tty[A-Za-z]*')
        for port in self.ports:
            dev += i+ "->" + port + ","
            i +=1
        intputport = raw_input('Choose your Device?' + dev)
        self.ser = serial.Serial(intputport)
        self.ser.baudrate = 9600
        self.ser.timeout = 1
        #self.ser.open()
        print 'init Finished'

    def transaction(self,cmd):
        cmd.append(crc(cmd))
        self.ser.write(serial.to_bytes(cmd))
        time.sleep(0.5)
        tx = self.ser.read(self.ser.inWaiting())
        Re = []
        for r in tx:
            Re.append(ord(r))
        #print Re
        return self.changeReturn(Re)

    def changeReturn(self,R):
        print R

    def crc(self,data):
       crc=0
       for i in data:
         crc=crc^i
       return crc
    def __del__(self):
        self.ser.close()
if __name__ == '__main__':
    power = power()
    while True:
        power.transaction(power.Vcom)
        time.sleep(2)
