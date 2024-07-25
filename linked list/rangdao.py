class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

    def __str__(self):
        return str(self.data)


class List:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, data):
        new = Node(data)

        the_node = self.head
        if the_node == None:
            self.head = new
            self.tail = new
        else:
            new.prev = self.tail
            self.tail.next = new
            self.tail = new  # update tailer (swift)
        self.size += 1

    def head_insert(self, data):
        new = Node(data)

        the_node = self.head
        if the_node == None:
            self.head = new
            self.tail = new
        else:
            new.next = self.head
            self.head.prev = new
            self.head = new  # update header
        self.size += 1

    def isEmpty(self):
        return self.head == None

    def __str__(self):
        text = ""
        the_node = self.head
        while the_node != None:
            text += str(the_node)
            the_node = the_node.next
            if the_node != None:
                text += "->"
        return text


stations = List()
f_route, b_route = List(), List()
print("***Railway on route***")
command = list(
    data.split(",")
    for data in input(
        "Input Station name/Source, Destination, Direction(optional): "
    ).split("/")
)

for st in command[0]:
    stations.append(st)
source = command[1][0]
dest = command[1][1]
try:
    direct = command[1][2]
except IndexError:
    direct = "FB"

if "F" in direct:
    train = stations.head
    # go to start station
    while train.data != source:
        train = train.next
    f_route.append(train.data)
    # move until terminal station
    while train.data != dest:
        if train.next != None:
            train = train.next
            f_route.append(train.data)
        else:
            train = stations.head
            f_route.append(train.data)
            break
    # turn direction and move until dest
    while train.data != dest:
        if train.next != None:
            train = train.next
            f_route.append(train.data)
        else:  # not found destination
            break

if "B" in direct:
    train = stations.head

    while train.data != source:
        train = train.next
    b_route.append(train.data)

    while train.data != dest:
        if train.prev != None:
            train = train.prev
            b_route.append(train.data)
        else:
            train = stations.tail
            b_route.append(train.data)
            break

    while train.data != dest:
        if train.prev != None:
            train = train.prev
            b_route.append(train.data)
        else:
            break

if (b_route.isEmpty() and not f_route.isEmpty()) or 0 < f_route.size <= b_route.size:
    print(f"Forward Route: {f_route},{f_route.size - 1}")
if (f_route.isEmpty() and not b_route.isEmpty()) or 0 < b_route.size <= f_route.size:
    print(f"Backward Route: {b_route},{b_route.size - 1}")
