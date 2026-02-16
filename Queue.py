#!/usr/bin/env python
# coding: utf-8

# In[6]:


numbers = [10, 20, 30, 40, 50]

for number in numbers:
    print(number, end=" ")
    print()  
    count = 10
    price = 99.50
    grade = 'A'

    print(f"Count: {count}")
    print(f"Price: {price:.2f}")
    print(f"Grade: {grade}")
    # Queue implementation in Python
    class Queue:
        def __init__(self, size):
            self.size = size
            self.queue = []
        
        def enqueue(self, value):
            if len(self.queue) >= self.size:
                print("Queue Overflow")
            else:
                self.queue.append(value)
        
        def dequeue(self):
            if not self.queue:
                print("Queue Underflow")
            else:
                print(f"Dequeued element: {self.queue.pop(0)}")


# In[7]:


# Queue implementation in Python
class Queue:
      def __init__(self, size):
          self.size = size
          self.queue = []
      
      def enqueue(self, value):
          if len(self.queue) >= self.size:
              print("Queue Overflow")
          else:
              self.queue.append(value)
      
      def dequeue(self):
          if not self.queue:
              print("Queue Underflow")
          else:
              print(f"Dequeued element: {self.queue.pop(0)}")


# In[8]:


# Example usage
q = Queue(5)
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.dequeue()


# In[ ]:




