# Functional Programming Prompt
# Implement a function that will flatten and sort an array of integers in ascending order, and which adheres to a functional programming paradigm.

def sortList(list):
    # Copy list so it does not modify the original
    sortedList = list.copy()
    # Use the sort method to sort the copied list
    sortedList.sort()
    # Return the sorted list
    return sortedList


list = [1, 4, 2, 6, 82, 4]
print(sortList(list))

# How does this solution ensure data immutability?
# This solution ensures data immutability because the array is copied to avoid it from being overriden.
# Is this solution a pure function? Why or why not ?
# Yes, this is a pure function because it returns the desired result independtly from other functions
# Is this solution a higher order function? Why or why not ?
# No it is not, because it does not take in one or more functions as a argument. It only takes in a list.
# Would it have been easier to solve this problem using a different programming style?
# I think it was pretty straight forward. I am wondering if I should "flatten" the list as this solution does not because the input lists are 1D by default.
# Why in particular is functional programming a helpful paradigm when solving this problem?
# This is a helpful paradigm becaue its result is not dependent on external functions. There for a result can be achieved with one simple funcitonal funciton
# -------------------------------------------------------------------------------
# Object Oriented Prompt
# Watto needs a new system for organizing his inventory of podracers. Help him do this by implementing an Object Oriented solution according to the following criteria.

class Podracer:
# First, he'll need a general Podracer class defined with max_speed, condition(perfect, trashed, repaired) and price attributes.
    def __init__(self, max_speed, condition, price):
        self.max_speed = max_speed
        self.condition = condition
        self.price = price
# Define a repair() method that will update the condition of the podracer to "repaired".
    def repair(self):
        self.condition = "repaired"

# Define a new class , AnakinsPod that inherits the Podracer class, but also contains a special method called boost that will multiply max_speed by 2.
class AnakinsPod(Podracer):
    def __init__(self, max_speed, condition, price):
        super().__init__(max_speed, condition, price)
        self.max_speed = max_speed
        self.condition = condition
        self.price = price
    def boost(self):
        return self.max_speed * 2

# Define another class that inherits Podracer and call this one SebulbasPod. This class should have a special method called flame_jet that will update the condition of another podracer to "trashed".


class SebulbasPod(Podracer):
    def __init__(self, max_speed, condition, price):
        super().__init__(max_speed, condition, price)
    def flame_jet(self):
        self.condition = "trashed"


# How does this solution demonstrate the four pillars of OOP? (It may not demonstrate all of them, describe only those that apply)
# Encapsulation: Each class that is created utilizes encapsulation. Due to each class having its own independtent function underneath the "hood"
# Abstraction: The classes also abstract which information is public to the application. It hides the detailed functionality within
# Inheritance: Some of the classes inherit properties and functionality from other classes. Classes have a relationship together illustrate inheritance.
# Polymorphism: These classes can take multiple forms based on the information submitted by the application to initialize the classes
# Would it have been easier to implement a solution to this problem using a different coding style? Why or why not ? No, it would not have been. The process becomes much easier using OOP because it allows us to inherit properties from other classes, have multiple instances of classes, among allowing us to group specific functionality with classes based on the objects purpose.
# How in particular did Object Oriented Programming assist in the solving of this problem? It helped because it allowed us to create different classes for the different objects we needed to create with the required funcitonality within each.

# Is one of these coding paradigms "better" than the other? Why or why not ? 
#Answer: No not neccasarily, depending on the use case it may be beneficial to use either for a faster and more efficient deployment. It depends on the objective that your program should complete.
# Given the opportunity to work predominantly using either of these coding paradigms, which seems more appealing? Why? 
# Answer: It would make most sense to utilize the OOP paradigms because most applications that we create involve objects in the real world. Breaking apart you application into objects that perform seperate functionality along with using inheritance when applicable allows for a seamless development process. It makes it clearer to use and enables to update code in less places.
# Now being more familiar with these coding paradigms, what tasks/features/pieces of logic would be best handled using functional programming? Object Oriented Programming? 
# Answer: If the task at hand does not involve inheritance, external functions result, and is a straight forward task functional programming may be a desirable paradigm. But if youre working with a more complex applicaiton it would make most sense to implement OOP for a cleaner, more concise code.
# Personally, which of these styles takes more work to understand? What should be done in order to deepen understanding related to this paradigm?
# Answer: It seems that functional programming would require more work to understand when it comes to reviewing code. Without the super() and init aspects it would likely take more time to identify what code the function is inheriting. This would likely cause confusion and may be the root of spaghetti code?
