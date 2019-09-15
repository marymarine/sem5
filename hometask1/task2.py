class Node(object):
    def __init__(self, data= None, next = None):
        self.data = data
        self.next = next

    def set_next(self, newNext):
        self.next = newNext

class LinkedList(object):
    def __init__(self, headNode = None):
        self.headNode = headNode
        self.length = 0

    def insert_node(self, data):
        #insert to the end
        self.length += 1
        if self.headNode == None:
            self.headNode = Node(data)
        else:
            newNode = Node(data)
            currNode = self.headNode
            while currNode.next:
                currNode = currNode.next
            currNode.set_next(newNode)

    def print_list(self):
            currNode = self.headNode
            while currNode:
                print(currNode.data, end=' ')
                currNode = currNode.next

def number_to_list(number):
    lst = LinkedList()
    while number != 0:
        digit = number % 10
        number //= 10
        lst.insert_node(digit)
    return lst

def get_sum(first, second):
    lst1 = number_to_list(first)
    lst2 = number_to_list(second)
    sum = LinkedList()
    minLength = min(lst1.length, lst2.length)
    maxLength = max(lst1.length, lst2.length)
    carryFlag = 0
    currNode1 = lst1.headNode
    currNode2 = lst2.headNode
    for i in range(minLength):
        sum.insert_node((currNode1.data + currNode2.data + carryFlag) % 10)
        if (currNode1.data + currNode2.data + carryFlag) > 9:
            carryFlag = 1
        else:
            carryFlag = 0
        currNode1 = currNode1.next
        currNode2 = currNode2.next
    if currNode1 != None:
        currNode = currNode1
    elif currNode2 != None:
        currNode = currNode2
    else:
        if carryFlag:
            sum.insert_node(carryFlag)
        return sum
    for i in range(minLength, maxLength):
        sum.insert_node(currNode.data + carryFlag)
        carryFlag = 0
        currNode = currNode.next
    return sum

#main
print("Input 2 numbers to add:")
first = int(input())
second = int(input())
sum = get_sum(first, second)
print("The sum is:")
sum.print_list()
