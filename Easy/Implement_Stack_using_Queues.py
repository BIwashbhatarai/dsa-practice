from collections import deque
class MyStack(object):

    def __init__(self):
        self.stack = deque()

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        if not self.stack:
            return None
        return self.stack.pop()
        

    def top(self):
        if not self.stack:
            return None
        return self.stack[-1]
        

    def empty(self):
        return len(self.stack) == 0
        


obj = MyStack()
obj.push(5)
param_2 = obj.pop()
param_3 = obj.top()
param_4 = obj.empty()

