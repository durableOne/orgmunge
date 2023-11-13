from orgmunge import Org

def test_can_read_org():
    test = Org("./README.org", debug=True, todos={'todo_states': {'fake_todo': 'TDO'},
                                                  'done_states': {'fake_done': 'DNE'},})
    assert test
