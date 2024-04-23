import requests
from requests.exceptions import HTTPError
import mysql.connector
from mysql.connector import connect, Error
from datetime import date
from datetime import datetime

response = requests.get('https://altin.in/fiyat/gram-altin')
x = response.content
xalt = x.split(b'Gram Alt')
xalt = xalt[11].split(b'</li>')
xalt = xalt[0].split(b'>')
xalt = xalt[1].split(b"'")
lst = str(xalt[0])
xalt= lst[2]+lst[3]+lst[4]+lst[5]+lst[6]+lst[7]+lst[8]
if int(lst[2]) == 9:
   xalt=lst[2]+lst[3]+lst[4]+"."+lst[6]+lst[7]+lst[8]
print(xalt)

xdol = x.split(b'OLAR')
xdol = xdol[1].split(b'>')
lst = str(xdol[2])
xdol = lst[2]+lst[3]+lst[4]+lst[5]+lst[6]+lst[7]
print(xdol)

xeur = x.split(b'<h1>EURO<')
xeur = xeur[1].split(b'<')
xeur = xeur[1].split(b'>')
lst = str(xeur[1])
xeur = lst[2]+lst[3]+lst[4]+lst[5]+lst[6]+lst[7]
print(xeur)

xag = x.split(b'<h1>G')
xag = xag[1].split(b'<')
xag = xag[2].split(b'>')
lst = str(xag[1])
xag = lst[2]+lst[3]+lst[4]+lst[5]+lst[6]+lst[7]
print(xag)

response = requests.get('https://bigpara.hurriyet.com.tr/borsa/hisse-fiyatlari/isdmr-iskenderun-demir-celik-detay/','html.parser')
xx = response.content
xisd = xx.split(b'piyasaBox')
xisd = xisd[1].split(b"area1")
xisd = xisd[1].split(b"</li")
xisd = xisd[0].split(b">")
xlst = [] 
xlst = xisd[1]
xisdx = (str(xisd[1]).replace(",", "."))
xisdx = xisdx.split("'")
print(xisdx[1])

response = requests.get('https://finans.mynet.com/borsa/hisseler/thyao-turk-hava-yollari/')
x = response.content
xthy = x.split(b'<span>Son')
xthy = xthy[1].split(b'<span>')
xthy = xthy[1].split(b"</span>")
xthy = str(xthy[0].split(b"'"))

if str(xthy[6]) == ".":
    xthyx = xthy[3]+xthy[4]+xthy[5]+xthy[6]+xthy[7]
else:
    xthyx=xthy[3]+xthy[4]+xthy[5]
print(xthyx)

try:
   conx = connect(host="127.0.0.1",user="mrblgn",password="Stron6P@ss",database="mqtt")
   #cony = connect(host="10.10.10.81",user="terminal",password="Stron6P@ss",database="forx")
   seql = "SELECT idx FROM forecast ORDER BY idx DESC LIMIT 1"
   curs = conx.cursor()
   curs.execute(seql)
   res = curs.fetchall()
   for row in res:
       snID = int(row[0]) + 1
   #print(snID)
   tdy = date.today()
   tar = tdy.strftime("%Y-%m-%d")
   tm = datetime.now()
   tim = tm.strftime("%Y-%m-%d %H:%M:%S")
   esql = """INSERT INTO forecast (idx, emtia, fyt, tarx, timx) VALUES (%s, 'altın', %s, %s ,%s)"""
   #eesql = """INSERT INTO forecast (idx, emtia, fyt, tar, addx) VALUES (%s, 'altın', %s, %s ,%s)"""
   reco = [snID,xalt,tar,tim]

   with conx.cursor() as cursA:
       cursA.execute(esql,reco)
       conx.commit()
   # with conx.cursor() as cursA:
   #      cursA.execute(eesql,reco)
   #      cony.commit()
             
   tm = datetime.now()
   tim = tm.strftime("%Y-%m-%d %H:%M:%S")
   esql = """INSERT INTO forecast (idx, emtia, fyt, tarx, timx) VALUES (%s, 'gümüs', %s, %s ,%s)"""
   snID = snID + 1
   reco = [snID,xag,tar,tim]
   with conx.cursor() as cursA:
       cursA.execute(esql,reco)
       conx.commit()
   tm = datetime.now()
   tim = tm.strftime("%Y-%m-%d %H:%M:%S")
   esql = """INSERT INTO forecast (idx, emtia, fyt, tarx, timx) VALUES (%s, 'dolar', %s, %s ,%s)"""
   snID = snID + 1
   reco = [snID,xdol,tar,tim]
   with conx.cursor() as cursA:
       cursA.execute(esql,reco)
       conx.commit()
   tm = datetime.now()
   tim = tm.strftime("%Y-%m-%d %H:%M:%S")
   esql = """INSERT INTO forecast (idx, emtia, fyt, tarx, timx) VALUES (%s, 'euro', %s, %s ,%s)"""
   snID = snID + 1
   reco = [snID,xeur,tar,tim]
   with conx.cursor() as cursA:
       cursA.execute(esql,reco)
       conx.commit()
   tm = datetime.now()
   tim = tm.strftime("%Y-%m-%d %H:%M:%S")
   esql = """INSERT INTO forecast (idx, emtia, fyt, tarx, timx) VALUES (%s, 'thy', %s, %s ,%s)"""
   snID = snID + 1
   reco = [snID,xthyx,tar,tim]
   with conx.cursor() as cursA:
    cursA.execute(esql,reco)
    conx.commit()
       
   tm = datetime.now()
   tim = tm.strftime("%Y-%m-%d %H:%M:%S")
   esql = """INSERT INTO forecast (idx, emtia, fyt, tarx, timx) VALUES (%s, 'isdemir', %s, %s ,%s)"""
   snID = snID + 1
   reco = [snID,float(xisdx[1]),tar,tim]
   with conx.cursor() as cursA:
        cursA.execute(esql,reco)
        conx.commit()
        conx.close()
        
   
except Error as e:
   print(e)
