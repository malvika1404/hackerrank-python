#Given an integer,n, and n space-separated integers as input, create a tuple,t, of those integers. 
#Then compute and print the result of hash(t).

#Level - Easy

N = int(input(" Enter tuple size"))
list = map(int, input(" Enter tuple data").split())
print(hash(tuple(list)))