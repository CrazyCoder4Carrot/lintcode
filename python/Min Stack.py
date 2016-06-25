import sys
class MinStack(object):

    def __init__(self):
        # do some intialize if necessary
        self.stack = []
        self.minstack = []
        self.minval = sys.maxint

    def push(self, number):
        # write yout code here
        self.stack.append(number)
        if number < self.minval:
            self.minval = number
        self.minstack.append(self.minval)

    def pop(self):
        # pop and return the top item in stack
        temp = self.minstack.pop()
        self.minval = sys.maxint if not self.minstack else self.minstack[-1]
        return self.stack.pop()
    def min(self):
        # return the minimum number in stack
        return self.minstack[-1]