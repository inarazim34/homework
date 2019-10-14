#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Enter your code here. Read input from STDIN. Print output to STDOUT
n, x = map(int, input().split()) 

arr = []
for _ in range(x):
    arr.append( map(float, input().split()) ) 

for i in zip(*arr): 
    print( sum(i)/len(i) )

