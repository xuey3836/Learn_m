# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    def push(self, node):
        # write code here
        self.stack1.append(node)
    def pop(self):
        if self.stack2 == []:
            if self.stack1 == []:
                return None
            else:
                while self.stack1:
                    self.stack2.append(self.stack1.pop())
                return self.stack2.pop()
        else:
            return self.stack2.pop()
        # return xx

times=5
testList=list(range(times))
testQueue=Solution()
for i in range(times):
    testQueue.push(testList[i])
print(testList)
for i in range(times):
    print(testQueue.pop(),',',end='')


###two queue to stack
class Stack:
    def __init__(self):
        self.queue1 = []
        self.queue2 = []
    def push(self, node):
        self.queue1.append(node)
    def pop(self):
        ##将队列1依次出队，进入队2，直到还剩一个元素
        if len(self.queue1) == 0:
            return None
        while len(self.queue1) != 1:
            self.queue2.append(self.queue1.pop(0))
        ##交换下次
        self.queue1, self.queue2 = self.queue2, self.queue1
        return self.queue2.pop(0)

times=5
testList=list(range(times))
testStack=Stack()
for i in range(times):
    testStack.push(testList[i])
print(testList)
for i in range(times):
    print(testStack.pop(),',',end='')   
