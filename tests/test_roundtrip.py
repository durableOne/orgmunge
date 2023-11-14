"""
Example snippets which should roundtrip and produce
an identical result.
"""

from orgmunge import Org
import pytest


EXAMPLES = (
    """\
* Calculation TODO
** Input
3+4+5+6
** Evaluation
""",
    """\
* Parse{}weird characters

There is a weird {} character {} between 2 of these words.
""".format(chr(160), chr(8239), chr(160)),
"""\
* A normal title
* TODO A title with the -- word TODO in the title which triggers a syntax error
* TODO Another normal title.
""",
"""\
* :atitlewithjustatag:
"""
)


@pytest.mark.parametrize("text", EXAMPLES)
def test_roundtrip(text):
    fake_todos = {
        "todo_states": {"fake_todo": "TDO"},
        "done_states": {"fake_done": "DNE"},
    }
    parsed = Org(text, from_file=False, todos=fake_todos)

    # Doesn't produce errors when roundtripped
    Org(str(parsed), from_file=False, todos=fake_todos)

    # Produces identical output roundtripped
    assert str(parsed) == text
