from flask import Flask,request,jsonify,render_template
import sqlite3
import json
import bottle
def createparkingtable():
  con=sqlite3.connect("parking.db")
  cursor=con.cursor()
  #cursor.execute("CREATE TABLE IF NOT EXISTS PARKING (NUMBER INT(6), UBIT VARCHAR(30),TIME VARCHAR(30), SFO VARCHAR(2))")
  con.commit()
def insertintoparking(pn,ubn,tm,status):
  con=sqlite3.connect("parking.db")
  cursor=con.cursor()
  cursor.execute("INSERT INTO PARKING VALUES('"+str(pn)+"'"+","+"'"+ubn+"'"+","+"'"+tm+"'"+","+"'"+status+"'"+")")
  con.commit()
def testtable():
  con=sqlite3.connect("parking.db")
  cursor=con.cursor()
  x=cursor.execute("SELECT * FROM parking")
  for m in x:
    print(m)
  con.commit()
import requests
def finder(personname):
  text=requests.get("https://www.buffalo.edu/search/search.html?searchUrl=https://www.buffalo.edu/search/search.html&query="+personname+"%40buffalo.edu&collection=meta-search&f.Tabs%7Cdb-people=People")
  with open("data.txt","w") as f:
    f.write(text.text)
  with open("data.txt","r") as f:
    for m in f.readlines():
      if('              <a href="mailto:'+personname+'@buffalo.edu">'+personname+'@buffalo.edu</a>'in m):
        
        return 1
    else:
      return 0
finder("vrushaal")
@bottle.route("/")
def server():
  return bottle.static_file("/index.html",root=".")
@bottle.route("/index.html")
def htmltwo():
  return bottle.static_file("/index.html",root=".")
@bottle.route("/script.js")
@bottle.route("/style.css")
def csss():
  return bottle.static_file("/style.css",root=".")
@bottle.route("/script.js")
def scriptserver():
  return bottle.static_file("/script.js",root=".")
@bottle.route("/parking.db")
def databasee():
  return bottle.static_file("/parking.db",root=".")
@bottle.route("/ajax.js")
def ajaxserver():
  return bottle.static_file("/ajax.js",root=".")
@bottle.route("/parking.html")
def parkingtogo():
  return bottle.static_file("/parking.html",root=".")
@bottle.route("/studying.html")
def studyingtogo():
  return bottle.static_file("/studying.html",root=".")
@bottle.route("/eating.html")
def khana():
  return bottle.static_file("/eating.html",root=".")
@bottle.route("/main.py")
def py():
  return bottle.static_file("/main.py",root=".")
@bottle.route("/action_page.php")
def formm():
  return bottle.static_file("/action_page.php",root=".")
@bottle.route("/opendisplay")
def opendisplay():
  createparkingtable()
  return testtable()

# #Set up Flask:
# app = Flask(__name__)
# #Set up Flask to bypass CORS:
# cors = CORS(app)
# #Create the receiver API POST endpoint:
# @app.route("/receiver", methods=["POST"])
# def postME():
#  data = request.get_json()
#  data = jsonify(data)
#  return data
# if __name__ == "__main__": 
#  app.run(debug=True)

#Setup flask server
# app.py
app = Flask(__name__)
@app.route('/hello', methods=['GET', 'POST'])
def hello():
  # POST request
    if request.method == 'POST':
        print('Incoming..')
        print(request.get_json())  # parse as JSON
        return 'OK', 200

    # GET request
    else:
        message = {'greeting':'Hello from Flask!'}
        return jsonify(message)  # serialize and use JSON headers
  
@bottle.post("/newdata")
def newparking():
  info=bottle.request.body.read().decode()
  info2=json.loads(info)
  ubitname1=info2["ubit"]
  if(finder(ubitname1)==1):
    pname=info2["pname"]
    time=info2["time"]
    status=info2["status"]
    insertintoparking(pname,ubitname1,time,status)
bottle.run(host="0.0.0.0",port=8080)