from orgmunge import Org
import re

def test_get_headings():
    test_file = '''* My first node
** My first sub node
* My first Node
** My second sub node
'''    
    parsed = Org(test_file, from_file=False)
    search_1 = parsed.get_headings_by_headline('node')
    search_2 = parsed.get_headings_by_headline('node', re_flags=re.IGNORECASE)
    search_3 = parsed.get_headings_by_headline('node', exact=True)
    search_4 = parsed.get_headings_by_headline('My first node', exact=True)
    assert [n.title for n in search_1] == ['My first node', 'My first sub node', 'My second sub node']
    assert [n.title for n in search_2] == ['My first node', 'My first sub node', 'My first Node', 'My second sub node']
    assert search_3 == []
    assert [n.title for n in search_4] == ['My first node']
