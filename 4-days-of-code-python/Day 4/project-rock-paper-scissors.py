# Rock, Paper and Scissors

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
print("User starts!")
user_choice =  int(input("Input 0 for Rock, 1 for Paper, 2 for Scissors "))
if(user_choice<=2):
  computer_choice = random.randint(0,2)
  print(f"Computer chooses {computer_choice}")
  if(user_choice == 0 and computer_choice == 2 ):
    print("User Wins!")
  elif(computer_choice == 0 and user_choice == 2 ):
    print("Computer Wins!")
  elif(user_choice > computer_choice):
    print("User Wins!")
  elif(user_choice < computer_choice):
    print("Computer Wins!")
  else:
    print("Draw")
else:
  print("Invalid Input")

