#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys 
import factorial
import csv

try:
    var = factorial.GFG()
    #sys.exit(0)
except AttributeError:
    print("Required class is not present")
    sys.exit(1)

sys.exit(0)





