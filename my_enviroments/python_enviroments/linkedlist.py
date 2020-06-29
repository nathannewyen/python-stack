class Node:
    def __init__(self, valueInput):
        self.value = valueInput
        self.next = None


class SLL:
    def __init__(self):
        self.head = None

    def append(self, value):
        newnode = Node(value)
        if self.head == None:
            self.head = newnode
        else:
            # runner is created to have a variable i can use to iterate to singly linked list
            runner = self.head
            # use a while loop to iterate
            # print(runner.next) #this would print a node object
            while runner.next != None:
                runner = runner.next
            runner.next = newnode
        return self

    def display(self):
        print(self.head)
        runner = self.head
        outputstr = ""
        while runner != None:
            outputstr += f"{runner.value}-->"
            runner = runner.next

        print(outputstr)
        return self

    def addtoFront(self, value):
        newnode = Node(value)
        newnode.next = self.head
        self.head = newnode
        return self

    def contains(self, valueToFind):
        if self.head == None:
            return False
        else:
            runner = self.head
            while runner != None:
                if runner.value == valueToFind:
                    print("true")
                    return True
                else:
                    runner = runner.next
            print("false")
            return False

    def removefront(self):
        if self.head == None:
            return self
        else:
            self.head = self.head.next
            return self

    def removeback(self):
        if self.head == None:
            return self
        if self.head.next == None:
            self.head = None
            return self
        else:
            runner = self.head
            while runner.next.next != None:
                runner = runner.next
            runner.next = None
            return self

    def movemintofront(self):
        minval = self.head.value
        rnr = self.head
        while rnr.next != None:
            if rnr.next.value < minval:
                minval = rnr.next.value
                nodeBeforeMin = rnr
                minNode = rnr.next
            rnr = rnr.next
        nodeBeforeMin.next = nodeBeforeMin.next.next
        minNode.next = self.head
        self.head = minNode
        return self

    def appendVal(self, value, valueToFind):
        newNode = Node(value)
        # If nothing in list
        if self.head == None:
            self.head = newNode
        runner = self.head
        while runner.next != None:
            if runner.next == valueToFind:
                newnode.next = runner.next
                runner.next = newNode
                return self
            else:
                runner = runner.next
        runner.next = newNode
        return self

    # def movemaxtoback(self):
    #     maxval = self.head.value
    #     runner = self.head
    #     while runner.next != None:
    #         if runner.next.value > maxval:
    #             maxval = runner.next.value
    #             nodeBeforeMax = runner
    #             maxNode = runner.next
    #         runner = runner.next
    #     nodeBeforeMax.next = nodeBeforeMax.next.next

    #     print(maxNode.value, nodeBeforeMax.value)
    #     return self


sll1 = SLL()
sll1.append(5).append(10).append(6).append(
    2).appendVal(6, 5).display()

list2 = SLL()
list2.append(8)
