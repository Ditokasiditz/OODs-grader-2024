class Stack:
    def __init__(self, list=None):
        if list is None:
            self.item = []
        else:
            self.item = list
    
    def push(self, item):
        self.item.append(item)
    
    def pop(self):
        return self.item.pop()
    
    def peek(self):
        return self.item[-1]
    
    def isEmpty(self):
        return self.item == []
    
    def size(self):
        return len(self.item)

def parenMatching(s):
    stack = Stack()
    open_paren = '(['
    close_paren = ')]'
    unmatched_open = 0
    unmatched_close = 0

    for ele in s:
        if ele in open_paren:
            stack.push(ele)
        elif ele in close_paren:
            if not stack.isEmpty():
                if close_paren.index(ele) == open_paren.index(stack.peek()):
                    stack.pop()
                else:
                    unmatched_close += 1
            else:
                unmatched_close += 1
    
    unmatched_open = stack.size()

    if unmatched_open == 0 and unmatched_close == 0:
        print(0)
        print("Perfect ! ! !")
    else:
        print(unmatched_open + unmatched_close)

inp = input("Enter Input : ")
parenMatching(inp)
