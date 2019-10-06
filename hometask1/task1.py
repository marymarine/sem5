"""Task 1, Program 1"""
class Node(object):
    """Describes node of list: data and link to next node"""
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        """Get data value of node"""
        return self.data

    def get_next(self):
        """Get next_node of node"""
        return self.next_node

    def set_next(self, new_next):
        """Set next_node as new_next"""
        self.next_node = new_next

class LinkedList(object):
    """Describes linked list - a sequence of nodes, started with head_node"""
    def __init__(self, head_node=None):
        self.head_node = head_node
        self.length = 0

    def insert_node(self, data):
        """Insert node data to the end of list"""
        #insert to the top
        #new_node = Node(data)
        #new_node.set_next(self.head_node)
        #self.head_node = new_node

        #insert to the end
        self.length += 1
        if self.head_node is None:
            self.head_node = Node(data)
        else:
            new_node = Node(data)
            cur_node = self.head_node
            while cur_node.next_node:
                cur_node = cur_node.next_node
            cur_node.set_next(new_node)

    def search_node(self, data):
        """Search node data in list, return this node"""
        cur_node = self.head_node
        is_found = False
        while cur_node and is_found is False:
            if cur_node.data == data:
                is_found = True
            else:
                cur_node = cur_node.next_node
        return cur_node

    def delete_node(self, data):
        """Delete node data from list"""
        #delete the first occurrence of data
        cur_node = self.head_node
        pre_node = None
        is_found = False
        while cur_node and is_found is False:
            if cur_node.get_data() == data:
                is_found = True
            else:
                pre_node = cur_node
                cur_node = cur_node.get_next()
        if cur_node is None:
            raise ValueError("Data is not found")
        if pre_node is None:
            self.head_node = cur_node.get_next()
        else:
            pre_node.set_next(cur_node.get_next())

    def print_list(self):
        """Print list as a sequence of data"""
        cur_node = self.head_node
        while cur_node:
            print(cur_node.data, end=' ')
            cur_node = cur_node.next_node

def number_to_list(num):
    """Transform string to list"""
    num_lst = LinkedList()
    while num != '':
        char = num[len(num)-1]
        num = num[0:len(num)-1]
        num_lst.insert_node(int(char))
    return num_lst

if __name__ == '__main__':
    print("Input number:")
    number = input()
    lst = number_to_list(number)
    print("Entered list:")
    lst.print_list()
    print("\nInput digit to search:")
    search_key = int(input())
    searched_node = lst.search_node(search_key)
    if searched_node:
        print("This value is found")
    else:
        print("This value is not found")
    print("Input digit to delete:")
    del_key = int(input())
    lst.delete_node(del_key)
    print("New list:")
    lst.print_list()
