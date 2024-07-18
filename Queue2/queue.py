
class Queue:

    def __init__(self,list = None):
        if list == None:
            self.item = []
        else :
            list.item = list 

    def deQueue(self):
        return self.item.pop(0)

    def enQueue(self,ele):
        self.item.append(ele)

    def isEmpty(self):
        return self.item == []

    def size(self):
        return len(self.item)
    



