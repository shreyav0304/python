# '''1) write a program to take a input from the user and print the details
#    *Employee Name
#    *Employee Age
#    *Employee Phone Number\
#    *EMployee Address
# along with this print the type of all the variables

# print(type(input("Enter Employee Name:")))
# print(type(int(input("Enter Employee Age:"))))
# print(type(int(input("Enter your Age:"))))
# print(type(int(input("Enter your Mobile Number:"))))
# age=type(int(input("Enter your Age:")))
# print(age)
# Phone=type(int(input("Enter your Number:")))
# print("Here is Employee number",Phone)
# Address=type(input("Enter your Address:"))
# print(Address)

# 2)write a program to take a input from the user and print the details
#   *Student Name 
#   *Student maths marks
#   *Student science marks
# ->print student name in Upper case
# ->add students marks (math+science) then print the total marks
# ->then find the average of two subjects
Name=input("Enter your Name:\n")
Maths=int(input("Enter your Maths marks:\n"))
science=int(input("Enter your science marks:\n"))
print("i am coverting name into uppercase")

print("name is",Name.upper())
total=Maths+science
print("total marks obtained by ",Name,':',total)
print("average marks obtained by ",Name,':',total//2)