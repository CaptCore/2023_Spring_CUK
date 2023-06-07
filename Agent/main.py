from Source import *
from Agent import *
import pygame as pg

pg.init()
SCREEN = pg.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pg.display.set_caption("Traveler")
clock = pg.time.Clock()

pos_list = []

def pos_return(n):
    n = n-1
    if n > 0:
        x = 140+50*(n%4)
        y = 70+50*(n//4)
    else:
        x = 140
        y = 70
    return (x,y)
        
def main():
    timecounter = 0
    now = zero_pos
    player = Agentshow()
    back = wall()
    Mon = Monster()
    G = Gold()
    W = Wumpus()
    coin = True
    all_sprite = pg.sprite.Group(player)
    backback = pg.sprite.Group(back)
    moner = pg.sprite.Group(Mon)
    gg = pg.sprite.Group(G)
    ww = pg.sprite.Group(W)
    while coin:
        if timecounter < len(pos_list):
            now = pos_return(pos_list[timecounter])
            timecounter = timecounter+1
        else:
            timecounter = timecounter
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()
        ww.update()
        gg.update()
        moner.update()
        all_sprite.update(now)
        backback.update()
        SCREEN.fill(BACKGROUND_COLOR)
       
        backback.draw(SCREEN) 
        ww.draw(SCREEN)
        gg.draw(SCREEN)
        moner.draw(SCREEN)
        all_sprite.draw(SCREEN)
        pg.display.update()
        clock.tick(FPS)
        
if __name__ == '__main__':
    alpha = Traveler(graph[0],graph)
    alpha.travelroute()
    delta = alpha.superroute
    beta = alpha.trace[::-1]
    for i in delta:
        for j in i:
            pos_list.append(j.u)
        pos_list.append(0)
    pos_list.pop()
    for i in beta:
        pos_list.append(i.u)
    pos_list.append(0)
    main()

#1 2 3 4
#5 6 7 8
#9 10 11 12
#13 14 15 16

#1 = 0,0