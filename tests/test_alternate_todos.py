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
