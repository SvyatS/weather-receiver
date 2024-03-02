from random import randint
import time
import serial
import sys




def generate_temp(avg_temp: int) -> int:
    return randint(avg_temp - 1, avg_temp + 1)


if len(sys.argv) &lt; 3:
    print("Ошибка: необходимо указать аргументы port и baudrate")
    sys.exit(1)


port = sys.argv[1] #"/dev/pts/3" 
baudrate = sys.argv[2]  

ser = serial.Serial(port)

avg_temp = 0

while(1):
    avg_temp = generate_temp(avg_temp)
    message = f'{avg_temp}\n'.encode() 
    print(f'generate: {message}')
    ser.write(message)
    time.sleep(30)


ser.close()