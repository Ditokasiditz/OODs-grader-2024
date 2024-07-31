# ให้น้องๆเขียนโปรแกรมรับ input เป็นวงเล็บ โดยมีรูปแบบดังนี้  วงเล็บเปิด :  (  กับ  [    วงเล็บปิด :  )  กับ  ]   โดยให้หาว่าถ้าหากนำวงเล็บมาจับคู่กัน จะครบทุกคู่หรือไม่  โดยให้แสดงผลลัพธ์ออกมาเป็นจำนวนวงเล็บที่จะต้องเติมหากวงเล็บมีไม่ครบคู่   แต่ถ้าหากครบคู่ให้แสดงคำว่า  Perfect  ออกมาด้วย


class Stack:

    def __init__(self, list=None):
        if list == None:
            self.item = []
        else:
            self.item = list

    def pop(self):
        return self.item.pop()

    def push(self, e):
        self.item.append(e)

    def peek(self):
        return self.item[-1]

    def isEmpty(self):
        return self.item == []

    def size(self):
        return len(self.item)


inp = input("Enter Input : ")

open = "([{"
close = ")]}"

stack = Stack()

for e in inp:
    if e in open:
        stack.push(e)
    elif e in close:
        if not stack.isEmpty():
            try:
                open.index(stack.peek()) == close.index(e)
                stack.pop()
            except:
                stack.push(e)
        else:
            stack.push(e)

print(stack.size())
if stack.isEmpty():
    print("Perfect ! ! !")
