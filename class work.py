#1.Function for (a + b)^2
def calculate_formula(a, b):
    return a**2 + b**2 + 2*a*b
a = int(input("Enter value for a: "))
b = int(input("Enter value for b: "))
print("Result:", calculate_formula(a, b))

#2.Using a Lambda Function for (a + b)^2
calculate_lambda = lambda a, b: a**2 + b**2 + 2*a*b
a = int(input("Enter value for a: "))
b = int(input("Enter value for b: "))
print("Result:", calculate_lambda(a, b))

#3. Recursive Factorial Function
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
n = int(input("Enter a number: "))
print(f"Factorial of {n} is {factorial(n)}")

#4.Function to Check if a Number is Prime
  
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
n = int(input("Enter a number: "))
print(f"{n} is prime" if is_prime(n) else f"{n} is not prime")

#5.List Tasks
############
a = [1, 3, 5, 7, 4]

# a. Access elements and find length and type
print(a[-2], a[2])
print(len(a), type(a))

# b. Modify elements
a[3] = 50
a[2:4] = [100, 200]
print(a)

# c. Add elements
a.append(100)
a.insert(2, 200)
print(a)

# d. Remove elements
a.pop() 
del a[1] 
print(a)

# e. Join with a new list
b = [2, 4, 6]
a.extend(b)
print(a)

# f. Copy to a new list
b = a.copy()
print(b)

# g. Sort the list
b.sort()
print(b)

# h. Print elements with a loop and break at 5
for i in a:
    if i == 5:
        break
    print(i)

# i. Find the largest number
print(max(a))


#6.Tuple Tasks
###########
a = (1, 3, 5, 7, 4)

# a. Find the sum of all odd numbers
odd_sum = sum(i for i in a if i % 2 != 0)
print("Sum of odd numbers:", odd_sum)

# b. Access elements by index
print(a[2], a[-2])  # Access elements

# c. Count odd and even numbers
odd_count = len([i for i in a if i % 2 != 0])
even_count = len([i for i in a if i % 2 == 0])
print("Odd numbers:", odd_count, "Even numbers:", even_count)

# d. Extend the tuple
a = a + (2, 4, 6)
print(a)

# e. Add a new item at index 2 (tuples are immutable, so convert to list first)
a_list = list(a)
a_list.insert(2, 400)
a = tuple(a_list)
print(a)

# f. Remove the last element
a = a[:-1]
print(a)

# g. Perform slicing
print(a[-4::-1])

# h. Print tuple using a loop and continue if 5 is found
for i in a:
    if i == 5:
        continue
    print(i)

#7.sets
#################
a = {13, 5, 8, 3, 75}
b = {10, False, 4, 5}

print (a, b)

Print length and type
type(a), len(a)
type(b), len(b)

Add and remove elements in set a
a.add(2)
a.remove(13)

Perform union, intersection, difference, and symmetric difference
union = a | b
intersection = a & b
difference = a - b
symmetric_difference = a ^ b

Check subset operation
is_subset = a <= b

Create a new list
data_list = [2, 13, 14]

#8.Working with dictionaries
##################
employee = {
    "name": "John",
    "age": 40,
    "type": "developer",
    "skills": ["python", "SQL"],
    "permanent": True,
    "salary": 30000
}

Print length and type of dictionary
len(employee), type(employee)

Accessing dictionary values
employee["type"], employee["skills"]

Change the value of "permanent" to False
employee["permanent"] = False

Add a new key-value pair
employee["gender"] = "male"

Remove a key
employee.pop("age")

Extract keys, values, and items
keys = employee.keys()
values = employee.values()
items = employee.items()

#9.Working with strings
###############
a = "hello"
b = "bob"
c = "1234"

Create a new variable d
d = a + b + c

Find the length of d
len(d)

Check if "hello" is present in d
"hello" in d

Perform string operations
upper = d.upper()
lower = d.lower()
strip = d.strip()
is_digit = d.isdigit()
find_pos = d.find("34")
capitalize = d.capitalize()
replace_text = d.replace("hello", "hi")  

#10.Polymorphism example
##################
class Teacher:
    def introduce(self):
        return "I am a Teacher"

class Student:
    def introduce(self):
        return "I am a Student"

# Demonstrate polymorphism
def introduction(person):
    return person.introduce()

teacher = Teacher()
student = Student()

introduction(teacher)
introduction(student)

#11.Exception handling example
###################
# Custom Exception
class InvalidVoter(Exception):
    pass

age = int(input("Enter your age: "))

if age < 18:
    raise InvalidVoter("You are not eligible to vote.")

# Another custom exception
class SalaryTooLow(Exception):
    pass

salary = float(input("Enter your salary: "))

if salary < 20000:
    raise SalaryTooLow("Salary is too low.")

# General exception handling
try:
    result = 10 / int(input("Enter divisor: "))
except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueError:
    print("Invalid input!")
finally:
    print("Execution complete.")

#12.Class and Object
#################
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display_detail(self):
        print(f"Product Name: {self.name}, Price: {self.price}")

  class ElectronicProduct(Product):
    def __init__(self, name, price, warranty):
        super().__init__(name, price)
        self.warranty = warranty

    def display_detail(self):
        super().display_detail()
        print(f"Warranty: {self.warranty} years")

# Example Usage
product = Product("Generic Product", 100)
product.display_detail()

electronic_product = ElectronicProduct("Laptop", 1500, 2)
electronic_product.display_detail()

class Shape:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def display_info(self):
        print(f"Shape Name: {self.name}")

class Rectangle(Shape):
    def __init__(self, name, length, width):
        super().__init__(name)
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def display_info(self):
        super().display_info()
        print(f"Length: {self.length}, Width: {self.width}")
        print(f"Area: {self.area()}, Perimeter: {self.perimeter()}")

# Example Usage
rect = Rectangle("Rectangle", 5, 3)
rect.display_info()

 #13.Encapsulation
 ######################
class Vehicle:
    def __init__(self, color):
        self.color = color

    def vehicle_info(self):
        print(f"Vehicle Color: {self.color}")

class Taxi(Vehicle):
    def __init__(self, color, model, capacity, variant):
        super().__init__(color)
        self.__model = model
        self.__capacity = capacity
        self.__variant = variant

    def get_model(self):
        return self.__model

    def set_model(self, model):
        self.__model = model

    def get_capacity(self):
        return self.__capacity

    def set_capacity(self, capacity):
        self.__capacity = capacity

    # Getter and Setter for variant
    def get_variant(self):
        return self.__variant

    def set_variant(self, variant):
        self.__variant = variant

    def vehicle_info(self):
        super().vehicle_info()
        print(f"Model: {self.__model}, Capacity: {self.__capacity}, Variant: {self.__variant}")

# Example Usage
t1 = Taxi("Yellow", "Model X", 4, "Electric")
t1.vehicle_info()

t2 = Taxi("White", "Model Y", 6, "Hybrid")
t2.set_capacity(7)
t2.vehicle_info()

#14.Inheritance
####################
class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def display(self):
        print(f"Name: {self.first_name} {self.last_name}")

class Student(Person):
    def __init__(self, first_name, last_name, graduation_year):
        super().__init__(first_name, last_name)
        self.graduation_year = graduation_year

    def display(self):
        super().display()
        print(f"Graduation Year: {self.graduation_year}")

class Alumni(Student):
    def __init__(self, first_name, last_name, graduation_year, passing_year):
        super().__init__(first_name, last_name, graduation_year)
        self.passing_year = passing_year

    def display(self):
        super().display()
        print(f"Passing Year: {self.passing_year}")

class CurrentStudent(Student):
    def __init__(self, first_name, last_name, graduation_year, current_semester):
        super().__init__(first_name, last_name, graduation_year)
        self.current_semester = current_semester

    def display(self):
        super().display()
        print(f"Current Semester: {self.current_semester}")

class Teacher(Person):
    def __init__(self, first_name, last_name, joining_year):
        super().__init__(first_name, last_name)
        self.joining_year = joining_year

    def display(self):
        super().display()
        print(f"Joining Year: {self.joining_year}")

class Admin(Person):
    def __init__(self, first_name, last_name, joining_year):
        super().__init__(first_name, last_name)
        self.joining_year = joining_year

    def display(self):
        super().display()
        print(f"Joining Year: {self.joining_year}")

class Employee(Person):
    def __init__(self, first_name, last_name, emp_id):
        super().__init__(first_name, last_name)
        self.emp_id = emp_id

    def display(self):
        super().display()
        print(f"Employee ID: {self.emp_id}")

# Example Usage
person = Person("John", "Doe")
person.display()

student = Student("Alice", "Smith", 2025)
student.display()

alumni = Alumni("Bob", "Brown", 2020, 2023)
alumni.display()

current_student = CurrentStudent("Charlie", "Davis", 2025, "5th")
current_student.display()

teacher = Teacher("Eve", "Wilson", 2015)
teacher.display()

admin = Admin("Grace", "Adams", 2018)
admin.display()

employee = Employee("Frank", "Taylor", 12345)
employee.display()
  
#15.Numpy
######################## 
import numpy as np
score = np.array([85, 90, 78, 92, 88])

# Task a) Convert the data type into float
score_float = score.astype(float)
print("Score as float:", score_float)

# Task b) Create a copy of "score" named "a_score" and add 5 points to it
a_score = score.copy()
a_score += 5
print("Original score:", score)
print("a_score with +5 points:", a_score)

# Task c) Find shape, ndim, size, itemsize, dtype, and sort
print("Shape of score:", score.shape)
print("Number of dimensions (ndim):", score.ndim)
print("Size of score:", score.size)
print("Item size (in bytes):", score.itemsize)
print("Data type (dtype):", score.dtype)

# Sorting the array
sorted_score = np.sort(score)
print("Sorted score:", sorted_score)

# Task d) Find the index of those who got more than 80
indexes_above_80 = np.where(score > 80)
print("Indexes with scores > 80:", indexes_above_80)

# Task e) Find min, max, std, var, sum, mean
print("Minimum score:", np.min(score))
print("Maximum score:", np.max(score))
print("Standard deviation:", np.std(score))
print("Variance:", np.var(score))
print("Sum of scores:", np.sum(score))
print("Mean of scores:", np.mean(score))

# Task f) Print specific slices
print("Elements with step 2:", score[::2])
print("Last three elements:", score[-3:])
print("Elements from index 1 to 4:", score[1:4])  

#16.Class and OOP tasks
#######################
#task 1
class Vehicle:
    def start(self):
        print("Vehicle has started")
    
    def stop(self):
        print("Vehicle has stopped")

class Car(Vehicle):
    pass

class Motorcycle(Vehicle):
    pass
car = Car()
car.start()
car.stop()

bike = Motorcycle()
bike.start()
bike.stop()

#task 2
from abc import ABC, abstractmethod
class Vehicle(ABC):
    def _init_(self, brand):
        self.brand = brand
    
    def start_engine(self):
        pass
    
    def description(self):
        return f"This is a vehicle of brand {self.brand}"
class Car(Vehicle):
    def _init_(self, brand, model):
        super()._init_(brand)
        self.model = model
    
    def start_engine(self):
        print(f"The engine of the car (model: {self.model}) has started.")

my_car = Car("Toyota", "Corolla")
my_car.start_engine()
print(my_car.description())

try:
    vehicle = Vehicle("GenericBrand")  # This will fail
except TypeError as e:
    print("Error:", e)
