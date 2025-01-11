from orgmunge import Org
import re

CONTENT = """:PROPERTIES:
:ID: some-bogus-id
:END:
#+title: Test Roam Node

* You can write orgfiles!!
"""

def test_read_org_roam_node(tmp_path):
    p = tmp_path / "testtmp_roam.org"
    assert len(list(tmp_path.iterdir())) == 0 # Nothing exists here
    test = Org(CONTENT, from_file=False)
    assert test.properties['ID'] == 'some-bogus-id'
    test.write(p)
    assert len(list(tmp_path.iterdir())) == 1 # testtmp. org exists
    assert p.read_text().strip(" \n") == re.sub(r'^\s*$', '', CONTENT.strip(" \n"), flags=re.MULTILINE)
