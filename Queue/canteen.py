# Chapter : 4 - item : 4 - Canteen

# โรงอาหารของบริษัทแห่งหนึ่ง จะมีเจ้าหน้าที่คอยจัดแถวสำหรับการซื้ออาหาร โดยจะมีหลักการคือจะดูจากแผนกของพนักงานแต่ละคนว่าอยู่แผนกไหน ถ้าหากในแถวที่ต่ออยู่มีแผนกนั้น จะนำพนักงานคนนั้นแทรกไปด้านหลังของแผนกเดียวกัน ตัวอย่างเช่น
# Front | 1 2 2 2 2 3 3 3 | Rear  จาก Queue ถ้าหากมีพนักงานแผนก1เข้ามา Queue จะกลายเป็น Front | 1 1 2 2 2 2 3 3 3 | Rear

# Input :
# จะแบ่งเป็น 2 ฝั่งแบ่งด้วย /   คือ ซ้าย : เป็นแผนกของพนักงานและIDของพนักงานแต่ละคน  ขวา : จะแบ่งเป็น 2 ส่วน คือ D กับ E
# E < id >  ->   เป็นการนำพนักงานเข้า Queue
# D  ->  เป็นการนำพนักงานคนหน้าสุดออกจากแถว โดยจะแสดงผลเป็น id ของพนักงานคนนั้น ถ้าหากไม่มีพนักงานในแถวจะทำการแสดงผลเป็น Empty

# อธิบาย TestCase_1 :  จะมีพนักงาน 4 คน คือแผนก 1 id=101,102 และแผนก 2 id=201,202  ต่อมาจะแสดงผล Empty เพราะยังไม่มีพนักงานในแถว  และนำพนักงาน id=101และ201 เข้าแถวตามลำดับ ต่อมาจะแสดงผลเป็น 101 เพราะพนักงาน 101 อยู่คนแรกและแสดงผล 201 เพราะอยู่คนแรก

class Queue:
    def __init__(self , items=None):
        if items :
            self.items = items
        else :
            self.items = []
    def enQueue(self,item):
        self.items.append(item)
        return item
    def deQueue(self):
        if self.isEmpty():
            return -1
        return self.items.pop(0)
    def isEmpty(self):
        return len(self.items) == 0
    def size(self):
        return len(self.items)



q1 = Queue()

left,right =  input("Enter Input : ").split("/")

employee = {}

def getKey(department_id):
    for key in employee.keys() :
            if department_id in employee[key] :
                department = key
    return department


for condition in left.split(",") :
    department , department_id =  condition.split(" ")
    try :
        employee[department].append(department_id)
    except :
        employee[department] = [department_id]

for condition in right.split(",") :
    try :
        opt , department_id =  condition.split(" ")
    except :
        opt = condition
    if opt == "D" :
        # print(q1.items)
        check = q1.deQueue()
        if check == -1 :
            print("Empty")
        else :
            print(check)
    elif opt == "E" :
        if q1.isEmpty() :
            q1.enQueue(department_id)
            continue
        department = getKey(department_id)
        q2 = Queue()
        check = False
        ok = False
        for i  in range(q1.size()):
            department_id_q1 = q1.deQueue() 
            department_q1 = getKey(department_id_q1) 
            if department != department_q1:
                if check :
                    q2.enQueue(department_id)
                    check = False
                    ok = True
                q2.enQueue(department_id_q1)
            elif department == department_q1 :
                q2.enQueue(department_id_q1)
                check = True
        else :
            if not ok :
                q2.enQueue(department_id)
        
        for i in range(q1.size()):
            q2.enQueue(q1.deQueue())

        for i in range(q2.size()):
            q1.enQueue(q2.deQueue())