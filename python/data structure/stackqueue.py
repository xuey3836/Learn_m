class Stack:
    def __init__(self):
        self.stack = []
    ##进栈
    def add(self, newdata):
        if newdata not in self.stack:
            self.stack.append(newdata)
            return True
        else:
            return False
    ##最顶层元素
    def peek(self):
        return self.stack[-1]

    ##删除元素
    def remove(self):
        if len(self.stack) <= 0:
            return ("No element in the Stack")
        else:
            return self.stack.pop()

AStack = Stack()
AStack.add("Mon")
AStack.add("Tue")
AStack.add("Wed")
AStack.add("Thu")
print(AStack.remove())
print(AStack.remove())


class Queue:

  def __init__(self):
      self.queue = list()

  def addtoq(self,dataval):
# 进入队列
      if dataval not in self.queue:
          self.queue.insert(0,dataval)
          return True
      return False
##
  def size(self):
      return len(self.queue)

  def removefromq(self):
      if len(self.queue)>0:
          return self.queue.pop()
      return ("No elements in Queue!")

TheQueue = Queue()
TheQueue.addtoq("Mon")
TheQueue.addtoq("Tue")
TheQueue.addtoq("Wed")
print(TheQueue.removefromq())
print(TheQueue.removefromq())


## Deque 两边可以增加和删除的队列
import collections
# 初始化一个deque
DoubleEnded = collections.deque(["Mon","Tue","Wed"])
print (DoubleEnded)

# 右边增加元素
print("Adding to the right: ")
DoubleEnded.append("Thu")
print (DoubleEnded)

# 左边增加元素
print("Adding to the left: ")
DoubleEnded.appendleft("Sun")
print (DoubleEnded)

# 右边删除元素
print("Removing from the right: ")
DoubleEnded.pop()
# 左边删除元素
print("Removing from the left: ")
DoubleEnded.popleft()

# 逆序
print("Reversing the deque: ")
DoubleEnded.reverse()
