# Chapter : 4 - item : 5 - Search Portal

# พี่ซันฟงได้รับคำสั่งจากอาจารย์ให้ออกโจทย์เขียนโปรแกรมให้แก่น้องๆ พี่จึงกลับไปนอนคิดที่บ้าน 
#รู้สึกตัวอีกทีก็อยู่ในห้องมืดๆ พี่สามารถมองเห็นและเดินไปยังพื้นที่ที่อยู่ติดกันได้ (4 ทิศ เหนือ ใต้ ออก ตก) 
# พี่จะต้องหาประตูทางออกจากฝันเพื่อไปส่งโจทย์ให้กับอาจารย์
# ต่อมาพี่ก็คิดวิธีในการเดินหาประตูทางออกได้โดยใช้วิธีหาแบบ Breadth First Search โ
#ดยพี่จะเริ่มยืนในจุดเริ่มต้นแล้วมองหาและจำทางเริ่มจากทิศเหนือ ทิศตะวันออก ทิศใต้ ทิศตะวันตก ตามลำดับ 
# แล้วเดินไปยังช่องถัดไปแล้วหาใหม่ ในเมื่อคิดวิธีออกแล้วพี่จึงต้องการโปรแกรมที่จะบอกพี่ว่าสามารถไปถึงทางออกได้หรือพี่จะต้องติดอยู่ในฝันไปตลอดกาล 
# ปัญหาคือพี่ขี้เกียจเขียนโค้ด พี่เลยอยากให้น้องๆเขียนโค้ดให้พี่หน่อย เขียนสวยๆกะทัดรัด ไม่งั้นจะส่งกลับไปเขียนใหม่
# โดยรายละเอียดโปรแกรมจะมีดังนี้
# Input
# รับความกว้าง ความสูง และแผนที่ โดยแผนที่แต่ละบรรทัดจะขั้นด้วย ','
# ตัวอย่าง input: 3 3 F__,##_,O__
# จะมีความหมายว่าแผนที่กว้าง 3 สูง 3 และแผนที่จะเป็นแบบนี้
# F__
# ##_
# O__
# ภายในแผนที่
# 'F' แทนตำแหน่งเริ่มต้นของพี่
# 'O' แทนประตูทางออก
# '_' แทนพื้นที่ที่สามารถเดินได้
# ตัวอักษรอื่นๆทั้งหมดแทนกำแพง ไม่สามารถเดินไปที่ช่องนั้นได้
# Output
# หากไม่มีพี่ (F) อยู่ในห้องหรือแผนที่ที่ใส่เข้ามาไม่ตรงกับขนาดของ width ให้แสดงว่า "Invalid map input."
# แสดง queue ระหว่างหาทางออก
# ถ้าหาทางออกเจอให้แสดงว่า "Found the exit portal."
# ถ้าหาไม่เจอให้แสดงว่า "Cannot reach the exit portal."

class Queue :
    def __init__(self, items=None):
        if items :
            self.items = items
        else :
            self.items = []
    def deQueue(self):
        if self.isEmpty() :
            return -1
        return self.items.pop(0)
    def enQueue(self,item):
        self.items.append(item)
        return item
    def isEmpty(self):
        return len(self.items) == 0 
    def size(self):
        return len(self.items)
    def clear(self):
        self.items = []
    
q1 = Queue() # ทางที่เคยเดิน
q3 = Queue() # ทางที่เดินได้
width , height , room =  input("Enter width, height, and room: ").split(" ")
room  = room.split(",")
map_room = []
start = False
err =  False
exit_room = True
frist = False
width = int(width)
height = int(height)

move_ment = [(0,-1) , (1,0), (0,1) , (-1,0)]


for i in range(height):
    try :
        if len(room[i]) == width:
            map_room.append(room[i])
        else :
            print("Invalid map input.")
            err = True
            frist = True
            break
        if "F" in room[i]:
            q3.enQueue((room[i].index("F"),i))
            start = True
    except :
        print("Invalid map input.")
        err = True
        frist = True
        break
else :
    if len(map_room) != height :
        print("Invalid map input.")
        frist = True
        err = True
if not start :
    err = True
    if not frist:
        print("Invalid map input.")
if not err :
    # print('\n'.join(map_room))
    print(f"Queue: {q3.items}")
    while not q3.isEmpty() :
        x , y = q3.deQueue()
        q1.enQueue((x,y))
        for move_x , move_y in move_ment :
            if ( x+move_x >= 0 and x+move_x < width ) and ( y+move_y >= 0 and y+move_y < height) :
                if map_room[y+move_y][x+move_x] == "_" :
                    list_move = q1.items
                    list_will_move = q3.items
                    if ( x+move_x , y+move_y ) not in list_move and ( x+move_x , y+move_y ) not in list_will_move :
                        q3.enQueue(( x+move_x , y+move_y ))
                elif map_room[y+move_y][x+move_x] == "O" :
                    exit_room = False
                    err = True
                    print("Found the exit portal.")
                    q3.clear()
                    break
        if not q3.isEmpty():
            print(f"Queue: {q3.items}")
if not err :
    print("Cannot reach the exit portal.")

# 6 4 
# F__###
# __####
# _#####
# __#O##

