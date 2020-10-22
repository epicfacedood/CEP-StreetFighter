import pygame
import math
from random import randint
import os
import time 
import random

#initiates the pygame engine

pygame.init()

#Setting of basic Variables
WIDTH = 1152
HEIGHT = 648
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)
YELLOW = (255, 255, 0)
SILVER = (192, 192, 192)
BROWN = (128,  0,   0)
COLOURS = [WHITE,BLUE,GREEN,RED,YELLOW,SILVER,BROWN]
#Setting main screen 
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("cod")
clock = pygame.time.Clock()
#Opening the assets folder
game_folder = os.path.dirname(__file__)
asset_folder = os.path.join(game_folder, 'assets')

played_times = 0

character_list = ['KEN', '1', '2', '3', '4', '5','6','7','8','9']

#Transforming and Scaling External Images
def scaleimage(width,height,img):
    image = pygame.image.load(os.path.join(asset_folder, img)).convert()
    image = pygame.transform.scale(image, (width, height))
    return image

image_size = 25
explosion_sound = pygame.mixer.Sound(os.path.join(asset_folder, 'Big_Explosion_Effect_Video_Mp4_HD_Sound-bhZs3ALdL7Y.wav'))
snowflake_img = scaleimage(10,10,'christmas_star_png_transparent_background_269546.png')
background_img = scaleimage(1152,648,"image.png")
logo = scaleimage(400, 169, "logo.png")
background1_img = scaleimage(1152,648,"Preview_107.png")
option_border = scaleimage(400,100,"c94a5bb73628c4e.png")
background2_img = scaleimage(1152,648,"screen1.png")
background3_img = scaleimage(1152,648,"asde.png")
OK_img = scaleimage(100,100,"ikesoksmall-01-2000x1200.png")


backgrounds = [scaleimage(1152,648,"arena3.png"),scaleimage(1152,648,"arena1.png"),scaleimage(1152,648,"arena2.png"),scaleimage(1152,648,"arena4.png")]



class Button:
    def __init__(self, text, x, y, width, height,font_size):
        self.x = x
        self.y = y
        self.color = [255,255,255]
        self.color2 = [0,0,0]
        self.font_color = self.color
        self.font_size = font_size
        self.text = text
        self.height = height
        self.width = width
        self.round = pygame.Rect(0,0, self.width, self.height)
        self.font = Bazooka
        self.txt_surface = self.font.render(self.text, True, self.font_color)
        self.image = self.drawImage()
        self.rect = self.image.get_rect()
        self.rect.centerx = x//2
        self.rect.centery = y
        self.hover = False
        self.chr = chr
    def drawImage(self):
        surface = pygame.Surface((self.width, self.height ))
        surface.fill([0,0,0])
        surface.set_colorkey([0,0,0])
        RoundRect(surface, self.color2, self.round, 0, 8)
        RoundRect(surface, self.color, self.round, 5, 8)
        temprect = self.txt_surface.get_rect()
        temprect.centerx = self.round.centerx
        temprect.centery = self.round.centery
        surface.blit(self.txt_surface, temprect)
        return surface.convert()

    def update(self,displacementy=0):
        if pygame.mouse.get_pos()[0] > self.rect.left and pygame.mouse.get_pos()[0] < self.rect.right and pygame.mouse.get_pos()[1] > self.rect.top + displacementy and pygame.mouse.get_pos()[1] < self.rect.bottom + displacementy:
            self.hover = True
        if pygame.mouse.get_pos()[0] < self.rect.left or pygame.mouse.get_pos()[0] > self.rect.right or pygame.mouse.get_pos()[1] < self.rect.top + displacementy or pygame.mouse.get_pos()[1] > self.rect.bottom + displacementy:
            self.hover = False
        if self.hover:
            self.color = (max(self.color[0]-1,0), max(self.color[1]-1,0), max(self.color[2]-1,0))
            self.color2 = (min(self.color2[0]+1,255), min(self.color2[1]+1,255), min(self.color2[2]+1,255))
            self.txt_surface = self.font.render(self.text, True, self.color)
            self.image = self.drawImage()
        else:
            if self.color != [255,255,255]:
                self.color = (min(self.color[0]+1,255), min(self.color[1]+1,255), min(self.color[2]+1,255))
                self.color2 = (max(self.color2[0]-1,0), max(self.color2[1]-1,0), max(self.color2[2]-1,0))
                self.txt_surface = self.font.render(self.text, True, self.color)
                self.image = self.drawImage()

class border(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = option_border
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH//2
        self.rect.centery = 100
    
    def draw(self,screen):
        screen.blit(self.image,self.rect)

class border1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = option_border
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH//2
        self.rect.centery = 250
    
    def draw(self,screen):
        screen.blit(self.image,self.rect)

class border2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = option_border
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH//2
        self.rect.centery = 400
    
    def draw(self,screen):
        screen.blit(self.image,self.rect)

class border4(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = option_border
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH//2
        self.rect.centery = 550
    
    def draw(self,screen):
        screen.blit(self.image,self.rect)



class border3(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = OK_img
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH//2
        self.rect.centery = HEIGHT//2
    
    def draw(self,screen):
        screen.blit(self.image,self.rect)


border = border()
border1 = border1()
border2 = border2()
border3 = border3()
border4 = border4()
    

class food(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = foods_img_list[randint(0,2)]
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = randint(50,WIDTH-50)
        self.rect.centery = randint(50,HEIGHT-50)



class stars(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = snowflake_img
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = randint(0,WIDTH)
        self.rect.centery = randint(0,200)
        self.speedx = 1
        self.speedy = 3

    def update(self):
        if self.rect.left < 0:
            self.speedx *= -1
            self.rect.centerx += 5
        if self.rect.centerx > WIDTH:
            self.speedx *= -1
            self.rect.centerx -= 5
        if self.rect.bottom > HEIGHT + 10:
            self.rect.centery = randint(0,200)
            self.rect.centerx = randint(0,WIDTH)
        self.rect.centerx += self.speedx
        self.rect.centery += self.speedy

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.playernum = 1
        self.color = WHITE
        self.status = 1
        self.statecount = 0
        self.actionnum = 0
        self.statelimitlower = 1
        self.statelimit = [4, 5, 7, 3]
        self.action = "idle"
        self.radius = 50
        self.image = self.drawImage()
        self.rect = self.image.get_rect()
        self.speedy = 20
        self.health = 500
        self.rect.centerx = 80
        self.rect.centery = 500
        self.jump = False
        self.crouch = False
        self.damage = 0
        self.mask = pygame.mask.from_surface(self.image)
        self.cooldown = 1000
        self.jabpunchnumber = 0
        self.fiercepunchnumber = 0
        self.lowkicknumber = 0
        self.highkicknumber = 0
        self.previousjabpunch = 0
        self.previousfiercepunch = 0
        self.previouslowkick = 0
        self.previoushighkick = 0
        self.previoushadouken = 0
        self.hadoukennumber = 0
        self.hadoukenstate = False
        self.lastaction = []
        self.hit2 = False
    
 

        
    def drawImage(self):
        
        ball_surface = pygame.Surface((160,320))
        chr = scaleimage(140, 280, "{}{}.png".format(self.action,self.status))
        ball_surface.set_colorkey(ball_surface.get_at((0,0)))
        ball_surface.blit(chr,(0,0))
        return ball_surface.convert_alpha()
    def walk(self, key):
        self.action = "walking"
        self.actionnum = 1
        if key == 1:
            self.speedx = -5
        elif key == -1:
            self.speedx = 5
    def jumpinga(self):
        if self.jump:
            self.action = "jump"
            self.actionnum = 2
            self.rect.centery -= self.speedy
            self.speedy -= 1
            if self.rect.centery > 500:
                self.rect.centery = 500
                self.speedy = 22
                self.jump = False
        return 
    def jabpunch(self, modifier=None):
        if modifier == None:
            self.action = "lp"
            self.actionnum = 3
            self.damage = 20
        elif modifier == "Crouch":
            self.action = "crouchlp"
            self.actionnum = 3
            self.damage = 20
        elif modifier == "Forward":
            self.action = "fwdlp"
            self.actionnum = 3
            self.speedx = 5
            self.damage = 20
    def mp(self, modifier=None):
        if modifier == None:
            self.action = "rp"
            self.actionnum = 1
            self.damage = 25
        elif modifier == "Crouch":
            self.action = "crouchhp"
            self.actionnum = 1
            self.damage = 25
        elif modifier == "Forward":
            self.action = "crouchhp"
            self.action = 1
            self.speedx = 5
            self.damage = 25
    def fiercepunch(self, modifier=None):
        if modifier == None:
            self.action = "rp"
            self.actionnum = 1
            self.damage = 30
        elif modifier == "Crouch":
            self.action = "crouchhp"
            self.actionnum = 1
            self.damage = 30
        elif modifier == "Forward":
            self.action = "fwdhp"
            self.actionnum = 1
            self.speedx = 5
            self.damage = 30
    def lk(self, modifier=None): #Normal, Crouch and Forward
        if modifier == None:
            self.action = "lk"
            self.actionnum = 3
            self.damage = 25
        elif modifier == "Forward":
            self.action = "fwdlk"
            self.actionnum = 3
            self.speedx = 5
            self.damage = 25
    def mk(self, modifier=None):
        if modifier == None:
            self.action =  "lk"
            self.actionnum = 3
            self.damage = 35
        elif modifier == "Forward":
            self.action = "placeholderval"
            self.actionnum = 1
            self.speedx = 5
            self.damage = 35
        elif modifier == "Crouch":
            self.action = "placeholderval"
            self.actionnum = 3
            self.damage = 35
    
    def hadouken(self):
        self.action = "h"
        self.actionnum = 0
        self.damage = 80
        self.hadoukenstate = True

    def fsho(self):
            self.action = "fsho"
            self.actiionnum = 5
            self.damage = 75
    def hk(self, modifier=None): #Normal, Crouch and Forward
        if modifier == None:
            self.action = "hk"
            self.actionnum = 1
            self.damage = 45
        elif modifier == "Forward":
            self.action = "fwdhk"
            self.actionnum = 1
            self.speedx = 5
            self.damage = 60
    def hit(self, modifier = None):
        if modifier == None:
            self.action = "fhit"
            self.actionnum = 0 
    def update(self):
        key = pygame.key.get_pressed()
        self.speedx = 0
        if self.health < 0:
            self.health = 0
        if not self.crouch:
            self.statecount += 3
        if key[pygame.K_w]:
            self.jump = True
        self.jumpinga()
        
    
        

        

        if key[pygame.K_j]:
            if self.jabpunchnumber < 10:
                self.jabpunchnumber += 1
                self.previousjabpunch = pygame.time.get_ticks()
                if key[pygame.K_d]:
                    self.jabpunch("Forward")
                elif key[pygame.K_LSHIFT]:
                    self.jabpunch("Crouch")
                else:
                    self.jabpunch()
            if self.jabpunchnumber == 10:
                now = pygame.time.get_ticks()
                self.action = "idle"
                self.actionnum = 0
                if now - self.previousjabpunch < 10:
                    self.status = 1
                if now - self.previousjabpunch >= 300:
                    self.jabpunchnumber -= self.jabpunchnumber 
                    if key[pygame.K_d]:
                        self.jabpunch("Forward")
                    elif key[pygame.K_LSHIFT]:
                        self.jabpunch("Crouch")
                    else:
                        self.jabpunch()
            
        elif key[pygame.K_k]:
            if self.fiercepunchnumber < 15:
                self.fiercepunchnumber += 1
                self.previousfiercepunch = pygame.time.get_ticks()
                if key[pygame.K_d]:
                    self.fiercepunch("Forward")
                elif key[pygame.K_LSHIFT]:
                    self.fiercepunch("Crouch")
                else:
                    self.fiercepunch()
            if self.fiercepunchnumber == 15:
                now = pygame.time.get_ticks()
                if now - self.previousfiercepunch < 10:
                    self.status = 1
                self.action = "idle"
                self.actionnum = 0
                if now - self.previousfiercepunch >= 600:
                    self.fiercepunchnumber -= self.fiercepunchnumber
                    if key[pygame.K_d]:
                        self.fiercepunch("Forward")
                    elif key[pygame.K_LSHIFT]:
                        self.fiercepunch("Crouch")
                    else:
                        self.fiercepunch()
        elif key[pygame.K_i] and key[pygame.K_w]:
            self.fsho()
        elif key[pygame.K_l]:   
            if self.hadoukennumber == 0:
                self.hadoukenball = Hadouken(self)
            if self.hadoukennumber < 15:
                self.hadoukennumber += 1
                self.previoushadouken = pygame.time.get_ticks()
                self.hadouken()
            if self.hadoukennumber == 15:
                now = pygame.time.get_ticks()
                if now - self.previoushadouken < 10:
                    self.status = 1
                self.action = "idle"
                self.actionnum = 0
                if now - self.previoushadouken >= 3000:
                    self.hadoukennumber -= self.hadoukennumber
                    self.hadouken()
        elif key[pygame.K_n]:
            if self.lowkicknumber < 15:
                self.lowkicknumber += 1
                self.previouslowkick = pygame.time.get_ticks()
                if key[pygame.K_d]:
                    self.lk("Forward")
                else:
                    self.lk()
            if self.lowkicknumber == 15:
                now = pygame.time.get_ticks()
                if now - self.previouslowkick < 10:
                    self.status = 1
                self.action = "idle"
                self.actionnum = 0
                if now - self.previouslowkick >= 500:
                    self.lowkicknumber -= self.lowkicknumber
                    if key[pygame.K_d]:
                        self.lk("Forward")
                    else:
                        self.lk()

        elif key[pygame.K_m]:
            if self.highkicknumber < 15:
                self.highkicknumber += 1
                self.previoushighkick = pygame.time.get_ticks()
                if key[pygame.K_d]:
                    self.hk("Forward")
                else:
                    self.hk()
            if self.highkicknumber == 15:
                now = pygame.time.get_ticks()
                if now - self.previoushighkick < 10:
                    self.status = 1
                self.action = "idle"
                self.actionnum = 0
                if now - self.previoushighkick >= 800:
                    self.highkicknumber -= self.highkicknumber
                    if key[pygame.K_d]:
                        self.lk("Forward")
                    else:
                        self.lk()
        
        elif key[pygame.K_a]:
            self.walk(1)
        elif key[pygame.K_d]:
            self.walk(-1)
        elif key[pygame.K_s]:
            self.action = "crouch"
            self.crouch = True
            self.status = 2
        else:
            if not self.jump:
                self.action = "idle"
                self.actionnum = 0
            self.crouch = False
        self.rect.centerx += self.speedx
        if self.status >= self.statelimit[self.actionnum]:
            self.status = 1
        if self.rect.top < 0:
            self.rect.top = 0
        if self.statecount > 25:
            self.status += 1 
            self.statecount = 0
        if len(self.lastaction) < 2:
            self.lastaction.append(self.action)
        if len(self.lastaction) > 1:
            if self.lastaction[len(self.lastaction) -1 ]!= self.action:
                self.lastaction.append(self.action)
        self.image = self.drawImage()
        if self.hadoukenstate == True:
            self.hadoukenball.image = self.hadoukenball.drawImage()
    def draw(self,screen):
        screen.blit(self.image,self.rect)
        if self.hadoukenstate == True:
            screen.blit(self.hadoukenball.image, self.hadoukenball.rect)

class Hadouken(pygame.sprite.Sprite):
    def __init__(self, player):
        pygame.sprite.Sprite.__init__(self)
        self.player = player
        self.playernum = self.player.playernum
        self.status = 5
        self.image = self.drawImage()
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.centerx = self.player.rect.right
        self.rect.centery = self.player.rect.centery - 50
        self.xvelocity = 10
        self.statuscount = 0
        self.hit_player = False
    def drawImage(self):
        surface = pygame.Surface((80,80))
        if self.playernum == 1:
            blast = scaleimage(80,80, "h{}.png".format(self.status))
            surface.set_colorkey(surface.get_at((0,0)))
            surface.blit(blast,(0,0))
        if self.playernum == 2:
            blast = pygame.transform.flip(scaleimage(40,40,"h{}.png".format(self.status)))
        return surface.convert_alpha()
    def update(self):
        self.rect.x += self.xvelocity
        offset_x = self.rect.left - player2.rect.left
        offset_y = self.rect.top - player2.rect.top
        if self.playernum == 1:
            if self.mask.overlap(player2.mask, (offset_x, offset_y)):
                self.hit_player = True
        if not self.hit_player:
            self.statuscount += 1
            if self.statuscount > 25:
                self.status += 1
            if self.status > 6:
                self.status = 5
        if self.hit_player:
            self.player.hadoukenstate = False
            self.kill()
            self.status += 1
            if self.status > 9:
                self.status = 9
        self.drawImage()
        



    
    def draw(self,screen):

        screen.blit(self.image,self.rect)



class Player2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.playernum = 2
        self.color = WHITE
        self.status = 1
        self.statecount = 0
        self.actionnum = 0
        self.statelimitlower = 1
        self.statelimit = [4, 5, 7]
        self.action = "idle"
        self.damage = 50
        self.radius = 50
        self.image = self.drawImage()
        self.rect = self.image.get_rect()
        self.speedy = 22
        self.health = 500
        self.rect.centerx = 1100
        self.rect.centery = 500
        self.jump = False
        self.mask = pygame.mask.from_surface(self.image)
        self.hit1 = False
        self.crouch = False
        self.cooldowntime = 0

    def drawImage(self, hit=False):
        if not hit:
            ball_surface = pygame.Surface((160,320))
            chr = pygame.transform.flip(scaleimage(140, 280, "{}{}.png".format(self.action,self.status)), True, False)
            ball_surface.set_colorkey(ball_surface.get_at((0,0)))
            ball_surface.blit(chr,(0,0))
            return ball_surface.convert_alpha()
        elif hit:
            ball_surface = pygame.Surface((200,320))
            chr = pygame.transform.flip(scaleimage(140, 280, "{}{}.png".format(self.action,self.status)), True, False)
            ball_surface.set_colorkey(ball_surface.get_at((0,0)))
            ball_surface.blit(chr,(0,0))
            return ball_surface.convert_alpha()
    def hit(self, modifier = None):
        if modifier == None:
            self.action = "fhit"
            self.actionnum = 0  

    def walk(self, key):
        self.action = "walking"
        self.actionnum = 1
        if key == 1:
            self.speedx = -5
        elif key == -1:
            self.speedx = 5
    def jumpinga(self):
        if self.jump:
            self.action = "jump"
            self.actionnum = 2
            self.rect.centery -= self.speedy
            self.speedy -= 1
            if self.rect.centery > 500:
                self.rect.centery = 500
                self.speedy = 22
                self.jump = False
        return 
    def jabpunch(self, modifier=None):
        if modifier == None:
            self.action = "lp"
            self.actionnum = 3
            self.damage = 20
        elif modifier == "Crouch":
            self.action = "crouchlp"
            self.actionnum = 3
            self.damage = 20
        elif modifier == "Forward":
            self.action = "fwdlp"
            self.actionnum = 3
            self.speedx = 5
            self.damage = 20
    def mp(self, modifier=None):
        if modifier == None:
            self.action = "rp"
            self.actionnum = 1
            self.damage = 25
        elif modifier == "Crouch":
            self.action = "crouchhp"
            self.actionnum = 1
            self.damage = 25
        elif modifier == "Forward":
            self.action = "crouchhp"
            self.action = 1
            self.speedx = 5
            self.damage = 25
    def fiercepunch(self, modifier=None):
        if modifier == None:
            self.action = "rp"
            self.actionnum = 1
            self.damage = 30
        elif modifier == "Crouch":
            self.action = "crouchhp"
            self.actionnum = 1
            self.damage = 30
        elif modifier == "Forward":
            self.action = "fwdhp"
            self.actionnum = 1
            self.speedx = 5
            self.damage = 30
    def lk(self, modifier=None): #Normal, Crouch and Forward
        if modifier == None:
            self.action = "lk"
            self.actionnum = 3
            self.damage = 25
        elif modifier == "Forward":
            self.action = "fwdlk"
            self.actionnum = 3
            self.speedx = 5
            self.damage = 25
    def mk(self, modifier=None):
        if modifier == None:
            self.action =  "lk"
            self.actionnum = 3
            self.damage = 35
        elif modifier == "Forward":
            self.action = "placeholderval"
            self.actionnum = 1
            self.speedx = 5
            self.damage = 35
        elif modifier == "Crouch":
            self.action = "placeholderval"
            self.actionnum = 3
            self.damage = 35
    
    def hadouken(self):
        self.action = "h"
        self.actionnum = 0
        self.damage = 80
        self.hadoukenstate = True

    def fsho(self):
            self.action = "fsho"
            self.actiionnum = 5
            self.damage = 75
    def hk(self, modifier=None): #Normal, Crouch and Forward
        if modifier == None:
            self.action = "hk"
            self.actionnum = 1
            self.damage = 45
        elif modifier == "Forward":
            self.action = "fwdhk"
            self.actionnum = 1
            self.speedx = 5
            self.damage = 60
    def hit(self, modifier = None):
        if modifier == None:
            self.action = "fhit"
            self.actionnum = 0 

    def update(self):
        key = pygame.key.get_pressed()
        self.speedx = 0
        if self.health < 0:
            self.health = 0
        if not self.crouch:
            self.statecount += 3
        if self.hit1:
            self.hit()
        elif not self.hit1:
            if self.jump:
                self.rect.centery -= self.speedy
                self.speedy -= 1
                if self.rect.centery > 500:
                    self.rect.centery = 500
                    self.speedy = 22
                    self.jump = False
                
            #if key[pygame.K_w]:
                #self.speedy = -10
            #if key[pygame.K_s]:
                #self.speedy = 10
            if key[pygame.K_LEFT]:
                self.action = "walking"
                self.actionnum = 1
                self.speedx = -5
            elif key[pygame.K_RIGHT]:
                self.action = "walking"
                self.actionnum = 1
                self.speedx = 5
            elif key[pygame.K_UP]:
                self.jump = True
            elif self.jump:
                self.action = "jump"
                self.actionnum = 2
            else:
                self.action = "idle"
                self.actionnum = 0

        self.rect.centerx += self.speedx
        if not self.hit1:
            if self.rect.top < 0:
                self.rect.top = 0
            if self.statecount > 25:
                self.status += 1 
                self.statecount = 0
            if self.status >= self.statelimit[self.actionnum]:
                self.status = 1
            self.image = self.drawImage()
        elif self.hit1:
            if self.statecount > 50:
                self.status += 1
                self.statecount = 0
            if self.status >= self.statelimit[self.actionnum]:
                self.status = 1
                self.hit1 = False
            self.image = self.drawImage(True)

    def draw(self,screen):
        pygame.draw.rect(screen, [50, 40, 60], [self.rect.x, self.rect.y, 140, 280])
        screen.blit(self.image,self.rect)

player1 = Player()
player2 = Player2()

class Healthbar():
    def __init__(self, player):
        self.player = player
        self.width = self.player.health
        if player.playernum == 1:
            self.x = 40
        elif player.playernum == 2:
            self.x = WIDTH//2 + 40
        self.y = 30

    
    def update(self):
        self.width = self.player.health

    def draw(self, screen):
        pygame.draw.rect(screen, [255,255,255], (self.x-2, self.y-2, 500+4, 34), 2)
        pygame.draw.rect(screen, [255,0,0], (self.x,self.y , self.width , 30))


class Centre(pygame.sprite.Sprite):
    def __init__(self,player):
        pygame.sprite.Sprite.__init__(self)
        self.color = RED
        self.radius = 5
        self.image = self.drawImage()
        self.player = player
        self.rect = self.image.get_rect()
        self.rect.centerx = self.player.rect.centerx
        self.rect.centery = self.player.rect.centery

    def drawImage(self):
        ball_surface = pygame.Surface((self.radius*2,self.radius*2))
        ball_surface.fill(self.color)
        ball_surface.set_colorkey(self.color)
        return ball_surface.convert()

    def update(self):
        self.radius = self.player.radius - 30
        self.rect.centerx = self.player.rect.centerx
        self.rect.centery = self.player.rect.centery
        self.rect = self.image.get_rect(center=(self.rect.centerx,self.rect.centery))
        self.image = self.drawImage()


class Centre2(pygame.sprite.Sprite):
    def __init__(self,player):
        pygame.sprite.Sprite.__init__(self)
        self.color = RED
        self.radius = 5
        self.player = player
        self.image = self.drawImage()
        self.rect = self.image.get_rect()
        self.rect.centerx = self.player.rect.centerx
        self.rect.centery = self.player.rect.centery

    def drawImage(self):
        ball_surface = pygame.Surface((self.radius*2,self.radius*2))
        ball_surface.fill(self.color)
        ball_surface.set_colorkey(self.color)
        return ball_surface.convert()


    def update(self):
        self.rect.centerx = self.player.rect.centerx
        self.rect.centery = self.player.rect.centery
        self.rect = self.image.get_rect(center=(self.rect.centerx,self.rect.centery))
        self.image = self.drawImage()


def RoundRect(surface, color, rect, width, r): # Function for making rounded rectangles (for the buttons)

    clip = surface.get_clip() #makes a clip
    
    surface.set_clip(clip.clip(rect.inflate(0, -r*2)))
    pygame.draw.rect(surface, color, rect.inflate(1-width,0), width)

    surface.set_clip(clip.clip(rect.inflate(-r*2, 0)))
    pygame.draw.rect(surface, color, rect.inflate(0,1-width), width)

    surface.set_clip(clip.clip(rect.left, rect.top, r, r)) #top left
    pygame.draw.ellipse(surface, color, pygame.Rect(rect.left, rect.top, 2*r, 2*r), width)

    surface.set_clip(clip.clip(rect.right-r, rect.top, r, r)) #top right
    pygame.draw.ellipse(surface, color, pygame.Rect(rect.right-2*r, rect.top, 2*r, 2*r), width)

    surface.set_clip(clip.clip(rect.left, rect.bottom-r, r, r)) # bottom left
    pygame.draw.ellipse(surface, color, pygame.Rect(rect.left, rect.bottom-2*r, 2*r, 2*r), width)

    surface.set_clip(clip.clip(rect.right-r, rect.bottom-r, r, r)) # bottom right
    pygame.draw.ellipse(surface, color, pygame.Rect(rect.right-2*r, rect.bottom-2*r, 2*r, 2*r), width)

    surface.set_clip(clip) 

#Fonts and Text
def textrect(text,x,y):
    textbox = text.get_rect()
    textbox.centerx = x//2
    textbox.centery = y
    screen.blit(text,textbox)
    
Bazooka = pygame.font.SysFont("bazooka",30,True,False)
Bazooka1 = pygame.font.SysFont("bazooka",20,True,False)
text1 = Bazooka.render("P L A Y  G A M E", True, BLACK)
text2 = Bazooka.render("I N S T R U C T I O N S", True, BLACK)
text3 = Bazooka1.render("USE KEY A TO MOVE LEFT KEY AND D TO MOVE RIGHT", True, WHITE)
text4 = Bazooka1.render("PRESS W TO JUMP", True, BLACK)
text9 = Bazooka1.render("PRESS J AND K TO DO PUNCHES", True, BLACK)
text10 = Bazooka1.render("PRESS N AND M TO DO KICKS", True, BLACK)
text5 = Bazooka1.render("USE YOUR FIGHTING SKILLS                                                   TO BEAT THE OPPONENT!", True, YELLOW)
text6 = Bazooka.render("PLAYER 1 WON", True, YELLOW)
text7 = Bazooka.render("PLAYER 2 WON", True, YELLOW)
text8 = Bazooka.render("M A P  S E L E C T", True, WHITE)

#RESTART
def restart():
    for x in all_sprites:
        x.kill()


#START MENU
def menu():
    
    menu = False
    # buttona = Button("E X P L O S I V E  A G A R I O",WIDTH,100, 400, 100, 30)
    buttonb = Button("P L A Y  G A M E ",WIDTH,250, 400, 100, 30)
    buttonc = Button("I N S T R U C T I O N S", WIDTH, 400, 400, 100, 30)
    buttond = Button("S E L E C T  C H A R A C T E R", WIDTH, 550, 400, 100, 30)
    img_rect = logo.get_rect()
    img_rect.centerx = WIDTH//2
    img_rect.centery = 100
    game_started = False
    # reset1()
    # reset2()
    while not menu:
        # buttona.update()
        buttonb.update()
        buttonc.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseposx, mouseposy = pygame.mouse.get_pos()
                if (border1.rect.left + 1) <= mouseposx and (border1.rect.right - 1) >= mouseposx and (border1.rect.top - 1) <= mouseposy and (border1.rect.bottom + 1) >= mouseposy:
                    pygame.mixer.Sound.play(explosion_sound)
                    pygame.mixer.music.stop()
                    restart()
                    selection()
                    menu = True
                if (border2.rect.left + 1) <= mouseposx and (border2.rect.right - 1) >= mouseposx and (border2.rect.top - 1) <= mouseposy and (border2.rect.bottom + 1) >= mouseposy:
                    pygame.mixer.Sound.play(explosion_sound)
                    pygame.mixer.music.stop()
                    instructions()
                    menu = True
                
        pygame.draw.rect(screen, [0,0,0], (0,0 , WIDTH ,HEIGHT))
        # screen.blit(buttona.image, buttona.rect)
        screen.blit(buttonb.image, buttonb.rect)
        screen.blit(buttonc.image, buttonc.rect)
        # textrect(text, WIDTH, 100)
        screen.blit(logo, img_rect)
        # textrect(text2,WIDTH,450)
        # border2.draw(screen)
        pygame.display.flip()

def pause():
    pause = False
    buttonc = Button("C O N T I N U E", 1176, HEIGHT/2, 400, 100, 30)
    buttona = Button("Q U I T  T O  M E N U", 1176, HEIGHT * (3/4), 400, 100, 30)
    while not pause:
        buttonc.update()
        buttona.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseposx, mouseposy = pygame.mouse.get_pos()
                if (buttonc.rect.left + 1) <= mouseposx and (buttonc.rect.right - 1) >= mouseposx and (buttonc.rect.top - 1) <= mouseposy and (buttonc.rect.bottom + 1) >= mouseposy:
                        pygame.mixer.Sound.play(explosion_sound)
                        pygame.mixer.music.stop()
                        main_game()
                        pause = True
                if (buttona.rect.left + 1) <= mouseposx and (buttona.rect.right - 1) >= mouseposx and (buttona.rect.top - 1) <= mouseposy and (buttona.rect.bottom + 1) >= mouseposy:
                        pygame.mixer.Sound.play(explosion_sound)
                        pygame.mixer.music.stop()
                        menu()
                        pause = True
        screen.blit(background3_img,[0,0])
        screen.blit(buttonc.image,buttonc.rect)
        screen.blit(buttona.image, buttona.rect)
        pygame.display.flip()

#INSTRUCTIONS MENU
def instructions():
    instructions = False
    while not instructions:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseposx, mouseposy = pygame.mouse.get_pos()

                if (border3.rect.left + 1) <= mouseposx and (border3.rect.right - 1) >= mouseposx and (border3.rect.top - 1) <= mouseposy and (border3.rect.bottom + 1) >= mouseposy:
                        pygame.mixer.Sound.play(explosion_sound)
                        pygame.mixer.music.stop()
                        menu()
                        instructions = Truex
        screen.blit(background2_img,[0,0])
        # buttona = Button(text3,WIDTH//2, 100)
        textrect(text4,(2*(WIDTH - WIDTH//4)), HEIGHT - 100)
        textrect(text9, (2*(WIDTH - WIDTH//4)), HEIGHT - 200)
        textrect(text10, (2*(WIDTH-WIDTH//4)), HEIGHT - 150)
        textrect(text5,WIDTH,HEIGHT//2)
        textrect(text3,WIDTH//2, 100)

        border3.draw(screen)
        pygame.display.flip()

#SELECTION MENU
def selection():
    global map_number 
    buttonc = Button("arena1.png", 525, 200, 500, 275, 30)
    buttoni = Button("iasdawsd", 525, 500, 500, 275, 30)
    buttonj = Button("j", 1775, 500, 500, 275, 30)
    buttonk = Button("k", 1775, 200, 500, 275, 30)
   
    selection = False
 
    while not selection:


        buttonj.update()

        buttonk.update()
    
        buttoni.update()
      
        buttonc.update() 

        for event in pygame.event.get():
            if event.type == pygame.QUIT:   
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseposx, mouseposy = pygame.mouse.get_pos()
                if (buttoni.rect.left + 1) <= mouseposx and (buttoni.rect.right - 1) >= mouseposx and (buttoni.rect.top - 1) <= mouseposy and (buttoni.rect.bottom + 1) >= mouseposy:
                    
                    map_number = 0
                    pygame.mixer.Sound.play(explosion_sound)
                    pygame.mixer.music.stop()
                    restart()
                    main_game()
                elif (buttonj.rect.left + 1) <= mouseposx and (buttonj.rect.right - 1) >= mouseposx and (buttonj.rect.top - 1) <= mouseposy and (buttonj.rect.bottom + 1) >= mouseposy:
                    
                    map_number = 1
               
                    pygame.mixer.Sound.play(explosion_sound)
                    pygame.mixer.music.stop()   
                    restart()
                    main_game()
                elif (buttonc.rect.left + 1) <= mouseposx and (buttonc.rect.right - 1) >= mouseposx and (buttonc.rect.top - 1) <= mouseposy and (buttonc.rect.bottom + 1) >= mouseposy:
                    
                    map_number = 2

                    pygame.mixer.Sound.play(explosion_sound)
                    pygame.mixer.music.stop()
                    restart()
                    main_game()
                elif (buttonk.rect.left + 1) <= mouseposx and (buttonk.rect.right - 1) >= mouseposx and (buttonk.rect.top - 1) <= mouseposy and (buttonk.rect.bottom + 1) >= mouseposy:
                    
                    map_number = 3


                    pygame.mixer.Sound.play(explosion_sound)
                    pygame.mixer.music.stop()
                    restart()
                    main_game()
        screen.blit(background3_img,[0,0])
        textrect(text8, WIDTH, 50)
        screen.blit(scaleimage(500,275,"arena1.png"), buttonj.rect)
        screen.blit(scaleimage(500,275,"arena2.png"), buttonc.rect)
        screen.blit(scaleimage(500,275,"arena3.png"), buttoni.rect)
        screen.blit(scaleimage(500,275,"arena4.png"), buttonk.rect)
        
        
       
        
        pygame.display.flip()
# centre1 = centre()
# centre2 = centre2()
foods = pygame.sprite.Group()
players = pygame.sprite.Group()
# players.add(player1)
# players.add(player2)
all_sprites = pygame.sprite.Group()
# all_sprites.add(player1)
# all_sprites.add(player2)
# all_sprites.add(centre1)
# all_sprites.add(centre2)

def reset1(p1,p2,c1,c2):
    c1.radius = 5
    c2.radius = 5
    p1.radius = 50 
    p2.radius = 50
    p1.rect = p1.image.get_rect(center=(80,HEIGHT//2))
    p2.rect = p2.image.get_rect(center=(WIDTH-80,HEIGHT//2))
    players.add(p2)
    all_sprites.add(p2)
    all_sprites.add(c2)
    
def reset2(p1,p2,c1,c2):
    c1.radius = 5
    c2.radius = 5
    p1.radius = 50 
    p2.radius = 50
    p1.rect = p1.image.get_rect(center=(80,HEIGHT//2))
    p2.rect = p2.image.get_rect(center=(WIDTH-80,HEIGHT//2))
    players.add(p1)
    all_sprites.add(p1)
    all_sprites.add(c1)


    # all_sprites.add(x)


def main_game():
    done = False
    cooldowntimer = 1000
    cooldownnumber = 0
    cooldown = False
    cooldown2 = False
    overlap_once = False
    for x in range(10):
        i = stars()
        all_sprites.add(i)
    player1 = Player()
    player2 = Player2()
    centre1 = Centre(player1)
    centre2 = Centre2(player2)
    Healthbar1 = Healthbar(player1)
    Healthbar2 = Healthbar(player2)
    players.add(player1)
    players.add(player2)
    all_sprites.add(player1)
    all_sprites.add(player2)
    all_sprites.add(centre1)
    all_sprites.add(centre2)
    buttonp = Button(" I I ",WIDTH, 50, 50, 50, 20)

    time_elapsed = 0
    attackmode = False


    while not done:
        if player1.hadoukenstate == True:
            if player2.rect.centerx - player1.hadoukenball.rect.centerx < 199.888888 and player1.hadoukenball.rect.centerx < 1100:
                player2.jump = True
                player2.action = "jump"
                player2.actionnum = 2
                player2.jumpinga()
                    
        if player1.rect.centerx == 50:
            player1.rect.centerx += 5
        if player2.rect.centerx == 50:
            player2.rect.centerx += 5
        if player1.rect.centerx == 1100:
            player1.rect.centerx -= 5
        if player2.rect.centerx == 1100:
            player2.rect.centerx -= 10
        
        timepassed = pygame.time.get_ticks()
        time_elapsed += timepassed
       
        if time_elapsed > 1500000:
            x = random.randint(0,2)
            time_elapsed = 0

    
        if x == 0:
            if player1.rect.centerx - player2.rect.centerx != 0:
                if (player1.rect.centerx - player2.rect.centerx) < 0:
                    player2.action = "walking"
                    player2.actionnum = 1
                    player2.rect.centerx -= 5
                    if player2.rect.centerx == player1.rect.centerx:
                        player2.action = "walking"
                        player2.actionnum = 1
                        player2.rect.centerx += 10
                elif (player1.rect.centerx - player2.rect.centerx) > 0:
                    player2.action = "walking"
                    player2.actionnum = 1
                    player2.rect.centerx += 5
                    if player2.rect.centerx == player1.rect.centerx:
                        player2.action = "walking"
                        player2.actionnum = 1
                        player2.rect.centerx -= 10
            
        elif x == 1:
            if player2.rect.centerx == player1.rect.centerx + 200:
                if player1.rect.centerx == player1.rect.centerx + 5:
                    player2.action = "walking"
                    player2.actionnum = 1
                    player2.rect.centerx += 5
                elif player1.rect.centerx == player1.rect.centerx - 5:
                    player2.action = "walking"
                    player2.actionnum = 1
                    player2.rect.centerx -= 5
        elif x == 2:
            hold = True
            player2.action = "walking"
            player2.actionnum = 1
            player2.rect.centerx += 5
            if player2.rect.centerx == 1070:
                hold = False
            if hold == False:
                player2.rect.centerx -= 5

        if player1.hadoukenstate == True:
            all_sprites.add(player1.hadoukenball)
        # if player2.hadoukenstate == True:
        #     all_sprites.add(player2.hadoukenball) 
        buttonp.update()
        Healthbar1.update()
        Healthbar2.update()
        if player1.health == 0:
            gameover(2)
        if player2.health == 0:
            gameover(1)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseposx, mouseposy = pygame.mouse.get_pos()
                if (buttonp.rect.left + 1) <= mouseposx and (buttonp.rect.right - 1) >= mouseposx and (buttonp.rect.top - 1) <= mouseposy and (buttonp.rect.bottom + 1) >= mouseposy:
                        pygame.mixer.Sound.play(explosion_sound)
                        pygame.mixer.music.stop()
                        pause()
        offset_x = player1.rect.left - player2.rect.left
        offset_y = player1.rect.top - player2.rect.top
        collide = player1.mask.overlap(player2.mask, (offset_x, offset_y))
        collide_hadouken = None
        if player1.hadoukenstate != False:
            collide_hadouken = player1.hadoukenball.mask.overlap(player2.mask, (player1.hadoukenball.rect.left - player2.rect.left, player2.rect.top - player1.hadoukenball.rect.top)) 
        if collide_hadouken:
            if cooldown != True:
                hittime = pygame.time.get_ticks()
                player2.health -= player1.damage
                player2.hit1 = True
                cooldown = True
            if cooldown:
                now = pygame.time.get_ticks()
                if now - hittime >= cooldowntimer:
                    cooldown = False
        if collide:
            hit = False
            if time_elapsed > 1500000 and hit == False:
                print("truE")
                player2.action = "rp"
                player2.actionnum = 1
                player2.fiercepunch()
                hit = True
            
                if player2.action == "lp" or player2.action == "fwdlp" or player2.action == "rp" or player2.action == "fwdhp" or player2.action == "fwdlk" or player2.action == "lk" or player2.action == "hk" or player2.action == "fwdhk":
                    if cooldown!= True:
                        hittime = pygame.time.get_ticks()
                       
                        player1.hit2 = True
                        cooldown = True
                    if cooldown:
                        now = pygame.time.get_ticks()
                        if now - hittime >= cooldowntimer: 
                            cooldown = False
            
           
            if player1.action == "lp" or player1.action == "fwdlp" or player1.action == "rp" or player1.action == "fwdhp" or player1.action == "fwdlk" or player1.action == "lk" or player1.action == "hk" or player1.action == "fwdhk" or player1.action == "h" or player1.action == "fsho":
                if cooldown!= True:
                    hittime = pygame.time.get_ticks()
                    player2.health -= player1.damage
                    player2.hit1 = True
                    cooldown = True
                if cooldown:
                    now = pygame.time.get_ticks()
                    if now - hittime >= cooldowntimer: 
                        cooldown = False
            
                

        screen.blit(backgrounds[map_number],[0,0])
        screen.blit(buttonp.image, buttonp.rect)
        Healthbar1.draw(screen)
        Healthbar2.draw(screen)
        all_sprites.draw(screen)
        all_sprites.update()
        clock.tick(60)
        pygame.display.flip()


def gameover(who_won):
    gameover = False
    buttona = Button("Q U I T  T O  M E N U", 1176, HEIGHT * (3/4), 400, 100, 30)
    while not gameover:
        buttona.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseposx, mouseposy = pygame.mouse.get_pos()
                if (buttona.rect.left + 1) <= mouseposx and (buttona.rect.right - 1) >= mouseposx and (buttona.rect.top - 1) <= mouseposy and (buttona.rect.bottom + 1) >= mouseposy:
                        pygame.mixer.Sound.play(explosion_sound)
                        pygame.mixer.music.stop()
                        menu()
                        gameover = True
        screen.blit(background3_img,[0,0])
        if who_won == 1:
            textrect(text6, WIDTH, 50)
        elif who_won == 2:
            textrect(text7, WIDTH, 50)
        screen.blit(buttona.image, buttona.rect)
        pygame.display.flip()

menu()
pygame.quit()
    