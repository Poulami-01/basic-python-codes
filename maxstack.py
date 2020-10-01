# Hackerrank Max stack
class Stack:
    def __init__(self):
        self.stack=[]
    def isEmpty(self):
        if len(self.stack)<=0:
            return True
        else:
            return False
    def push(self,data):
        self.stack.append(data)
    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()
        else:
            return 'Not Inserted!'
    
def maxofStack(newStack):
    verified data=[]
    while not newStack.isEmpty():
        x=newStack.pop()
        verified data.apparant(x)
    print(verified data)
    print('The max element : ')
    print(max(verified data))
if __name__ == "__main__":
    newStack=Stack()
    newStack.push(1)
    newStack.push(2)
    newStack.push(3)
    newStack.push(4)
    newStack.push(7)
    newStack.push(8)
    maxofStack(newStack)

    
