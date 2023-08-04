class DLNode:
    def __init__(self, val) -> None:
        self.value = val
        self.next = None
        self.prev = None

class DList:
    def __init__(self) -> None:
        self.head = None
    
    def add_to_front(self, val):
        new_node = DLNode(val)
        current_head = self.head
        if current_head:
            current_head.prev = new_node
        new_node.next = current_head
        self.head = new_node
        return self
    
    def print_values(self):
        runner = self.head
        while runner != None:
            print(runner.value)
            runner = runner.next
        return self
    
    def add_to_back(self, val):
        if self.head == None:
            self.add_to_front(val)
            return self
        new_node = DLNode(val)
        runner = self.head
        while runner.next !=None:
            runner = runner.next
        runner.next = new_node
        new_node.prev = runner
        return self

    def remove_from_front(self):
        if self.head == None:
            print('list is empty')
            return self
        if self.head.next == None:
            self.head = None
            return self
        temp = self.head
        new_head = temp.next
        self.head = new_head
        
        return self
    # not working
my_list = DList()

my_list.add_to_front(3).print_values().add_to_front(4).print_values().remove_from_front().print_values()
