def odd_list(al):
    new_odd_list = []
    for i in al :
        if i%2 == 1 :
            new_odd_list.append(i)
    
    return new_odd_list 




print(" ***Function Odd List***")
ls = [int(e) for e in input("Enter list numbers : ").split()]

opls = odd_list(ls)
print("Input list : ", ls, "\nOutput list : ", opls)
