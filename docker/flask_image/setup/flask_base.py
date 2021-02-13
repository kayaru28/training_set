
import mysql_proc as sql
from logging import FileHandler,getLogger
from flask import *  
import random
import datetime
from os import environ

LOG_FILE = '/applog_flask.log'

app = Flask(__name__)  
app.secret_key = environ['root_password']

get_handler = FileHandler(LOG_FILE)
werkzeug_logger = getLogger("werkzeug")
werkzeug_logger.addHandler(get_handler)


def formatRatio(ratio):
    return format(ratio, '.2f')

def getMachineChoice():
    return int(random.random()*3)

def calcMachineChoiceFromResult(client_choice,result):
    if result == "draw":
        return client_choice
    elif client_choice == 0:
        if result == "win":
            return 2
        elif result == "loose":
            return 1
    elif client_choice == 1:
        if result == "win":
            return 0
        elif result == "loose":
            return 2
    elif client_choice == 2:
        if result == "win":
            return 1
        elif result == "loose":
            return 0
    return -1

def judgeBattleResult(client_choice,machine_choice):
    if client_choice == machine_choice:
        return "draw"
    elif client_choice == 0 and machine_choice == 2:
        return "win"
    elif client_choice == 2 and machine_choice == 0:
        return "loose"
    elif client_choice > machine_choice:
        return "win"
    else:
        return "loose"

def procRpsBattle(client_name,client_choice):

    result = judgeBattleResult(client_choice, getMachineChoice() )
    sql.recordedBattleResult(client_name,client_choice,result)

    return render_template('rps_result.html'
        , get_val=client_choice
        , duel_val=calcMachineChoiceFromResult(client_choice,result)
        , res = result
    )



#------------------------------------------------------------------------------
#-
#- Rootting
#-
#------------------------------------------------------------------------------



@app.route("/") 
def main():
    return "I am iron man!!!!"

@app.route("/rps", methods=["GET", "POST"])
def rpspage():
    if 'user_name' in session:
        shown_name = session['user_name']
    else:
        shown_name = "noname"
    return render_template("rps_form.html",user_name=shown_name)

@app.route("/rpsapi", methods=["GET"])
def rpsapi():
    client_name = request.args.get('name', default='noname')
    client_choice = request.args.get('value', default=0, type=int)

    return procRpsBattle(client_name,client_choice)
    
@app.route("/rps_result", methods=["GET", "POST"])
def rpsResultpage():
    client_name = request.form["name"]
    client_choice = int(request.form["value"])

    session['user_name'] = client_name

    return procRpsBattle(client_name,client_choice)

@app.route("/ratio", methods=["GET", "POST"])
def ratiopage():
    battle_count = sql.rpsGetBattleCountAll()
    win_count = sql.rpsGetBattleCountForResult("win")
    win_ratio = float(win_count) / battle_count
    return "your win ratio is " + formatRatio(win_ratio)


if __name__ == "__main__":  # 実行されたら
    app.run(debug=True, host='0.0.0.0', port=80, threaded=True)
