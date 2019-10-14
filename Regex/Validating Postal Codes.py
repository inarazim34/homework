#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#input
p_code = input().strip()

#conditions
digit = p_code.isdigit()
in_range = digit and 100000 <= int(p_code) <= 999999
repetitive_digit = digit and sum([p_code[i]==p_code[i+2] for i in range(0,4)]) > 1

#print True or False
print(in_range and not repetitive_digit)

