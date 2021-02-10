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
LOG_FILE = '/applog_sqlalchemy.log'

#------------------------------------------------------------------------------
#-
#- Logger
#-
#------------------------------------------------------------------------------

logging.basicConfig()
sqlalchemy_logger = logging.getLogger('sqlalchemy.engine')
sqlalchemy_logger.setLevel(logging.INFO)
get_handler = logging.FileHandler(LOG_FILE)
sqlalchemy_logger.addHandler(get_handler)

#------------------------------------------------------------------------------
#-
#- DB function
#-
#------------------------------------------------------------------------------

def getEngineKey(db_name):
    return "mysql://"+ROOT_USER+":"+ROOT_PASS+"@"+ROOT_HOST+"/" + db_name

def getEngineRps():
    engine_key = getEngineKey(DB_NAME_RPS)
    engine=create_engine(engine_key)

    return engine

def getSession(engine):
    SessionClass=sessionmaker(engine)
    session=SessionClass()
    return session

rps_engine = getEngineRps()
Base=declarative_base()


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


def getBattleCount():
    session = getSession(rps_engine)
    count_total = session.query(func.count(BattleHistory.result)).first()
    #.filter(battle_history.result=="win")
    session.close()
    return count_total[0]

def getBattleCountForResult(res):
    session = getSession(rps_engine)
    count_total = session.query(func.count(BattleHistory.result)) \
    .filter(BattleHistory.result==res).first()
    session.close()
    return count_total[0]


def rpsInsert(br:BattleResult ):
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

def recordedBattleResult(name,choice_id,result):
    br=BattleResult()
    br.time_now = datetime.datetime.now()
    br.name = name
    br.choice_id = choice_id
    br.result = result
    rpsInsert(br) 



if __name__ == '__main__':
    #recordedBattleResult("SS",1,"win")
    battle_count = getBattleCount()
    win_count = getBattleCountForResult("win")
    victory_ratio = float(win_count) / battle_count
    print("your victory ratio is " +  format(victory_ratio, '.2f'))
    
