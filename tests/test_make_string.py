from orgmunge import Org

def test_make_org():
    test = Org('* TODO Something important\n', from_file=False)
    assert test
