from orgmunge import Org

def test_can_read_org():
    test = Org("./README.org", debug=True)
    assert test
