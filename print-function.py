#The included code stub will read an integer,n , from STDIN.
#Without using any string methods, try to print the following: 123...n
#Note that "..." represents the consecutive values in between. Example: n=5, print 12345
#Contraints: 1<=n<=150

#Level - Easy

n = int(input("Enter the value for n: "))
for i in range(1, n+1):
    print(i, end = "")