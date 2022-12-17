# Write a program that adds the digits in a 2 digit number. 
# e.g. if the input was 35, then the output should be 3 + 5 = 8


two_digit_number = input("Type a two digit number: ")
num = type(two_digit_number)
one = two_digit_number[0]
two = two_digit_number[1]
print(int(one)+int(two))