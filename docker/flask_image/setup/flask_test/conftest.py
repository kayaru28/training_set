import pytest
import mysql_proc as mysql_proc

#------------------------------------------------------------------------------
#-
#- Fixture
#-
#------------------------------------------------------------------------------


@pytest.fixture(scope='function')
def all_delete_battle_history():
    print('function')
    engine = mysql_proc.rps_engine
    session = mysql_proc.getSession(engine)
    session.query(mysql_proc.BattleHistory).delete()
    session.commit()
    session.close()







