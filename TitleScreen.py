import pygame
import POOPDECKSCRIPTS as pds

def TitleScreen(OnTitleScreen):
    pygame.init()

    screen = pygame.display.set_mode([500,500])

    pygame.display.set_caption("Title Screen")
    Font = pds.GetFont("HighTide",47)
    FontRender = Font.render('START', True, (255,255,255))
    StartButton = (125,375,250,50)
    while OnTitleScreen:
        pygame.mouse.set_visible(True)
        pygame.time.delay(20)
        screen.fill((255,255,255))
        pygame.draw.rect(screen, (0,0,0), StartButton)
        screen.blit(FontRender, (172,375,(FontRender.get_rect()).width,(FontRender.get_rect()).height))
        CursorRect = pygame.Rect(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1],1,1)
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 'EXIT'

        if CursorRect.colliderect(StartButton):
            if pygame.mouse.get_pressed()[0]:
                OnTitleScreen = False
                return 'Ocean'
                break
            pygame.draw.rect(screen, (0,0,255), StartButton)
            screen.blit(FontRender, (172,375, (FontRender.get_rect()).width,(FontRender.get_rect()).height))

        pygame.display.flip()    
