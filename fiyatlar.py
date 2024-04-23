# -*- coding: utf-8 -*-
#"""
#Created on Fri Jun 17 16:23:26 2022

#@author: omer.bilgin
#"""
import requests
from requests.exceptions import HTTPError
#import mysql.connector
#from mysql.connector import connect, Error
from datetime import date
from datetime import datetime
print(datetime.now())
response = requests.get('https://altin.in/fiyat/gram-altin')
x = response.content
xalt = x.split(b'Gram Alt')
xalt = xalt[11].split(b'</li>')
xalt = xalt[0].split(b'>')
xalt = xalt[1].split(b"'")
lst = str(xalt[0])
print("Altin: ",lst)
xalt= lst[2]+lst[3]+lst[4]+lst[5]+"."+lst[7]+lst[8]
if lst[2] == str(9):
    xalt = lst[2]+lst[3]+lst[4]+lst[5]+lst[6]+lst[7]
#print("Altın: ",xalt)
resp = requests.get('https://altin.in/fiyat/gumus')
xx = resp.content
xag = xx.split(b'midrow sati')
xag2 = xag[1].split(b'</li>')
xag3 = xag2[0].split(b'>')
xag4 = xag3[1]
print("Test: ",xag4)
#xag = xag[3].split(b'>')
#print(xag)
#lst = str(xag[1])
#xag = lst[2]+lst[3]+lst[4]+lst[5]+lst[7]#+lst[8]
#print("Gümüş: ",xag)
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
print("İsdemir: ",xisdx[0])

response = requests.get('https://finans.mynet.com/borsa/hisseler/thyao-turk-hava-yollari/')
x = response.content
xthy = x.split(b'<span>Son')
xthy = xthy[1].split(b'<span>')
xthy = xthy[1].split(b"</span>")
xthy = str(xthy[0].split(b"'"))
xthyx=xthy[3]+xthy[4]+xthy[5]
print("THY: ", xthyx)
#link = "http://pro.bilginiot.com/upHesap.php?a=%s&g=%s"%(xalt,xag)
#print(link)
#link2 = "http://pro.bilginiot.com/hesap.php"
#response = requests.get(link)
#response2 = requests.get(link2)
#response2 = response2.content
#response2 = response2.split(b'</td></tr>')
#response2 = response2[0].split(b'eri')
#print(response2[1])
