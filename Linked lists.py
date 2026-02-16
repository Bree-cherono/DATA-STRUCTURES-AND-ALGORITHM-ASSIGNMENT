#!/usr/bin/env python
# coding: utf-8

# In[2]:


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Create nodes
head = Node(5)
second = Node(25)

# Link nodes
head.next = second

# Traverse and print the linked list
temp = head
while temp is not None:
    print(temp.data, end=" ")
    temp = temp.next


# In[ ]:




