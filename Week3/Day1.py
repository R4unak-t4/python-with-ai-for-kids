# OOP (Object oriented Programming)

# class

class car:
    # attributes (Class attributes)
    color = None
    headlight = None
    speed = None
    wheel = 4
    spoiler = None

    # constructor
    def __init__(self,color,headlight,speed,spoiler):
        self.color = color
        self.headlight = headlight
        self.speed = speed
        self.spoiler = spoiler

    # methods
    def accelerate(self):
        print("Car is now accelerating")

    def brake(self):
        print("Car is stopped")

    # getter
    def getColor(self):
        return self.color

    # setter
    def setColor(self,color):
        self.color = color


# making object of a class
myCar = car("red","square","60 KM/H",True)

# accessing attributes of a class
# print(myCar.headlight)

# changing the value of an attribute
# myCar.color = 'red'
# print(myCar.color)

# running object's methods
# myCar.accelerate()
# myCar.brake()

# use getter setter
myCar.setColor('green')
print(myCar.getColor())


'''
Modify the car class to include a method called increase_speed() that increases the car’s speed by a given value (passed as a parameter). Assume the speed is stored as an integer in km/h instead of a string. Then, create an object of the class, increase its speed by 20 km/h, and print the updated speed using a getter method.
'''