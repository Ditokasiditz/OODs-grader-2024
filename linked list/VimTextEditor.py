# Chapter : 5 - item : 4 - VIM Text Editor

# กฤษฎาได้มีไอเดียสุดบรรเจิดคือการสร้างโปรแกรม Text Editor แบบ VIM ขึ้นมาใช้งานเอง
# โดยโปรแกรมนี้จะมีอยู่แค่ 1 Mode คือ Command Mode (inputของเรานั่นแหละ) โดยจะมีคำสั่งอยู่ 5 แบบ คือ
# Insert (I) , Left (L) , Right (R) , Backspace (B) และ Delete (D)
# (โดยความสามารถของคำสั่งต่างๆจะอธิบายด้านล่าง) แต่กฤษฎาไม่มีความสามารถทางด้านการสร้างโปรแกรมเลย
# กฤษฎาจึงได้มาขอร้องน้องๆที่เรียนอยู่วิศวกรรมคอมพิวเตอร์ ให้ช่วยสร้างโปรแกรม Text Editor
# ที่กฤษฎาต้องการให้หน่อย โดยผลลัพธ์ให้แสดงออกมาเป็น word ที่เหลืออยู่จาก Command ที่เราใส่ลงไป
# พร้อมกับตำแหน่งของ Cursor

# ***** อธิบาย Input 5 แบบ *****

# 1.  I <word > :   เป็นการนำ word ลงไปใส่ในตำแหน่งของ Cursor ปัจจุบัน หลังจากใส่ word
# เสร็จ ตำแหน่งของ Cursor จะมาอยู่ด้านหลังของ word ที่ใส่ลงไป

# 2.  L :   เป็นการเลื่อน Cursor จากตำแหน่งปัจจุบันไปทางด้านซ้าย 1 ตำแหน่ง
# หากอยู่ทางซ้ายสุดอยู่แล้วจะไม่เกิดผลอะไร

# 3.  R :   เป็นการเลื่อน Cursor จากตำแหน่งปัจจุบันไปทางด้านขวา 1 ตำแหน่ง
#  หากอยู่ทางขวาสุดอยู่แล้วจะไม่เกิดผลอะไร

# 4.  B :   เป็นการลบ word 1 ตัวทางด้านซ้ายของ Cursor หากอยู่ทางซ้ายสุดอยู่แล้วจะไม่เกิดผลอะไร

# 5.  D :   เป็นการลบ word 1 ตัวทางด้านขวาของ Cursor หากอยู่ทางขวาสุดอยู่แล้วจะไม่เกิดผลอะไร


class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

    def __str__(self) -> str:
        return f"{self.data}"


class LinkedList:
    def __init__(self):
        self.head = None


start_node = Node("|")
position = start_node

inp = input("Enter Input : ").split(",")

for section in inp:
    try:
        action, word = section.split(" ")
    except:
        action = section

    if action == "I":
        # print(word)
        n = Node(word)
        if position.prev:
            position.prev.next = n
            n.prev = position.prev
        position.prev = n
        n.next = position

    elif action == "L":
        if position.prev and position.prev.prev:
            a = position.prev.prev
            b = position.prev
            c = position
            d = position.next
            a.next = c
            c.prev = a
            c.next = b
            b.prev = c
            b.next = d
        elif position.prev and not position.prev.prev:
            a = position.prev
            b = position
            c = position.next
            a.next = c
            b.prev = None
            b.next = a
            a.prev = b
    elif action == "R":
        if position.next and position.next.next and position.prev:
            a = position.prev
            b = position
            c = position.next
            d = position.next.next
            a.next = c
            c.prev = a
            c.next = b
            b.prev = c
            b.next = d
            d.prev = b
        elif position.next and not position.next.next and position.prev:
            a = position.prev
            b = position
            c = position.next
            a.next = c
            c.prev = a
            c.next = b
            b.prev = c
            b.next = None
        elif position.next and position.next.next and not position.prev:
            a = position
            b = position.next
            c = position.next.next
            a.next = c
            c.prev = a
            b.next = a
            b.prev = None
            a.prev = b
        elif position.next and not position.next.next and not position.prev:
            a = position
            b = position.next
            a.prev = b
            a.next = None
            b.next = a
            b.prev = None

    elif action == "B":
        if position.prev and position.prev.prev:
            a = position.prev.prev
            b = position.prev
            c = position
            d = position.next
            a.next = c
            c.prev = a
        elif position.prev and not position.prev.prev:
            a = position.prev
            b = position
            c = position.next
            b.prev = None
            a.next = None
    elif action == "D":
        if position.next and position.next.next:
            b = position
            c = position.next
            d = position.next.next
            b.next = d
            d.prev = b
            c.prev = None
            c.next = None
        elif position.next and not position.next.next:
            b = position
            c = position.next
            b.next = None
            c.prev = None
    # print(position.prev , position.next)


while position.prev:
    position = position.prev

s = []
while position:
    s.append(position.data)
    position = position.next
print(" ".join(s))
