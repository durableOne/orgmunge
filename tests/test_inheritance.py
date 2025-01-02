
from orgmunge import Org
import re

def test_tag_inheritance():
    test_file = '''* Node 1    :parent:
** Subnode 1
** Subnode 2    :child:
* Node 2
** Subnode 1
* Node 3   :parent:
** Subnode 1
*** Subnode 1
*** Subnode 2
    '''
    parsed = Org(test_file, from_file=False)
    subnodes = [parsed.get_heading_by_path(p) for p in
                [['Node 1', 'Subnode 2'],
                 ['Node 3', 'Subnode 1', 'Subnode 2']]]
    for subnode in subnodes:
        assert 'parent' in subnode.all_tags

def test_property_inheritance():
    test_file = '''* Node 1
:PROPERTIES:
:parent: me
:END:
** Subnode 1
** Subnode 2
* Node 2
** Subnode 1
* Node 3
:PROPERTIES:
:parent: me
:END:
** Subnode 1
*** Subnode 1
*** Subnode 2
    '''
    parsed = Org(test_file, from_file=False)
    subnodes = [parsed.get_heading_by_path(p) for p in
                [['Node 1', 'Subnode 2'],
                 ['Node 3', 'Subnode 1', 'Subnode 2']]]
    for subnode in subnodes:
        assert 'parent' in subnode.inherited_properties
        assert 'parent' in subnode.get_all_properties()
