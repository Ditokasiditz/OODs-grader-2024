class Queue():
    def __init__(self, items=None, max=None, ) -> None:
        if items is None:
            self.items = []
        else:
            self.items = items
        
        self.max = max

    
    def __str__(self) -> str:
        return str(self.items)

    def __len__(self) -> int:
        return len(self.items)

    def __getitem__(self, i:int):
        return self.items[i]

    def isEmpty(self):
        return len(self) == 0

    def isFull(self):
        if self.max is not None:
            return len(self) == self.max
        else:
            return False

    def deQueue(self):
        if not self.isEmpty():
            return self.items.pop(0)

    def enQueue(self, x):
        if not self.isFull():
            self.items.append(x)

class Cashier(Queue):
    def __init__(self, inp:str, items=None, max=None) -> None:
        super().__init__(items=[*inp], max=max)
        self.cashier1 = Queue(max=5)
        self.cashier2 = Queue(max=5)

    # def __str__(self) -> str:
    #     return '[' + '\', \''.join([str(st) for st in self.items]) + ']'

    def solve(self):
        cmax = 5
        c1time = 3
        c2time = 2
        idx = 1
        while not self.isEmpty():
            if not self.cashier1.isFull():
                self.cashier1.enQueue(self.deQueue())
            elif not self.cashier2.isFull():
                self.cashier2.enQueue(self.deQueue())
            print(f'{idx} {self} {self.cashier1} {self.cashier2}')
            if idx % 3 == 0 and not self.cashier1.isEmpty():
                self.cashier1.deQueue()
            idx += 1
            if idx % 2 == 0 and not self.cashier2.isEmpty():
                self.cashier2.deQueue()

inp = input('Enter people : ')
c = Cashier(inp)
c.solve()