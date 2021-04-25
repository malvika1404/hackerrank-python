#The provided code stub reads an integer, n , from STDIN. For all non-negative integers i<n, print i^2.
#Constraints: 1<=n<=20

#Level - Easy

n= int(input("Enter value of n: "))
for i in range(n):
    print(i ** 2)
