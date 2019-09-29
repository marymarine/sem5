class Node(object):
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_next(self, newNext):
        self.next = newNext

class LinkedList(object):
    def __init__(self, headNode=None):
        self.headNode = headNode
        self.length = 0

    def insert_node(self, data):
        #insert to the top
        #newNode = Node(data)
        #newNode.set_next(self.headNode)
        #self.headNode = newNode

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

    def search_node(self, data):
        currNode = self.headNode
        isFound = False
        while(currNode and isFound is False):
            if currNode.data == data:
                isFound = True
            else:
                currNode = currNode.next
        return currNode

    def delete_node(self, data):
        #delete the first occurrence of data
        currNode = self.headNode
        preNode = None
        isFound = False
        while currNode and isFound is False:
            if currNode.get_data() == data:
                isFound = True
            else:
                preNode = currNode
                currNode = currNode.get_next()
        if currNode is None:
            raise ValueError("Data is not found")
        if preNode is None:
            self.headNode = currNode.get_next()
        else:
            preNode.set_next(currNode.get_next())

    def print_list(self):
        currNode = self.headNode
        while currNode:
            #print(currNode.data, end=' ')
            currNode = currNode.next

def number_to_list(number):
    lst = LinkedList()
    while number != '':
        char = number[len(number)-1]
        number = number[0:len(number)-1]
        lst.insert_node(int(char))
    return lst

#main
print("Input number:")
number = input()
lst = number_to_list(number)
print("Entered list:")
lst.print_list()
print("\nInput digit to search:")
searchKey = int(input())
currNode = lst.search_node(searchKey)
if currNode:
    print("This value is found")
else:
    print("This value is not found")
print("Input digit to delete:")
delKey = int(input())
lst.delete_node(delKey)
print("New list:")
lst.print_list()
