"""Task 1, Program 2"""
from task1 import *

def get_sum(first, second):
    """Adds two lists"""
    lst1 = number_to_list(first)
    lst2 = number_to_list(second)
    summ = LinkedList()
    min_length = min(lst1.length, lst2.length)
    max_length = max(lst1.length, lst2.length)
    carry_flag = 0
    cur_node1 = lst1.head_node
    cur_node2 = lst2.head_node
    i = 0
    while i < min_length:
        summ.insert_node((cur_node1.data + cur_node2.data + carry_flag) % 10)
        if (cur_node1.data + cur_node2.data + carry_flag) > 9:
            carry_flag = 1
        else:
            carry_flag = 0
        cur_node1 = cur_node1.next_node
        cur_node2 = cur_node2.next_node
        i += 1
    if cur_node1 != None:
        cur_node = cur_node1
    elif cur_node2 != None:
        cur_node = cur_node2
    else:
        if carry_flag:
            summ.insert_node(carry_flag)
        return summ
    for i in range(min_length, max_length):
        summ.insert_node(cur_node.data + carry_flag)
        carry_flag = 0
        cur_node = cur_node.next_node
    return summ

if __name__ == '__main__':
    print("Input 2 numbers to add:")
    first_add = input()
    second_add = input()
    s = get_sum(first_add, second_add)
    print("The sum is:")
    s.print_list()
