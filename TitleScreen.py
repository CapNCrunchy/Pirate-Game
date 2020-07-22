import pygame
import POOPDECKSCRIPTS as pds
from ClassesLib import Button

def OptionsScreen(screen):
    pygame.time.delay(150)
    EXIT = Button((200,200,120,50),(255,255,255), (0,0,255), 'EXIT', pds.GetFont("HighTide",25),(0,0,0))
    Back = Button((125,375,250,50), (255,255,255), (0,0,255), 'Back', pds.GetFont("HighTide",47),(0,0,0))

    options = True
    while options:
        pygame.time.delay(20)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 'EXIT'
        
        CursorRect = pygame.Rect(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1],1,1)
        screen.fill((0,0,0))
        pygame.draw.rect(screen,EXIT.CurrentColor, EXIT.rect)
        pygame.draw.rect(screen,Back.CurrentColor, Back.rect)
        pds.DrawCursor(screen, (0,255,0))

        if pds.ButtonIsActive(EXIT,CursorRect) and pygame.mouse.get_pressed()[0]:
            options = False
            return 'EXIT'
                    
        if pds.ButtonIsActive(Back,CursorRect) and pygame.mouse.get_pressed()[0]:
            options = False
            return 'Nothing'
            break

        screen.blit(Back.Render, (172,375,(Back.Render.get_rect()).width,(Back.Render.get_rect()).height))
        screen.blit(EXIT.Render, (205,200,(EXIT.Render.get_rect()).width,(EXIT.Render.get_rect()).height))

        pygame.display.flip()

def TitleScreen(OnTitleScreen):
    pygame.init()

    screen = pygame.display.set_mode([500,500], pygame.RESIZABLE|pygame.SCALED)
    Start = Button((125,375,250,50), (0,0,0), (0,0,255), 'START', pds.GetFont("HighTide",47),(255,255,255))
    Options = Button((200,200,120,50),(0,0,0), (0,0,255), 'Options', pds.GetFont("HighTide",35),(255,255,255))
    
    pygame.display.set_caption("Title Screen")
    
    
    while OnTitleScreen:
        pygame.mouse.set_visible(True)
        pygame.time.delay(20)
        screen.fill((255,255,255))
        
        
        
        CursorRect = pygame.Rect(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1],1,1)
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 'EXIT'
        
        
        
        if pds.ButtonIsActive(Start,CursorRect) and pygame.mouse.get_pressed()[0]:
            OnTitleScreen = False
            return 'Ocean'
            break
            
        if pds.ButtonIsActive(Options,CursorRect) and pygame.mouse.get_pressed()[0]:
            
            option = OptionsScreen(screen)

            if option == 'EXIT':
                return 'EXIT'
            pygame.time.delay(100)
            if pygame.mouse.get_pressed()[0]:
                while pygame.mouse.get_pressed()[0]:
                    pygame.event.get()
                    pass
                
                
                

        
            
        pygame.draw.rect(screen, Start.CurrentColor, Start.rect)
        pygame.draw.rect(screen, Options.CurrentColor, Options.rect)
        
        screen.blit(Start.Render, (172,375,(Start.Render.get_rect()).width,(Start.Render.get_rect()).height))
        screen.blit(Options.Render, (205,200,(Options.Render.get_rect()).width,(Options.Render.get_rect()).height))
        
        pygame.display.flip()    
