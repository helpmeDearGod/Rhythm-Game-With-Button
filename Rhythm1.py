#11-18-23

import pygame, sys
pygame.init()
x=800
y=1000
screen=pygame.display.set_mode((x,y))
 
pygame.display.set_caption('Rhythm Game')

color3=(34, 59, 110)
color4=(212, 242, 252)

font = pygame.font.Font('freesansbold.ttf', 32)
text=font.render("Hit keys   \"d  ,  f  ,  g  ,  h  ,  j  ,  k  \"", True, color3, color4)
wordRect=text.get_rect()
wordRect.center=(x // 2, y //1.5)

#music file
from pygame import mixer
mixer.init()

clock=pygame.time.Clock()

#key classes
class Key():
    def __init__(self,x,y,color1,color2,key):
        self.x=x
        self.y=y
        self.color1=((209,219,235))
        self.color2=((64, 66, 69))
        self.key=key
        self.rect=pygame.Rect(self.x,self.y,100,40)
        self.handled=False


keys=[
    Key(100,500,(255,0,0),(220,0,0),pygame.K_s),
    Key(200,500,(0,255,0),(0,220,0),pygame.K_d),
    Key(300,500,(0,0,255),(0,0,220),pygame.K_f),
    
    Key(400,500,(255,255,0),(220,220,0),pygame.K_j),
    Key(500,500,(255,255,0),(220,220,0),pygame.K_k),
    Key(600,500,(255,255,0),(220,220,0),pygame.K_l),
]


#MAP  loaded
def load(map):
    rects=[]
    mixer.music.load(map + ".mp3")
    mixer.music.play()
    mixer.music.set_volume(0.5)
    f = open(map+ ".txt",'r')
    data=f.readlines()

    #for y in range(len(data)):
    #    for x in range(len(data[y])):
     #       if data[y][x]=='0':
      #              rects.append(pygame.Rect(keys[x].rect.centerx -25,y * -100,50,25))
    #return rects

    for y in range(len(data)):
        for x in range(len(data[y])):
            if data[y][x] == '0':
                rects.append(pygame.Rect(keys[x].rect.centerx -25,y* -100,50,25))
            
    return rects

map_rect=load("A_Sealed_Away_Loser")

hit=pygame.mixer.Sound("Hit.mp3")

color5=((0,0,0))
color6=((255,255,255))

font2= pygame.font.Font('freesansbold.ttf', 32)
text2=font2.render("Good", True, color6, color5)
wordRect2=text.get_rect()
wordRect2.center=(x // 1.3, y //2.2)

font4= pygame.font.Font('freesansbold.ttf', 32)
text4=font4.render("Level 1", True, color3, color4)
wordRect4=text4.get_rect()
wordRect4.center=(x // 2, y //2.5)



import time
run=True
while run:
    screen.fill((0,0,0))

    screen.blit(text,wordRect)
    screen.blit(text4,wordRect4)
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
            pygame.quit()
            sys.exit()
            quit()

            
    k=pygame.key.get_pressed()
    for key in keys:
        if k[key.key]:
            pygame.draw.rect(screen,key.color1,key.rect)
            key.handled=False
        if not k[key.key]:
            pygame.draw.rect(screen,key.color2,key.rect)
            key.handled=True
    for rect in map_rect:
        pygame.draw.rect(screen,(255,255,255),rect)
        rect.y+=5
        for key in keys:
            if key.rect.colliderect(rect) and not key.handled:
                hit.set_volume(0.7)
                hit.play()
                screen.blit(text2, wordRect2)
                map_rect.remove(rect)
                
                key.handled=True
                break        
    


    
    pygame.display.update()
    clock.tick(60)

