""" Problem 4
Create a salary calculator.

Input:
Basic salary
Hours worked
Overtime hours
Overtime rate

Calculate the total salary.
"""

print("Salary Calculator")
basic_salary = float(input("Enter the basic salary: "))
hours_worked = float(input("Enter the hours worked: "))
overtime_hours = float(input("Enter the overtime hours: "))
overtime_rate = float(input("Enter the overtime rate: "))

total_salary = basic_salary + (overtime_hours * overtime_rate)
print(f"The total salary is: ${total_salary:.2f}")
