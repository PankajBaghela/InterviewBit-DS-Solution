class tree:
    def __init__(self,data):
        self.val=data
        self.left=None
        self.right=None

    def print_inorder(self):
        print(self.val)
        if self.left:
            self.left.print_inorder()
       
        if self.right:
            self.right.print_inorder()
        

    def hasPathSum(self, A, B):
        if not A:
            return 0
            
        # checking if current node is a leaf node and then if its satisfying sum constraint
        if A.left is None and A.right is None and A.val == B:
            return 1
            
        return self.hasPathSum(A.left, B - A.val) or self.hasPathSum(A.right, B - A.val)
if __name__=="__main__":
    root=tree(5)
    root.left=tree(4)
    root.right=tree(8)
    root.left.left=tree(11)
    root.left.left.left=tree(7)
    root.left.left.right=tree(2)
    root.right.right=tree(4)
    root.right.left=tree(13)
   # print(root.hasPathSum(root, 22))
    print(root.print_inorder())