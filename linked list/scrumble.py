class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, str(self.head.value) + " "
        while cur.next != None:
            s += str(cur.next.value) + " "
            cur = cur.next
        return s

    def isEmpty(self):
        return self.head == None

    def append(self, item):
        new_node = Node(item)
        if self.head == None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next != None:
                cur = cur.next
            cur.next = new_node

    def addHead(self, item):
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node

    def search(self, item):
        cur = self.head
        while cur != None:
            if cur.value == item:
                return cur
            cur = cur.next
        return None

    def index(self, item):
        cur = self.head
        idx = 0
        while cur != None:
            if cur.value == item:
                return idx
            cur = cur.next
            idx += 1
        return -1

    def size(self):
        size = 0
        cur = self.head
        while cur != None:
            cur = cur.next
            size += 1
        return size

    def pop(self, pos):
        if self.isEmpty() or pos < 0 or pos >= self.size():
            return "Out of Range"

        if pos == 0:
            removed_value = self.head.value
            self.head = self.head.next
        else:
            prev = None
            cur = self.head
            count = 0
            while cur != None and count < pos:
                prev = cur
                cur = cur.next
                count += 1
            removed_value = cur.value
            prev.next = cur.next

        return "Success"

    def bottom_up(self, pos, size):
        if self.isEmpty() or pos < 0 or pos >= self.size():
            return None
        else:
            cur = self.head
            count = 0
            while cur is not None and count < pos - 1:
                cur = cur.next
                count += 1

            new_head = cur.next
            cur.next = None

            cur = new_head
            while cur.next is not None:
                cur = cur.next

            cur.next = self.head
            self.head = new_head

    def de_bottom_up(self, pos, size):
        if self.isEmpty() or pos < 0 or pos >= self.size():
            return None
        else:
            cur = self.head
            count = 0
            while cur is not None and count < pos - 1:
                cur = cur.next
                count += 1

            new_head = cur.next
            cur.next = None

            cur = new_head
            while cur.next is not None:
                cur = cur.next

            cur.next = self.head
            self.head = new_head

    def riffle(self, pos, size):
        if self.isEmpty() or pos < 0 or pos >= self.size():
            return None

        else:
            list1 = LinkedList()
            list2 = LinkedList()

            cur = self.head
            count = 0
            while cur is not None and count < pos - 1:
                cur = cur.next
                count += 1

            list2.head = cur.next
            cur.next = None

            list1.head = self.head
            self.head = None

            cur1 = list1.head
            cur2 = list2.head

            while cur1 is not None and cur2 is not None:
                self.append(cur1.value)
                self.append(cur2.value)
                cur1 = cur1.next
                cur2 = cur2.next

            while cur1 is not None:
                self.append(cur1.value)
                cur1 = cur1.next

            while cur2 is not None:
                self.append(cur2.value)
                cur2 = cur2.next

    def de_riffle(self, pos, size):
        if self.isEmpty() or pos < 0 or pos >= self.size():
            return None

        else:
            if pos < size / 2:
                pull_out = pos - 1
            elif pos >= size / 2:
                pull_out = size - pos

            list1 = LinkedList()
            cur = self.head
            while cur is not None:
                if cur.next is not None and list1.size() < pull_out:
                    list1.append(cur.next)
                    cur.next = cur.next.next
                cur = cur.next

            if list1.isEmpty():
                return None

            cur = list1.head
            while cur.next is not None:
                cur = cur.next
            cur.next = None

            if pos < size / 2:
                cur = self.head
                count = 0
                while cur is not None and count < pos - 1:
                    cur = cur.next
                    count += 1

                search_cur = cur

                cur = list1.head
                while cur.next is not None:
                    cur = cur.next

                cur.next = search_cur.next
                search_cur.next = list1.head
            elif pos >= size / 2:
                cur = self.head
                while cur.next is not None:
                    cur = cur.next
                cur.next = list1.head


def createLL(LL):
    linked_list = LinkedList()
    for l in LL:
        linked_list.append(l)
    return linked_list


def printLL(head):
    return head


def SIZE(head):
    return head.size()


def scarmble(head, b, r, size):
    pos_b, pos_r = int(b / 100 * size), int(r / 100 * size)
    head.bottom_up(pos_b, size)
    print(f"BottomUp {b:.3f} % : {head}")
    head.riffle(pos_r, size)
    print(f"Riffle {r:.3f} % : {head}")
    head.de_riffle(pos_r, size)
    print(f"Deriffle {r:.3f} % : {head}")
    head.de_bottom_up(size - pos_b, size)
    print(f"Debottomup {b:.3f} % : {head}")


inp1, inp2 = input("Enter Input : ").split("/")
print("-" * 50)
h = createLL(inp1.split())
for i in inp2.split("|"):
    print("Start : {0}".format(printLL(h)))
    k = i.split(",")
    if k[0][0] == "B" and k[1][0] == "R":
        scarmble(h, float(k[0][2:]), float(k[1][2:]), SIZE(h))
    elif k[0][0] == "R" and k[1][0] == "B":
        scarmble(h, float(k[1][2:]), float(k[0][2:]), SIZE(h))
    print("-" * 50)
