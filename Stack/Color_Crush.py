class Stack:
    def __init__(self, list=None):
        if list == None:
            self.items = []
        else:
            self.items = list

    def push(self, value):
        self.items.append(value)
    
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[-1]
    
    def isEmpty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)


inp = input('Enter Input : ').split()

S = Stack()

char = ''
count = 0
combo = 0
for color in inp:
    S.push(color)

    if color == char:
        count += 1
    else:
        char = color
        count = 1

    if count == 3:
        S.pop()
        S.pop()
        S.pop()

        count = 0
        combo += 1

        if S.size() > 1:
            if S.items[-1] == S.items[-2]:
                char = S.items[-1]
                count = 2
            else:
                char = S.items[-1]
                count = 1
        elif S.size() == 1:
            char = S.items[-1]
            count = 1


print(S.size())

if S.size() < 1:
    print("Empty", end='')

for i in range(S.size() -1, -1, -1):
    print(S.items[i], end='')

if combo > 1:
    print("\nCombo :", combo, "! ! !")