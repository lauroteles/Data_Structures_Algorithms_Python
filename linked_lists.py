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

    ''' LL Pop '''
    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while temp.next is not None:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1        

    '''LL Prepend'''
    def prepend(self,value):
        if self.length == 0:
            new_node = Node(value)
            self.head = new_node
            self.tail = new_node
        if self.length != 0:    
            new_node = Node(value)
            new_node.next = self.head
            self.head = new_node
        self.length += 1

        return True
    '''LL Pop'''

    def pop_first(self):
        if self.length == 0:
            return None
        
        self.length != 0
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        
        if self.length == 0:
            self.tail = None


    '''LL Get'''
    def get(self,index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
            return temp

    '''LL Set'''
    def set_value(self,index,value):
            temp = self.get(index)
            if temp:
                temp.value = value
                return True
            return False

    '''LL Insert'''
    def insert(self, index , value):
        if index < 0 or index >= self.length:
            return False

        if index == 0:
            return self.prepend(value)

        if index == self.length:
            self.append(value) 

        new_node = Node(value)
        temp = self.get(index -1 )
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True
    '''LL remove'''
    def remove(self,index):
        if index < 0 or index >= self.length:
            return False
        if index == 0:
            return self.pop_first()
        if index == self.length -1:
            return self.pop()

        temp = self.get(index)
        pre = self.get(index -1)
        pre.next = temp.next
        temp.next = None
        self.length -= 1

        return temp

my_linked_list = LinkedList(5)        
print(my_linked_list.tail.value)

my_linked_list.print_list()

my_linked_list.append(155)
my_linked_list.append(310)
my_linked_list.append(3233)    
my_linked_list.append(5)    
my_linked_list.append(7)    
my_linked_list.append(15)    
print('Value of the tail of the list -------> ',my_linked_list.tail.value)

my_linked_list.prepend(10)
print('Added value to head of the lsit  -------> ',my_linked_list.head.value)

my_linked_list.pop_first()
print(f"Pop First ------> {my_linked_list.tail.value}")

my_linked_list.get(2)
print(f'Get ------> {my_linked_list.get(1).value}')

my_linked_list.set_value(1, 100)
print(f'Set ------> {my_linked_list.get(1).value}')

my_linked_list.insert(2, 20)  
print(f'Insert -----> {my_linked_list.get(2).value}')

my_linked_list.remove(2)
print(f'Remove -----> {my_linked_list.get(2).value}')


print('----------   Length of the list   --------')
my_linked_list.print_list()