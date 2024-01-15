"""
Example snippets which should roundtrip and produce
an identical result.
"""

from orgmunge import Org
import pytest


@pytest.fixture
def todo_and_done_states():
    return {
        "todo_states": {"todo": "TODO"},
        "done_states": {"done": "DONE"},
    }


EXAMPLES = (
    """\
* TODO Calculation
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
*     :atitlewithjustatag:
"""
)


@pytest.mark.parametrize("text", EXAMPLES)
def test_roundtrip(text, todo_and_done_states):
    # Shouldn't produce errors when parsed
    parsed = Org(text, from_file=False, todos=todo_and_done_states)

    # Shouldn't produce errors when roundtripped
    Org(str(parsed), from_file=False, todos=todo_and_done_states)

    # Should produce identical output roundtripped
    assert str(parsed) == text


def test_roundtrip_after_adding_child(todo_and_done_states):
    parent_note = Org("* N1\n", from_file=False, todos=todo_and_done_states)
    child_note = Org("* N2\n", from_file=False, todos=todo_and_done_states)
    parent_note.root.children[0].add_child(child_note.root)
    assert "* N1\n* N2\n" == str(parent_note)
