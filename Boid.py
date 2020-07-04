#boid simulation to emulate ship movement in a specified area
import random 
import pygame
pygame.init()

screen = pygame.display.set_mode([800,800])
pygame.display.set_caption("Ship sim")

running = True
x = 250
y = 250
speed = 1
ship = pygame.image.load('.\\Images\\ShipSampletiny.PNG')

class Boid:
    def __init__(self,vectorX,vectorY):
        self.x = x
        self.y = y
        self.velocity = (vectorX,vectorY)
        self.rect = pygame.Rect(self.x,self.y,5,5)
        
boid = Boid(0,1)
boid1 = Boid(1,3)
boid2 = Boid(2,4)
boid3 = Boid(2,3)
boid4 = Boid(3,3)
boid5 = Boid(3,2)
boid6 = Boid(2,1)
boid7 = Boid(3,1)
BoidsList = [boid,boid1,boid2,boid3,boid4,boid5,boid6,boid7]
for i in range(100):
    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            break

    screen.fill((255,255,255))

    screen.blit(ship,boid.rect)
    screen.blit(ship,boid1.rect)
    screen.blit(ship,boid2.rect)
    screen.blit(ship,boid3.rect)
    screen.blit(ship,boid4.rect)
    screen.blit(ship,boid5.rect)
    screen.blit(ship,boid6.rect)
    screen.blit(ship,boid7.rect)
    for Boids in BoidsList:
        (Boids.rect).x+=Boids.velocity[0]
        (Boids.rect).y+=Boids.velocity[1]
        pygame.draw.line(screen,(255,0,0),(250,250),((Boids.rect).x,(Boids.rect).y),10)
    
    
    pygame.display.flip()


