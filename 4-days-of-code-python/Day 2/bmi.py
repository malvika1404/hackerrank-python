# Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.
# The BMI is a measure of some's weight taking into account their height.

height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
bmi = int(height) /int (float(weight)*float(weight))
print(int(bmi))