#!/usr/bin/env python3

import ply.lex as lex
import re

class Lexer:
    tokens = ('ATIMESTAMP',
            'ITIMESTAMP',
            'DRAWER',
            'SCHEDULING',
            'COOKIE',
            'PRIORITY',
            'TODO',
            'STARS',
            'COMMENT',
            'SPACE',
            'NEWLINE',
            'TAGS',
            'TEXT',
            'SEPARATOR',
            'METADATA',)
    DATE = r'[1-9][0-9]{3}-(?:0[1-9]|1[0-2])-(?:0[1-9]|[12][0-9]|3[01])'
    hours_regex = r'(?:0[0-9]|1[0-9]|2[0-3])'
    minutes_regex = r'[0-5][0-9]'
    TIME = fr'{hours_regex}:{minutes_regex}'
    REPEATER = r'[.+]?\+[0-9]+[hdwmy]'
    DEADWARN = r'-[0-9]+[hdwmy]'
    DAYOFWEEK = r'(?:Mon|Tue|Wed|Thu|Fri|Sat|Sun)'
    TIMESTAMP = fr'({DATE})\s({DAYOFWEEK})(\s{TIME})?(-{TIME})?(\s{REPEATER})?(\s{DEADWARN})?' 
    ATIMESTAMP = fr'<{TIMESTAMP}>'
    ITIMESTAMP = fr'\[{TIMESTAMP}\]'

    def __init__(self, todos):

        def t_error(t):
            print(f"Illegal character encountered: {t.value[0]}")
            raise ValueError("Lexer error!")

        self.todos = todos
        all_todo_keywords = {**todos['todo_states'], **todos['done_states']}
        TODO = fr'(?:{"|".join(list(all_todo_keywords.values()))})'

        def t_METADATA(t):
            r'(?:^\#\+[^:\n]+:[^\n]*\n)*^\#\+[^:\n]+:[^\n]*'
            return t

        @lex.TOKEN(self.ATIMESTAMP)
        def t_ATIMESTAMP(t):
            return t

        @lex.TOKEN(self.ITIMESTAMP)
        def t_ITIMESTAMP(t):
            return t

        def t_DRAWER(t):
            r'^\s*:[^:]+:.+?:(?:end|END):'
            return t

        def t_SCHEDULING(t):
            r'(?:CLOSED|SCHEDULED|DEADLINE):'
            return t

        def t_COOKIE(t):
            r'\[(?:[0-9]*/[0-9]*|[0-9]*%)\]'
            return t

        def t_PRIORITY(t):
            r'\[\#(?:A|B|C)\]'
            return t

        @lex.TOKEN(TODO)
        def t_TODO(t):
            return t

        def t_STARS(t):
            r'^\*+(?=\s)'
            return t

        def t_COMMENT(t):
            r'COMMENT'
            return t

        # Needed to distinguish a regular newline from one that starts a new heading or ends the file
        def t_SEPARATOR(t):
            r'(?:\r?\n)+(?=\*+\s|\Z)'
            return t

        def t_NEWLINE(t):
            r'\r?\n+'
            return t

        def t_TAGS(t):
            r'(?::\S+)+:'
            return t

        def t_SPACE(t):
            r'[^\S\r\n]+'
            return t

        def t_TEXT(t):
            r'\S+'
            return t

        token_funcs = [func for func in locals() if func.startswith('t_')]
        for func in token_funcs:
            setattr(self, func, locals()[func])

        self.lexer = lex.lex(module=self, reflags=re.DOTALL|re.MULTILINE)

