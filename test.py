#!/usr/bin/env python3

from orgmunge import Org
import os

root = Org(f'{os.environ["HOME"]}/Dropbox/org/agenda.org', from_file=True, debug=True)
print(root)
