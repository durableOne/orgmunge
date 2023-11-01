from orgmunge import Org
from orgmunge.classes import Headline, Cookie

def test_alternate_todos():
    parsed = Org('* NEXT Some task [1/2]\n', from_file=False,
                 todos = {'todo_states': {'todo': 'TODO',
                                          'next': 'NEXT'},
                          'done_states': {'done': 'DONE'}})
    assert parsed.root.children[0].headline == Headline(parsed.todos,
                                                        level='* ',
                                                        comment=False,
                                                        todo='NEXT',
                                                        priority=None,
                                                        title='Some task',
                                                        cookie='[1/2]',
                                                        tags=None)

def test_todos_from_file():
    parsed = Org('''#+TODO: FOO | BAR
* FOO Some heading
* BAR Some other heading
''', from_file=False)
    assert parsed.root.children[0].headline == Headline(parsed.todos,
                                                        level='* ',
                                                        comment=False,
                                                        todo='FOO',
                                                        priority=None,
                                                        title='Some heading',
                                                        cookie=None,
                                                        tags=None,)
    assert parsed.root.children[1].headline == Headline(parsed.todos,
                                                        level='* ',
                                                        comment=False,
                                                        todo='BAR',
                                                        priority=None,
                                                        title='Some other heading',
                                                        cookie=None,
                                                        tags=None,)
    assert parsed.root.children[0].done == False
    assert parsed.root.children[1].done == True
