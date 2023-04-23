#!/usr/bin/env python3

from orgmunge import Org

root = Org('test.org', from_file=True)
print(root)
