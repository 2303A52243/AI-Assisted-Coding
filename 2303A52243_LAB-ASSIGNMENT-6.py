'''class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def is_pass(self):
        return self.marks >= 40


# ---- Taking input from user ----
name = input("Enter student name: ")
roll_no = int(input("Enter roll number: "))
marks = float(input("Enter marks: "))

# Creating Student object
student1 = Student(name, roll_no, marks)

# Displaying student details
print("\n--- Student Details ---")
print("Name:", student1.name)
print("Roll No:", student1.roll_no)
print("Marks:", student1.marks)

# Checking pass/fail
if student1.is_pass():
    print("Result: Pass ✅")
else:
    print("Result: Fail ❌")
    

# Function using FOR loop
def triangle_for(n):
    print("\nTriangle using FOR loop:")
    for i in range(1, n + 1):
        print("*" * i)


# Function using WHILE loop
def triangle_while(n):
    print("\nTriangle using WHILE loop:")
    i = 1
    while i <= n:
        print("*" * i)
        i += 1


# ---- Main Program ----
rows = int(input("Enter number of rows: "))

triangle_for(rows)
triangle_while(rows)

def analyze_number(num):
    if num > 0:
        return "Positive number"
    elif num < 0:
        return "Negative number"
    else:
        return "Zero"


# ---- Main Program ----
numbers = []

count = int(input("How many numbers do you want to test? "))

for i in range(count):
    n = float(input(f"Enter number {i+1}: "))
    numbers.append(n)

print("\n--- Number Analysis Results ---")
for n in numbers:
    result = analyze_number(n)
    print(f"{n} → {result}")
    
    
    
    
def check_discount(age, is_member):
    if age >= 60:
        print("Eligible for Senior Citizen Discount.")
        
        if is_member:
            print("Also eligible for Additional Member Discount.")
        else:
            print("Not a member, so no additional discount.")
    
    else:
        print("Not eligible for Senior Citizen Discount.")
        
        if is_member:
            print("But eligible for Member Discount.")
        else:
            print("No discounts applicable.")


# ---- Main Program ----
age = int(input("Enter age: "))
member_input = input("Are you a member? (yes/no): ").lower()

is_member = True if member_input == "yes" else False

print("\n--- Discount Eligibility ---")
check_discount(age, is_member)'''

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def circumference(self):
        return 2 * math.pi * self.radius


# ---- Main Program ----
r = float(input("Enter the radius of the circle: "))

c1 = Circle(r)

print("\n--- Circle Calculations ---")
print("Radius:", c1.radius)
print("Area:", c1.area())
print("Circumference:", c1.circumference())


