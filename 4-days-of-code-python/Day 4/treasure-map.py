# Your job is to write a program that allows you to mark a square on the map using a two-digit system.
# The first digit is the vertical column number and the second digit is the horizontal row number
# First your program must take the user input and convert it to a usable format. 
# Next, you need to use it to update your nested list with an "X". 

row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
hor = int(position[0])
ver = int(position[1])
selected_row = map[ver -1]
selected_row[hor-1]="X"