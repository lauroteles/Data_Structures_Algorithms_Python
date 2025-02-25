class Node:
    def __init__(self,value):

        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def __r_contains(self, current_node, value):
        if current_node == None:
            return False
        if value == current_node.value:
            return True
        if value < current_node.value:
            return self.__r_contains(current_node.left, value)
        if value > current_node.value:
            return self.__r_contains(current_node.right, value)
        
    def r_contains(self, value ):
        return self.__r_contains(self.root, value)

    def __r_insert(self, current_node, value):
        if current_node == None:
            return Node(value)
        
        if value < current_node.value:  
            if current_node.left is None:
                current_node.left = Node(value) 
            else:
                self.__r_insert(current_node.left, value)
        elif value > current_node.value:
            if current_node.right is None:
                current_node.right = Node(value) 
            else:
                self.__r_insert(current_node.right, value)
        
        return current_node
        

    def r_insert(self,value):
        if self.root == None:
            self.root = Node(value)         
        self.__r_insert(self.root, value)



print("Recursive Binary Tree")
print("Inserting 10, 5, 15")
match_tree = BinaryTree()
match_tree.r_insert(10)
match_tree.r_insert(5)
match_tree.r_insert(15)
print(match_tree.root.value)
print(match_tree.root.left.value)
print(match_tree.root.right.value)


