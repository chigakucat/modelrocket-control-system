# -*- coding: utf-8 -*-
from pygame.locals import *
import pygame
import sys
import io

def main():
    pygame.init()    # Pygame reset
    screen = pygame.display.set_mode((300, 100))    # window
    pygame.display.set_caption("model rocket control app")    #app title
    
    StartBtn = pygame.Rect(30, 30, 70, 50)
    pausBtn  = pygame.Rect(115, 30, 70, 50)
    StopBtn  = pygame.Rect(200, 30, 70, 50)
    emergencyBtn = pygame.Rect(200, 30, 70, 50)
    #button font
    font = pygame.font.SysFont(None, 25)
    
    #button text
    text1 = font.render("alert", True, (0,0,0))
    text2 = font.render("stop", True, (0,0,0))
    #text3 = font.render("STOP",  True, (0,0,0))
    text4 = font.render("urgency", True, (0,0,0))
    textpos  = text1.get_rect()
    textpos  = text2.get_rect()
    textpos  = text4.get_rect()
 

    #Mixer reset
    pygame.mixer.init(frequency = 44100)
    
    paused = False
    
    running = True

    #loop
    while running:
        screen.fill((0,0,0))  #Fill with black
        
        pygame.draw.rect(screen, (255, 0, 0), StartBtn)
        pygame.draw.rect(screen, (0, 255, 0), pausBtn)
        pygame.draw.rect(screen, (255, 0, 255), StopBtn)
        pygame.draw.rect(screen, (255, 0, 255), emergencyBtn)

        screen.blit(text1, (40, 45))
        screen.blit(text2, (125,45))
     #   screen.blit(text3, (205,45))
        screen.blit(text4, (205,45))

        pygame.display.update() #draw
        for event in pygame.event.get():
            if event.type == QUIT:  #end event
                running = False
                pygame.quit()  #close pygame window
                sys.exit() #exit
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if StartBtn.collidepoint(event.pos):
                    pygame.mixer.music.load("sound/alert.mp3")     # sound read
                    pygame.mixer.music.play()
                    print("lunch alert")
                    
                if pausBtn.collidepoint(event.pos):
                    pygame.mixer.music.pause()
                    paused = True
                    print("stop alert")
                
                if StopBtn.collidepoint(event.pos):
                    paused = True
                    pygame.mixer.music.stop()
                    print("emergency alert")

                if emergencyBtn.collidepoint(event.pos):
                    pygame.mixer.music.load("sound/emergency.mp3")
                    pygame.mixer.music.play()
                    print("emergency")

if __name__=="__main__":
    main()
