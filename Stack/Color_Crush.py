# หลังจากกฤษฎาล้างจานเสร็จ ก็ได้มาเล่นเกมส์ที่กำลังเป็นที่นิยมทั่วโลกในตอนนี้   Microsoft Flight Simulator ?  Fall Guys ?  Valorant ?  ผิดทั้งหมดกฤษฎาได้กล่าวไว้  เกมที่กำลังเป็นที่นิยมคือ Color Crush ต่างหาก   โดยเกมนี้จะเป็นการนำสีมาเรียงต่อกัน โดยสีจะหายไปก็ต่อเมื่อมีการเรียงสีเหมือนกันครบ 3 อัน เช่น  A B B B A  -> A A เนื่องจาก B เรียงติดกัน 3 ตัวทำให้ระเบิดหายไปโดยที่สีจะมีทั้งหมด 26 สี และจะถูกแทนด้วย A - Z  โดยถ้าหากมีการระเบิดตั้งแต่ 2 ครั้งขึ้นไปจะแสดง Combo ขึ้นมา
# 
# โดยเมื่อการระเบิดสิ้นสุดลงให้แสดงลำดับของสีที่เหลือจากขวาไปซ้าย

class Stack :

    def __init__(self,list = None) :
        if list == None:
            self.item = []
        else :
            self.item = list

    def __str__(self) :
        s = ''
        for ele in self.item:
            s += ele
        return s

    def push(self,item):
        self.item.append(item)
    
    def pop(self):
        return self.item.pop()

    def peek(self):
        if stack.isEmpty():
            out = None
        else :
            out = self.item[-1]
        return out
    
    def isEmpty(self):
        return self.item == []
    
    def size(self):
        return len(self.item)
    

inp = input("Enter Input : ")
list_inp = [ele for ele in inp.split()]

stack = Stack()
count = 0
combo = 0

for i in range(len(list_inp)) :
    alp = list_inp[i]
    if stack.peek() == alp:
        count += 1
    else :
        count = 0
    print(f'push {alp}')
    stack.push(alp) 

    print(f'count = {count}')

    if  count == 2 :
        combo += 1
        for i in range(3) :
            stack.pop()
        count = 0
    i = 0
#แก้ตรง ทุกครั้งที่ ออก มีการ reset color ใหม่

print(stack.size())
if stack.isEmpty() :
    print("Empty")
else :
    str = ''
    for i in range(stack.size()) :
        str += stack.pop()
    print(str)
    if combo >= 2 :
        print(f'Combo : {combo} ! ! !')









