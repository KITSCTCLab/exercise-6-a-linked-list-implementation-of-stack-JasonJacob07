class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class Stack:
  def __init__(self):
    self.head = None
    
  def push(self, data) -> None: #pushing value into the stack by using head pointer
    new_node=Node(data)
    new_node.next=self.head
    self.head=new_node
    
  def pop(self) -> None: #removing value from the stack by changing the position of head pointer
     if self.head is not None:
      self.head = self.head.next
      
  def status(self):#It prints all the elements of stack.
    temp = self.head
    while temp is not None:
      print (temp.data, end="=>")
      temp = temp.next
    print (None)

stack = Stack()
operations = []
for specific_operation in input().split(','):
    operations.append(specific_operation.strip())
input_data = input()
data = input_data.split(',')
for i in range(len(operations)):
  if operations[i] == "push":
    stack.push(int(data[i]))
  elif operations[i] == "pop":
    stack.pop()
stack.status()
