
import mysql_proc as sql

from flask import *  # 必要なライブラリのインポート
import random
import datetime
import logging
app = Flask(__name__)  # アプリの設定

LOGFILE = "/access.log"
file_handler = logging.FileHandler(LOGFILE)
file_handler.setLevel(logging.DEBUG)
file_handler.setLevel(logging.ERROR)
file_handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
app.logger.setLevel(logging.DEBUG)
app.logger.setLevel(logging.ERROR)
app.logger.setLevel(logging.INFO)
app.logger.addHandler(file_handler)


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

@app.route("/")  # どのページで実行する関数か設定
def main():
    return "Hello, World! I am iron man"  # Hello, World! を出力

@app.route("/ratio", methods=["GET", "POST"])
def ratiopage():
    battle_count = sql.getBattleCount()
    win_count = sql.getBattleCountForResult("win")
    win_ratio = float(win_count) / battle_count
    return "your win ratio is " + formatRatio(win_ratio)

@app.route("/rps", methods=["GET", "POST"])
def rpspage():
    return render_template("rps_form.html")

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

    res,duel_val,duel_time = duel(get_name,get_val)

    return render_template('rps_result.html'
        , get_val=get_val
        , duel_val=duel_val
        , res = res
        , duel_time=duel_time
    )

if __name__ == "__main__":  # 実行されたら
    app.run(debug=True, host='0.0.0.0', port=80, threaded=True)
