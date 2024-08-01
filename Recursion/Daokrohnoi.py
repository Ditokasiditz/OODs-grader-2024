# นักศึกษาจะได้รับ Input เป็น list<int> ของดาวเคราะห์น้อย
# สำหรับดาวเคราะห์น้อยแต่ละดวงนั้น ค่าสัมบูรณ์ จะแสดงขนาดของมัน และเครื่องหมายแสดงถึงทิศทางของมัน (ถ้าเลขเป็นบวกแสดงว่าวิ่งไปทางขวา ,ลบทางซ้าย) โดยที่ดาวเคราะห์น้อยแต่ละดวงเคลื่อนที่ด้วยความเร็วเท่ากัน

# ค้นหาสถานะของดาวเคราะห์น้อยหลังจากการชนกันทั้งหมด

# 1.หากดาวเคราะห์น้อยสองดวงมาพบกันดวงที่เล็กกว่าจะระเบิด

# 2.ถ้าทั้งสองมีขนาดเท่ากันทั้งคู่จะระเบิด

# 3.ดาวเคราะห์น้อยสองดวงที่เคลื่อนที่ไปในทิศทางเดียวกันจะไม่มีวันพบกัน

# ****ห้ามใช้คำสั่ง for, while, do while*****


# หมายเหตุ ฟังก์ชันมี parameter ได้ไม่เกิน 2 ตัว
def asteroid_collision(asts):
    def collide(stack, asts):
        if not asts:
            return stack
        asteroid = asts[0]
        if not stack or asteroid > 0 or stack[-1] < 0:
            return collide(stack + [asteroid], asts[1:])
        elif stack[-1] == -asteroid:
            return collide(stack[:-1], asts[1:])
        elif stack[-1] > -asteroid:
            return collide(stack, asts[1:])
        else:
            return collide(stack[:-1], asts)

    return collide([], asts)


x = input("Enter Input : ").split(",")
x = list(map(int, x))
print(asteroid_collision(x))
