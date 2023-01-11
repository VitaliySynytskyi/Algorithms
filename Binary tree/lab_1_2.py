#from lab_1_1 import *
COUNT = [10]

class Node:

	
	def __init__(self, key):
		self.key = key
		self.left = None
		self.right = None



def inorder(root):
        
	if root is not None:
		inorder(root.left)
		print (root.key,end=" ")
		inorder(root.right)

		
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
    print(root.key)
 
    # Process left child
    print2DUtil(root.left, space)
 
# Wrapper over print2DUtil()
 
 
def print2D(root):
 
    # space=[0]
    # Pass initial space count as 0
    print2DUtil(root, 0)

# ф-я для вставки
def insert(node, key):

	if search(node, key):
		return print("Є такий елекмент")

	if node is None:
		return Node(key)

	# рекурсія
	if key < node.key:
		node.left = insert(node.left, key)
	else:
		node.right = insert(node.right, key)



	
	return node

#мінімальний елемент


def minValueNode(node):
	current = node

	# пошук найбільш лівого елемента
	while(current.left is not None):
		current = current.left

	return current

# ф-я видалення


def deleteNode(root, key):

	
	if root is None:
		return root

	
	if key < root.key:
		root.left = deleteNode(root.left, key)

	
	elif(key > root.key):
		root.right = deleteNode(root.right, key)

	
	else:

		# дерево без нащадків
		if root.left is None:
			temp = root.right
			root = None
			return temp

		elif root.right is None:
			temp = root.left
			root = None
			return temp

		# з двома нащадками
		temp = minValueNode(root.right)

		
		root.key = temp.key

		
		root.right = deleteNode(root.right, temp.key)

	return root
def minimum(root):
        if root==None:
            return float('+inf')
        else:
            res=root.key
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
    return y.key
def search_node(root,data):#пошук елементу
        if data < root.key:
            if root.left is None:
                print(data," not found")
                root=search_node(root.left,data)
            print(root.key,' is found ')
        elif data > root.key:
            if root.right is None:
               print(data," not found")
               root=search_node(root.right,data)
            print(root.key,' is found ')
        else:
            print(root.key," is found!")

def search(root,key):
     
    # Base Cases: root is null or key is present at root
    if root is None or root.key == key:
        return root
 
    # Key is greater than root's key
    if root.key < key:
        return search(root.right,key)
   
    # Key is smaller than root's key
    return search(root.left,key)
 
# діаграма
""" Let us create following BST
			50
		/	 \
		30	 70
		/ \ / \
	20 40 60 80 """

'''root = None
root = insert(root, 50)
root = insert(root, 30)
root = insert(root, 20)
root = insert(root, 40)
root = insert(root, 70)
root = insert(root, 60)
root = insert(root, 80)

print ("Inorder traversal of the given tree")
inorder(root)

print ("\nDelete 20")
root = deleteNode(root, 20)
print ("Inorder traversal of the modified tree")
inorder(root)

print ("\nDelete 30")
root = deleteNode(root, 30)
print ("Inorder traversal of the modified tree")
inorder(root)

print ("\nDelete 50")
root = deleteNode(root, 50)
print ("Inorder traversal of the modified tree")

'''
root=None

while(True):
        x=int(input('Choose option\n1) Insert\n2) delete\n3) search\n4) successor node\n5) show tree\n'))
        if x==0:
                root = insert(root, 50)
                root = insert(root, 30)
                root = insert(root, 20)
                root = insert(root, 40)
                root = insert(root, 70)
                root = insert(root, 60)
                root = insert(root, 80)
                print2D(root)

        elif x==1:
                
                try:
                        a=int(input('Put for insert '))
                        root=insert(root,a)
                        print('\n\n\n')
                        print2D(root)
                except ValueError:
                        print("only int!")
                
                
        elif x==2:
                a=int(input("element for delete "))
                root=deleteNode(root,a)
                print('\n\n\n')
                print2D(root)
        elif x==3:
                a=int(input('Put for insert '))
                print(search(root,a))
                
                print('\n\n\n')
                print2D(root)
        elif x==4:
                print(tree_successor(root))
        elif x==5:
                print2D(root)
