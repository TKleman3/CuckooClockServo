import time
from multiprocessing import Process
from board import SCL, SDA
import busio
from adafruit_motor import servo
from adafruit_pca9685 import PCA9685

i2c = busio.I2C(SCL, SDA)

pca = PCA9685(i2c, address=0x42)

pca.frequency = 50

king = servo.Servo(pca.channels[0]) #45,120,9
queen = servo.Servo(pca.channels[1])#32,120,12
cuckoo = servo.Servo(pca.channels[2]) #35,115,12
clock = servo.Servo(pca.channels[3]) #30,150,2


def moveServo(name,start: int,stop:int,delta:int):        
        incMove = (stop-start)/100.0
        incTime = delta/100.0
        #using start angle(first value in moveServo) plus incremental moves(incMove) to rotate servo to stop angle in time(delta) increments(incTime) specified
        for x in range(100):
            name.angle = start + x*incMove         
            time.sleep(incTime)
        for x in range(100):
            name.angle = stop - x*incMove        
            time.sleep(incTime)

def moveServo_2(start: int,stop:int,delta:int):        
        incMove = (stop-start)/100.0
        incTime = delta/100.0
        #using start angle(first value in moveServo) plus incremental moves(incMove) to rotate servo to stop angle in time(delta) increments(incTime) specified
        for x in range(100):
            if king.angle <=120:
                king.angle = (start+13) + 1.75*x*incMove
                queen.angle = start + x*incMove                
            else:
                queen.angle = start + x*incMove
            time.sleep(incTime) 
        for x in range(100):
            if king.angle > 45:
                king.angle = stop - 1.75*x*incMove
                queen.angle = stop - x*incMove                
            else:
                queen.angle = stop - x*incMove
            time.sleep(incTime)
#cuckoo, king, queen, cuckoo, king and queen, repeat


if __name__ == "__main__":
    p = Process(target =moveServo, args=(clock,30,150,2,) )
    p.start()
    playing = True
    while playing:
        moveServo(cuckoo,35,115,12)
        time.sleep(5)
        moveServo(king,45,120,9)
        time.sleep(5)
        moveServo(queen,32,120,12)
        time.sleep(5)
        moveServo(cuckoo,35,115,12)
        time.sleep(5)
        moveServo_2(32,120,12)

    pca.deinit()
    pca.reset()
