class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class Stack:
  def __init__(self):
    self.head = None
    
 #pushing value into the stack
  def push(self, data) -> None:
    new_node=Node(data)
    new_node.next=self.head
    self.head=new_node
    
#if head is connected with some node, to remove the node we will change the head to the next node.
  def pop(self) -> None:
     if self.head is not None:
      self.head = self.head.next
      
  def status(self):
    #It prints all the elements of stack.
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
