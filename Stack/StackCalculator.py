'''
ให้เขียน class calculator  ที่มีการทำงานผ่านฟังก์ชัน run(instructions) โดยมี instructions ดังนี้
+: Pop 2 ค่าออกจาก stack, นำมาบวกกัน และ push ผลลัพธ์ลง stack
-: Pop 2 ค่าออกจาก stack, นำค่าที่อยู่ข้างบนลบด้วยค่าที่อยู่ข้างล่าง และ push ผลลัพธ์ลง stack
*: Pop 2 ค่าออกจาก stack, นำมาคูณกัน และ push ผลลัพธ์ลง stack
/: Pop 2 ค่าออกจาก stack, นำค่าที่อยู่ข้างบนหารด้วยค่าที่อยู่ข้างล่าง และ push ผลลัพธ์ลง stack
DUP: Duplicate (not double) ค่าบนสุดของ stack
POP: Pop ค่าบนสุดออกจาก stack และ discard.
PSH: ทำการ push ตัวเลขลง stack
หมายเหตุ 1. คำสั่งอื่น ๆ (เช่นตัวอักษร) ควรทำให้เกิดค่า "Invalid instruction: [instruction]"
2. การนำค่าออกจาก stack สำหรับ calculator นี้ให้ การนำค่าออกจาก stack ครั้งแรกเป็น operand ด้านซ้าย และ การนำค่าออกจาก stack ครั้งที่ 2 เป็น operand ด้านขวา
*************************************************
print("* Stack Calculator *")
arg = input("Enter arguments : ")
machine = StackCalc()
machine.run(arg)
print(machine.getValue())
'''

class Stack():

    def __init__(self,list = None) :
        if list == None:
            self.item = []
        else:
            self.item = list
        
    def pop(self):
        return self.item.pop()
    
    def push(self,item):
        return self.item.append(item)
    
    def peek(self):
        return self.item[-1]
    
    def isEmpty(self):
        return self.item == []

    def size(self):
        return len(self.item)
    

class StackCalc():

    def __init__(self) -> None:
        self.stack = Stack()
         

    def run(self,arg):
        arg_list = [ele for ele in arg.split()]
        operator = '+-*/'

        for ele in arg_list:
            if ele.isdigit() :
                ele = ele
                self.stack.push(ele)
            elif ele in operator:
                temp1 = int(self.stack.pop())
                temp2 = int(self.stack.pop())
                result = 0

                if ele == '+':
                    result = temp1 + temp2 
                elif ele == '-':
                    result = temp1 - temp2
                elif ele == '*':
                    result = temp1 * temp2
                elif ele == '/':
                    result = int(temp1 / temp2)
                self.stack.push(str(result))
            
            elif ele == 'DUP':
                self.stack.push(self.stack.peek())
            
            elif ele == 'POP':
                self.stack.pop()

            else:
                self.stack.push(ele)
                break
            


    def getValue(self):
        if self.stack.isEmpty():
            out = 0
        else:
            top_stack = self.stack.peek()
            if top_stack.isalpha():
                out = f'Invalid instruction: {top_stack}'
            else:
                out = top_stack
        return out


print("* Stack Calculator *")
arg = input("Enter arguments : ")
machine = StackCalc()
machine.run(arg)
print(machine.getValue())







