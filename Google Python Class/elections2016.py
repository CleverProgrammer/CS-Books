# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 08:01:27 2015

@author: Rafeh
"""
import re
f = open('elections2016.txt', 'r')
match = re.search(r'target="_blank">\w+',f)
match