#!/usr/bin/env python3

from .parser import parser as p
from .classes import *
from typing import List, Dict, Optional

class Org:
    def __init__(self, input_string: str, from_file: bool = True, debug: bool = False):
        if from_file:
            with open(input_string, 'r') as IN:
                string = IN.read()
        else:
            string = input_string
        metadata, initial_body, headings = p.parse(string, debug=debug)
        self.metadata = self._read_metadata(metadata)
        self.initial_body = initial_body
        self.root = self._classify_headings(headings)

    def _classify_headings(self, lst: Optional[List[Heading]]) -> Heading:
        """Takes a list of headings and classifies them according to their
        parent and sibling relationships. It creates an empty top-level heading
        named ROOT and returns it, with all the other level-1 headings in the
        tree as its children.
        """
        ROOT = Heading(Headline(' ', title='ROOT'), (None, None, None))
        if lst is not None:
            ROOT.add_child(lst[0], new=True)
            if lst[0].level !=1:
                raise ValueError("Org tree can't start with a heading of level > 1")
            if len(lst) > 1:
                for elem1, elem2 in zip(lst[:-1], lst[1:]):
                    if elem2.level == 1:
                        if ROOT.children:
                            elem2.sibling = ROOT.children[-1]
                        ROOT.add_child(elem2, new=True)
                    elif elem2.level > elem1.level:
                        if elem1.children:
                            elem2.sibling = elem1.children[-1]
                        elem1.add_child(elem2, new=True)
                    elif elem2.level < elem1.level:
                        levels_to_climb = elem1.level - elem2.level
                        sibling = elem1.parent
                        for _ in range(levels_to_climb-1):
                            sibling = sibling.parent
                        elem2.sibling = sibling
                        elem2.sibling.parent.add_child(elem2, new=True)
                    else:
                        elem2.sibling = elem1
                        elem1.parent.add_child(elem2, new=True)
        return ROOT

    def _read_metadata(self, metadata: str) -> Dict[str, List[str]]:
        """Reads the metadata string into a dictionary mapping
        each metadata keyword to a list of values assigned to it.
        This allows for cumulative metadata assignments (e.g. multiple
        #+options lines). The metadata keywords are all converted to
        lower case and that's how they will be written out to file.
        """
        metadata_lines = [l for l in metadata.split('\n') if l != '']
        result = dict()
        for line in metadata_lines:
            keyword, value = re.search(r'^\#\+([^:]+):\s*(.*)', line).groups()
            if keyword.lower() in result:
                result[keyword.lower()].append(value)
            else:
                result[keyword.lower()] = [value]
        return result

    def _metadata_values_to_string(self, keyword: str) -> str:
        return "\n".join([f"#+{keyword}: {v}" for v in self.metadata[keyword]]) + '\n'

    def write(self, out_file: str):
        "Writes out the org tree into a file."
        with open(out_file, 'w') as OUT:
            OUT.write(str(self))

    def __repr__(self):
        result = ''
        for keyword in self.metadata:
            result += self._metadata_values_to_string(keyword)
        result += '\n'
        result += self.initial_body + '\n'
        result += ''.join([c.__repr__() for c in self.root.children])
        return result

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        else:
            return str(self) == str(other)
    
                                
