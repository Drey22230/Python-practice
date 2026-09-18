"""
Problem 3
Create a simple student profile program.

Input:
Name
Age
Course
Year
GWA

Display the complete profile.
"""

name = input("Enter your name: ")
age = int(input("Enter your age: "))
course = input("Enter your course: ")
year = int(input("Enter your year: "))
gwa = float(input("Enter your GWA: "))
print("\nStudent Profile:")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Course: {course}")
print(f"Year: {year}")
print(f"GWA: {gwa}")