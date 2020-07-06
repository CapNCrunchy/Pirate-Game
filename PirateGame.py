import pygame
import OceanOverworld
import ExploreIsland
import TitleScreen
Loops = {'Ocean':False,'Title':True,'Island':False,'EXIT':False}

LoopRightNow = ''



def RunningTheLoop(Loop):
    NextLocation = False
    if Loop == 'Ocean':
        NextLocation = OceanOverworld.OceanOverworldFunc(True)
        return NextLocation
    if Loop == 'Island':
        NextLocation =ExploreIsland.IslandExploration(True)
        return NextLocation
    if Loop == 'Title':
        NextLocation = TitleScreen.TitleScreen(True)
        return NextLocation
    if Loop == 'EXIT':
        pygame.quit()
        exit()

Mainloop = True
while Mainloop:
    for loop in Loops:
        if Loops[loop] == True:
            NewLocation = RunningTheLoop(loop)
            Loops[loop] = False
            Loops[str(NewLocation)] = True
