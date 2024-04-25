import requests
import time
import datetime
import math
import mysql.connector
from mysql.connector import connect, Error
from datetime import datetime, timedelta

try:
    conx = connect(host="127.0.0.1",user="mrblgn",password="Stron6P@ss",database="mqtt")
except Error as e:
    print(e)
# Rotayı Al
seql1 = "select * from agv where idx=35"
curs1 = conx.cursor()
curs1.execute(seql1)
res1 = curs1.fetchall()
for rotan in res1:
    nereden = rotan[2]
    nereye = rotan[3]
    pasn = rotan[4]

pasx = pasn.split("-")
#print(pasx[6])
gecx = []
gecy = []
sehirGec = []

for nok in pasx:
    seqln = "select * from payn where ordx=" + nok
    cursn = conx.cursor()
    cursn.execute(seqln)
    resn = cursn.fetchall()
    for gec in resn:
        sehirGec.append(gec[3])
        gecx.append(gec[1])
        gecy.append(gec[2])

print("Nereden: ",nereden," Nereye:",nereye," Geçilecek: ")

# Simülasyon girdi noktaları
koordx = []
koordy = []
for gird in range(0,len(sehirGec)-1):
    uskx = gecx[gird]
    nisx = gecx[gird+1]
    usky = gecy[gird]
    nisy = gecy[gird+1]
    
    farx = uskx - nisx
    fary = usky - nisy
    if(farx <0):
        farx = farx * -1
    if(fary < 0):
        fary = fary * -1

    if uskx > nisx:
        for xx in range(0,33):
            #print(xx)
            koordx.append(round(uskx - xx*farx/33,6))
    else:
        for xx in range(0,33):
            koordx.append(round(uskx + xx*farx/33,6))

    if nisy > usky:
        for yy in range(0,33):
            koordy.append(round(usky + yy*fary/33,6))
    else:
        for yy in range(0,33):
            koordy.append(round(usky - yy*fary/33,6))

#koord = koordx + koordy
#for nokt in range(0,len(koordx)):
#    print("Nokta",nokt," Lat:",koordx[nokt],"Lon:",koordy[nokt])
#print(len(koord))
init_t = datetime.now()
topNok = len(koordx)
timSeri = []
xx = init_t
for dk in range(0,topNok):
    xx = (init_t + dk*timedelta(minutes=1))
    timSeri.append(xx.strftime('%Y-%m-%d %H:%M:%S'))

print(timSeri[31])
cony = connect(host="192.168.1.11",user="python",password="Stron6P@ss",database="mqtt")
for nokt in range(0,len(koordx)):
    # DB Ekleme Kodu
    print("Nokta",nokt,"Lat:",koordx[nokt],"Lon:",koordy[nokt],"T:",timSeri[nokt])
    seqls = "select idx from sim order by idx desc limit 1"
    curss = conx.cursor()
    curss.execute(seqls)
    ress = curss.fetchall()
    for sons in ress:
        sonid = sons[0] + 1
    seqle = """update sim set lat=%s where idx=%s"""
    param1 = (koordx[nokt],1)
    curss.execute(seqle,param1)
    seqle2 = """update sim set lon=%s where idx=%s"""
    param2 = (koordy[nokt],1)
    curss.execute(seqle2,param2)
    cursu = conx.cursor(prepared=True)
    seqli = """insert into sim (idx,arac,lat,lon,tim) values (%s,%s,%s,%s,%s)"""
    suan = (sonid,"Araç1",koordx[nokt],koordy[nokt],timSeri[nokt])
    cursu.execute(seqli,suan)
    conx.commit()
    time.sleep(0.05)
    cursRem = cony.cursor(prepared=True)
    cursRem.execute(seqle,param1)
    cursRem.execute(seqle2,param2)
    cursRem.execute(seqli,suan)
    cony.commit()

conx.close()


