# โรงอาหารของบริษัทแห่งหนึ่ง จะมีเจ้าหน้าที่คอยจัดแถวสำหรับการซื้ออาหาร โดยจะมีหลักการคือจะดูจากแผนกของพนักงานแต่ละคนว่าอยู่แผนกไหน ถ้าหากในแถวที่ต่ออยู่มีแผนกนั้น จะนำพนักงานคนนั้นแทรกไปด้านหลังของแผนกเดียวกัน ตัวอย่างเช่น
# Front | 1 2 2 2 2 3 3 3 | Rear  จาก Queue ถ้าหากมีพนักงานแผนก1เข้ามา Queue จะกลายเป็น Front | 1 1 2 2 2 2 3 3 3 | Rear
# Input :
# จะแบ่งเป็น 2 ฝั่งแบ่งด้วย /   คือ ซ้าย : เป็นแผนกของพนักงานและIDของพนักงานแต่ละคน  ขวา : จะแบ่งเป็น 2 ส่วน คือ D กับ E
# E < id >  ->   เป็นการนำพนักงานเข้า Queue
# D  ->  เป็นการนำพนักงานคนหน้าสุดออกจากแถว โดยจะแสดงผลเป็น id ของพนักงานคนนั้น ถ้าหากไม่มีพนักงานในแถวจะทำการแสดงผลเป็น Empty

# อธิบาย TestCase_1 :  จะมีพนักงาน 4 คน คือแผนก 1 id=101,102 และแผนก 2 id=201,202  ต่อมาจะแสดงผล Empty เพราะยังไม่มีพนักงานในแถว  และนำพนักงาน id=101และ201 เข้าแถวตามลำดับ ต่อมาจะแสดงผลเป็น 101 เพราะพนักงาน 101 อยู่คนแรกและแสดงผล 201 เพราะอยู่คนแรก


class Queue:

    def __init__(self, list=None):
        if list == None:
            self.item = []
        else:
            self.item = list

    def __str__(self) -> str:
        s = ""
        for i in self.item:
            s += i
            s += ","
        return s

    def deQueue(self):
        return self.item.pop(0)

    def enQueue(self, e):
        self.item.append(e)

    def size(self):
        return len(self.item)

    def isEmpty(self):
        return self.item == []


inp1, inp2 = input("Enter Input : ").split("/")

start_inp = [e for e in inp1.split(",")]
action_inp = [e for e in inp2.split(",")]

print(start_inp)
print(action_inp)

list_panek = []

for i in start_inp:
    if i[0] in list_panek:
        pass
    else:
        list_panek.append(i[0])

print(list_panek)
list_allQ = []
print(len(list_panek))


for i in range(len(list_panek)):
    print(i)
    q = Queue()
    list_allQ.append(q)

for i in list_allQ:
    print("++ ", i)
    for j in start_inp:
        # print(type(i))

        i.enQueue(j)

# print(list_allQ[1])


# for i in start_inp:
#     for j in list_panek:
#         if i[0] == j:
#             list_allQ[j].append(i[2:])


# print(list_allQ)
