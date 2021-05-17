import turtle           # To simulate our project to check all algorithm.
import random           # To provide different value instead of some sensors.
import time             # To control our simulation.

class motor:

    def __init__(self,speed = 0):
        self.speed = speed

    def getspeed(self):
        return self.speed

    def setspeed(self,motorspeed):
        self.speed = motorspeed

    def run(self,motorspeed):
        self.setspeed(motorspeed)
        return self.speed

    def stop(self):
        self.speed = 0

def lineControl(distance_Rightside,distance_Leftside):  # This function controls the speed of the autonomous car.

    if distance_Rightside == distance_Leftside :
        print("Keep going",end="             ")

    elif distance_Leftside > distance_Rightside :
        print("Steer left",end="             ")

    elif distance_Leftside < distance_Rightside :
        print("Steer right",end="             ")

def move():                                             # This function controls the speed of the autonomous car.

    for distance in range(250,0,-5) :                   # For Simulate.We expect to use Ultrasonic Sensor for this.

        print("Distance : {} cm".format(distance),end="               ")

        motorspeed = 255

        if distance > 100 :
            motor1.run(motorspeed)
            motor2.run(-motorspeed)
            car.speed(5)
            car.forward(3)
        elif 80 < distance <= 100 :
            motor1.run(motorspeed - 100)
            motor2.run(-motorspeed + 100)
            car.speed(5)
            car.forward(3)
        elif 60 < distance <= 80 :
            motor1.run(motorspeed - 140)
            motor2.run(-motorspeed + 140)
            car.speed(4)
            car.forward(3)
        elif 40 < distance <= 60 :
            motor1.run(motorspeed - 180)
            motor2.run(-motorspeed + 180)
            car.speed(2)
            car.forward(3)
        elif 10 < distance <= 40 :
            motor1.run(motorspeed - 220)
            motor2.run(-motorspeed + 220)
            car.speed(1)
            car.forward(3)
        else :
            motor1.stop()
            motor2.stop()

        distance_Rightside = random.randint(5, 10)      # For Simulate.We expect to use OpenCV for this.
        distance_Leftside = random.randint(5, 10)       # For Simulate.We expect to use OpenCV for this.

        lineControl(distance_Rightside, distance_Leftside)

        print("Motor1 Speed = {}                 Motor2 Speed = {} ".format(motor1.getspeed(),motor2.getspeed()))

def sign_control(sign):                                 # The function to define our aim for different signals.


    if sign == "Green" :
        car.color("green")
        for i in range(18):
            car.forward(5)                              # Green means "Turn Right
            car.right(5)
            print("         Turning Right")
        car.color("grey")
        move()

    elif sign == "Blue" :
        car.color("blue")
        for i in range(18):
            car.forward(5)                              # Blue means "Turn Left"
            car.left(5)
            print("         Turning Left")
        car.color("grey")
        move()

    elif sign == "Red" :
                                        # Red means "Stop 10 Seconds"
        for t in range(10,-1,-1):
            car.color("red")
            print("             ",t)
            time.sleep(0.5)
            car.color("grey")
            time.sleep(0.5)
sign_list = ["Red","Green","Blue","Green","Green","Red"]  #For Simulate. We expect to use OpenCV for this.
motor1 = motor()
motor2 = motor()

car = turtle.Turtle()
car.shape("square")
car.pensize(3)
car.penup()
car.goto(290,-250)                                    # To simulate our project to check all algorithm.
car.pendown()
car.left(180)
car.speed(1)
car.color("grey")

tt = 0
for signal in sign_list :
    tt += 1
    sign_control(signal)
    if tt == 1 :
        move()

turtle.done()