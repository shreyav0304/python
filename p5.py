# 1)write a python program to create a dictionary
# add key value pairs using input
# employee name,employee age,employee number
# employe role and print the keys and values

# 2)create a python program to add the 
# values in the sets
# a)add 1,2,3,4,6
# b)union the set with 7,4,5,9,0,10
# c)find the common elements using intersection

# 3)write a python program
# to create a new file name "ark.txt"
# a)add below content using write file
# "Ria Institue of Technology
# Ria is at Marathalli Bangalore
# We are the Developer"
# b)read the file and print
# c)read only two lines frome file
# d)append "Developer" in new lines
# e)read the Developer using readlines

employeename=input("enter en:\n")
employeeage=input("enter ea:\n")
employeenumber=input("enter enn:\n")
employeerole=input("enter er:\n")
mydict={
    "employeename":employeename,
    "employeeage":employeeage,
    "employeenumber":employeenumber,
    "employeerole":employeerole
}
print(mydict)
print(mydict.keys())
print(mydict.values())
print(mydict.items())
