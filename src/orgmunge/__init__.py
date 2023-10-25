#!/usr/bin/env python3

import re
import json
import os
import platform
from .parser import Parser
from .lexer import Lexer
from .classes import *
from typing import List, Dict, Optional, Generator, Callable

class Org:
    def get_todos(self):
        base_file_name = 'todos.json'
        current_dir_file = os.path.join(os.getcwd(), base_file_name)
        home_dir = os.environ['HOMEPATH'] if platform.system() == 'Windows' else os.environ['HOME']
        home_dir_file = os.path.join(home_dir, base_file_name)
        package_dir_file = os.path.join(os.path.dirname(__file__), base_file_name)
        # First try the current directory, then the user's home directory then finally the package directory
        # to find the todos.json file.
        if os.path.isfile(current_dir_file):
            input_file_name = current_dir_file
        elif os.path.isfile(home_dir_file):
            input_file_name = home_dir_file
        else:
            input_file_name = package_dir_file
        if os.path.isfile(input_file_name):
            with open(input_file_name, 'rb') as JSON:
                return json.load(JSON)
        else:
            return {'todo_states':
                    {'todo': 'TODO',
                    'next': 'NEXT',
                    'wait': 'WAIT',},
                    'done_states': 
                    {'cncl': 'CNCL',
                    'done': 'DONE',}}
    def __init__(self, input_string: str, from_file: bool = True, debug: bool = False,
               todos: Optional[Dict[str, Dict[str, str]]] = None,):
        if from_file:
            with open(input_string, 'rb') as IN:
                string = IN.read().decode('utf-8')
        else:
            string = input_string
        if todos is None:
            todos = self.get_todos()
        self.todos = todos
        lexer = Lexer(todos)
        parser = Parser(lexer)
        metadata, initial_body, headings = parser.parser.parse(string, debug=debug)
        self.metadata = self._read_metadata(metadata)
        self.initial_body = initial_body
        self.root = self._classify_headings(headings)

    def _classify_headings(self, lst: Optional[List[Heading]]) -> Heading:
        """Takes a list of headings and classifies them according to their
        parent and sibling relationships. It creates an empty top-level heading
        named ROOT and returns it, with all the other level-1 headings in the
        tree as its children.
        """
        ROOT = Heading(Headline(self.todos, ' ', title='ROOT'), (None, None, None))
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

    def get_all_headings(self) -> Generator[Heading, None, None]:
        """Generator function to recursively return all headings in the Org tree.
        The headings are returned in the order they're encountered in the file
        (so the tree is searched depth-first)."""
        def _helper(tree: List[Heading]) -> Generator[Heading, None, None]:
            for heading in tree:
                yield heading
                yield from _helper(heading.children)
        yield from _helper(self.root.children)

    def filter_headings(self, func: Callable[..., bool]) -> Generator[Heading, None, None]:
        """Takes a predicate function and returns all headings in the tree
        that return True when passed through that function."""
        return (heading for heading in self.get_all_headings() if func(heading))
        
    def get_headings_by_title(self, search_string: str, exact: bool = False,
                              re_flags: int = 0) -> Generator[Heading, None, None]:
        """Return a heading whose headline matches the given string.
        If exact is True, get the heading whose headline is exactly
        the given string. If not, the given string is interpreted
        as a regex (so any special characters must be quoted).
        Matching is only done on headline title, no cookies,
        todo keywords or tags are considered."""
        if exact:
            condition = lambda h: h.title == search_string
        else:
            condition = lambda h: bool(re.search(fr'{search_string}', h.title, flags=re_flags))
        return self.filter_headings(condition)

    def __repr__(self):
        result = ''
        for keyword in self.metadata:
            result += self._metadata_values_to_string(keyword)
        if self.metadata:
            result += '\n'
        if self.initial_body:
            result += self.initial_body + '\n'
        result += ''.join([c.__str__() for c in self.root.children])
        if result[-1] != '\n':
            result += '\n'
        return result

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        else:
            return str(self) == str(other)
    
                                
