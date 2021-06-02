import random
import datetime
from os import environ
from sqlalchemy import func
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import Column
from sqlalchemy.types import VARCHAR, Integer, TIMESTAMP

import logging
#from sqlalchemy import distinct
ROOT_USER = "root"
ROOT_PASS = environ['root_password']
ROOT_HOST = "mysql"
DB_NAME_RPS = "rps"



#------------------------------------------------------------------------------
#-
#- Logger
#-
#------------------------------------------------------------------------------

LOG_DIR  = "/log"
LOG_FILE = LOG_DIR + "/applog_sqlalchemy.log"

from flask_fluentd_handler import FlaskFluentHandler
FLUENTD_TAG  = 'sql-alchemy'
FLUENTD_PORT = 24221
fluent_handler = FlaskFluentHandler(tag=FLUENTD_TAG, host='fluentd', port=FLUENTD_PORT)

logging.basicConfig()
sqlalchemy_logger = logging.getLogger('sqlalchemy.engine')
sqlalchemy_logger.setLevel(logging.INFO)
get_handler = logging.FileHandler(LOG_FILE)

sqlalchemy_logger.addHandler(get_handler)
sqlalchemy_logger.addHandler(fluent_handler)



#------------------------------------------------------------------------------
#-
#- DB function
#-
#------------------------------------------------------------------------------

# general -------------------------

Base=declarative_base()

def getEngineKey(user,password,host,db_name):
    return "mysql://"+user+":"+password+"@"+host+"/" + db_name


def getSession(engine):
    SessionClass=sessionmaker(engine)
    session=SessionClass()
    return session

class BattleResult():
    time_now = datetime.datetime.now()
    name = "NA"
    choice_id = 0
    result = ""

class BattleHistory(Base):
    __tablename__ = "battle_history"
    time        = Column(TIMESTAMP, primary_key=True)
    id          = Column(Integer, primary_key=True)
    name        = Column(VARCHAR(10))
    choice_id   = Column(Integer)
    result      = Column(VARCHAR(10))


class BattleCount(Base):
    __tablename__ = "battle_count"
    name           = Column(VARCHAR(10), primary_key=True)
    battle_count   = Column(Integer)

# spacial -------------------------

def getEngineRps():
    engine_key = getEngineKey(ROOT_USER,ROOT_PASS,ROOT_HOST,DB_NAME_RPS)
    engine=create_engine(engine_key)

    return engine

rps_engine = getEngineRps()


def rpsCount(**kwargs):
    session = getSession(rps_engine)

    count_query = session.query(func.count(BattleHistory.result))

    if( "result" in kwargs):
        bh_result = kwargs["result"]
        count_query = count_query.filter(BattleHistory.result==bh_result)

    count_total = count_query.first()

    session.close()
    return count_total[0]

def rpsSelectBattleCountForName(username):
    session = getSession(rps_engine)
    battle_count = session.query(BattleCount.battle_count).filter(BattleCount.name==username).first()
    session.close()
    return battle_count[0]

def rpsInsertBattleResult(br:BattleResult ):
    session = getSession(rps_engine)
    tmpid = getRandomId9()
    insert_battle_history=BattleHistory(
        id          = tmpid,
        time        = br.time_now,
        name        = br.name,
        choice_id   = br.choice_id,
        result      = br.result
    )
    session.add(insert_battle_history)
    session.commit()
    session.close()

#------------------------------------------------------------------------------
#-
#- Standerd function
#-
#------------------------------------------------------------------------------


def getRandomId9():
    return int(random.random()*1000000000)


#------------------------------------------------------------------------------
#-
#- Proc function
#-
#------------------------------------------------------------------------------


def rpsGetBattleCountAll():
    return rpsCount()
    
def rpsGetBattleCountForResult(res):
    return rpsCount(result=res)
    
def recordedBattleResult(name,choice_id,result):
    br=BattleResult()
    br.name = name
    br.choice_id = choice_id
    br.result = result
    rpsInsertBattleResult(br) 



if __name__ == '__main__':
    #recordedBattleResult("SS",1,"win")
    battle_count = rpsGetBattleCountAll()
    win_count = rpsGetBattleCountForResult("win")
    victory_ratio = float(win_count) / battle_count
    print("your victory ratio is " +  format(victory_ratio, '.2f'))
    
