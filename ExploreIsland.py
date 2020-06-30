#Island exploration loop
import pygame

pygame.init()
background = pygame.image.load('Images\\IslandTest.jpg')
def IslandExploration():
    screen = pygame.display.set_mode([800,555])
    pygame.display.set_caption("Dungeon Crawl")
    screen.blit(background,(0,0))
    running = True
    x = 0
    y = 0
    speed = 20
    while running:
        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        keys = pygame.key.get_pressed()
            
        if keys[pygame.K_LEFT] and x != 0:
            x -= speed
        if keys[pygame.K_RIGHT] and x != 545:
            x += speed
        if keys[pygame.K_UP] and y != 0:
            y -= speed
        if keys[pygame.K_DOWN] and y != 545:
            y += speed
        if keys[pygame.K_x]:
            running = False
        

        pygame.draw.rect(screen, (255, 0, 0), (x,y,10,10), 5)

        pygame.display.flip()
    screen = pygame.display.set_mode([1000,1000])
