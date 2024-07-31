# evuate postfix


class Stack:

    def __init__(self, list=None):
        if list == None:
            self.item = []
        else:
            self.item = list

    def push(self, e):
        self.item.append(e)

    def pop(self):
        return self.item.pop()

    def peek(self):
        return self.itemp - [-1]

    def isEmpty(self):
        return self.item == []

    def size(self):
        return len(self.item)


inp = input("Input Postfix : ")
stack = Stack()
for e in inp:
    if e.isdigit():
        stack.push(int(e))
    elif e in "+-*/":
        rightOP = stack.pop()
        leftOP = stack.pop()

        if e == "+":
            stack.push(leftOP + rightOP)
        if e == "-":
            stack.push(leftOP - rightOP)
        if e == "*":
            stack.push(leftOP * rightOP)
        if e == "/":
            stack.push(leftOP / rightOP)
        print(stack.item)


# print(stack.item)
"""
input 

for e in input 
    if e in '+-*/'       
        rightop = stack.pop
        leftop = stack.pop

        if e == '+'
            result = r + l
        elif
        elif
        elif

        stack.push(result)
"""
