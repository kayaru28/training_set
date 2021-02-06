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











