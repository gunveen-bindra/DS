class Node :
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key

    def insert(self,data):
       if self.val:
           if data < self.val:
               if self.left is None:
                   self.left = Node(data)
               else:
                    self.left.insert(data)
           elif data>self.val:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
       else :
            self.val = data

    def PrintTree(self):
        if  self.left:
            self.left.PrintTree()
        print(self.val)
        if self.right:
            self.right.PrintTree()


    def printPreorder(self):
        if self.val:
            print(self.val)
            if self.left:
                self.left.printPreorder()
            if self.right:
                self.right.printPreorder()
                
    
    
    def  printInorder(self):
        if self.val :
            if self.left:
                self.left.printInorder()
            print(self.val)
            if self.right:
                self.right.printInorder()

    def printPostorder(self):
        if self.val:
            if self.left:
                self.left.printPostorder()
            if self.right:
                self.right.printPostorder()
            print(self.val)

            

      

root1 = Node(48)
root1.left = Node(64)
root1.right=Node(21)
print('Without any ordering')
root1.PrintTree()
print('Now ordering with insert' )
root1_=Node(None)
root1_.insert(18)
root1_.insert(1)
root1_.PrintTree()
print("Next Node")
root1 = Node(None)
root1.insert(56)
root1.insert(78)
root1.insert(34)
root1.insert(14)
root1.insert(98)
root1.insert(54)
root1.PrintTree()

print("Preorder")
root1.printPreorder()

print("Inorder")
root1.printInorder()

print("Postorder")
root1.printPostorder()
