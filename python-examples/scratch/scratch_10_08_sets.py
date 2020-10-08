# Sets 
students = {"Will", "Tom", "Nathan", "Kim", "Charlette", "Phil", "Jon", "Babacar"}
 
students.add("Clinton")

students.add("Hobbes")

students.remove("Clinton")

# Generators
def numbergen(start, stop):
    for n in range(start, stop):
        yield n

# demonstrating usage of generator
# for i in numbergen(0, 20):
#    print(i)

# Comprehensions
# How would I create a list of numbers between 0 and 9
# Option 1: using functions
with_functions = list(range(10))

# print("Using a function:")
# print(with_functions)

# Option 2: using a for loop. This is the most general
with_loop = []

for i in range(10):
    with_loop.append(i)

# print("Using a loop:")
# print(with_loop)


# Option 3: Using a comprehension
with_comprehensions = [i for i in range(10)]
# print("Using comprehehnsions:")
# print(with_comprehensions)

# You can use an arbitrary expression in the first part of a list comprehension
squares_with_comprehensions = [i**2 for i in range(10)]
# print(squares_with_comprehensions)

squares_with_functions = list(map(lambda x: x**2, range(10)))

squares_with_loops = []

for i in range(10):
    square = i**2
    squares_with_loops.append(square)

# You can filter results by including an if statement after the for statement
even_squares = [i**2 for i in range(20) if i**2 % 2 == 0]
# print(even_squares)

# You can create generator comprehensions as well by surrounding comprehension expression with parentheses
even_squares_gen_comp = (i**2 for i in range(20) if i**2 % 2  == 0)

for s in even_squares_gen_comp:
    print(s)

# You can also create generator comprehensions by using a comprehension expression wherever a sequence is desired
students_names = ["Will", "Derek", "Phil", "Babacar", "Charlette", "Jon", "Nathan", "Kim", "Tom"]
students_names_lengths = set(len(s) for s in students_names)
print(students_names_lengths)