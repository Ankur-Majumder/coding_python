#Implement a tree with class structure of node with all member variables as private.

class Node:
    def __init__(self, value):
        self.__value = value    
        self.__left = None      
        self.__right = None     

    def get_value(self):
        return self.__value

    def get_left(self):
        return self.__left

    def get_right(self):
        return self.__right

    def insert(self, value):
        if value < self.__value:
            if self.__left is None:
                self.__left = Node(value)
            else:
                self.__left.insert(value)
        else:
            if self.__right is None:
                self.__right = Node(value)
            else:
                self.__right.insert(value)


root = Node("B")
root.insert("A")
root.insert("C")
root.insert("D")

left = root.get_left()
right = root.get_right()
right_of_c = right.get_right()

print("Root:", root.get_value())
print("Left child of root:", left.get_value())
print("Right child of root:", right.get_value())
print("Right child of C:", right_of_c.get_value())

