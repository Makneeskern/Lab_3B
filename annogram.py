# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Node(object):
    def __init__(self, data = None, height = 0, color = ""):
        self.key = data
        self.height = height
        self.color = color
        self.left = None
        self.right = None
        self.parent = None

class AVLBBST(object):
    def __init__(self, root = None):
        if (root != None):
            self.root = Node(root)
        else:
            self.root = root
    
    def AVLTreeUpdateHeight(self, node):
       leftHeight = -1
       if node.left != None:
           leftHeight = node.left.height
       rightHeight = -1
       if node.right != None:
           rightHeight = node.right.height
       node.height = max(leftHeight, rightHeight) + 1


    def AVLTreeSetChild(self, parent, whichChild, child):
        if whichChild != "left" and whichChild != "right":
          return False
  
        if whichChild == "left":
          parent.left = child
        else:
          parent.right = child
        if child != None:
          child.parent = parent
      
        self.AVLTreeUpdateHeight(parent)
        return True

    def AVLTreeReplaceChild(self, parent, currentChild, newChild):
        if parent.left == currentChild:
          return self.AVLTreeSetChild(parent, "left", newChild)
        elif parent.right == currentChild:
          return self.AVLTreeSetChild(parent, "right", newChild)
        return False

    def AVLTreeGetBalance(self, node):
        leftHeight = -1
        if node.left != None:
          leftHeight = node.left.height
        rightHeight = -1
        if node.right != None:
          rightHeight = node.right.height
        return leftHeight - rightHeight
    
    def AVLTreeRebalance(self, node):
        self.AVLTreeUpdateHeight(node)        
        if self.AVLTreeGetBalance(node) == -2:
            if self.AVLTreeGetBalance(node.right) == 1:
                self.AVLTreeRotateRight(node.right)
            return self.AVLTreeRotateLeft(node)
        elif self.AVLTreeGetBalance(node) == 2:
            if self.AVLTreeGetBalance(node.left) == -1:
                self.AVLTreeRotateLeft(node.left)
            return self.AVLTreeRotateRight(node)
        return node
    
    def AVLTreeInsert(self, node):
        if self.root == None:
            self.root = node
            node.parent = None
            return
        cur = self.root
        while cur != None:
            if node.key <= cur.key:
                if cur.left == None:
                    cur.left = node
                    node.parent = cur
                    cur = None
                else:
                    cur = cur.left
            else:
                if cur.right == None:
                    cur.right = node
                    node.parent = cur
                    cur = None
                else:
                    cur = cur.right
        while node != None:
            self.AVLTreeRebalance(node)
            node = node.parent
        
    def AVLTreeRotateRight(self, node):
        leftRightChild = node.left.right
        if node.parent != None:
            self.AVLTreeReplaceChild(node.parent, node, node.left)
        else: #// node is root
            self.root = node.left
            self.root.parent = None
        self.AVLTreeSetChild(node.left, "right", node)
        self.AVLTreeSetChild(node, "left", leftRightChild)
    
    def AVLTreeRotateLeft(self, node):
        rightLeftChild = node.right.left
        if node.parent != None:
            self.AVLTreeReplaceChild(node.parent, node, node.right)
        else: #// node is root
            self.root = node.right
            self.root.parent = None
        self.AVLTreeSetChild(node.right, "left", node)
        self.AVLTreeSetChild(node, "right", rightLeftChild)

class RBBBST(object):
    def __init__(self, root = None):
        if (root != None):
            self.root = Node(root, "black")
        else:
            self.root = root
        
    def RBTreeSetChild(self, parent, whichChild, child):
       if whichChild != "left" and whichChild != "right":
           return False
       if whichChild == "left":
           parent.left = child
       else:
           parent.right = child
       if child != None:
           child.parent = parent
       return True
   
    def RBTreeReplaceChild(self, parent, currentChild, newChild):
        if parent.left == currentChild:
            return self.RBTreeSetChild(parent, "left", newChild)
        elif parent.right == currentChild:
            return self.RBTreeSetChild(parent, "right", newChild)
        return False
    
    def RBTreeRotateLeft(self, node):
        rightLeftChild = node.right.left
        if node.parent != None:
            self.RBTreeReplaceChild(node.parent, node, node.right)
        else:
            self.root = node.right
            self.root.parent = None
        self.RBTreeSetChild(node.right, "left", node)
        self.RBTreeSetChild(node, "right", rightLeftChild)
        
    def RBTreeRotateRight(self, node):
        leftRightChild = node.left.right
        if node.parent != None:
            self.RBTreeReplaceChild(node.parent, node, node.left)
        else:
            self.root = node.left
            self.root.parent = None
        self.RBTreeSetChild(node.left, "right", node)
        self.RBTreeSetChild(node, "left", leftRightChild)
        
    def RBTreeInsert(self, node):
        print(node.key)
        self.BSTInsert(node)
        node.color = "red"
        self.RBTreeBalance(node)
    
    def RBTreeGetGrandparent(self, node):
        if node.parent == None:
            return None
        return node.parent.parent

    def RBTreeGetUncle(self, node):
        grandparent = None
        if node.parent != None:
            grandparent = node.parent.parent
        if grandparent == None:
            return None
        if grandparent.left == node.parent:
            return grandparent.right
        else:
            return grandparent.left
    
    def RBTreeBalance(self, node):
        if node.parent == None:
            node.color = "black"
            return
        if node.parent.color == "black":
            return
        parent = node.parent
        grandparent = self.RBTreeGetGrandparent(node)
        uncle = self.RBTreeGetUncle(node)
        if uncle != None and uncle.color == "red":
            parent.color = uncle.color = "black"
            grandparent.color = "red"
            self.RBTreeBalance(grandparent)
            return
        if node == parent.right and parent == grandparent.left:
            self.RBTreeRotateLeft(parent)
            node = parent
            parent = node.parent
        elif node == parent.left and parent == grandparent.right:
            self.RBTreeRotateRight(parent)
            node = parent
            parent = node.parent
        parent.color = "black"
        grandparent.color = "red"
        if node == parent.left:
            self.RBTreeRotateRight(grandparent)
        else:
            self.RBTreeRotateLeft(grandparent)
     
    def BSTInsert (self, node):
         cur = self.root
         if cur == None:
             self.root = node
         else:
             while cur != None:
                 if node.key > cur.key:
                     cur = cur.right
                 else:
                     cur = cur.left
             cur = node
             
def BST_search (tree, key):
    cur = tree.root
    while cur != None:
        if cur.key.lower() == key.lower():
            return True
        if key.lower() < cur.key.lower():
            cur = cur.left
        else:
            cur = cur.right
    return False

def BST_print (tree):
    cur = tree.root
    print(cur.key)
    BST_print_h(cur.left)
    BST_print_h(cur.right)
    
def BST_print_h(node):
    if node == None:
        return
    print(node.key)
    BST_print_h(node.left)
    BST_print_h(node.right)
    
#I did too much wordplay with "planting" the trees, even bringing in a reference to genetics

def plant_AVL (file):
    seed = file.readline()
    tree = AVLBBST(seed.strip())
    seed = file.readline()
    while seed != "":
        tree.AVLTreeInsert(Node(seed.lower().strip()))
        seed = file.readline()
    return tree
    
def plant_RB (file):
    seed = file.readlines()
    tree = RBBBST(seed[0].strip())
    for gene in range(1, len(seed)):
        tree.RBTreeInsert(Node(seed[gene].lower().strip()))
    return tree
    
def count_anagrams (word, english_words, prefix = ""):
   if len(word) <= 1:
       str = prefix + word

       if BST_search(english_words, str):
           return 1
       return 0
   else:
       count = 0
       for i in range(len(word)):
           cur = word[i: i + 1]
           before = word[0: i] # letters before cur
           after = word[i + 1:] # letters after cur

           if cur not in before: # Check if permutations of cur have not been generated.
               count = count + count_anagrams(before + after, english_words, prefix + cur)
       return count
    
def print_anagrams (word, english_words, prefix = ""):
   if len(word) <= 1:
       str = prefix + word

       if BST_search(english_words, str):
           print(prefix + word)
   else:
       for i in range(len(word)):
           cur = word[i: i + 1]
           before = word[0: i] # letters before cur
           after = word[i + 1:] # letters after cur

           if cur not in before: # Check if permutations of cur have not been generated.
               print_anagrams(before + after, english_words, prefix + cur)
    
def main ():
    english_words = ""
    tree_choice = input("Which type of three shall we use? \n For AVL, type: \"AVL\", \"A\", or \"1\" \n For Red-Black, type: \"RB\", \"B\", or \"2\"\n")
    file_choice = input('What is the file\'s name which contains the words we will find the annograms for? (include ".txt" at the end)\n')
    file = open("words.txt", 'r')
    word_file = open(file_choice, 'r')
    if tree_choice.lower() == "avl" or tree_choice.lower() == "a" or tree_choice.lower() == "1":
        english_words = plant_AVL(file)
    elif tree_choice.lower() == "rb" or tree_choice.lower() == "b" or tree_choice.lower() == "2":
        english_words = plant_RB(file)
    else:
        print("I'm sorry, but I couldn't understand which tree you were choosing. Please try again, and be sure to read the instructions carefully.")
        return
    all_words = word_file.readlines()
    for words in all_words:
        print("There are ", count_anagrams(words.strip(), english_words), "anagrams for", words, ". They are:")
        print_anagrams(words.strip(), english_words)
    
main()