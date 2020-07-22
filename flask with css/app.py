from flask import Flask, render_template 
import api
import requests
from pprint import pprint

app = Flask(__name__)

@app.route('/')
def login():
        return render_template('sample.html')

@app.route('/link')
def sagar():
    return render_template('redirect.html')

list=[]
@app.route('/temp')
def weather():
    for i,j in api.data.items():
        list.append([i,j])

    return render_template('redirect.html',  output=list)
@app.route('/test')    
def test():
    url = 'https://samples.openweathermap.org/data/2.5/weather?q={}&appid=b6907d289e10d714a6e88b30761fae22'
    res = requests.get(url)
    data = res.json()
    return data   

if __name__ == '__main__':
   app.run(debug = True)