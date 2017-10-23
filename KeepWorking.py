from flask import Flask
from flask import render_template
from flask import request
import requests
import sqlite3

app = Flask(__name__)

user_woop_list = []

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('KWhome.html')
    
@app.route('/user_request', methods=['GET', 'post']) 
def order_request():
    if request.args.get('found') == "提交":
        wish = request.args.get('wish')
        outcome = request.args.get('outcome')
        obstacle = request.args.get('obstacle')
        plan = request.args.get('plan')
        date = request.args.get('date')
        time = request.args.get('time')
        where = request.args.get('where')
        result = "【WOOP内容】---【期望】%s【结果】%s【开始时间】%s【地点】%s【行动】%s %s" %(wish, outcome, date, where, time, plan)
        if wish == '' or outcome == '' or obstacle == '' or plan == '':
            return render_template('error.html')
        else:
            user_woop_list.append(result)
            return render_template('WOOP.html', Submit = result)
    else:
        #request.args.get('history') == "历史":
        return render_template('history.html', history = user_woop_list)
                
if __name__ == '__main__':
    app.run(debug=True)