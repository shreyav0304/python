def first_last_name(numberlist):
    print("Given list:",numberlist)
    first_num=numberlist[0]
    last_num=numberlist[-1]
    if first_num==last_num:
        return True
    else:
        return False
    numbers_x=[10,20,30,40,10]
    print("result is",first_last_name(numbers_x))
    numbers_y=[75,65,35,75,30]
    print("result is",first_last_name(numbers_y))

