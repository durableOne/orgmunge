#!/usr/bin/env python3

__package__ = 'orgmunge'
from .lexer import tokens
from .classes import *
from functools import reduce
from operator import add
import ply.yacc as yacc
import re

'''Grammar:
org_file := metadata org_tree
            | org_tree

org_tree   := heading SEPARATOR
              | org_tree heading SEPARATOR
              | org_tree heading
              | empty

heading    := headline NEWLINE contents
              | headline SEPARATOR

headline   := STARS SPACE comment todo priority title cookie tags

comment    := COMMENT SPACE
              | empty

todo       := TODO SPACE
              | empty

priority   := PRIORITY SPACE
              | empty

title      := TEXT 
              | title SPACE TEXT
              | title SPACE

cookie     := COOKIE SPACE
              | COOKIE
              | empty

tags       := COLON TEXT
              | COLON TEXT SPACE
              | empty

contents   := scheduling drawers body

scheduling := SCHEDULING SPACE any_timestamp NEWLINE
              | SCHEDULING SPACE any_timestamp SPACE scheduling
              | empty

any_timestamp :=  atimestamp
                  | itimestamp

atimestamp := LBRACK timestamp RBRACK

itimestamp := LSQUARE timestamp RSQUARE

timestamp := DATE SPACE DAYOFWEEK SPACE TIME end_time repeater deadline_warn

end_time := DASH TIME
            | empty

repeater := SPACE REPEATER
            | empty

deadline_warn := SPACE DEADWARN
                 | empty

drawers := DRAWER NEWLINE
           | drawers DRAWER NEWLINE
           | empty

body := body_text
        | empty

body_text := TEXT
             | SPACE
             | body_text TEXT
             | body_text SPACE
             | body_text NEWLINE body_text
'''

def p_org_file(p):
    '''org_file : metadata org_tree
                | org_tree'''
    if len(p) > 2:
        p[0] = (p[1], p[2])
    else:
        p[0] = ('', p[1])
          
def p_metadata(p):
    '''metadata : METADATA NEWLINE
                  | METADATA SEPARATOR
                  | metadata METADATA NEWLINE
                  | metadata METADATA SEPARATOR'''
    p[0] = reduce(add, p[1:])
    

def p_org_tree(p):
    '''org_tree : heading
                | heading SEPARATOR
                | org_tree heading SEPARATOR
                | org_tree heading
                | empty'''
    if len(p) == 2:
        p[0] = [p[1]]
    elif len(p) == 3:
        if isinstance(p[1], Heading):
            p[0] = [p[1]]
        else:
            p[0] = p[1] + [p[2]]
    elif len(p) == 4:
        p[0] = p[1] + [p[2]]

def p_heading(p):
    '''heading : headline NEWLINE contents
               | headline SEPARATOR'''
    if len(p) == 4:
        p[0] = Heading(p[1], p[3])
    else:
        p[0] = Heading(p[1], contents=(None, None, None))
    

def p_headline(p):
    '''headline : STARS SPACE comment todo priority title cookie tags'''
    p[0] = Headline(level=p[1], comment=bool(p[3]), todo=p[4], priority=p[5], title=p[6], cookie=p[7], tags=p[8])

def p_comment(p):
    '''comment : COMMENT SPACE
               | empty'''
    p[0] = p[1] if len(p) > 2 else None

def p_todo(p):
    '''todo : TODO SPACE
            | empty'''
    p[0] = p[1] if len(p) > 2 else None

def p_priority(p):
    '''priority : PRIORITY SPACE
                | empty'''
    p[0] = p[1] if len(p) > 2 else None

def p_title(p):
    """title : TEXT 
             | title SPACE TEXT
             | title SPACE"""
    p[0] = reduce(add, p[1:]).strip()

def p_cookie(p):
    '''cookie : COOKIE SPACE
              | COOKIE
              | empty'''
    p[0] = p[1] if len(p) > 1 else None

def p_tags(p):
    '''tags : COLON TEXT
            | COLON TEXT SPACE
            | empty''' # Everything after the leading colon gets parsed as TEXT
    if len(p) > 2:
        p[0] = [x for x in p[2].split(':') if x != '']
    else:
        p[0] = None

def p_contents(p):
   '''contents : scheduling drawers body'''
   p[0] = (p[1], p[2], p[3])

def p_scheduling(p):
    '''scheduling : SCHEDULING SPACE any_timestamp NEWLINE
                  | SCHEDULING SPACE any_timestamp SPACE scheduling
                  | empty'''
    if len(p) == 5:
        p[0] = Scheduling(p[1], timestamp=p[3])
    elif len(p) == 6:
        p[0] = reduce(add, [Scheduling(p[1], timestamp=p[3]), *p[5]])
    else:
        p[0] = None

def p_any_timestamp(p):
    '''any_timestamp : atimestamp
                     | itimestamp'''
    p[0] = p[1]

def p_atimestamp(p):
    '''atimestamp : LBRACK timestamp RBRACK'''
    p[0] = TimeStamp(*p[2], active=True)

def p_itimestamp(p):
    '''itimestamp : LSQUARE timestamp RSQUARE'''
    p[0] = TimeStamp(*p[2], active=False)

def p_timestamp(p):
    '''timestamp : DATE SPACE DAYOFWEEK SPACE TIME end_time repeater deadline_warn'''
    p[0] = (p[1], p[3], p[5], p[6], p[7], p[8])

def p_end_time(p):
    '''end_time : DASH TIME
                | empty'''
    p[0] = p[2] if len(p) >=3 else None

def p_repeater(p):
    '''repeater : SPACE REPEATER
                | empty'''
    p[0] = p[2] if len(p) >= 3 else None

def p_deadline_warn(p):
    '''deadline_warn : SPACE DEADWARN
                     | empty'''
    p[0] = p[2] if len(p) >= 3 else None

def p_drawers(p):
    '''drawers : DRAWER NEWLINE
               | drawers DRAWER NEWLINE
               | empty'''
    if len(p) == 4:
        p[0] = ([d for d in p[1] if d is not None]) + ([Drawer(p[2])])
    elif len(p) == 3:
        p[0] = ([Drawer(p[1])])
    else:
        p[0] = ([])

def p_body(p):
    '''body : body_text
            | empty'''
    p[0] = p[1]

def p_body_text(p):
    '''body_text : TEXT
                 | SPACE
                 | body_text TEXT
                 | body_text SPACE
                 | body_text NEWLINE body_text'''
    p[0] = reduce(add, p[1:])

def p_empty(p):
    'empty :' 
    pass

parser = yacc.yacc(write_tables=True)
