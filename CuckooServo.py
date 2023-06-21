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
    time.sleep(5)
    for x in range(100):
        name.angle = stop - x*incMove        
        time.sleep(incTime)
    time.sleep(5)
def moveServo_2(start: int,stop:int,delta:int):        
    incMove = (stop-start)/100.0
    incTime = delta/100.0
    #using start angle(first value in moveServo) plus incremental moves(incMove) to rotate servo to stop angle in time(delta) increments(incTime) specified
    for x in range(100):
        king.angle = (start+15) + x*incMove
        queen.angle = start + x*incMove
        time.sleep(incTime) 
    time.sleep(5)
    for x in range(100):
        king.angle = stop - x*incMove-.15
        queen.angle = stop - x*incMove                
        time.sleep(incTime)
    time.sleep(5)
def moveServoInf(name,start:int,stop:int,delta:int):        
    incMove = (stop-start)/100.0
    incTime = delta/100.0
    #using start angle(first value in moveServo) plus incremental moves(incMove) to rotate servo to stop angle in time(delta) increments(incTime) specified
    while True:
        for x in range(100):
            name.angle = start + x*incMove         
            time.sleep(incTime)
        for x in range(100):
            name.angle = stop - x*incMove        
            time.sleep(incTime)

def startTheShow():
    while True:
        
        moveServo(cuckoo,35,110,5)
        time.sleep(3)
        moveServo(king,45,115,5)
        time.sleep(3)
        moveServo(queen,30,115,5)
        time.sleep(6)# pause after first program
        moveServo(cuckoo,35,110,5)
        time.sleep(3)        
        moveServo_2(30,115,5)
        time.sleep(6) # pause after second program
#cuckoo, king, queen, cuckoo, king and queen, repeat
if __name__ == "__main__":
        
    p1 = Process(target=moveServoInf, args=(clock,30,150,2))
    p1.start()
    p2 = Process(target=startTheShow)
    p2.start()    
    
    p1.join()
    p2.join()
    
    pca.deinit()
    pca.reset()
