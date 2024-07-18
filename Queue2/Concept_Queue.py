# รับ input 1 บรรทัด โดย แต่ละลำดับ จะมีอักษรกำกับไว้และตามด้วยจำนวนครั้งที่ต้องทำตามตัวอักษรนั้น E คือ การ enqueue และ D คือการ dequeue แต่หากเป็นตัวอักษรอื่นให้นับเป็น error input
# ต้องบอกว่า มีการ dequeue ที่ไม่เกิดผลกี่ครั้งตามลำดับ และแต่ละครั้งที่มีการเกิดขึ้นใน Queue มีการเปลี่ยนแปลงอย่างไรตามขั้นตอน


class Queue:

    def __init__(self,list = None):
        if list == None:
            self.item = []
        else :
            list.item = list 

    def deQueue(self):
        return self.item.pop(0)

    def enQueue(self,ele):
        self.item.append(ele)

    def isEmpty(self):
        return self.item == []

    def size(self):
        return len(self.item)
    
inp = [ele for ele in input('input : ').split(',')]
queue = Queue()
number=0
error=0
errorInp=0
for i in inp:
    
    if i[0] == 'D':
        if queue.size()<int(i[1:]):
            error+=-int(i[1:])+queue.size()
            for j in range(queue.size()):
                queue.deQueue()
            
        else:
            for j in range(int(i[1:])):
                queue.deQueue()
        
        
    elif i[0] == 'E':
        # print(i[1],type(i[1]))D
        for j in range(int(i[1:])):
            queue.enQueue(f'*{number}')
            number += 1
    else:
        errorInp+=1 


    print(f'Step : {i}')
    if i[0] == 'D':
        print("Dequeue : ",queue.item)
    elif i[0] == 'E':
        print("Enqueue : ",queue.item)
    else:
        print(queue.item)
    print("Error Dequeue : " ,-error)
    print("Error input : ",errorInp)
    print('--------------------')


        

    





