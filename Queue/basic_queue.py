# Chapter : 4 - item : 1 - มาใช้ Queue กันเถอะ

# ให้น้องๆเขียนโปรแกรมโดยรับ input 2 แบบ โดยใช้ Queue ในการแก้ปัญหา
# E  <value>  ให้นำ value ไปใส่ใน Queue และทำการแสดงผล ข้อมูลปัจจุบันของ Queue

# D                 ให้ทำการ Dequeue ตัวที่อยู่หน้าสุดของ Queue ออก หลังจากนั้นแสดงตัวเลขที่เอาออกมา และ แสดงผลข้อมูล
#                     ปัจจุบันของ Queue

# ***และเมื่อจบการทำงานให้แสดงผลข้อมูลปัจจุบันของ Queue พร้อมกับข้อมูลที่ถูก Dequeue ทั้งหมดตามลำดับ
# ***ถ้าหากไม่มีข้อมูลใน Queue แล้วให้แสดงคำว่า  Empty

class Queue:
    def __init__(self):
        self.items = []
    def enQueue(self , i) :
        self.items.append(i)
        return i
    def deQueue(self ):
        return self.items.pop(0)
    def isEmpty(self):
        return len(self.items) == 0
    def size(self):
        return len(self.items)
    def __str__(self) -> str:
        if self.isEmpty() :
            return "Empty"
        return ', '.join([str(x) for x in self.items])

text = input("Enter Input : ").split(",")

q1 =  Queue()
dq = Queue()
i = 0
for char in text:
    opt = char.split(" ")
    if opt[0] == "E" :
        q1.enQueue(opt[1])
        print(f'Add {opt[1]} index is {q1.size()-1}')
    elif opt[0] == "D" :
        if q1.isEmpty():
            print(-1)
            continue
        # print(f"{dq.enQueue(q1.deQueue())} <- {q1}")
        print(f'Pop {q1.deQueue()} size in queue is {q1.size()}')
    i += 1

if q1.isEmpty():
    print('Empty')
else:
    print(f'Number in Queue is :  {q1.items}')


