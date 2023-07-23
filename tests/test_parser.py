from orgmunge import Org
from orgmunge.classes import *
from orgmunge.lexer import all_todo_keywords
from itertools import product

def test_parsing_headlines():
    def ctor_arg(arg):
        return arg if arg != '' else None
    comments = ['COMMENT ', '']
    todos = [f'{todo}' for todo in all_todo_keywords.values()] + ['']
    priorities = ['[#A] ', '[#B] ', '[#C] ', '']
    titles = ['My heading']
    cookies = ['[1/2]', '[50%]', '']
    tags = [':tag1:', ':tag1:tag2:', '']
    for comment, todo, priority, title, cookie, tag in product(comments, todos, priorities, titles, cookies, tags):
        headline_string = f'* {comment}{todo}{" " if todo != "" else ""}{priority}{title} {cookie}{10 * " " if tag != "" else ""}{tag}\n'
        parsed = Org(headline_string, from_file=False)
        parsed_headline = parsed.root.children[0].headline
        assert parsed_headline == Headline(level='* ',
                                           comment=(len(comment) > 0),
                                           todo=ctor_arg(todo),
                                           priority=ctor_arg(priority),
                                           title=title,
                                           cookie=ctor_arg(cookie),
                                           tags=[t for t in tag.split(':') if t != ''])
    
