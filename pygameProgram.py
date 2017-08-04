import pygame
import time
import random

pygame.init()

crash_sound = pygame.mixer.Sound("crash.wav")
pygame.mixer.music.load("Jazz_In_Paris.wav")

display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)

red = (200,0,0)
green = (0,200,0)
blue = (0,0,255)

bright_red = (255,0,0)
bright_green = (0,255,0)

block_color = (53,115,255)

car_width = 82

gameDisplay = pygame.display.set_mode((display_width,display_height))  # (width,height)
pygame.display.set_caption('Race F5')
clock = pygame.time.Clock()

carImage = pygame.image.load('mycar.png')
carIcon = pygame.image.load('icon.png')

pygame.display.set_icon(carIcon)

pause = False
#crash = True

def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: "+str(count), True, black)
    gameDisplay.blit(text,(0,0))

def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])
    
    

def car(x,y):
    gameDisplay.blit(carImage,(x,y))

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(2)

    game_loop()

def crash():

    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(crash_sound)

    largeText = pygame.font.SysFont("comicsansms",115)
    TextSurf, TextRect = text_objects("You Crashed", largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    while True:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        #gameDisplay.fill(white)

        button("Play Again",150,450,100,50,green,bright_green,game_loop)
        button("Quit",550,450,100,50,red,bright_red,quitgame)
        
        pygame.display.update()
        clock.tick(15)

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    print(click)
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
         pygame.draw.circle(gameDisplay,ac,(x+int(.05*w),y),int(.05*w))
         pygame.draw.circle(gameDisplay,ac,(x+int(.95*w),y),int(.05*w))
         pygame.draw.circle(gameDisplay,ac,(x+int(.05*w),y+h),int(.05*w))
         pygame.draw.circle(gameDisplay,ac, (x+int(.95*w),y+h),int(.05*w))
         pygame.draw.rect(gameDisplay,ac,(x+.05*w,y-.05*w,.9*w,.05*w))
         pygame.draw.rect(gameDisplay,ac,(x+.05*w,y+h,.9*w,.05*w))
         if click[0] == 1 and action != None:
             action()
             
##             if action == "play":
##                 game_loop()
##             elif action == "quit":
##                 pygame.quit()
##                 quit()

    else:
        pygame.draw.circle(gameDisplay,ic,(x+int(.05*w),y),int(.05*w))
        pygame.draw.circle(gameDisplay,ic,(x+int(.95*w),y),int(.05*w))
        pygame.draw.circle(gameDisplay,ic,(x+int(.05*w),y+h),int(.05*w))
        pygame.draw.circle(gameDisplay,ic, (x+int(.95*w),y+h),int(.05*w))
        pygame.draw.rect(gameDisplay,ic,(x+.05*w,y-.05*w,.9*w,.05*w))
        pygame.draw.rect(gameDisplay,ic,(x+.05*w,y+h,.9*w,.05*w))


    smallText = pygame.font.Font("freesansbold.ttf",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)),(y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)
    

def quitgame():
    pygame.quit()
    quit()

def unpause():
    global pause
    pygame.mixer.music.unpause()
    pause = False
    

def paused():

    pygame.mixer.music.pause()

    largeText = pygame.font.SysFont("comicsansms",115)
    TextSurf, TextRect = text_objects("Paused", largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    while pause:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        #gameDisplay.fill(white)

        button("Continue",150,450,100,50,green,bright_green,unpause)
        button("Quit",550,450,100,50,red,bright_red,quitgame)
        
        pygame.display.update()
        clock.tick(15)

    
def game_intro():
    intro = True
    pygame.mixer.music.play(-1)
    
    while intro:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf',115)
        TextSurf, TextRect = text_objects("Race F5", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)

        button("Play!",150,450,100,50,green,bright_green,game_loop)
        button("Quit!",550,450,100,50,red,bright_red,quitgame)
        
        pygame.display.update()
        clock.tick(15)


def game_loop():

    global pause
    x = (display_width * 0.45)
    y = (display_height * 0.85)

    x_change = 0

    thing_startx = random.randrange(0,display_width)
    thing_starty = -500
    thing_speed = 7
    thing_width = 100
    thing_height = 100

    dodged = 0
    
    gameExit = False

    while not gameExit:
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
               pygame.quit()
               quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5
                if event.key == pygame.K_p:
                    pause = True
                    paused()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        
        x += x_change
        gameDisplay.fill(white)

        # things(thingx, thingy, thingw, thingh, color)
        things(thing_startx, thing_starty, thing_width, thing_height, blue)
        thing_starty += thing_speed    
        car(x,y)
        things_dodged(dodged)

        if x > display_width - car_width or x < 0:
            crash()

        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0,display_width)
            dodged += 1
            thing_speed += 1
            thing_width += (dodged * 1.2)

        if y < thing_starty+thing_height:
            print('y crossover')

            if x > thing_startx and x < thing_startx+thing_width or x+car_width > thing_startx and x+car_width < thing_startx+thing_width:
                print('x crossover')
                crash()
            
        pygame.display.update()
        clock.tick(60)

game_intro()
game_loop()
pygame.quit()
quit()
