# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 08:01:27 2015

@author: Rafeh
"""
import re
import io
f = open('elections2016.txt', 'r',encoding = 'UTF-8').read()
#match = re.search(r'\w',f)
#match
match = re.search(r't', f) 
print(match)
