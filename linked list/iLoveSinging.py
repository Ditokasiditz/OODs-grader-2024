class Node:

    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class LinkList:
    def __init__(self):
        self.head = None
        self.size = 0

    def appendHead(self, value):
        node = Node(value, self.head)
        self.head = node

    def appendLast(self, value):
        if self.head is None:
            self.appendHead(value)
        else:
            q = self.head
            while q.next != None:
                q = q.next
            p = Node(value)
            q.next = p

    def removeLast(self):
        if self.head == None:
            return "Error!!!"
        if self.head.next == None:
            self.head = None
            self.size -= 1
        else:
            p = self.head
            while p.next.next != None:
                p = p.next
            p.next = p.next.next
            self.size -= 1

    def rename(self, newName):
        if self.head == None:
            return "Error!!!"
        else:
            p = self.head
            while p.next != None:
                p = p.next
            p.value = newName

    def printList(self):
        if self.head == None:
            print("LinkedList is empty!")
        else:
            p = self.head
            while p.next != None:
                print(p.value, end=" -> ")
                p = p.next
            print(p.value)

    def printListWithNoDuplicate(self):
        p = self.head
        item_list = []
        while p.next != None:
            item_list.append(p.value)
            p = p.next
        item_list.append(p.value)

        noDup_list = []
        [noDup_list.append(x) for x in item_list if x not in noDup_list]

        for i in noDup_list[:-1]:
            print(i, end=" -> ")
        print(noDup_list[-1])


def convertToLinkList(ls):
    linklist = LinkList()
    for ele in ls:
        linklist.appendLast(ele)
    return linklist


print("*** My Favourite Keynote ***")

inputl = input("Enter Input / List of operation : ").split("/")

listSong = [ele for ele in inputl[0].strip().split(" ")]

operations = [ele for ele in inputl[1].strip().split(", ")]


myLinkList = convertToLinkList(listSong)

myLinkList.printList()
for ele in operations:
    if ele[0] == "D":
        myLinkList.removeLast()
    elif ele[0] == "A":
        myLinkList.appendLast(ele[2:])
    elif ele[0] == "R":
        myLinkList.rename(ele[2:])

myLinkList.printList()

myLinkList.printListWithNoDuplicate()
