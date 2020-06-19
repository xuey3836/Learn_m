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



def func(a):
    if a< 1e-6:
        return 0
    last = a
    c = a/2
    while abs(c - last) > 1e-6:
        f = c*c - a
        f1 = 2*c
        last = c
        c = c - f/f1
    return c

a = [2, 3, 1, 4, 2, 1, 1, 1, 1]

ns = 3
grid = [0]*ns
for i in range(ns):
    grid[i] = a[i*ns:ns*(i+1)]
minPathSum(grid)
def minPathSum( grid):
    if grid == None :
        return 0
    if len(grid)==0 or len(grid[0])==0:
        return sum(grid)
    row = len(grid)
    loc = len(grid[0])
    dp = grid
    for i in range(1,row):
        dp[i][0] = dp[i-1][0] + grid[i][0]
    for i in range(1,loc):
        dp[0][i] = dp[0][i-1] + grid[0][i]
    for i in range(1,row):
        for j in range(1,loc):
            dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])
    
    return dp[i][j]

