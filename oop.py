# Class example - Creating one

class Car:
  # Setting variables
  gravity = -9.8
  wheels = 4

  # Constructor
  def __init__(self, name, age, id):
    print(f"{name}'s Car has been initialized")
    self.name = name
    self.age = age
    self.id = id

  def start(self):
    return("vroom!")

  def talk(self, driver):
    return(f"Hello, {driver}")

# Class Inheritance, pass in the class you would like to inherit from in the class declaration
class Robot_Car(Car):
  def __init__(self, name, age, id, type):
    super().__init__(name, age, id)
    self.type = type



# Holds the instance of the class
# Each instance of a class holds seperate values
my_car = Car("John",21,1253)
his_car = Car("Karen",24,1234)

new_car = Robot_Car("robo-cop",23,1235,"cool")

print(my_car.start())
print(my_car.talk("tom"))