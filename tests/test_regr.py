#!/usr/bin/env python3
from orgmunge import Org

def test_regr(file_regression):
    agenda = Org('./tests/files/regr.org')
    file_regression.check(str(agenda), extension='.txt',)
    
