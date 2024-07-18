# ให้น้องๆเขียนโปรแกรมโดยรับ input 2 แบบ โดยใช้ QUEUE ในการแก้ปัญหา
# E  <value>  ให้นำ value ไปใส่ใน QUEUE และทำการแสดงผลค่าที่ทำการ enqueue และ index ของตัวที่ทำการเพิ่มเข้าไป
# D                 ให้ทำการ dequeue ตัวที่อยู่หน้าสุดของ Queue ออกและแสดงตัวเลขที่เอาออกและแสดงขนาดของ Queue
#                     หลังจากทำการ dequeue แล้ว
# *** ในตอนสุดท้ยถ้าหากใน Queue ยังมี Value อยู่ให้แสดงผลออกมา  ถ้าหากไม่มีแล้วให้แสดงคำว่า  Empty ***

class Queue:
    def __init__(self,list = None):
        if list == None:
            self.item = []
        else :
            self.item = list 
    
    def enQueue(self,ele):
        self.item.append(ele)

    def deQueue(self):
        return self.item.pop(0)

    def isEmpty(self):
        return self.item == [] 

    def size(self):
        return len(self.item)


inp = [ele for ele in input('Enter Input : ').split(',')]
queue = Queue()

for ele in inp:
    if ele[0] == 'E':
        queue.enQueue(ele[2:])
        print(f'Add {ele[2:]} index is {queue.size()-1}')
    elif ele[0] == 'D':
        if queue.isEmpty():
            print(-1)
        else:
            print(f'Pop {queue.deQueue()} size in queue is {queue.size()}')

if queue.isEmpty():
    print('Empty')
else:
    print(f'Number in Queue is : {queue.item}')