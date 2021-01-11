
import mysql_proc as sql

from flask import *  # 必要なライブラリのインポート
import random
import datetime
app = Flask(__name__)  # アプリの設定

def formatRatio(ratio):
    return format(ratio, '.2f')

@app.route("/")  # どのページで実行する関数か設定
def main():
    return "Hello, World! I am iron man"  # Hello, World! を出力

@app.route("/formrm", methods=["GET", "POST"])
def formpage():
    return render_template("form.html")

@app.route("/test", methods=["GET", "POST"])
def testpage():
    return render_template("test.html")

@app.route("/ratio", methods=["GET", "POST"])
def ratiopage():
    battle_count = sql.getBattleCount()
    win_count = sql.getBattleCountForResult("win")
    win_ratio = float(win_count) / battle_count
    return "your win ratio is " + formatRatio(win_ratio)

@app.route("/rps", methods=["GET", "POST"])
def rpspage():
    return render_template("rps_form.html")

@app.route("/rps_result", methods=["GET", "POST"])
def rpsResultpage():
    get_val = int(request.form["value"])
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

    sql.recordedBattleResult("GUEST",get_val,res)
    return render_template('rps_result.html'
        , get_val=get_val
        , duel_val=duel_val
        , res = res
        , duel_time=duel_time
    )

if __name__ == "__main__":  # 実行されたら
    app.run(debug=True, host='0.0.0.0', port=80, threaded=True)
