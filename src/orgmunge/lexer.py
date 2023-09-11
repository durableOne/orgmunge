#!/usr/bin/env python3

import ply.lex as lex
import json
import os
import re

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

def t_error(t):
    print(f"Illegal character encountered: {t.value[0]}")
    t.lexer.skip(1)

def get_todos():
    base_file_name = 'todos.json'
    current_dir_file = os.path.join(os.getcwd(), base_file_name)
    home_dir_file = os.path.join(os.environ['HOME'], base_file_name)
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

todos_dict = get_todos()
all_todo_keywords = {**todos_dict['todo_states'], **todos_dict['done_states']}

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

TODO = fr'(?:{"|".join(list(all_todo_keywords.values()))})'

def t_METADATA(t):
    r'(?:^\#\+[^:\n]+:[^\n]*\n)*^\#\+[^:\n]+:[^\n]*'
    return t

@lex.TOKEN(ATIMESTAMP)
def t_ATIMESTAMP(t):
    return t
    
@lex.TOKEN(ITIMESTAMP)
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
    r'\n+(?=\*+\s|\Z)'
    return t

def t_NEWLINE(t):
    r'\n+'
    return t

def t_TAGS(t):
    r'(?::\S+)+:'
    return t

def t_SPACE(t):
    r'[ \t]+'
    return t

def t_TEXT(t):
    r'\S+'
    return t

lexer = lex.lex(optimize=False, reflags=re.DOTALL|re.MULTILINE)
