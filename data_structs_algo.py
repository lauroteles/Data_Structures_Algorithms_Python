'''Big O structures'''

''' O(n)'''
def print_items(n):
    for i in range(n):
        print(i)


''' O(n^2)'''

def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i,j)


'''0(1)'''
def add_items(n):
    return n + n




''' LL(Linked List)'''


''' Constructo'''
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1



    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next


    '''LL Append'''

    def append(self,value):
        
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node    

        self.length += 1

        return True


my_linked_list = LinkedList(5)        
print(my_linked_list.tail.value)
my_linked_list.print_list()
my_linked_list.append(3)    
print(my_linked_list.tail.value)


