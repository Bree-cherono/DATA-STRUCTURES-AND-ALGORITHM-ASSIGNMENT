#!/usr/bin/env python
# coding: utf-8

# In[12]:


class TreeNode:
    def __init__(self, data):
        self.data = data  # The value stored in the node
        self.left = None  # Pointer to the left child node
        self.right = None  # Pointer to the right child node


    # Create the root node
    root = TreeNode(10)
    print("Root Node:")
    print_tree(root)


# In[13]:


# Insert more nodes into the tree
root = insert_node(root, 20)
root = insert_node(root, 30)
root = insert_node(root, 40)
root = insert_node(root, 50)

# Print the tree after inserting nodes
print("After inserting other nodes:")
print_tree(root)

