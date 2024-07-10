# ให้นักศึกษาเขียนโปรแกรมภาษา Python โดยใช้ Function ในการหาตำแหน่ง คู่ กับ คี่ จาก List และ String
# โดยที่รูปแบบการรับ Input ตำแหน่งแรกจะเป็นตัวบอกว่าเป็น String หรือ List ถ้าใส่ S = String ถ้าใส่ L = List
# Input ตำแหน่งที่สองเป็นค่าใน String หรือ List ที่นำเข้ามา
# Input ตำแหน่งที่สามเป็นการบอกว่าจะแสดงตำแหน่งคู่หรือคี่ ถ้าใส่ Odd = คี่ ถ้าใส่ Even = คู่



def odd_even(type, data, mode):
    if mode == 'Odd':
        mode = 0
    elif mode == 'Even':
        mode = 1

    new_string = ''

    if type == 'S':
        s = data
        for i in s[mode::2] :
            new_string += i
        return new_string
    
    elif type == 'L':
        list = []
        new_list = []

        list = data.split()
        for i in list[mode::2] :
            new_list.append(i)
        return new_list

    return None

print('*** Odd Even ***')

t,d,m = input('Enter Input : ').split(',')

print(odd_even(t,d,m))
    

