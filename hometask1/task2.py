from task1 import *

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

if __name__ == '__main__':
    print("Input 2 numbers to add:")
    first = input()
    second = input()
    sum = get_sum(first, second)
    print("The sum is:")
    sum.print_list()
