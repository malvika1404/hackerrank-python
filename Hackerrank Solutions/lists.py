#Consider a list (list = []). Perform the following commands
#print the list
#remove element from list
#append element to end of the list
#sort the list
#pop last element from list
#reverse the list

#Level - Easy

N = int(input(" Input number of commands you want to run "))
list = []
for i in range(0,N):
    ip=input(" enter command ").split()
    if ip[0] == "insert":
        list.insert(int(ip[1]),int(ip[2]))
    elif ip[0] == "print":
        print(list)
    elif ip[0] == "append":
        list.append(int(ip[1]))
    elif ip[0] == "remove":
        list.remove(int(ip[1]))
    elif ip[0] == "pop":
        list.pop()
    elif ip[0] == "sort":
        list.sort()
    else:
        list.reverse()