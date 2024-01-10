import pygame
pygame.init()
from pygame.locals import *
from time import sleep
from random import randint
import json
import math as m
from datetime import datetime

# Planet Types:
# 0 - Solid Planet
# 1 - Gas Planet
# 2 - Small Star
# 3 - Big Star
# 4 - Black Hole

with open("settings.json", "r") as f:
    st=json.load(f)

btypes=st["btypes"]
maxTemps=st["mtemps"]

lnot="Stable universe"
lnott=datetime.now().timestamp()

muls=st["showAnything"]
center=st["center"]
fn=st["rf"]

kpp=st["kmperpx"]
qty=[0,0,0]
f=open(fn)
data=json.load(f)
md=0
fs=0
winSize = st["winSize"]
display = pygame.display.set_mode(winSize)
mpos=[0,0,0,0]#max x, max y, min x, min y
fps = 30
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 24)
pygame.display.set_caption(st["title"])

simSpeed = 0.01

def collision_outcome(type1, type2):
    if type1 == 4 or type2 == 4:
        return 4
    if type1 == 0:
        if type2 == 0 or type2 == 1: return 0
    elif type1 == 1:
        if type2 == 0 or type2 == 1: return 1
    elif type1 == 2:
        if type2 == 0: return 2
        if type2 == 1 or type2 == 2: return 3
    elif type1 == 3:
        if type2 == 0 or type2 == 1: return 3
        if type2 == 2 or type2 == 3: return 4
    elif type1 == 4:
        return 4
    else:
        return 2

stars = [((randint(150, 200), randint(150, 200), randint(150, 200)), (randint(1, winSize[0]), randint(1, winSize[1])), randint(1, 2)) for _ in range(250)]
def draw_stars():
    try:
        cp=data[center]
        cx,cy=cp["pos"]
    except:
        cx=winSize[0]/2
        cy=winSize[1]/2
    for star in stars:
        pygame.draw.circle(display, star[0], (round(cx-star[1][0]+winSize[0]/2)%winSize[0],round(cy-star[1][1]+winSize[1]/2)%winSize[1]), star[2])

def draw_planets():
    try:
        cp=data[center]
        cx,cy=cp["pos"]
    except:
        cx=winSize[0]/2
        cy=winSize[1]/2
    for planet in data:
        if muls:
            pygame.draw.circle(display, data[planet]['col'], ((cx-data[planet]['pos'][0]+winSize[0]/2)%winSize[0],(cy-data[planet]['pos'][1]+winSize[1]/2)%winSize[1]), data[planet]['rad'])
            text = font.render(planet+" "+str(data[planet]["temp"])+"°C", True, "#ffffff")
            display.blit(text, ((cx-data[planet]['pos'][0]+winSize[0]/2)%winSize[0],(cy-data[planet]['pos'][1]+winSize[1]/2-data[planet]["rad"]-29)%winSize[1]))
        else:
            pygame.draw.circle(display, data[planet]['col'], ((cx-data[planet]['pos'][0]+winSize[0]/2),(cy-data[planet]['pos'][1]+winSize[1]/2)), data[planet]['rad'])
            text = font.render(planet+" "+str(data[planet]["temp"])+"°C", True, "#ffffff")
            display.blit(text, ((cx-data[planet]['pos'][0]+winSize[0]/2),(cy-data[planet]['pos'][1]+winSize[1]/2)-data[planet]["rad"]-29))

def update_planets():
    toDelete = []
    global md
    global fs
    global mpos
    fs=0
    md=99999999999999999999999999999999999999999999999999999999999999999999999999
    global qty
    qty=[0,0,0]
    for planet in data:
        if data[planet]["type"] == 0 or data[planet]["type"] == 1:
            qty[0]+=1
        elif data[planet]["type"] == 2 or data[planet]["type"] == 3:
            qty[1]+=1
        else:
            qty[2]+=1
        ss=False
        try:
            if data[planet]["type"]<2:
                ss=True
                sd=99999999999999999
                sn=""
        except:
            pass
        for oPlanet in data:
            if oPlanet != planet:
                dx = data[oPlanet]['pos'][0] - data[planet]['pos'][0]
                dy = data[oPlanet]['pos'][1] - data[planet]['pos'][1]

                distance = m.sqrt(dx*dx + dy*dy)
                try:
                    if data[oPlanet]["type"]>1 and data[oPlanet]["type"]<4 and ss:
                        if distance < sd:
                            sd=distance
                            sn=oPlanet
                except:
                    pass
                        
                if distance*kpp < md:
                    md=distance*kpp
                if m.sqrt(data[planet]["vel"][0]**2+data[planet]["vel"][1]**2)*kpp > fs:
                    fs=m.sqrt(data[planet]["vel"][0]**2+data[planet]["vel"][1]**2)*kpp

                dx = dx / (distance+0.0000000000000000001) * data[oPlanet]['grav'] * simSpeed
                dy = dy / (distance+0.0000000000000000001) * data[oPlanet]['grav'] * simSpeed
                
                

                data[planet]['vel'][0] += dx
                data[planet]['vel'][1] += dy
                
                px=data[planet]['pos'][0]
                py=data[planet]['pos'][1]
                mpos=[max(mpos[0],px),max(mpos[1],py),min(mpos[2],px),min(mpos[3],py)]
                if distance <= data[oPlanet]['rad']:
                    toDelete.append(planet)
                    global lnot
                    data[oPlanet]['grav'] += data[planet]['grav']
                    data[oPlanet]['rad'] += data[planet]['rad'] / 2
                    co = collision_outcome(data[oPlanet]['type'], data[planet]['type'])
                    lnott=datetime.now().timestamp()
                    if co == 0:
                        data[oPlanet]['col'] = (150, 0, 0)
                        lnot=planet+" collided with "+oPlanet+" generating a "+btypes[0]
                    elif co == 1:
                        data[oPlanet]['col'] = (255, 150, 150)
                        lnot=planet+" collided with "+oPlanet+" generating a "+btypes[1]
                    elif co == 2:
                        data[oPlanet]['col'] = (255, 255, 0)
                        lnot=planet+" collided with "+oPlanet+" generating a "+btypes[2]
                    elif co == 3:
                        data[oPlanet]['col'] = (255, 0, 0)
                        lnot=planet+" collided with "+oPlanet+" generating a "+btypes[3]
                    elif co == 4:
                        data[oPlanet]['col'] = (20, 20, 20)
                        data[oPlanet]['grav'] *= 2
                        lnot=planet+" collided with "+oPlanet+" generating a "+btypes[4]
                    data[oPlanet]['type'] = co

        data[planet]['pos'][0] += data[planet]['vel'][0]
        data[planet]['pos'][1] += data[planet]['vel'][1]
        if ss:
            try:
                sd*=kpp
                data[planet]["temp"] = round(data[sn]["temp"] * (data[sn]["rad"] / (2 * sd)) ** 0.5)
            except:
                pass

    for item in toDelete:
        try:
            del data[item]
        except:
            pass

run = True


while run:
    display.fill((0, 0, 0))

    draw_stars()
    draw_planets()
    update_planets()

    clock.tick(fps)
    
    #Rendering datas
    
    text = font.render(str(len(data))+' bodies remaining', True, "#ffffff")
    display.blit(text, (20, 20))
    text = font.render('Minimum distance: '+str(round(md))+"km", True, "#ffffff")
    display.blit(text, (20, 46))
    text = font.render('Fastest speed: '+str(round(fs))+"km/s", True, "#ffffff")
    display.blit(text, (20, 72))
    text = font.render('Universe\'s size: '+str(abs(round(kpp*(abs(mpos[0])-abs(mpos[2])))))+"x"+str(abs(round(kpp*(abs(mpos[1])-abs(mpos[3])))))+"km", True, "#ffffff")
    display.blit(text, (20, 98))
    text = font.render(str(qty[0])+" planets", True, "#ffffff")
    display.blit(text, (20, 124))
    text = font.render(str(qty[1])+" stars", True, "#ffffff")
    display.blit(text, (20, 150))
    text = font.render(str(qty[2])+" black holes", True, "#ffffff")
    display.blit(text, (20, 176))
    text = font.render(lnot, True, "#ffffff")
    display.blit(text, ((winSize[0]-text.get_width())/2, 30))
    if datetime.now().timestamp()-lnott > 10:
        lnott=datetime.now().timestamp()
        lnot="Stable universe"
    
    pygame.display.update()
    
    if len(data) <= 2:
        run=False
        sleep(2)
        print("Just",len(data),"bodies remaining, ending simulation\n")
        for n in data:
            print("Name:",n)
            try:
                print("Type:",btypes[data[n]["type"]])
            except:
                print("Type: unknown")
            print("Radius:",data[n]["rad"])
            print("Mass:",data[n]["grav"],"times earth (",5.972e24*data[n]["grav"],"kg )")
            print("Position: X"+str(data[n]["pos"][0])+", Y"+str(data[n]["pos"][1]),"\n\n")
    
    for event in pygame.event.get():
        if event.type == QUIT:
            run = False
            
    pygame.display.update()

pygame.quit()
f.close()



