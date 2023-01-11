COUNT = [10]

class Tree:

    def __init__(root,data):#конструктор  __init__ використовуватиметься для вставки елементів в дерево
        root.right=None
        root.left=None
        root.value=data
        
    def search_node(root,data):#пошук елементу
        if data < root.value:
            if root.left is None:
                print(data," not found")
            print(root.left.search_node(data))
        elif data > root.value:
            if root.right is None:
               print(data," not found")
            print(root.right.search_node(data))
        else:
            print(root.value," is found!")
        
    def insert(root,data):#метод для вставки елементів
        if root.value:
            if root.value>data:
                if root.left is None:
                    root.left=Tree(data)
                else:
                    root.left.insert(data)
            elif root.value<data:
                if root.right is None:
                    root.right=Tree(data)
                else:
                    root.right.insert(data)
        else:
            root.value=data
        
    def create_root_bst(root,data):
        root.right=None
        root.left=None
        root.parent=None
        root.value=data







def inorder(root):
        if root:
            inorder(root.left)
            print(str(root.value)," -> ",end='')
            inorder(root.right)
            
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(str(root.value)," -> ",end='')

def preorder(root):
    if root:
        print(str(root.value)," -> ",end='')
        postorder(root.left)
        postorder(root.right)

def print2DUtil(root, space):
 
    # Base case
    if (root == None):
        return
 
    # Increase distance between levels
    space += COUNT[0]
 
    # Process right child first
    print2DUtil(root.right, space)
 
    # Print current node after space
    # count
    print()
    for i in range(COUNT[0], space):
        print(end=" ")
    print(root.value)
 
    # Process left child
    print2DUtil(root.left, space)
 
# Wrapper over print2DUtil()
 
 
def print2D(root):
 
    # space=[0]
    # Pass initial space count as 0
    print2DUtil(root, 0)
        
def minimum(root):
        if root==None:
            return float('+inf')
        else:
            res=root.value
            lres=minimum(root.left)
            rres=minimum(root.right)
            if lres<res:
                res=lres
            if rres<res:
                res=rres
        return res
def tree_successor(root):
    if root.right!=None:
        return minimum(root.right)
    y=root.parent
    while(y!=None and x==y.right):
        x=y
        y=y.parent
    return y.value

root=Tree(10)
root.insert(15)
root.insert(121)
root.insert(22)
root.insert(12)
root.insert(143)
print("inorder :\n")
inorder(root)
print("\n\npostorder :\n")
postorder(root)
print("\n\npreorder :\n")
preorder(root)
print2D(root)    
        
