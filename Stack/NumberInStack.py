# จงสร้างฟังก์ชัน ManageStack() ในการจัดการตัวเลขที่อยู่ใน Stack โดยที่จะมีคำสั่งดังนี้
# A (add) : ทำการเพิ่มตัวเลขเข้าไปใน Stack
# P (pop) : ทำการนำเลขสุดท้ายใน Stack ออก ( ถ้า Stack ว่างให้แสดงผล -1 )
# D (delete) : ทำการลบตัวเลขที่ต้องการใน Stack ( ถ้า Stack ว่างให้แสดงผล -1 )  
# LD (lessthan delete) : ทำการลบตัวเลขที่น้อยกว่าตัวเลขที่กำหนดทั้งหมดออกจาก Stack และแสดงผลตัวเลขที่ถูกลบไป ( ถ้า Stack ว่างให้แสดงผล -1 )
# MD (Morethan delete) : ทำการลบตัวเลขที่มากกว่าตัวเลขที่ต้องการทั้งหมดออกจาก Stack และแสดงผลตัวเลขที่ถูกลบไป ( ถ้า Stack ว่างให้แสดงผล -1 )
# การ Delete ทุกแบบ ถ้าหากไม่มีเลขที่ถูกลบเลย ไม่ต้องแสดงผลอะไรและให้ทำการแสดงผลค่าที่อยู่ใน Stack เมื่อจบโปรแกรม

# *** Hint ***
# ฟังก์ชัน Delete ต่างๆให้สร้าง Stack ขึ้นมาอีก 1 อันเพื่อใช้เป็น Temp ในการเก็บค่าตัวเลขต่างๆ

class Stack():
    def __init__(self,list = None):
        if list == None:
            self.item = []
        else:
            self.item = list 

    # def __str__(self) :
    #     return self.item

    def push(self,ele):
        self.item.append(ele)

    def pop(self):
        return self.item.pop()
    
    def peek(self):
        return self.item[-1]
    
    def size(self):
        return len(self.item)
    
    def isEmpty(self):
        return self.item == []
    
def ManageStack(str):
    stack = Stack()
    temp_stack = Stack()

    inp_list = [ele for ele in str.split(',') ]

    for i in inp_list:
        # print(i)
        if i == 'P'  : 
            if stack.isEmpty():
                print(-1)
            else :
                stack.pop()
        
        else:
            command ,value = i.split(' ')
            # print(f'comm={command} valu={value}')
            if command == 'A':
                stack.push(value)
                
            elif command == 'D':
                if stack.isEmpty():
                    print(-1)
                else:
                    while not stack.isEmpty() and stack.peek() != value:
                        temp_stack.push(stack.pop())

                    if not stack.isEmpty() and stack.peek() == value:
                        stack.pop()

                    while not temp_stack.isEmpty():
                        stack.push(temp_stack.pop())

                    
            elif command == 'LD':
                pass
            elif command == 'MD':
                pass
        


    

                

    return stack.item 

# Enter Input : A 1,A 2,A 3,A 2,MD 2

inp = input('Enter Input : ')

print(ManageStack(inp))












