"""
Example snippets which should roundtrip and produce
an identical result.
"""

from orgmunge import Org
import pytest


EXAMPLE_1 = """\
* Calculation TODO 
** Input
3+4+5+6
** Evaluation
"""


@pytest.mark.parametrize("text", (EXAMPLE_1,))
def test_roundtrip(text):
    parsed = Org(EXAMPLE_1, from_file=False)

    # Doesn't produce errors when roundtripped
    Org(str(parsed), from_file=False)

    # Produces identical output roundtripped
    assert str(parsed) == EXAMPLE_1
