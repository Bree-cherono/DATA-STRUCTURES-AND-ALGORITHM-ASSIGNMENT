#!/usr/bin/env python
# coding: utf-8

# In[10]:


nodes= 4

graph = [
    [1, 1, 0, 0],
    [1, 0, 1, 0],
    [1, 1, 0, 1],
    [1, 0, 0, 0]
]

for row in range(nodes):
    for col in range(nodes):
        print(graph[row][col], end=" ")
    print()


# In[ ]:




