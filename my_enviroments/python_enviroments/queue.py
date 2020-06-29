class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.back = None

    def enqueue(self, value):
        newnode = Node(value)
        if self.front == None:
            self.front = newnode
            self.back = newnode
        else:
            self.back.next = newnode
            self.back = self.back.next
        return self

    def dequeue(self):
        if self.front == None:
            return None
        else:
            valtoreturn = self.front.val
            # frontToDequeue = self.front
            self.front = self.front.next
            # frontToDequeue.next = None
            return valtoreturn

    def front(self):
        if self.front != None:
            return self.front.value
        else:
            return None

    def contains(self, valueToFind):
        if self.front == None:
            return False
        else:
            runner = self.front
            while runner != None:
                if runner.value == valueToFind:
                    print("true")
                    return True
                else:
                    runner = runner.next
            print("false")
            return False

    def isEmpty(self):
        if self.front == None:
            return True
        else:
            return False

    def size(self):
        count = 0
        if self.front == None:
            return count
        else:
            runner = self.front
            while runner != None:
                count += 1
                runner = runner.next
            print(count)
            return count


class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        newnode = Node(value)
        if self.top == None:
            self.top = newnode
        else:
            newnode.next = self.top
            self.top = newnode
        return self

    def pop(self):
        if self.top != None:
            topvalue = self.top.value
            self.top = self.top.next
            # x = {
            #     'value': topvalue,
            #     'self': self
            # }

            return topvalue
        else:
            print("nothing to pop aka you got no pancakes")
            return self

    def size(self):
        count = 0
        if self.top == None:
            return count
        else:
            runner = self.top
            while runner != None:
                count += 1
                runner = runner.next

            return count


def compareStacks(stack1, stack2):

    if stack1.size() != stack2.size():
        return False
    else:
        runner1 = stack1.top
        runner2 = stack2.top
        while runner1 != None:
            if runner1.value != runner2.value:
                return False
            else:
                runner1 = runner1.next
                runner2 = runner2.next
        return True


def queueIsPal(someQueue):
    runner = someQueue.front
    array1 = []
    while runner != None:
        array1.append(runner.value)
        runner = runner.next
    for i in range(0, len(array1)//2, 1):
        temp = array1[0]
        if array1[i] != array1[len(array1)-1-i]:
            return False
    print(array1)
    return True


queue1 = Queue()
queue1.enqueue(5).enqueue(8).enqueue(18).enqueue(18).enqueue(8).enqueue(5)

print(queueIsPal(queue1))
