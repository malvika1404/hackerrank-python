# write a program which will select a random name from a list of names. 
# The person selected will have to pay for everybody's food bill. 

# Split string method
import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
len_of_list = len(names)
bill = random.randint(0, len_of_list -1)
print(f"{names[bill]}, will pay the bill today!")