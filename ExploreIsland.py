#Island exploration loop
import pygame

pygame.init()
background = pygame.image.load('.\\Images\\IslandTest.jpg')
tutorial_font = (pygame.font.Font('HighTide-Demo.ttf',40)).render('Press \'x\' to leave', True, (0,0,0))

def IslandExploration():
    screen = pygame.display.set_mode([800,555])
    pygame.display.set_caption("Island Sample")
    
    running = True
    x = 0
    y = 0
    speed = 1
    while running:
        pygame.time.delay(1)
        screen.blit(background,(0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        keys = pygame.key.get_pressed()
            
        if keys[pygame.K_a] and x != 0:
            x -= speed
        if keys[pygame.K_d] and x != 790:
            x += speed
        if keys[pygame.K_w] and y != 0:
            y -= speed
        if keys[pygame.K_s] and y != 790:
            y += speed
        if keys[pygame.K_x]:
            running = False
        

        pygame.draw.rect(screen, (255, 0, 0), (x,y,10,10), 5)
        screen.blit(tutorial_font, (x,y+15,(tutorial_font.get_rect()).width,(tutorial_font.get_rect()).height))
        pygame.display.flip()
    screen = pygame.display.set_mode([1000,1000])
