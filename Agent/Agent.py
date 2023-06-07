import pygame as pg
from Source import *

class vertex:
    def __init__(self,u,c):
        self.u = u
        self.available = []
        self.cost = c
    def able(self,can):
        self.available.append(can)

#양방향이라서 이미 지나온 자리를 제거해야한다.
graph = []

for i in range(16):
    temp = vertex(i+1,10)
    a = i+1
    if a-1 > 0:
        temp.able(a-1)
    if a%4 != 0:
        temp.able(a+1)
    if a+4 < 16:
        temp.able(a+4)
    if a-4 > 0:
        temp.able(a-4)
    graph.append(temp)
    
temp = graph[2]
temp.cost = 1500
graph[2] = temp
#2+1

temp = graph[9]
temp.cost = 1000
graph[9] = temp
#9+1

temp = graph[13]
temp.cost = 1
graph[13] = temp
#13+1

class Wumpus(pg.sprite.Sprite):
    def __init__(self):
        super(Wumpus,self).__init__()
        size = (50,50)
        self.pos = (240,70)
        images = []
        images.append(pg.image.load('04.png'))
        self.rect = pg.Rect(self.pos,size)
        self.images = [pg.transform.scale(image,size)for image in images]
        self.image = images[0]
    def update(self):
        self.image = self.images[0]
class Monster(pg.sprite.Sprite):
    def __init__(self):
        super(Monster,self).__init__()
        size = (50,50)
        self.pos = (140,170)
        images = []
        images.append(pg.image.load('04.png'))
        self.rect = pg.Rect(self.pos,size)
        self.images = [pg.transform.scale(image,size)for image in images]
        self.image = images[0]
    def update(self):
        self.image = self.images[0]
class Gold(pg.sprite.Sprite):
    def __init__(self):
        super(Gold,self).__init__()
        size = (50,50)
        self.pos = (190,220)
        images = []
        images.append(pg.image.load('05.png'))
        self.rect = pg.Rect(self.pos,size)
        self.images = [pg.transform.scale(image,size)for image in images]
        self.image = images[0]
    def update(self):
        self.image = self.images[0]
class wall(pg.sprite.Sprite):
    def __init__(self):
        super(wall,self).__init__()
        size = (200,200)
        self.pos = zero_pos
        self.index = 0
        images = []
        images.append(pg.image.load('02.png'))
        self.rect = pg.Rect(self.pos,size)
        self.images = [pg.transform.scale(image,size)for image in images]
        self.image = images[self.index]
    def update(self):
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]
#그래프 집어넣기
class Agentshow(pg.sprite.Sprite):
    def __init__(self):
        super(Agentshow,self).__init__()
        self.position = zero_pos
        self.size = (50,50)
        images = []
        images.append(pg.image.load('01.png'))
        images.append(pg.image.load('03.png'))
        self.rect = pg.Rect(self.position,self.size)
        self.images = [pg.transform.scale(image,self.size)for image in images]
        self.index = 0
        self.image = images[self.index]
    def update(self,now):
        self.position = now
        if now == (140,70):
            self.index = 1
            self.image = self.images[self.index]
            self.rect = pg.Rect(zero_pos,self.size)
        else:
            self.index = 0
            self.rect = pg.Rect(self.position,self.size)
            self.image = self.images[self.index]
        if self.index >= len(self.images):
            self.index = 0
        
        
class Traveler():
    def __init__(self,start,g):
        self.superroute = []
        self.g = g
        self.life = True
        self.target = False
        self.travel = [start]
        self.trace = []
        self.monster = []
        self.wumpus = []
        self.gold = []
        self.now = start
        
    def travelroute(self):
        if self.target == True:
            if self.trace in self.superroute:
                return
            else:
                self.superroute.append(self.trace)
            return
        else:
            self.travel.remove(self.now)
            self.trace.append(self.now)
            print('now:',self.now.u)
            self.deadcheck(self.now.cost)
            self.targetcheck(self.now.cost)
            if self.life == False:
                self.superroute.append(self.trace)
                self.now = self.g[0]
                self.travel = [self.g[0]]
                self.trace = []
                self.life = True
                self.travelroute()
            for i in self.now.available:
                real = i-1
                self.travel.append(self.g[real])
                for j in self.trace:
                    if j in self.travel:
                        self.travel.remove(j)
                for k in self.monster:
                    if k in self.travel:
                        self.travel.remove(k)
                for k in self.wumpus:
                    if k in self.travel:
                        self.travel.remove(k)
                    
                if self.now != self.g[15] and self.travel != []:
                    self.now = self.travel[0]
                    self.travelroute()
        return
                
    def deadcheck(self,c):
        if c >= 1000:
            self.life = False
            if c == 1000:
                self.wumpus.append(self.now)
            if c == 1500:
                self.monster.append(self.now)
            print('traveler is dead.')
            
    def targetcheck(self,c):
        if c == 1:
            self.target = True
            self.gold.append(self.now)
            print('found the target.')