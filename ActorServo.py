import time
from board import SCL, SDA
import busio
from adafruit_motor import servo
from adafruit_pca9685 import PCA9685

i2c = busio.I2C(SCL, SDA)

pca = PCA9685(i2c, address=0x42)

pca.frequency = 50

witch = servo.Servo(pca.channels[0]) # start 60, 120, 2
doc = servo.Servo(pca.channels[1]) # 40, 130, 2
happy = servo.Servo(pca.channels[2]) # 75 brush up, 100 brush down, 2
dopey = servo.Servo(pca.channels[3])# 80, 105, 2
sleepy = servo.Servo(pca.channels[4])# 65, 90, 2 or 3
grumpy = servo.ContinuousServo(pca.channels[5], min_pulse=750, max_pulse=2250)
sneezy = servo.Servo(pca.channels[6])# 80 down, 100 up, 2
bashful = servo.Servo(pca.channels[7])# 70down, 90up, 2
snow = servo.Servo(pca.channels[8]) # 60, 120, 1
'''
  
        
class Actor(object):
    #initializer
    def __init__(self,channel,name,start,stop,delta):
        self.channel = channel
        self.name = name
        self.start = start
        self.stop = stop
        self.delta = delta
        
    def moveServo(start,stop,delta):
        name = servo.Servo(pca.channels[0])
        incMove = (stop-start)/100.0
        incTime = delta/100.0
        #using start angle(first value in moveServo) plus incremental moves(incMove) to rotate servo to stop angle in time(delta) increments(incTime) specified
        for x in range(100):
            name.angle = start + x*incMove         
            time.sleep(incTime)
        for x in range(100):
            name.angle = stop - x*incMove        
            time.sleep(incTime)
            #king (53,130,4)
            #queen linear (33,120,12)
def make_actor(channel,name,start,stop,delta):
    actor = Actor(channel,name,start,stop,delta)
    return actor

king = make_actor(0,'king',45,120,9)
playing = True
while playing:
    king.moveServo()

pca.deinit()
pca.reset()
