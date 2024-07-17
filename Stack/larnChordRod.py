# ที่จอดรถของนาย ก เป็นส่วนที่แรเงาสีฟ้า ส่วนสีแดงเป็นที่ของนาย ข ซี่งเป็นญาติกัน ที่จอดรถของนาย ก และ นาย ข แคบมาก จอดรถได้เรียงเดี่ยว นาย ข ไม่ได้ใช้ที่จอดรถ แต่ อนุญาติให้นาย ก ใช้ที่จอดรถของเขาได้โดยไม่จอดรถแช่ไว้ เนื่องจากซอยแคบ ดังนั้นการมาจอด (arrive) และการรับรถ (depart)จะเป็นลักษณะของ stack เงื่อนไขคือ ในการรับรถ x ใดๆอยากให้ลำดับรถเป็นเหมือนเดิม ดังรูป simulate การจอดรถในที่จอดรถของนาย ก โดยใช้ operation ของ stack ข้างล่างเป็นตัวอย่าง output

# การรับ input : รับ input 4 ค่าใน 1 บรรทัดโดยให้แยกโดย " " (space bar) โดยตำแหน่งแรกคือ จำนวนสูงสุดที่รถสามารถจอดได้ในซอยของ นาย ก ตำแหน่งที่สองคือ รถที่จอดอยู่ในซอยของ นาย ก ตำแหน่งที่สามคือ การกระทำเช่น ถ้าเป็น arrive จะทำการเพิ่มรถในซอย ส่วน depart จะทำการเอารถออกจากซอย โดยรถที่จะทำการเพิ่มหรือนำออกนั้นจะเป็น เลขในตำแหน่งที่ 4

# ***หมายเหตุ ถ้าในซอยไม่มีรถอยู่เลยให้ input = 0 ในตำแหน่งที่ 2***

class Stack():

    def __init__(self,list = None) -> None:
        if list == None:
            self.item = []
        else:
            self.item = list

    def push(self,ele):
        self.item.append(ele)

    def pop(self):
        return self.item.pop()
    
    def peek(self):
        return self.item[-1]

    def size(self):
        return len(self.item)
    
    def isEmpty(self):
        return self.item == []
    

def ParkCar(inp):
    stackA = Stack()
    stackB = Stack()

    soi_size = int(inp[0])
    car_list = [int(ele) for ele in inp[1].split(',') ]
    action = inp[2]
    car_action = int(inp[3])

    for ele in car_list :
        if ele > 0 :
            stackA.push(ele)
    
    if action == 'arrive' :
        if stackA.size() == soi_size:
            print(f'car {car_action} cannot arrive : Soi Full')
        elif stackA.size() < soi_size:
            if car_action in car_list:
                print(f'car {car_action} already in soi')
            else:
                stackA.push(car_action)
                print(f'car {car_action} arrive! : Add Car {car_action}')

    elif action == 'depart':
        if stackA.size() == 0:
            print(f'car {car_action} cannot depart : Soi Empty')
        else:
            if car_action in car_list :
                while not stackA.isEmpty():
                    if stackA.peek() == car_action:
                        stackA.pop()
                        print(f'car {car_action} depart ! : Car {car_action} was remove')
                    else:
                        stackB.push(stackA.pop())
                    
                while not stackB.isEmpty():
                    stackA.push(stackB.pop())
            
            else:
                print(f'car {car_action} cannot depart : Dont Have Car {car_action}')

    print(stackA.item)
            

print('******** Parking Lot ********')
inp_list = [ele for ele in input('Enter max of car,car in soi,operation : ').split()]
ParkCar(inp_list)










