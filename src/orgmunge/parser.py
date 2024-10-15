#!/usr/bin/env python3

from .classes import *
from functools import reduce
from operator import add
import ply.yacc as yacc

class Parser:
    def __init__(self, lexer):
        self.tokens = lexer.tokens
        self.lexer = lexer
        self.parser = yacc.yacc(module=self)
    def p_org_file(self, p):
        '''org_file : metadata org_tree
                    | non_metadata_body_text SEPARATOR org_tree
                    | non_metadata_body_text SEPARATOR
                    | metadata non_metadata_body_text SEPARATOR org_tree
                    | metadata non_metadata_body_text SEPARATOR 
                    | metadata
                    | org_tree
                    | SEPARATOR
                    | empty'''
        if len(p) == 5:
            p[0] = (p[1], p[2], p[4])
        elif len(p) == 4:
            if type(p[3]) is not str: 
                p[0] = ('', p[1], p[3])
            else:
                p[0] = (p[1], p[2], None)
        elif len(p) == 3:
            if p[1].startswith('#+'):
                p[0] = (p[1], '', p[2])
            else:
                p[0] = ('', p[1], None)
        else:
            if type(p[1]) is str:
                p[0] = (p[1], '', None)
            else:
                p[0] = ('', '', p[1])

    def p_metadata(self, p):
        '''metadata : METADATA SEPARATOR
                    | METADATA NEWLINE'''
        p[0] = reduce(add, p[1:])

    def p_org_tree(self, p):
        '''org_tree : heading
                    | heading SEPARATOR
                    | org_tree heading SEPARATOR
                    | org_tree heading'''
        if len(p) == 2:
            p[0] = [p[1]]
        elif len(p) == 3:
            if isinstance(p[1], Heading):
                p[0] = [p[1]]
            else:
                p[0] = p[1] + [p[2]]
        elif len(p) == 4:
            p[0] = p[1] + [p[2]]

    def p_heading(self, p):
        '''heading : headline NEWLINE contents
                | headline SEPARATOR'''
        if len(p) == 4:
            p[0] = Heading(p[1], p[3])
        else:
            p[0] = Heading(p[1], contents=(None, None, None))

    def p_headline(self, p):
        '''headline : STARS SPACE comment todo priority title cookie tags'''
        p[0] = Headline(level=p[1], comment=bool(p[3]), todo=p[4], priority=p[5], title=p[6], cookie=p[7], tags=p[8],
                        todos=self.lexer.todos)

    def p_comment(self, p):
        '''comment : COMMENT SPACE
                | empty'''
        p[0] = p[1] if len(p) > 2 else None

    def p_todo(self, p):
        '''todo : TODO SPACE
                | empty'''
        p[0] = p[1] if len(p) > 2 else None

    def p_priority(self, p):
        '''priority : PRIORITY SPACE
                    | empty'''
        p[0] = p[1] if len(p) > 2 else None

    def p_title(self, p):
        """title : TEXT 
                 | TODO
                 | title TODO
                 | title TEXT
                 | title SPACE TEXT
                 | title SPACE TODO
                 | title SPACE
                 | empty"""
        none_to_empty = [x if x else "" for x in p[1:]]
        p[0] = reduce(add, none_to_empty, "").strip()

    def p_cookie(self, p):
        '''cookie : COOKIE SPACE
                  | COOKIE
                  | empty'''
        p[0] = p[1] if len(p) > 1 else None

    def p_tags(self, p):
        '''tags : TAGS
                | empty''' 
        if p[1] is not None:
            p[0] = [x for x in p[1].split(':') if x != '']
        else:
            p[0] = None

    def p_contents(self, p):
        '''contents : scheduling drawers body'''
        p[0] = (p[1], p[2], p[3])

    def p_scheduling_data(self, p):
        '''scheduling_data : SCHEDULING SPACE any_timestamp NEWLINE
                        | SCHEDULING SPACE any_timestamp SEPARATOR
                        | SCHEDULING SPACE any_timestamp SPACE
                        | scheduling_data SCHEDULING SPACE any_timestamp NEWLINE
                        | scheduling_data SCHEDULING SPACE any_timestamp SEPARATOR
                        | scheduling_data SCHEDULING SPACE any_timestamp SPACE'''
        if len(p) > 5:
            p[0] = reduce(add, [p[1], Scheduling(p[2], timestamp=p[4])])
        elif len(p) > 2:
            p[0] = Scheduling(p[1], timestamp=p[3])
        else:
            p[0] = None

    def p_scheduling(self, p):
        '''scheduling : scheduling_data
                    | empty'''
        p[0] = p[1]

    def p_any_timestamp(self, p):
        '''any_timestamp : ATIMESTAMP
                        | ITIMESTAMP'''
        p[0] = TimeStamp(p[1])

    def p_drawer_data(self, p):
        '''drawer_data : DRAWER NEWLINE
                    | DRAWER SEPARATOR
                    | drawer_data DRAWER NEWLINE
                    | drawer_data DRAWER SEPARATOR'''
        if len(p) == 4:
            p[0] = ([d for d in p[1] if d is not None]) + ([Drawer(p[2])])
        elif len(p) == 3:
            if type(p[1]) is list:
                p[0] = ([d for d in p[1] if d is not None]) + ([Drawer(p[2])])
            else:
                p[0] = ([Drawer(p[1])])
        else:
            if type(p[1]) is str:
                p[0] = ([Drawer(p[1])])
            else:
                p[0] = ([])

    def p_drawers(self, p):
        '''drawers : drawer_data
                | empty'''
        p[0] = p[1]

    def p_body(self, p):
        '''body : body_text
                | empty'''
        p[0] = p[1]

    def p_non_metadata_body_text(self, p):
        '''non_metadata_body_text : TEXT
                                | SPACE
                                | any_timestamp
                                | non_metadata_body_text TEXT
                                | non_metadata_body_text SPACE
                                | non_metadata_body_text special_token
                                | non_metadata_body_text NEWLINE''' 
        p[0] = reduce(add, map(str, p[1:]))

    def p_special_token(self, p):
        '''special_token : SCHEDULING
                        | COOKIE
                        | PRIORITY
                        | TODO
                        | any_timestamp
                        | COMMENT
                        | TAGS'''
        p[0] = p[1]

    def p_body_text(self, p):
        '''body_text : TEXT
                    | SPACE
                    | METADATA
                    | special_token
                    | body_text TEXT
                    | body_text SPACE
                    | body_text special_token
                    | body_text METADATA
                    | body_text NEWLINE'''
        p[0] = reduce(add, map(str, p[1:]))

    def p_empty(self, p):
        'empty :' 
        pass

    def p_error(self, p):
        if p is not None:
            print(f'Syntax error: {p}')
            raise ValueError("Parser error!")
