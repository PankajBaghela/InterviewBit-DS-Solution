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
        

    def sumnumber(self):
        def find_path(root,val):
            if root is None:
                return 0
            val=(val*10+root.val)
            if root.left is None and root.right is None:
                return val
            return find_path(root.left, val) + find_path(root.right, val)

        return find_path(self, 0)%1003
if __name__=="__main__":
    root=tree(5)
    root.left=tree(4)
    root.right=tree(8)
    root.left.left=tree(11)
    root.left.left.left=tree(7)
    root.left.left.right=tree(2)
    root.right.right=tree(4)
    root.right.left=tree(13)
  
    print(root.sumnumber())