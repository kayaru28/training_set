
from flask import * 
import datetime
app = Flask(__name__) 

def formatRatio(ratio):
    return format(ratio, '.2f')

@app.route("/")  
def main():
    return "Hello, World! I am iron man"  


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80, threaded=True)
