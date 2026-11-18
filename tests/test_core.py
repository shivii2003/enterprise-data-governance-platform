from app.core import validate,authorize
def test_rules():
    assert validate([{'id':None}],['id'])==[(0,'id')]
    assert not authorize('viewer','restricted')
