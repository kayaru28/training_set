import pytest
import mysql_proc as mysql_proc
import datetime



#------------------------------------------------------------------------------
#-
#- Test Tools
#-
#------------------------------------------------------------------------------


class TestBattleResult(mysql_proc.BattleResult):
    name = "testname"
    choice_id = 1
    result = "win"

#------------------------------------------------------------------------------
#-
#- Test Function
#-
#------------------------------------------------------------------------------

def test_getEngineKey():

    get_key = mysql_proc.getEngineKey("testuser","testpass","testhost","testdb")
    assert "mysql://testuser:testpass@testhost/testdb" == get_key

def test_getEngineRps():
    get_engine = mysql_proc.getEngineRps()

    assert "mysql" == get_engine.name
    assert "mysqldb" == get_engine.driver
    assert True == get_engine.has_table("battle_history")


def test_rps_engine():
    get_engine = mysql_proc.rps_engine

    assert "mysql" == get_engine.name
    assert "mysqldb" == get_engine.driver
    assert True == get_engine.has_table("battle_history")

def test_getSession():
    engine = mysql_proc.rps_engine
    session = mysql_proc.getSession(engine)
    assert True == session.is_active
    
def test_ClassBattleResult():
    br = mysql_proc.BattleResult()
    nowdate = datetime.datetime.now()
    assert (nowdate - br.time_now ).total_seconds() <= 1

    assert br.name == "NA"
    assert br.choice_id == 0
    assert br.result == ""

    br.name = "testname"
    br.choice_id = 1
    br.result = "testresult"

    assert br.name == "testname"
    assert br.choice_id == 1
    assert br.result == "testresult"

def test_rpsInsert(
        all_delete_battle_history
    ):

    br=TestBattleResult()
    mysql_proc.rpsInsert(br)

    engine = mysql_proc.rps_engine
    session = mysql_proc.getSession(engine)
    query_result = session.query(mysql_proc.BattleHistory).all()
    session.close()

    nowdate = datetime.datetime.now()
    assert (nowdate - query_result[0].time ).total_seconds() <= 10
    assert query_result[0].name == "testname"
    assert query_result[0].choice_id == 1
    assert query_result[0].result == "win"

@pytest.mark.parametrize(
    "dictarg, expectresult1, expectresult2", [
    ({"None":"None"}, 2,3),
    ({"result":"win"}, 2,2)
])
def test_rpsCount(
        all_delete_battle_history,
        dictarg, expectresult1, expectresult2
    ):
    br=TestBattleResult()
    mysql_proc.rpsInsert(br)
    mysql_proc.rpsInsert(br)

    count_total = mysql_proc.rpsCount(**dictarg)
    assert count_total == expectresult1

    br.result = "loose"
    mysql_proc.rpsInsert(br)
    count_total = mysql_proc.rpsCount(**dictarg)
    assert count_total == expectresult2


#- test for Proc function -------------------------------------------

def test_rpsGetBattleCountAll(
        all_delete_battle_history
    ):
    br=TestBattleResult()
    mysql_proc.rpsInsert(br)
    mysql_proc.rpsInsert(br)
    assert mysql_proc.rpsGetBattleCountAll() == 2

    mysql_proc.rpsInsert(br)
    assert mysql_proc.rpsGetBattleCountAll() == 3
    
def test_rpsGetBattleCountForResult(
        all_delete_battle_history
    ):
    br=TestBattleResult()
    mysql_proc.rpsInsert(br)
    mysql_proc.rpsInsert(br)
    br.result = "loose"
    mysql_proc.rpsInsert(br)
    assert mysql_proc.rpsGetBattleCountForResult("win") == 2
    assert mysql_proc.rpsGetBattleCountForResult("loose") == 1

def test_recordedBattleResult(
        all_delete_battle_history
    ):

    mysql_proc.recordedBattleResult("testname",1,"win")

    engine = mysql_proc.rps_engine
    session = mysql_proc.getSession(engine)
    query_result = session.query(mysql_proc.BattleHistory).all()
    session.close()

    nowdate = datetime.datetime.now()
    assert (nowdate - query_result[0].time ).total_seconds() <= 10
    assert query_result[0].name == "testname"
    assert query_result[0].choice_id == 1
    assert query_result[0].result == "win"
















