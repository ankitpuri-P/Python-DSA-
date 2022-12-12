class binarytree:
    def __init__(self,data) -> None:  
        self.data=data
        self.left=None
        self.right=None
def call_the_tree(root):
    if root==None:
        return
    print(root.data,end=" ")
    if root.left!=None:
        print("L",root.left.data,end=',')
    if root.right!=None:
        print("R",root.right.data,end=' ')
    print()
    call_the_tree(root.left)
    call_the_tree(root.right)
def tree_input():
    rootdata=int(input())
    if rootdata==-1:
        return None
    root=binarytree(rootdata)
    leftTree=tree_input()
    rightTree=tree_input()
    root.left=leftTree
    root.right=rightTree
    return root
root=tree_input()
call_the_tree(root)
