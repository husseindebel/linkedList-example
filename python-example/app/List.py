
class Node:
    def __init__(self, item):
        self._next = None
        self._item = item 
    
    @property
    def item(self):
        return self._item 

    @property
    def next(self):
        return self._next 
    
    @next.setter
    def next(self, next_node):
        self._next = next_node 
    


class List:
    def __init__(self):
        self._head = None
        self._size = 0
    
    @property
    def is_empty(self):
        return self._head == None

    def add_item(self, item):
        new_node = Node(item)
        if self._head == None:
            self._head = new_node
        else:
            current = self._head
            while current.next != None:
                current = current.next
            
            current.next = new_node 
        self._size += 1
        return True


    def contains(self, item):
        current = self._head
        while current != None:
            if current.item == item:
                return True
            
            current = current.next
        
        return False
    
    @property
    def to_list(self):
        list_result = []
        current = self._head 
        while current != None:
            list_result.append(current.item)
            current = current.next
        return list_result
 

    @property
    def head(self):
        return self._head
    
    @property
    def size(self):
        return self._size