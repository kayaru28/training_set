
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

def duel(get_name,get_val):
    duel_val = int(random.random()*3)
    if get_val == duel_val:
        res = "draw"
    elif get_val == 0 and duel_val == 2:
        res = "win"
    elif get_val > duel_val:
        res = "win"
    else:
        res = "loose"

    duel_time = datetime.datetime.today().strftime("%Y/%m/%d/%H/%M/%S")
    sql.recordedBattleResult(get_name,get_val,res)

    return res,duel_val,duel_time

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
    get_name = request.args.get('name', default='noname')
    get_val = request.args.get('value', default=0, type=int)
    res,duel_val,duel_time = duel(get_name,get_val)
    return render_template('rps_result.html'
        , get_val=get_val
        , duel_val=duel_val
        , res = res
        , duel_time=duel_time
    )
    
@app.route("/rps_result", methods=["GET", "POST"])
def rpsResultpage():
    get_name = request.form["name"]
    get_val = int(request.form["value"])

    session['user_name'] = get_name

    res,duel_val,duel_time = duel(get_name,get_val)

    return render_template('rps_result.html'
        , get_val=get_val
        , duel_val=duel_val
        , res = res
        , duel_time=duel_time
    )

@app.route("/ratio", methods=["GET", "POST"])
def ratiopage():
    battle_count = sql.rpsGetBattleCountAll()
    win_count = sql.rpsGetBattleCountForResult("win")
    win_ratio = float(win_count) / battle_count
    return "your win ratio is " + formatRatio(win_ratio)


if __name__ == "__main__":  # 実行されたら
    app.run(debug=True, host='0.0.0.0', port=80, threaded=True)
