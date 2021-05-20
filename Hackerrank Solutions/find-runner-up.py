# Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given n scores. 
# Store them in a list and find the score of the runner-up.

#Level - Easy

n = int(input("enter number of scores "))
arr = map(int, input("Enter the numbers spaced out in same line ").split())
print (sorted(set(arr))[-2])