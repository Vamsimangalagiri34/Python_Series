# by default python not support abstraction

# Abstraction is one of the fundamental concepts in object-oriented programming (OOP). In Python, abstraction helps to simplify complex systems by hiding the unnecessary details and exposing only the essential features. This allows programmers to work with higher-level functionalities without needing to understand all the underlying complexities.

# ### Key Points About Abstraction:
# 1. **Simplification**: It hides the complex implementation details and shows only the functionality.
# 2. **Interface**: In Python, abstraction can be achieved using abstract base classes (ABCs) and interfaces.
# 3. **Encapsulation**: It often works in conjunction with encapsulation, which restricts access to certain components.

# ### How to Achieve Abstraction in Python 
# Python offers abstract classes through the `abc` module. Here's a step-by-step explanation of how to create and use abstraction in Python:

# #### Step 1: Import the abc Module
# To create an abstract class, import the `ABC` class and the `abstractmethod` decorator from the `abc` module.

# ```python
from abc import ABC, abstractmethod #abc abstract base class
# ```

# #### Step 2: Create an Abstract Class
# Define a class that inherits from `ABC`. This class can contain one or more abstract methods, which are methods decorated with `@abstractmethod`. These methods do not have a body and must be implemented by any subclass.

# ```python
class Animal(ABC):

    @abstractmethod
    def speak(self):
        pass
# ```

#### Step 3: Create Subclasses
# Any class that inherits from the abstract class must implement the abstract methods. Here’s how you can do it:

# ```python
class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

#### Step 4: Use the Subclasses
# Now you can create instances of the subclasses and call the implemented methods.

# ```python
dog = Dog()
cat = Cat()

print(dog.speak())  # Output: Woof!
print(cat.speak())  # Output: Meow!
# ```

# # ### Summary
# - **Abstraction** allows you to focus on what an object does instead of how it does it.
# - **Abstract Classes**: Defined using the `ABC` class and `@abstractmethod` decorator.
# - **Implementation**: Subclasses must implement all abstract methods to be instantiated.

# By using abstraction, you can design your application in a way that promotes code reuse and separation of concerns, allowing for cleaner and more maintainable code. If you have any specific scenarios or further questions about abstraction in Python, feel free to ask!