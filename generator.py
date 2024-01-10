from random import randint as rin
import json
import secrets
import string

with open("settings.json", "r") as f:
    st=json.load(f)

fname=st["rf"]

maxTemps=st["mtemps"]

planets=int(round(float(input("Planets: "))))
stars=int(round(float(input("Stars: "))))
blackHoles=int(round(float(input("Black holes:"))))
plength=8

planets=max(0, min(40,planets))
stars=max(0, min(20, stars))
blackHoles=max(0, min(30, blackHoles))
winSize=st["winSize"]

print(planets,stars,blackHoles)

def name():
    alphabet = string.ascii_letters + string.digits
    pwd = ''
    for i in range(plength):
        pwd += ''.join(secrets.choice(alphabet))
    return pwd

data={}

def gpos(x,y):
    un=planets+stars
    un/=2
    return[rin(-1*x*un,x*un),rin(-1*y*un,y*un)]

for i in range(stars):
    n=name()
    t=rin(2,3)
    data[n]={}
    r=rin(0,255)
    data[n]["col"]=(r,rin(0,255),255-r)
    data[n]["rad"]=rin(10,30)
    data[n]["grav"]=rin(20,50)
    data[n]["pos"]=gpos(winSize[0],winSize[1])
    data[n]["vel"]=[0,0]
    data[n]["type"]=t
    data[n]["temp"]=rin(int(round(maxTemps[t]/3)),maxTemps[t])
    st["center"]=n
    
for i in range(planets):
    n=name()
    data[n]={}
    data[n]["col"]=(rin(100,200),rin(100,200),0)
    data[n]["rad"]=rin(1,10)
    data[n]["grav"]=rin(1,20)
    data[n]["pos"]=gpos(winSize[0],winSize[1])
    data[n]["vel"]=[rin(-2,2),rin(-2,2)]
    data[n]["type"]=rin(0,1)
    data[n]["temp"]=0
    
for i in range(blackHoles):
    n=name()
    data[n]={}
    data[n]["col"]=(10,10,10)
    data[n]["rad"]=rin(10,40)
    data[n]["grav"]=rin(1000,2000)
    data[n]["pos"]=gpos(winSize[0],winSize[1])
    data[n]["vel"]=[rin(-2,2),rin(-2,2)]
    data[n]["type"]=4
    data[n]["temp"]=maxTemps[4]
    st["center"]=n

print(data)

with open(fname, "w") as f:
    f.write(json.dumps(data))
with open("settings.json", "w") as f:
    f.write(json.dumps(st))

