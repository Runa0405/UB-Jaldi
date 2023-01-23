import sqlite3
import json
import bottle
def createparkingtable():
  con=sqlite3.connect("parking.db")
  cursor=con.cursor()
  cursor.execute("CREATE TABLE IF NOT EXISTS PARKING (NUMBER INT(6), UBIT VARCHAR(30),TIME VARCHAR(30), SFO VARCHAR(2))")
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
@bottle.route("/script.js")
def scriptserver():
  return bottle.static_file("/script.js",root=".")
@bottle.route("/ajax.js")
def ajaxserver():
  return bottle.static_file("/ajax.js",root=".")
@bottle.route("/gotopark")
def parkgo():
  return bottle.static_file("/parking.html",root=".")
@bottle.route("/opendisplay")
def opendisplay():
  createparkingtable()
  return testtable()
@bottle.post("/newdata")
def newparking():
  info=bottle.request.body.read().decode()
  info2=json.loads()
  ubitname1=info2["ubit"]
  if(finder(ubitname1)==1):
    pname=info2["pname"]
    time=info2["time"]
    status=info2["status"]
    insertintoparking(pname,ubitname1,time,status)

