# จงสร้าง Class funString ที่จะรับพารามิเตอร์เป็น String และเลขคำสั่งโดยมีฟังก์ชันดังต่อไปนี้
# 1. หาความยาวของ String
# 2. สลับพิมพ์เล็กพิมพ์ใหญ่ใน String (ห้ามใช้คำสั่ง upper และ lower)
# 3. Reverse String (ห้ามใช้คำสั่ง reversed)
# 4. ลบตัวอักษรที่ปรากฏมาก่อนใน String

# ascii table 
# A == 65
# Z == 90

# a == 97
# z == 122

# upper => lower : +32
# lower => upper : -32 

class funString():

    def __init__(self,string = ""):
        self.string = string
        return None

    def __str__(self):
        return "what are you looking for?"

    def size(self) :
        return len(self.string)

    def changeSize(self):
        new_string = ''
        letter = 0
        for i in self.string:
            if 90 >= ord(i) >= 65 :
                letter = ord(i) + 32
            elif 97 <= ord(i) <= 122:
                letter = ord(i)-32
            new_string = new_string + chr(letter)
            
        return new_string
    
    def reverse(self):
        reverse_string = ''
        for i in self.string[-1::-1]:
            reverse_string += i

        return reverse_string

    def deleteSame(self):
        delSame_sting = ''
        ord_check = []
        for i in self.string:
            if ord(i) not in ord_check :
                ord_check.append(ord(i))
                delSame_sting += i

        return delSame_sting



str1,str2 = input("Enter String and Number of Function : ").split()

res = funString(str1)

if str2 == "1" :    print(res.size())

elif str2 == "2":  print(res.changeSize())

elif str2 == "3" : print(res.reverse())

elif str2 == "4" : print(res.deleteSame())



