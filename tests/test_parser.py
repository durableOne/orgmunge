from orgmunge import Org
from orgmunge.classes import *
from itertools import product

todos = Org('', from_file=False).todos
all_todo_keywords = {**todos['todo_states'], **todos['done_states']}
TODOS = [f'{todo}' for todo in all_todo_keywords.values()] + ['']
def test_parsing_headlines():
    def ctor_arg(arg):
        return arg if arg != '' else None
    comments = ['COMMENT ', '']
    priorities = ['[#A] ', '[#B] ', '[#C] ', '']
    titles = ['My heading']
    cookies = ['[1/2]', '[50%]', '']
    tags = [':tag1:', ':tag1:tag2:', '']
    for comment, todo, priority, title, cookie, tag in product(comments, TODOS, priorities, titles, cookies, tags):
        if cookie:
            cookie = ' ' + cookie
        headline_string = f'* {comment}{todo}{" " if todo != "" else ""}{priority}{title}{cookie}{10 * " " if tag != "" else ""}{tag}\n'
        parsed = Org(headline_string, from_file=False, todos=todos, debug=True)
        parsed_headline = parsed.root.children[0].headline
        assert parsed_headline == Headline(todos=todos,
                                           level='* ',
                                           comment=(len(comment) > 0),
                                           todo=ctor_arg(todo),
                                           priority=ctor_arg(priority),
                                           title=title,
                                           cookie=ctor_arg(cookie),
                                           tags=[t for t in tag.split(':') if t != ''])

def test_parsing_headings():
    heading = f'''* This is a sample heading
SCHEDULED: <2023-07-23 Sun 14:00>
:PROPERTIES:
:ID: my_sample_heading
:END:
Let's put some crazy content in here. For instance, all the todo keywords: {' '.join(TODOS)}.
#+something: that looks like metadata. And some priority [#A], and cookies [5%] [1/2] as well as :tags:
Now what about some formatting: *bold* /italic/ _underlined_ and =code=.
** COMMENT Child heading
:LOGBOOK:
CLOCK: [2023-07-23 Sun 10:00]--[2023-07-23 Sun 12:00] => 2:00
:END:
'''
    parsed = Org(heading, from_file=False)
    assert parsed
    main_heading = parsed.root.children[0]
    assert main_heading.children[0].headline.comment 
    assert main_heading.clocking(include_children=True) == [Clocking('2023-07-23 Sun 10:00', '2023-07-23 Sun 12:00')]
    assert main_heading.properties['ID'] == 'my_sample_heading'
    assert main_heading.done == False
    assert main_heading.todo is None
    assert main_heading.title == main_heading.headline.title
    

