from orgmunge import Org

def test_get_heading_by_path():
     parsed = Org('./tests/files/regr.org')
     heading = next(parsed.filter_headings(lambda h: h.level == 3))
     heading_path = [x.title for x in [heading.parent.parent, heading.parent, heading]]
     assert heading is parsed.get_heading_by_path(heading_path, exact=True)
