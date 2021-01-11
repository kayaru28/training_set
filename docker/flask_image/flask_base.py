

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


@app.route("/rps", methods=["GET", "POST"])
def rpspage():
    return render_template("rps_form.html")


if __name__ == "__main__":  # 実行されたら
    app.run(debug=True, host='0.0.0.0', port=80, threaded=True)
