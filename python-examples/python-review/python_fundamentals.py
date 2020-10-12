# 1: statements and expressions

# python expressions are pieces of python code that produce a value
# i.e., their value will eventually be substituted into the code where
# they're used. Arithmetic expressions, function calls, and method calls
# are examples of python expressions. Other common expressions are list
# literals, dictionary literals, string literals, etc.
1 + 2

"a string"

max(2, 3)

print("Hello!")

# statements are python code that contain a python keyword or an assignment operator.
# statements might produce a value just like an expression does,
# but can have other effects as well, like creating a variable. Statements
# are also used to introduce blocks (see below).

xs = [1, 2, 3]  # an assignment statement
xs += [4, 5]    # an augmented assignment operator
2 and 3         # a statement using the `and` keyword
letters = ''.join([chr(97 + i) for i in range(26)])

# 2: blocks

# blocks represent code whose execution is controlled by some python statement.
# the simplest example of a block is the block under an `if` statement, (it only
# runs when the `if` statement produces a value of `True`) but `for` and `while` loops
# also use blocks. A block is treated as all of the code after a colon that is indented
# one level more than the statement that introduced the block.

if len(xs) >= 3:
    print("xs is a long list.")

for letter in letters:
    letters +=  letter

with open("students.txt") as students:
    lines = students.read()
    print(lines)



# 3: types

# every value in python has a type. A value's type determines what operations it works with.
# integers work with addition, but not inside a `for` loop.

2 + 3  # fine!
# for i in 5: # an error!

# most common built-in types are int, float, str, list, tuple, and dict (examples of each below)
1

2.5

"2.5"

[2, 5]

(2, 5)

{ 2: 5, "will": "teacher" }
# 4: collections

# collections are groups of python objects. Collections can be thought of as 'things it makes
# sense to use within a for loop.'

setx = {1, 2, 3, 4}

# 5: function definitions

# function definitions are introduced with the `def` keyword and indicate
# the start of a function. A function takes variables, substitutes them in its
# bodies and produces a result (indicated by `return`).
def my_function():
    print ("Here is a function")
    return True


def add(a, b):
    return a + b

# 6: modules

# modules are units of python code outside the current Python file that can be used within the current Python file.
# modules can be included in the current file using the `import` keyword, or specific code can be imported using the 
# `from` <module> `import` <thing> special syntax.

# some python standard library modules
import math
import random
import json
import os
import sys
import pathlib

from collections import Counter, deque
from statistics import mean

import functools as ft
import itertools as it
import operator as op


# 7: methods and attributes

# attributes are data that can be accessed by name using the `.` operator. Methods are functions defined inside the body
# of a `class` (we'll see more of this tomorrow). Methods are also called using the `.` operator (in a way, classes are objects,
# and methods are attributes of those objects). It's a good rule of thumb to allow object modification (adding or removing members)
# to take place only within methods (rather than within arbitrary functions).

print(wordlist)

f"{wordlist}".lower()
"HELLO HOW ARE YOU".lower()

xs.append(6)

xs.remove(3)

# 8: Comprehensions

# Comprehensions are a syntax for building collections using a variant of the for statement.

[x for x in range(10)]                        # a simple comprehension
[chr(x*2) for x in range(100)]                # a more complex expression
[chr(x*2) for x in range(100) if x % 4 == 0]  # with a filter

# Comprehensions can be used to build lists, dicts, sets and generators

{random.randint(0,1000) for _ in range(25)}
{i: True for i in range(25)}
(chr(random.randint(0, 20000)) for _ in range(25))