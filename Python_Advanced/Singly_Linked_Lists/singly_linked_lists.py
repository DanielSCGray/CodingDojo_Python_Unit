class SLNode:
    def __init__(self, val) -> None:
        self.value = val
        self.next = None

class SList:
    def __init__(self) -> None:
        self.head = None

    def add_to_front(self, val):
        new_node = SLNode(val)
        current_head = self.head
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
        new_node = SLNode(val)
        runner = self.head
        while runner.next !=None:
            runner = runner.next
        runner.next = new_node
        return self
    
    def remove_from_front(self):
        if self.head == None:
            print('list is empty')
            return self
        temp = self.head
        self.head = temp.next
        return self

    def remove_from_back(self):
        if self.head == None:
            print('list is empty')
            return self
        runner = self.head
        while runner.next != None:
            runner = runner.next
        last_node = runner
        runner = self.head
        while runner.next != last_node:
            runner = runner.next
        runner.next = None
        return self
    
    def remove_val(self, val):
        if self.head == None:
            print('list is empty')
            return self
        if self.head.value == val:
            self.remove_from_front()
            return self
        runner = self.head
        while runner != None:
            if runner.value == val:
                break
            runner = runner.next
        if runner == None:
            print('value not found')
            return self
        node_to_remove = runner
        next_link = runner.next
        runner.next = None
        runner = self.head
        while runner.next != node_to_remove:
            runner = runner.next
        runner.next = next_link
        return self

    def insert_at(self, val, n):
        if n == 0 or n == 1:
            self.add_to_front(val)
            return self
        counter = 1
        runner = self.head
        while runner.next != None:
            if counter == n - 1:
                break
            runner = runner.next
            counter += 1
        if runner.next == None:
            self.add_to_back(val)
            return self
        insert_node = runner
        next_link = runner.next
        new_node = SLNode(val)
        insert_node.next = new_node
        new_node.next = next_link
        return self

        


#Testing
my_list = SList()

# print(my_list.head)

my_list.add_to_front(3)
# my_list.print_values()
my_list.add_to_front(2)
my_list.add_to_back(4)
my_list.add_to_front(1)
my_list.add_to_back(5)
my_list.print_values()
# my_list.remove_from_front()
# my_list.print_values()
# my_list.remove_from_back()
# my_list.print_values()
my_list.remove_val(3)
my_list.print_values()
my_list.remove_val(3)
my_list.insert_at(3,3).print_values()