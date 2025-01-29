class Node:
    def __init__(self,value):

        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None


    def insert(self,value):
        new_node = Node(value)
        if self.root == None:
            self.root = new_node
            return True
        temp = self.root
        while (True):
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left == None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right == None:
                    temp.right = new_node
                    return True  
                temp = temp.right


    def contains(self,value):

        temp = self.root

        while temp is not None:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True                
        return False


m_tree = BinaryTree()

m_tree.insert(10)
m_tree.insert(5)
m_tree.insert(15)


print(m_tree.root.value)
print(m_tree.root.left.value)
print( m_tree.root.right.value)

print(m_tree.contains(5))


        