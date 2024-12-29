# 1)Take a inputs and Evaluate the expressions
# a)Take the Students name
# b)Take the student english marks
# maths,science,social,kannada,hindi
# c)add the total marks 
# d)print average
# e)add languages marks (english,kannada,hindi)and print average
# f)add the core subjects (maths,science and social)and print average
name=input("Student name:\n")
english=int(input("Enter the english marks:\n"))
maths=int(input("Enter the maths marks:\n"))
science=int(input("Enter the science marks:\n"))
social=int(input("Enter the social marks:\n"))
kannada=int(input("Enter the kannada marks:\n"))
hindi=int(input("Enter the hindi marks:\n"))
total_marks=english+maths+science+social+kannada+hindi
average_marks=total_marks/6
languages_marks=english+kannada+hindi
average_of_languages=languages_marks/3
coresubjects_marks=maths+science+social
average_of_coresubjects=coresubjects_marks/3
print("student avg in all subjects",average_marks)
print("student avg in languages",average_of_languages)
print("student avg in coresubjects",average_of_coresubjects)

# 2)create a list mylist  ``  `
# add "apple","banana","orange","mosambi"
# a)append "pineapple"
# b)remove "orange" and find the length of list
# c)print "banana, mosambi, pineapple"

# d)add new list to the existing [1,2,3,4]
# e)print only [1,2,3,4] and reverse [4,3,2,1]----*--+

mylist=["apple","banana","orange","mosambi"]
print(mylist)
mylist.append("pineapple")
print(mylist)
mylist.remove("orange")
print(mylist)
print(mylist[1:4])
mylist=["apple","banana","orange","mosambi",[1,2,3,4]]
print(mylist[4:])
print(mylist[-3:])
