import requests

response = requests.get('http://pro.bilginiot.com/ip.php')
curr = response.content
#print(curr)
ipx1 = curr.split(b'Req:')
ipx2 = ipx1[1].split(b'<')
rr = str(ipx2[0])

ipy = open("rip.txt","r")
yy = str(ipy.read())
ipy.close()
ff = []
ff = yy
duzelt =""
for abc in ff:
    if abc != "\n":
        duzelt += abc
print(duzelt)

if rr == "1":
    link1 = "http://pro.bilginiot.com/ip.php?ipx='"
    link2 = "'"
    link = link1 + duzelt + link2
    res = requests.get(link)
