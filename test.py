#!/usr/bin/env python3

from orgmunge import Org
import os

cal_inbox = Org(f'{os.environ["HOME"]}/Dropbox/org/cal-inbox.org', from_file=True, debug=True)
cal_inbox.write('/tmp/inbox_reconstructed.org')
