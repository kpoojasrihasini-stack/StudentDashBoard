from builtins import int, print, input

print("==================================")
print("Welcome to Student Dashboard ")
print("===================================")
Studentid= int(input("Enter Student ID:"))
Studentname=input("Enter Student Nane: ")
Subject1=input("Enter Subject1: ")
Subject2=input("Enter Subject2: ")
Subject3=input("Enter Subject3: ")
NumofHrspersubject1=int(input("enter yoursubject1: "))
NumofHrspersubject2=int(input("enter yoursubject2: "))
NumofHrspersubject3=int(input("enter yoursubject3: "))

print("=========================")
print("Subject 1: ",Subject1)
print("Subject 2: ",Subject2)
print("Subject 3: ",Subject3)
print("NumofHrspersubject1: ",NumofHrspersubject1)
print("NumofHrspersubject2: ",NumofHrspersubject2)
print("NumofHrspersubject3: ",NumofHrspersubject3)

print("TotalHourspersubject:",NumofHrspersubject1+NumofHrspersubject2+NumofHrspersubject3)

