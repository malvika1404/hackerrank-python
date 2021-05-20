#You have a record of N students. 
# The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students. Print the average of the marks array for the student name provided, showing 2 places after the decimal.
# The user enters some integer N followed by the names and marks for N students.
# You are required to save the record in a dictionary data type. 
# The user then enters a student's name. 
# Output the average percentage marks obtained by that student, correct to two decimal places.

N = int(input(" Number of Students "))
marks = {}
for _ in range(N):
    name, *line = input(" Enter name of student and marks in subjects separated by ' ' ").split()
    scores = list(map(float, line))
    marks[name] = scores
query_name = input(" Enter name of student ")
result = list(marks[query_name])
per = sum(result)/len(result)
print(" %.2f" % per)

