import random
import datetime
from sqlalchemy import func
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
#from sqlalchemy import distinct
root_user = "root"
root_pass = "Root-0904"
root_host = "localhost"
db_name_rps = "rps"


#------------------------------------------------------------------------------
#-
#- DB function
#-
#------------------------------------------------------------------------------

def getEngineKey(db_name):
    return "mysql://"+root_user+":"+root_pass+"@"+root_host+"/" + db_name

class BattleResult():
    time_now = datetime.datetime.now()
    name = "NA"
    choice_id = 0
    result = ""

def getEngineRps():
    engine_key = getEngineKey(db_name_rps)
    engine=create_engine(engine_key)

    return engine

rps_engine = getEngineRps()
Base=declarative_base(bind=rps_engine)

class BattleHistory(Base):
    __tablename__="battle_history" 
    __table_args__={"autoload": True}

def getSession(engine):
    SessionClass=sessionmaker(engine)
    session=SessionClass()
    return session

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
    
