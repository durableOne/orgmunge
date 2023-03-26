#!/usr/bin/env python3

import sys
sys.path.append('/home/joe/Dropbox/Public/Scripts/')
from orgmunge import Org

s1 = '''#+title: Hello
#+options: blah
#+options: flah

* TODO Heading 1
 Something 
** NEXT subheading 1
'''

root = Org(s1, from_file=False)
print(root)
