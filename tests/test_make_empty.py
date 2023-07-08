from orgmunge import Org

def test_make_empty_org():
    test = Org("\n", from_file=False)
    assert test
