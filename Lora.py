import serial
import time
import sys
import glob

class Lora:
    chip_cmd = [0x80,0x00,0x00,0]
    chip_res = [0xc2,0x01,0x00,0x00]
    def __init__(self):
        self.Device_init()

    def Device_init(self):
        self.ports = glob.glob('/dev/tty[A-Za-z]*')
        dev =""
        i = 0
        for port in self.ports:
            dev += str(i)+ "->" + port + ","
            i +=1
        intputport = int(raw_input('Choose your Device?' + dev))
        self.ser = serial.Serial(self.ports[intputport])
        print self.ports[intputport]
        self.ser.baudrate = 115200
        self.ser.timeout = 1
        #self.ser.open()
        print 'init Finished'

    def transaction(self,cmd):
        n = cmd[:]
        n[len(n)-1] = self.crc(n)
        print 'send:' , n
        self.ser.write(serial.to_bytes(n))
        time.sleep(0.04)
        i=0
        self.waitCount = 99
        bytesToRead = self.ser.inWaiting()
        while True:
           data = self.ser.read(bytesToRead)
           i=i+1
           if len(data)>0 or i>self.waitCount:
               break
        #tx = self.ser.read(self.ser.inWaiting())
        #tx = self.ser.read()
        #Re = []
	#print 'tx:',tx.encode('hex')
        #for r in tx:
        #    Re.append(ord(r))
        #print 're:'
        #return self.changeReturn(Re)
        print data.encode('hex')
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
    Lora = Lora()
    Lora.transaction(Lora.chip_cmd)
    Lora.transaction(Lora.chip_res)
