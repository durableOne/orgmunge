#!/usr/bin/env python3

import re
import ply.lex as lex
from itertools import chain
import json
import os

def elapsed_time_regex():
    hours_regex = r'(?:0[1-9]|1[0-9]|2[0-3])'
    minutes_regex = r'[0-5][0-9]'
    return fr'{hours_regex}:{minutes_regex}'
def timestamp_regex():
    elapsed_time = elapsed_time_regex()
    return fr'\s+(?:\s+{elapsed_time}(?:-{elapsed_time})?)?(?:\s+[.+]?\+[0-9]+[hdwmy])?'

def active_timestamp_regex():
    return fr'<{timestamp_regex()}>'

def inactive_timestamp_regex():
    return fr'\[{timestamp_regex()}\]'

tokens = ('DATE',
          'TIME',
          'REPEATER',
          'DEADWARN',
          'DAYOFWEEK',
          'DRAWER',
          'SCHEDULING',
          'COOKIE',
          'PRIORITY',
          'TODO',
          'STARS',
          'COMMENT',
          'SPACE',
          'DASH',
          'NEWLINE',
          'LBRACK',
          'RBRACK',
          'LSQUARE',
          'RSQUARE',
          'COLON',
          'TEXT',
          'SEPARATOR',
          'METADATA',)

def t_error(t):
    print(f"Illegal character encountered: {t.value[0]}")
    t.lexer.skip(1)

def get_todos():
    input_file_name = 'todos.json'
    if os.path.isfile(input_file_name):
        with open(input_file_name, 'rb') as JSON:
            return json.load(JSON)
    else:
        return {'todo_states':
                {'todo': '',
                 'next': '',
                 'wait': '',},
                'done_states': 
                {'cncl': '',
                 'done': '',}}


all_todo_keywords = {**get_todos()['todo_states'], **get_todos()['done_states']}

t_DATE = r'[1-9][0-9]{3}-(?:0[1-9]|1[0-2])-(?:0[1-9]|[12][0-9]|3[01])'
t_TIME = elapsed_time_regex() 
t_REPEATER = '[.+]?\+[0-9]+[hdwmy]'
t_DEADWARN = '-[0-9]+[hdwmy]'
t_DAYOFWEEK = r'(?:Mon|Tue|Wed|Thu|Fri|Sat|Sun)'
t_DRAWER = r'(?ism)^\s*:[^:]+:.+?:end:'
t_SCHEDULING = r'(?:CLOSED|SCHEDULED|DEADLINE):'
t_COOKIE = r'\[(?:[0-9]+/[1-9][0-9]*|[0-9]%)\]'
t_PRIORITY = r'\[\#(?:A|B|C)\]'
t_TODO = fr'(?:{"|".join(all_todo_keywords)})'
t_STARS = r'^\*+'
t_COMMENT = r'COMMENT'
t_NEWLINE = r'\n+'
t_SPACE = r"\s+"
t_DASH = r"(?<=\d)[-](?=\d)"
t_LBRACK = '[<]'
t_RBRACK = '[>]'
t_LSQUARE = r'[\[]'
t_RSQUARE = r'[\]]'
t_COLON = r'[:]'
t_TEXT = r'\S+'
t_SEPARATOR = r'\n+(?=\*|\Z)'
t_METADATA = r'^\#(?-s:.*)'

lexer = lex.lex(optimize=False)
