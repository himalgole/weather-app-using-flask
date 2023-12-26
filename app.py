from flask import Flask, jsonify,request,render_template
import os,requests
from os import path
import json
from myvariables import api_key
app = Flask(__name__)
filename = "static\data.json"
listobj = []
if path.isfile(filename) is False:
  raise Exception("File not found")

with open(filename,'r') as fp:
  listObj = json.load(fp)


# print(listObj)
@app.route('/',methods = ['POST','GET'])
def home():
    data = []
    for x in listObj:
      res = requests.get(f'http://api.weatherapi.com/v1/current.json?key={api_key}&q={x["name"]}&aqi=no')
      var = res.json()
      data.append(var)
    return render_template('base.html',info = data)


@app.route('/weather-info',methods = ['post','get'])
def weather_info():
      str = request.form['search']
      res = requests.get(f'http://api.weatherapi.com/v1/current.json?key={api_key}&q={str}&aqi=no')
      if not res:
         return 'Invalid Input'
      info = res.json()   
      return render_template('details.html',data = info)
   

if __name__ == '__main__':
    app.run(debug=True)