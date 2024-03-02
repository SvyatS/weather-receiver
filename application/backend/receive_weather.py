import serial
import sys
from logs import realtime_log




if len(sys.argv) < 3:
    print("Ошибка: необходимо указать аргументы port и baudrate")
    sys.exit(1)

port = sys.argv[1] #"/dev/pts/4" 
baudrate = sys.argv[2]  

ser = serial.Serial(port)

while True:
    while ser.inWaiting() == 0:
        pass

    line = ser.readline()
    decode_line = line.decode()
    if decode_line[-1] == '\n':
        temp = int(decode_line[0:len(decode_line)-1])
        realtime_log(temp)


