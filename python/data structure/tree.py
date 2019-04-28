class Node:
    def __init__(self, data, left = None, right = None, cousion = None):
        self.data = data
        self.left = left 
        self.right = right
        self.isCousion = cousion

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data)
        if self.right:
            self.right.PrintTree()


# root = Node(12)
# root.insert(6)
# root.insert(14)
# root.insert(3)

# root.PrintTree()
####树的遍历
    # 中序遍历

    # Left -> Root -> Right
    def inorderTraversal(self, root):
        res = []
        if root:
            res = self.inorderTraversal(root.left)
            res.append(root.data)
            res = res + self.inorderTraversal(root.right)
        return res
    
    def inorderiter(self, root):
        res = []
        stack = []
        node = root
        while (node or stack):
            if node is None:
                node = stack.pop()
                res.append(node.data)
                node = node.right
            else:
                stack.append(node)
                node = node.left



    ##先序遍历.
# Root -> Left ->Right
    def PreorderTraversal(self, root):
        res = []
        if root:
            res.append(self.data)
            res = res + self.PreorderTraversal(root.left)
            res = res + self.PreorderTraversal(root.right)
        return res
    
    def preorderTraversal(self, root):
        res = []
        stack = []
        node = root
        while (node or stack):
            while node:
                res.append(node.data)
                stack.append(node)
                node = node.left
            if not stack:
                node = stack[-1]
                stack.pop()
                node = node.right
        return res


    ## 后序遍历
    # Left ->Right -> Root
    def PostorderTraversal(self, root):
        res = []
        if root:
            res = self.PostorderTraversal(root.left)
            res = res + self.PostorderTraversal(root.right)
            res.append(root.data)
        return res

    def level_queue(self, root):
        if root == None:
            return
        queue = []
        res = []
        queue.append(root)
        while queue:
            node = queue.pop(0)
            res.append(node.data)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
        return res
    
    def isfindCousion(self, root):
        if root == None:
            return
        queue = []
        queue.append(root)
        while queue:
            size = len(queue)
            for i in range(size):
                node = queue.pop(0)
                if node:
                    if i == size-1:
                        node.isCousion = None
                    else:
                        node.isCousion = queue[0]
                    queue.append(node.left)
                    queue.append(node.right)
        return 



root = Node(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)
root.inorderTraversal(root)
root.PrintTree()
root.PostorderTraversal(root)
root.level_queue(root)

