print("************")
mylist=[]
fname=input("enter your first name:\n")
lname=input("enter your last name:\n")
mylist.append(fname)
mylist.append(lname)
name="".join(mylist)
mylist.clear()
mylist.append(name)
mylist.append("")
sep="@gmail.com"
print(mylist)
print(sep.join(mylist))

