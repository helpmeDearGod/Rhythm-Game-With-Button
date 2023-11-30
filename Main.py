#11-29-23
import pygame, sys
pygame.init()
x=800
y=1000
screen=pygame.display.set_mode((x,y))
clock=pygame.time.Clock()

pygame.display.set_caption('Rhythm Game')

color1=(170,170,170)
color2=(100,100,100)
smallfont = pygame.font.SysFont('Corbel',35) 
text = smallfont.render('Start Game' , True , color1)


import time

run=True

while run:
    screen.fill((255,255,255))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
            pygame.quit()
            sys.exit()
            quit()

    if event.type == pygame.MOUSEBUTTONDOWN: 
        if x/2.48 <= mouse[0] <= x/2.48+200 and y/2.36 <= mouse[1] <= y/2.36+55:
            import Rhythm1 
    mouse = pygame.mouse.get_pos()
    if x/2 <= mouse[0] <= x/2.48+200 and y/2.36 <= mouse[1] <= y/2.36+55: 
        pygame.draw.rect(screen,color1,[x/2.48,y/2.36,200,55]) 
    else: 
        pygame.draw.rect(screen,color2,[x/2.48,y/2.36,200,55]) 
    screen.blit(text , (x/2.35,y/2.3))

    
    pygame.display.update()
    clock.tick(60)
pygame.quit()
