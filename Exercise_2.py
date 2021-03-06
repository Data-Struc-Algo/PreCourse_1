# Time Complexity: O(n)
# Space Complexity: O(1)

class Node:
    def __init__(self, data):
       self.data = data
       self.next = None
 
class Stack:
    def __init__(self):
        self.head = Node(float("inf"))
        
    def push(self, data):
        curr = self.head
        while curr.next != None:
            curr = curr.next
        new_node = Node(data)
        curr.next = new_node
        
        return   
        
        
    def pop(self):
        curr = self.head
        while curr.next.next != None:
            curr = curr.next
        elem = curr.next.data
        curr.next = None
        return elem


# Implement Stack using Linked List.

a_stack = Stack()
while True:
    print('push <value>')
    print('pop')
    print('quit')
    do = input('What would you like to do? ').split()
 
    operation = do[0].strip().lower()
    if operation == 'push':
        a_stack.push(int(do[1]))
    elif operation == 'pop':
        popped = a_stack.pop()
        if popped is None:
            print('Stack is empty.')
        else:
            print('Popped value: ', int(popped))
    elif operation == 'quit':
        break
