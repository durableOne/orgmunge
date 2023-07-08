def test_import():
    try:
        import orgmunge
        assert True
    except ImportError:
        assert False
