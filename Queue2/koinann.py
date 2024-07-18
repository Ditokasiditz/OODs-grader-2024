# จำลองการเลื่อนแถวคอยภายในเวลาที่กำหนดโดยใช้ class queue

# โดยที่มีแถวหลัก 1 แถวยาวกี่คนก็ได้

# แถวหน้า cashier 1 ยาว 5 คน โดยที่คนนี้จะใช้เวลา 3 นาทีในการคิดค่าบริการ

# แถวหน้า cashier 2 ยาว 5 คน โดยที่คนนี้จะใช้เวลา 2 นาทีในการคิดค่าบริการ

# ลูกค้าจะ move แถวทุกๆ 1 นาที โดยหากแถว 1 ว่างจะไปก่อนหากเต็มจึงไปแถว 2

# จงแสดง นาที [แถวหลัก] [แถว cashier 1] [แถว cashier 2] จนกว่าแถวหลักจะหมด

class Queue:

    def __init__(self,list = None):
        if list == None:
            self.item = []
        else :
            self.item = list 

    def deQueue(self):
        return self.item.pop(0)

    def enQueue(self,ele):
        self.item.append(ele)

    def isEmpty(self):
        return self.item == []

    def size(self):
        return len(self.item)

inp = [ele for ele in input('Enter people : ')]

i = 1
mainRow = Queue(inp)
c1Row = Queue()
c2Row =Queue()
countTime1 = 0
countTime2 = False

while not mainRow.isEmpty():
    print(i,end=' ')
    if c1Row.size() < 5 :
        c1Row.enQueue(mainRow.deQueue())
    else:
        c2Row.enQueue(mainRow.deQueue())
        countTime2 = True

    print(mainRow.item,end=' ')
    print(c1Row.item,end=' ')
    print(c2Row.item)

    if countTime2 :
        countTime1 += 1 

    if i % 3 == 0:
        if not c1Row.isEmpty():
            c1Row.deQueue()
    if countTime1 % 2 == 0 and countTime2:
        if not c2Row.isEmpty():
            c2Row.deQueue()

    i += 1





