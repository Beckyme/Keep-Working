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
    if request.args.get('found') == "创建":
        wish = request.args.get('wish')
        outcome = request.args.get('outcome')
        obstacle = request.args.get('obstacle')
        plan = request.args.get('plan')
        date = request.args.get('date')
        time = request.args.get('time')
        where = request.args.get('where')
        result = "你期望自己%s，达到%s的结果，计划从%s %s开始，在%s %s" %(wish, outcome, date, time, where, plan)
        if wish == '' or outcome == '' or obstacle == '' or plan == '':
            return render_template('error.html')
        else:
            user_woop_list.append(result)
            return render_template('WOOP.html', Submit = result)
    else:
        #request.args.get('history') == "历史":
        return render_template('history.html', history = user_woop_list)
 
user_woop_list.clear()
 
if __name__ == '__main__':
    app.run(debug=True)