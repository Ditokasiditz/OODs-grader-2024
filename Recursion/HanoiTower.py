# chapter : 6 - item : 1 - หอคอยแห่งฮานอย

# เขียนโปรแกรมแก้ปัญหา หอคอยแห่งฮานอย โดยเราจะมีแทงไม้อยู่ 3แท่งคื A B C และรับ input
# เป็นจำนวนแผ่นไม้ที่วางซ้อนกันให้แสดงลำดับการย้ายแผ่นไม้ทั้งหมดจากแท่ง A ไปยัง แท่งC
# โดยแผ่นไม้ที่มีขนาดเล็กกว่าจะอยู่ข้างบนแผ่นไม้ที่มีขนาดใหม่กว่าเสมอ(ห้ามวางแผ่นเล็กกว่าไว้ข้างล่าง)

# ****ห้ามใช้คำสั่ง for, while, do while*****

# หมายเหตุ ทุกฟังก์ชันต้องมี parameter มากที่สุดไม่เกิน 5 ตัว

# คำแนะนำ ให้สร้างฟังก์ชันสำหรับแสดงผล แยกต่างหาก และใช้ list ในการเก็บข้อมูลของแท่งไม้แต่ละแท่ง
# และให้ระวังเรื่องการสลับ list ให้ดีๆ

# หากมีข้อสงสัยเกี่ยวกับ หอคอยแห่งฮานอย สามารถสอบถาม TA เพิ่มเติม หรือ ลองเล่นได้ที่
# https://www.mathsisfun.com/games/towerofhanoi.html

# def move(n,A,B,C,maxn):
#     #code here
# n = int(input("Enter Input : "))


# A = start , B = พัก , C = ปลายทาง
class Stack:
    def __init__(self, name) -> None:
        self.items = []
        self.name = name

    def push(self, data):
        self.items.append(data)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def __str__(self) -> str:
        return " ".join(self.items)


A = Stack("A")
B = Stack("B")
C = Stack("C")


def move(n, A, B, C, maxn):
    if n == 1:
        display(maxn)
        print(f"move {A.peek()} from  {A.name} to {C.name}")
        # print("n==1")
        # print(f"A : {A} , B : {B} , C : {C}")
        C.push(A.pop())
        return
    else:
        move(n - 1, A, C, B, maxn)
        display(maxn)
        print(f"move {A.peek()} from  {A.name} to {C.name}")
        C.push(A.pop())
        move(n - 1, B, A, C, maxn)


def add_number(n):
    if n == 1:
        A.push(str(n))
        return
    A.push(str(n))
    add_number(n - 1)


def display(n):
    if n == 0:
        return
    else:
        print(
            f"{A.items[n-1] if A.size() >= n else '|'}  {B.items[n-1] if B.size() >= n else '|'}  {C.items[n-1] if C.size() >= n else '|'}"
        )
        display(n - 1)


n = int(input("Enter Input : "))
add_number(n)
# print(A)
move(n, A, B, C, n + 1)
display(n + 1)
