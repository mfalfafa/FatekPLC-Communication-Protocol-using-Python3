import serial
import serial.tools.list_ports
import time

from LRC_checksum_calculator import *

connected = False
serPort=0

## Establish connection to COM Port
## Connection from HMI
comlist = serial.tools.list_ports.comports()
## loop until the device tells us it is ready
while not connected:
    ## COM Port settings
    for device in comlist: 
        try:
            # print ("Trying...",device)
            ## Serial Initialization
            serPort = serial.Serial(device[0],      #port
                                38400,              #baudrate
                                serial.SEVENBITS,   #bytesize
                                serial.PARITY_EVEN,  #parity
                                serial.STOPBITS_ONE, #,#stop bit
                                0,                  #timeout
                                False,              #xonxoff
                                False,              #rtscts
                                0,                  #write_timeout
                                False,              #dsrdtr
                                None,               #inter byte timeout
                                None                #exclusive
                                )
            connected=True
        except:
            connected=False
            print ("trying to connect to ", device[0])
            time.sleep(1.5)
if connected:
    serin = serPort.read()
    print ("Connected to ",device[0])
    connected=False

recData=''
cmd=['0102','014406X0050','014401Y0000']
# get checksum
for i in range(len(cmd)):
    lrc=LRC_calc(cmd[i])
    cmd[i]='\x02'+ cmd[i] + (str(lrc)).upper() + '\x03'
print (cmd)
#cmd=['\x020102C5\x03', '\x02014406X00504E\x03']

while 1:
    serPort.write(cmd[2].encode('utf-8'))
    #print(cmd[1])
    if serPort.inWaiting():
        recData=serPort.readline()
        recData=recData.decode('ascii')
        try:
            start = recData.index( '\x02' ) + len( '\x02' )
            end = recData.index( '\x03', start )
            recData = recData[start:end]
            print (recData)
        except Exception as e:
            pass
            serPort.flushInput()
            serPort.flushOutput()
    time.sleep(0.5)
