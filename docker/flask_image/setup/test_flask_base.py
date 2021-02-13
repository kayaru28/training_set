import pytest
import flask_base as flaskb


#------------------------------------------------------------------------------
#-
#- Test for Normal Function
#-
#------------------------------------------------------------------------------


def test_formatRatio():
    assert "0.12" == flaskb.formatRatio(0.1234)

def test_getMachineChoice():

    dict_count = {
        0 : 0,
        1 : 0,
        2 : 0
    }

    num_iteration = 10000
    for iter in range(num_iteration):
        choice_id = flaskb.getMachineChoice()
        dict_count[choice_id] = dict_count[choice_id] + 1
        

    assert dict_count[0]+dict_count[1]+dict_count[2] == num_iteration
    assert abs(dict_count[0] - dict_count[1]) <= num_iteration * 0.05
    assert abs(dict_count[0] - dict_count[2]) <= num_iteration * 0.05
    assert abs(dict_count[1] - dict_count[2]) <= num_iteration * 0.05


@pytest.mark.parametrize(
    "client_choice,result,expectresult", [
        (0, "draw", 0),
        (1, "draw", 1),
        (2, "draw", 2),
        (0, "win", 2),
        (1, "win", 0),
        (2, "win", 1),
        (0, "loose", 1),
        (1, "loose", 2),
        (2, "loose", 0),
    ]
)
def test_calcMachineChoiceFromResult(
        client_choice,result,expectresult
    ):
    assert flaskb.calcMachineChoiceFromResult(client_choice,result) == expectresult

@pytest.mark.parametrize(
    "client_choice,machine_choice,expectresult", [
        (0, 0, "draw"),
        (1, 1, "draw"),
        (2, 2, "draw"),
        (0, 2, "win"),
        (1, 0, "win"),
        (2, 1, "win"),
        (0, 1, "loose"),
        (1, 2, "loose"),
        (2, 0, "loose"),
    ]
)
def test_judgeBattleResult(
        client_choice,machine_choice,expectresult
    ):
    assert flaskb.judgeBattleResult(client_choice,machine_choice) == expectresult

def test_arg_procRpsBattle(mocker):
    judgeBattleResult = mocker.patch('flaskb.judgeBattleResult')
    recordedBattleResult = mocker.patch('flaskb.sql.recordedBattleResult')

    result_html = flaskb.procRpsBattle(client_name,client_choice)



#------------------------------------------------------------------------------
#-
#- Test for Root
#-
#------------------------------------------------------------------------------


def test_flask_root_root():
    flaskb.app.config['TESTING'] = True
    client  = flaskb.app.test_client()
    ans     = b"I am iron man!!!!"
    result = client.get('/')
    assert ans == result.data

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















