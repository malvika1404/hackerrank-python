# You are going to write a program that tests the compatibility between two people.  
# To work out the love score between two people:
# Take both people's names and check for the number of times the letters in the word TRUE occurs. 
# Then check for the number of times the letters in the word LOVE occurs. 
# Then combine these numbers to make a 2 digit number. 
# For Love Scores **less than 10** or **greater than 90**, the message should be:
# `"Your score is **x**, you go together like coke and mentos."` 
# For Love Scores **between 40** and **50**, the message should be:
# `"Your score is **y**, you are alright together."`
# Otherwise, the message will just be their score. e.g.:
# `"Your score is **z**."`

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name_combine=name1.lower()+name2.lower()
count_t=name_combine.count("t")
count_r=name_combine.count("r")
count_u=name_combine.count("u")
count_e=name_combine.count("e")
total_true=count_t+count_r+count_u+count_e

count_l=name_combine.count("l")
count_o=name_combine.count("o")
count_v=name_combine.count("v")
count_e=name_combine.count("e")
total_love=count_l+count_o+count_v+count_e

total =str(total_love)+str(total_true)
total_for_calc = int(total)

if(total_for_calc<10 or total_for_calc>90):
    print(f" Your score is {total}, you go together like coke and mentos.")
elif( total_for_calc>40 and total_for_calc <50):
    print(f"Your score is {total}, you are alright together.")
else:
    print(f"Your score is {total}")