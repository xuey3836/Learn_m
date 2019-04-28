
##链表的节点
class Node:
    def __init__(self, dataval = None):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None

    ##打印链表
    def listprint(self):
        printval = self.headval
        while printval is not None:
            print (printval.dataval)
            printval = printval.nextval
    
    ##在链表头插入新节点
    def AtBegining(self,newdata):
        NewNode = Node(newdata)
        NewNode.nextval = self.headval
        self.headval = NewNode
    # 在尾部插入节点
    def AtEnd(self, newdata):
        NewNode = Node(newdata)
        if self.headval == None:
            self.headval = NewNode
            return
        lastnode = self.headval
        while(lastnode.nextval):
            lastnode = lastnode.nextval
        lastnode.nextval = NewNode
        
    ##在特定元素之后插入
    def Inmiddle(self, middlenode, newdata):
        if middlenode.dataval == None:
            print("The mentioned node is absent")
            return
        NewNode = Node(newdata)
        NewNode.nextval = middlenode.nextval
        middlenode.nextval = NewNode

    ##删除节点
    def RemoveNode(self, Removekey):
        Headval = self.headval
        #判断要删除的节点是否为头节点
        if(Headval.dataval is not None):
            if (Headval.dataval == Removekey):
                self.headval = Headval.nextval
                Headval = None
                return
        ##找到要删除的节点和它之前的节点
        while (Headval.dataval is not None):
            if Headval.dataval == Removekey:
                break
            prev = Headval
            Headval = Headval.nextval
        ##如果到最后也没有找到要删除的节点
        if (Headval == None):
            return
        #让前节点指向要删除节点的下一个节点
        prev.nextval = Headval.nextval
        Headval = None 

##test
llist = SLinkedList()
e2 = Node("Tue")
e3 = Node("Wed")
llist.headval = e2
e2.nextval = e3
llist.listprint()

llist.AtBegining("Mon")##在表头插入节点
llist.AtEnd("Fri")##在表尾插入节点
llist.Inmiddle(llist.headval.nextval.nextval, "Thu")##在中间某个元素之后插入节点
llist.Inmiddle(llist.headval.nextval, "Th") ## 插入节点
llist.RemoveNode("Th") ##删除节点
llist.listprint()##打印链表


class Node:
    def __init__(self, dataval):
        self.dataval = dataval
        self.next = None
        self.prev = None

class doubly_linked_list:
    def __init__(self):
        self.headval = None

    # 打印链表
    def listprint(self, node):
        while (node is not None):
            print(node.dataval),
            node = node.next
    #在表头添加节点
    def push(self, Newval):
        newnode = Node(Newval)
        newnode.next = self.headval
        if self.headval is not None:
            self.headval.prev = newnode
        self.headval = newnode
    
    ##插入节点
    def insert(self, prev_node, newdata):
        if prev_node is None:
            return 
        newnode = Node(newdata)
        newnode.next = prev_node.next
        prev_node.next = newnode
        newnode.prev = prev_node
        if newnode.next is not None:
            newnode.next.prev = newnode

dllist = doubly_linked_list()
dllist.push(12)
dllist.push(8)
dllist.push(62)
dllist.insert(dllist.headval.next, 13)
dllist.listprint(dllist.headval)



