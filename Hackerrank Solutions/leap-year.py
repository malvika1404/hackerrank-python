#Given a year, determine whether it is a leap year. If it is a leap year, return the Boolean True, otherwise return False.
#The code stub provided reads from STDIN and passes arguments to the is_leap function.
#Constraints: 1900<=year<=10^5

#Level - Medium

def is_leap(year):
    leap = False
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    else:
        print("Enter a year greater than or equal to 1990 ")
        return False
    
    return leap

year = int(input("Enter a year "))
print(is_leap(year))