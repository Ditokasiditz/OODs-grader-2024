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

    l1 = [1, 2, 3, 4, 5]
    l1.reverse()

    print(l1)
