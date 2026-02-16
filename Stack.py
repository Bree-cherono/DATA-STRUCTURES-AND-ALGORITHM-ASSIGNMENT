#!/usr/bin/env python
# coding: utf-8

# In[1]:


SIZE = 5
stack = []
top = -1

def push(value):
    global top
    if top == SIZE - 1:
        print("Stack Overflow")
        return
    stack.append(value)
    top += 1

def pop():
    global top
    if top == -1:
        print("Stack Underflow")
        return
    print(f"Popped element: {stack.pop()}")
    top -= 1

def main():
    push(10)
    push(20)
    push(30)
    pop()

if __name__ == "__main__":
    main()


# In[ ]:




