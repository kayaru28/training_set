import pytest
import flask_base as flaskb

def test_flask_root_root():
    flaskb.app.config['TESTING'] = True
    client  = flaskb.app.test_client()
    ans     = b"I am iron man!!!!"
    result = client.get('/')
    assert ans == result.data

def test_formatRatio():
    assert "0.12" == flaskb.formatRatio(0.1234)

def test_root_rps():
    flaskb.app.config['TESTING'] = True
    client  = flaskb.app.test_client()
    result = client.get('/rps')
    assert b'<form action="/rps_result" method="post">' in result.data
    assert b'name : <input type="text" name="name" value=noname />' in result.data
    assert b'<fieldset>' in result.data
    assert b'<legend>Rock-paper-scissors</legend>' in result.data
    assert b'<p><label><input type="radio" name="value" value="0">rock</label></p>' in result.data
    assert b'<p><label><input type="radio" name="value" value="1">paper</label></p>' in result.data
    assert b'<p><label><input type="radio" name="value" value="2">scissors</label></p>' in result.data
    assert b'</fieldset>' in result.data
    assert b'<p><input type="submit" value="duel"><input type="reset" value="reset"></p>' in result.data
    assert b'</form> ' in result.data

def test_root_rps_with_settion():
    flaskb.app.config['TESTING'] = True
    client  = flaskb.app.test_client()
    with client.session_transaction() as sess:
        sess['user_name'] = "testname"
    result = client.get('/rps')

    assert b'name : <input type="text" name="name" value=testname />' in result.data















