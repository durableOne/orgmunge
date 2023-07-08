from orgmunge import Org

def test_can_read_org():
    test = Org("./README.org")
    assert test

from orgmunge import Org

CONTENT = "* You can write orgfiles!!\n"

def test_save_org(tmp_path):
    p = tmp_path / "testtmp.org"
    assert len(list(tmp_path.iterdir())) == 0 # Nothing exists here
    test = Org(CONTENT, from_file=False)
    test.write(p)
    assert len(list(tmp_path.iterdir())) == 1 # testtmp. org exists
    assert p.read_text().strip(" \n") == CONTENT.strip(" \n") # Since org is plaintext these should be identical?
