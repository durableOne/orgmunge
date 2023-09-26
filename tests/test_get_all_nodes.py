from orgmunge import Org
import re

def test_get_all_nodes():
    test_file = '''* Node 1
** Subnode 1
** Subnode 2
* Node 2
** Subnode 1
* Node 3
** Subnode 1
*** Subnode 1
*** Subnode 2
    '''
    node_titles = re.sub(r'\*+\s+', '', test_file.strip()).split('\n')

    parsed = Org(test_file, from_file=False)
    assert [n.title for n in parsed.get_all_nodes()] == node_titles
