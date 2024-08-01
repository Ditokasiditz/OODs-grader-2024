# PSD48 (P-Saderd 48 Group) เป็นวงไอดอลวงหนึ่งที่กระแสกำลังมาแรง ณ ตอนนี้โดยเพลงที่ได้รับความนิยมอย่างมากคือเพลงจี่หอย โดยวง PSD48 กำลังจะจัดงานจับมือขึ้น โดยมีกฎอยู่ว่าถ้าหากคนที่กำลังต่อแถวอยู่เป็นคนจาก กองกำลังสำรวจ จะได้สิทธิพิเศษในการแทรกแถวไปข้างหน้าสุดทันที (แต่ถ้าหากคนหน้าสุดก็เป็นคนของกองกำลังสำรวจก็ต้องต่อหลังเขาอยู่ดี)  PSD48 อยากให้คุณช่วยเขียนโปรแกรมสำหรับหาว่าจะมีโอตะ id ใดบ้างที่ได้จับมือ

# เพลงประกอบ : https://youtu.be/Jd4Hd-HFgls

# Input :
# EN <value>  เป็นโอตะธรรมดา  id = value
# ES <value>  เป็นโอตะของกองกำลังสำรวจ  id = value
# D                  เป็นคำสั่งแสดงผล value ของหัวแถว ถ้าหากในแถวไม่มีคนจะแสดงคำว่า Empty


class Queue:
    def __init__(self):
        self.queue = []
        self.special_queue = []

    def enqueue(self, item, special=False):
        if special:
            self.special_queue.append(item)
        else:
            self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            if self.special_queue:
                return self.special_queue.pop(0)
            return self.queue.pop(0)
        return "Empty"

    def is_empty(self):
        return len(self.queue) == 0 and len(self.special_queue) == 0

    def display(self):
        if not self.is_empty():
            if self.special_queue:
                return self.special_queue[0]
            return self.queue[0]
        return "Empty"


def process_commands(commands):
    queue = Queue()
    results = []

    for command in commands:
        if command.startswith("EN"):
            _, value = command.split()
            queue.enqueue(value)
        elif command.startswith("ES"):
            _, value = command.split()
            queue.enqueue(value, special=True)
        elif command == "D":
            results.append(queue.dequeue())

    return results


input_commands = input("Enter Input : ").split(",")

results = process_commands(input_commands)


for result in results:
    print(result)
