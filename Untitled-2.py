class bintrees:
    def __init__(self,data)->None:
        self.data=data
        self.left=None
        self.right=None
def call_the_tree(root):
    if root==None:
        return
    print(root.data,end=" ")
    if root.left!=None:
        print("L: ",root.left.data,end=",")
    if root.right!=None:
        print("R: ",root.right.data,end=" ")
    print()
    call_the_tree(root.left)
    call_the_tree(root.right)
def count_nodes(root):
    if root==None:
        return 0
    left_count=count_nodes(root.left)
    right_count=count_nodes(root.right)
    return 1+left_count+right_count
def find_max(root):
    if root==None:
        return -1
    leftmax=find_max(root.left)
    rightmax=find_max(root.right)
    returnmax=max(leftmax,rightmax,root.data)
    return returnmax
def take_input():
    rootdata=int(input())
    if rootdata==-1:
        return None
    root=bintrees(rootdata)
    root.left=take_input()
    root.right=take_input()
    return root
root=take_input()
call_the_tree(root)
print(count_nodes(root))
print(find_max(root))