def classname(self, fmt=str.capitalize):
    """
    Helper function for getting the class name of an object.
    """
    return fmt(self.__class__.__name__)

# Object Oriented Programming Vocabulary

# OOP          - Object Oriented Programming
# class        - A template for an object describing what methods it 
#                implements and what attributes it posesses.
# instance     - a member of a class (if Cat is a class, my cat Hobbes is an instance of a Cat).
# methods      - functions defined within a class called as though they were attributes of the 
#                class or instance
# inheritance  - when one class is used as the basis for another class (see below)
# parent/child - the relationship between classes when one inherits from another
# extension    - when methods or attributes are added to a child class
# overriding   - when methods from a parent class are rewritten for a child class

# 1: The most basic type of class: an __init__ method where we initialize instance attributes
# and a __str__ method, allowing us to get a human-readable str representation of the object

class Creature:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"<{classname(self)} name={self.name} age={self.age}>"


# 2: The following class extends the Creature class using inheritance. When one class
# inherits from another, it receives all of the methods and attributes of the class it inherits
# from (the parent class). Inside the body of the class we can then add new methods (extending the parent
# class) or provide new definitions for existing methods (overriding the existing methods). Python
# also provides a `super` builtin function, which allows us to call methods that have been overriden.

class Pet(Creature):
    """
    Represents the pet (or child) of a Momentum Student.
    """
    def __init__(self, name, age, species):
        super().__init__(name, age)
        self.species = species


# 3: Python has a large set of special method names called magic methods or dunder methods ('dunder' is short for
# 'double underscore'). magic methods are looked up by Python when certain keywords or builtin operators are called
# on an object. __init__ and __str__ are magic methods that are looked up when a new object's attributes are being
# assigned for the first time and when an object is converted to a str (respectively). The Student class also defines
# the __eq__ magic method, which allows instances of student to be compared using `==` or `!=`. The Student class also
# defines an arbitrary 

class Student(Creature):
    """
    Represents a Momentum Student.

    instance attributes:
        - name
        - age
        - team
        - pet

    methods:
        __init__
        __str__
        __eq__
        teammates - return True if the two Students are on the same team. Raise a TypeError if
        non-instance argument is not an instance fo Student.
    """
    def __init__(self, name, age, team, pet):
        super().__init__(name, age)
        self.team = team
        self.pet = pet

    def __eq__(self, other):
        if isinstance(other, Student):
            return self.name == other.name and self.team == other.team and self.pet == other.pet and self.age == other.age

        return False

    def isteammate(self, other):
        if isinstance(other, Student):
            return self.team == other.team

        raise TypeError(f"{other} is a {type(other)}, not a Student.")
