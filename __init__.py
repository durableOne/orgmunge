#!/usr/bin/evn python3

__package__ = 'orgmunge'
from .parser import parser as p
from .classes import *

class Org:
    def __init__(self, input_string, from_file=True, debug=False):
        if from_file:
            with open(input_string, 'r') as IN:
                string = IN.read()
        else:
            string = input_string
        metadata, initial_body, headings = p.parse(string, debug=debug)
        self.metadata = self._read_metadata(metadata)
        self.initial_body = initial_body
        self.root = self._classify_headings(headings)

        
    def _classify_headings(self, lst):
        ROOT = Heading(Headline(' ', title='ROOT'), (None, None, None))
        ROOT.add_child(lst[0], new=True)
        if len(lst) > 1:
            for elem1, elem2 in zip(lst[:-1], lst[1:]):
                if elem2.level == 1:
                    elem2.parent = ROOT
                    ROOT.add_child(elem2, new=True)
                if elem2.level > elem1.level:
                    if elem1.children:
                        elem1.children.append(elem2)
                    else:
                        elem1.children = [elem2]
                    elem2.parent = elem1
                elif elem2.level < elem1.level:
                    elem2.sibling = elem1.parent
                else:
                    elem2.sibling = elem1
                    elem2.parent = elem1.parent
                    if elem1.parent:
                        elem1.parent.children.append(elem2)
        return ROOT

    def _read_metadata(self, metadata):
        metadata_lines = [l for l in metadata.split('\n') if l != '']
        result = dict()
        for line in metadata_lines:
            keyword, value = re.search(r'^\#\+([^:]+):\s*(.*)', line).groups()
            if keyword.lower() in result:
                result[keyword.lower()].append(value)
            else:
                result[keyword.lower()] = [value]
        return result

    def _metadata_values_to_string(self, keyword):
        return "\n".join([f"#+{keyword}: {v}" for v in self.metadata[keyword]]) + '\n'

    def __repr__(self):
        result = ''
        for keyword in self.metadata:
            result += self._metadata_values_to_string(keyword)
        result += '\n'
        result += self.initial_body + '\n'
        result += ''.join([c.__repr__() for c in self.root.children])
        return result
                                
