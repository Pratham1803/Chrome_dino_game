import pygame
import random
from time import sleep

pygame.init()
pygame.mixer.init()

#colors
white = (255, 255, 255)
black = (0,0,0)

# creating Window for game
screen_width = 1000
screen_hight = 600
game_window = pygame.display.set_mode((screen_width, screen_hight))
pygame.display.set_caption("TRAX Game Created by Pratham Rathod")
font1 = pygame.font.SysFont(None, 40)

def text_screen(text, color, x, y):
    screen_text = font1.render(text, True, color)
    game_window.blit(screen_text, [x,y])
#game loop
def game():
    #Import images and sounds
    bgimg = pygame.image.load("Gallary\\background.png")
    bgimg = pygame.transform.scale(bgimg, [screen_width,screen_hight])

    dino =  pygame.image.load("Gallary\\main-character3.png")
    dino = pygame.transform.scale(dino, [70,70])

    dino2 =  pygame.image.load("Gallary\\main-character1.png")
    dino2 = pygame.transform.scale(dino2, [70,70])

    dino3 =  pygame.image.load("Gallary\\main-character2.png")
    dino3 = pygame.transform.scale(dino3, [70,70])

    dino4 = pygame.image.load("Gallary\\main-character4.png")
    dino4 = pygame.transform.scale(dino4, [70,70])

    captus1 = pygame.image.load("Gallary\\cactus1.png")
    captus1 = pygame.transform.scale(captus1, [40,70])

    captus2 = pygame.image.load("Gallary\\cactus2.png")
    captus2 = pygame.transform.scale(captus2, [80,65])

    captus3 = pygame.image.load("Gallary\\cactus3.png")
    captus3 = pygame.transform.scale(captus3, [80,95])

    captus4 = pygame.image.load("Gallary\\cactus4.png")
    captus4 = pygame.transform.scale(captus4, [100,85])
    
    #dino_walking
    walk = 0
    dino_walk = [dino, dino, dino2, dino2, dino3, dino3,dino4]

    #game useful variables
    
    exit_game = False
    game_over = False
    bgvelocity_x = 0
    bg_x = 0
    bg_y = 0
    dino_x = 50
    dino_y = 315
    game_start = False
    captus_x = 600
    captus_y = 315
    gravity = 15
    jump = False
    score = 0
    bg_speed = 8
    while not exit_game:

        if game_over:
           
            game_over_img = pygame.image.load("Gallary\gameover_text.png")
            game_window.blit(game_over_img, [400,200])

            reply_img = pygame.image.load("Gallary\\replay_button.png")
            game_window.blit(reply_img, [480,250])

            text_screen("Score "+str(score),black, 800, 50)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.QUIT
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP or event.key == pygame.K_SPACE:
                        game()
            pygame.display.update()

        else:
              
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.QUIT
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP or event.key == pygame.K_SPACE:
                        bgvelocity_x = bg_speed
                        game_start = True

                        if dino_y > 314:
                            jump = True
                            pygame.mixer.music.load("Gallary\wing.wav")
                            pygame.mixer.music.play()
                            score += 10
                            bg_speed += 0.1
            
            # infinet background
            bg_x -= bgvelocity_x
            game_window.fill(white)
            if bg_x < -999:
                bg_x = 0
            game_window.blit(bgimg, [bg_x,bg_y])
            game_window.blit(bgimg, [bg_x+1000,bg_y])

            # captus
            captus_x -= bgvelocity_x
            
            game_window.blit(captus1, [captus_x, captus_y])
            if captus_x < -1805:
                captus_x = 999

            game_window.blit(captus2, [captus_x+600, captus_y])
            game_window.blit(captus3, [captus_x+1200, captus_y-20])
            game_window.blit(captus4, [captus_x+1800, captus_y-15])
        
            # dino blit
            game_window.blit(dino_walk[walk], [dino_x, dino_y])
            if game_start:
                walk += 1
                if walk > 5:
                    walk = 0
                
            #dino jump
            if 316 > dino_y > 125:
                if jump:
                    walk = 0
                    dino_y -= 15
                    
            else:
                jump = False
                
            if dino_y < 315:
                if jump == False:  
                    dino_y += gravity  
            
            # game out
            if dino_x -30 < captus_x < dino_x + 70 and dino_y > captus_y-60:
                game_window.blit(dino_walk[6], [dino_x, dino_y])
                pygame.mixer.music.load("Gallary\hit.wav")
                pygame.mixer.music.play()
                game_over = True
                
            if dino_x - 70 < captus_x + 600 < dino_x + 70 and dino_y > captus_y-55:
                game_window.blit(dino_walk[6], [dino_x, dino_y])
                pygame.mixer.music.load("Gallary\hit.wav")
                pygame.mixer.music.play()
                game_over = True
                 
            if dino_x - 70 < captus_x + 1200 < dino_x + 70 and dino_y > captus_y-75+20:
                game_window.blit(dino_walk[6], [dino_x, dino_y])
                pygame.mixer.music.load("Gallary\hit.wav")
                pygame.mixer.music.play()
                game_over = True
                
            if dino_x - 90 < captus_x + 1800 < dino_x + 70 and dino_y > captus_y-85+15:
                game_window.blit(dino_walk[6], [dino_x, dino_y])
                pygame.mixer.music.load("Gallary\hit.wav")
                pygame.mixer.music.play()
                game_over = True

            if score % 100 == 0 and score != 0:
                pygame.mixer.music.load("Gallary\point.wav")
                pygame.mixer.music.play()
                
            text_screen("Score "+str(score),black, 800, 50)
            pygame.display.update()

game()
