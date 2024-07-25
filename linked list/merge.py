class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)


# insert at tail
class List:
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, data):
        new = Node(data)

        the_node = self.head
        if the_node == None:
            self.head = new
        else:
            while the_node.next != None:
                the_node = the_node.next
            the_node.next = new
            self.size += 1

    def pop(self):
        if self.head is None:
            return
        if self.head.next is None:
            last_val = self.head.data
            self.head = self.head.next
            self.size -= 1
            return last_val
        else:
            the_node = self.head
            while the_node.next.next is not None:
                the_node = the_node.next
            last_val = the_node.next.data
            the_node.next = the_node.next.next
            self.size -= 1
            return last_val

    def isEmpty(self):
        return self.head == None

    def __str__(self):
        text = ""
        the_node = self.head
        while the_node != None:
            text += str(the_node) + " "
            the_node = the_node.next
        return text


a = List()
L1 = List()
L2 = List()

command = list(data.split("->") for data in input("Enter Input (L1,L2) : ").split(" "))

for data in command[0]:
    L1.append(data)
for data in command[1]:
    L2.append(data)

print(f"L1    : {L1}")
print(f"L2    : {L2}")

while not L2.isEmpty():
    num = L2.pop()
    L1.append(num)

print(f"Merge : {L1}")
