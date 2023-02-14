# Starting Code
class Car:
  def __init__(self, name, max_speed):
    self.name = name
    self.max_speed = max_speed

  def start(self):
    print('Vroom!')

  def talk(self, driver):
    print(f'Hello, {driver}, I am {self.name}.')


# Creating the Race Class

class Race:
  def __init__(self,name,driver_limit,drivers=[]):
    self.name = name
    self.driver_limit = driver_limit
    self.drivers = drivers

  def add_driver(self, driver):
    if len(self.drivers) < self.driver_limit:
      self.drivers.append(driver)
      return True
    else:
      return False
    
  def get_average_ranking(self):
    total = 0
    for driver in self.drivers:
      total += driver.get_ranking()

    return total / len(self.drivers)



# Creating the Driver Class
class Driver:
# Static Attribute - This attribute will increment each time a driver class is initiated
  number_of_drivers = 0

  def __init__(self, name, age, ranking):
    self.name = name
    self.age = age
    self.ranking = ranking
    # To add a counter to the number of drivers simply add to that number of drivers variable
    Driver.number_of_drivers += 1

  def get_ranking(self):
    return self.ranking


myCar = Car('Kitt', 180)
myOtherCar = Car('Speedy', 55)

# myCar.talk('Michael')

my_course = Race('Seattle 500', 4)
print(my_course.name, my_course.driver_limit, my_course.drivers)

# prints Seattle 500 4 []

my_driver = Driver('Dale Earnhardt', 29, 100)
print(my_driver.get_ranking())

# prints a returned value of "100"

s0 = Driver('Skip', 50,40)
s1 = Driver('Clip', 50,40)
s2 = Driver('Carl', 50,40)
s3 = Driver('John', 50,40)
s4 = Driver('Alex', 50,40)
s5 = Driver('Fred', 50,40)
s6 = Driver('Greg', 50,40)
s7 = Driver('Tony', 50,40)

my_course.add_driver(s0)
my_course.add_driver(s1)
my_course.add_driver(s2)
my_course.add_driver(s3)
my_course.add_driver(s4)
my_course.add_driver(s5)
my_course.add_driver(s6)
my_course.add_driver(s7)

print(my_course.get_average_ranking())