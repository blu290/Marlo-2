import pygame
import math
import time
import sys
import random
try:
  from pathfinding.core.diagonal_movement import DiagonalMovement
  from pathfinding.core.grid import Grid
  from pathfinding.finder.a_star import AStarFinder
  from pygame.constants import NOEVENT
except ModuleNotFoundError:
    print("pathfinding library not found. in order to play this game pathfinding is required.\n for more information on how to get pathfinding, visit https://pypi.org/project/pathfinding/ \n ")
    print("exiting in 10 seconds...")
    time.sleep(10)
    sys.exit()
#import numpy

class Marlo(pygame.sprite.Sprite):
  def __init__(self,image,scale,x,y,health,damage):
    super().__init__()
    self.name = "marlo"
    self.special = 0
    self.maxSpecial = 3
    width = image.get_width()
    height = image.get_height()
    self.image = image
    self.image = pygame.transform.scale(image,(int(width*scale),int(height*scale)))
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y
    self.maxHealth = health
    self.health = self.maxHealth
    self.invincibilityFrames = 30
    self.damage = damage
    self.specialTicks = 240
    self.specialReady = 240
    self.healthincrease = 4
    self.shootFrames = 20
    self.shootCooldown = self.shootFrames
    self.bulletPenetration = 1
  
  def SUPERMARLO(self):
    self.damage = 666               #increase damage
    self.specialReady = 20          #reduce cooldown on special ability
    self.specialTicks = 20
    self.bulletPenetration = 666    #increase bullet penetration
    self.special = 666              #increase special
    self.maxSpecial = 666
    self.health = 666               #increase health
    self.maxHealth = 666
    self.shootFrames = 0            #increase firerate to 3600RPM

  def getPen(self):
    return self.bulletPenetration

  def getShootFrames(self):
    return self.shootFrames

  def getShootCooldown(self):
    return self.shootCooldown

  def updateShootFrames(self):
    self.shootCooldown += 1
  
  def resetShootDelay(self):
    self.shootCooldown = 0

  def getTile(self,cameraOffset,resolution):
    self.tile = ((cameraOffset[0]+8)/32 + (resolution[0])/128), ((cameraOffset[1]+8)/32  + (resolution[1])/128) #formula for calculating currentTile
    return self.tile

  def updateScreenPosition(self,x,y):
    self.rect.x = x
    self.rect.y = y
  
  def getSpecial(self):
    return self.special
  
  def getMaxSpecial(self):
    return self.maxSpecial

  def newLevel(self):
    self.invincibilityFrames = -60

  def increaseSpecial(self,heal):
    self.special += 1
    self.healthincrease = heal
    if self.special > self.maxSpecial:
      self.special = self.maxSpecial

  def fullHealth(self):
    if self.maxHealth == self.health:
      return 1
    else:
      return 0

  def fullSpecial(self):
    if self.special >= self.maxSpecial:
      return True
    return False

  def moveright(self, pixels):
    self.rect.x += pixels

  def moveleft(self, pixels):
    self.rect.x -= pixels

  def moveup(self,pixels):
    self.rect.y -= pixels
  
  def movedown(self,pixels):
    self.rect.y += pixels
  
  def takeDamage(self,damage):
    if self.invincibilityFrames >= 30:
      self.health -= damage
      self.invincibilityFrames = 0
      return 1
    return 0
  
  def increment(self):
    self.specialTicks += 1

  def heal(self,heal):
    self.health += heal
    if self.health > self.maxHealth:
      self.health = self.maxHealth

  def increaseMaxHealth(self):
    self.maxHealth += 2
    self.health += 2
  
  def increaseFireRate(self):
    self.shootFrames -= 4
  
  def increaseDamage(self):
    if self.damage >= 12:
      self.bulletPenetration += 1
    else:
      self.damage += 2
  
  def increaseMaxSpecial(self):
    self.maxSpecial += 1
    self.special += 1

  def getName(self):
    return self.name

  def ability(self):
    if self.special > 0:                            #standard check
      if self.specialTicks >= self.specialReady:
        if self.health < self.maxHealth:
          self.special -= 1
          self.health += self.healthincrease          #standard health increase
          self.specialTicks = 0
          if self.health > self.maxHealth:
            self.health = self.maxHealth

class Bogos(Marlo):
  def __init__(self,image,scale,x,y,health,damage):
    super().__init__(image,scale,x,y,health,damage)
    self.name = "bogos"
    self.special = 3
  
  #def fullHealth(self):
    #if self.special >= self.maxSpecial:
      #return True
    #return False

  def ability(self,cameraOffset,resolution,floors):
    active = 0
    if self.special > 0:                                            #perform checks
      if self.specialTicks >= self.specialReady:
        active = 1                
        mx, my = pygame.mouse.get_pos()                             #get mouse position
        x = int(-resolution[0]/4 + mx/2)
        y = int(-resolution[1]/4 + my/2)                            #calculate vector based on displacement between player and mouse
        tile = self.getTile(cameraOffset,resolution)                
        mouseTile = (int(tile[1]+y/32),int(tile[0]+x/32))           #find what tile it's on
        if mouseTile in floors:                                     #check if valid tile
          cameraOffset = [cameraOffset[0] + x,cameraOffset[1] + y]  #if it is then make the player go to the new tile
          self.special -= 1                                         #remove 1 special and reset ticks
          self.specialTicks = 0
    return cameraOffset,active

  def heal(self,heal):                         #health won't heal bogos, it will instead recharge his teleporter
    self.special += 1
    if self.special > self.maxSpecial:
      self.special = self.maxSpecial


class life(pygame.sprite.Sprite):
  def __init__(self,image,scale,tilex,tiley):
    super().__init__()
    width = image.get_width()
    height = image.get_height()
    self.originalImage = image
    self.image = image
    self.image = pygame.transform.scale(image,(int(width*scale),int(height*scale)))
    self.rect = self.image.get_rect()
    self.rect.x = tilex*32
    self.rect.y = tiley*32
    self.startx = tilex
    self.starty = tiley
    self.heal = 4
  
  def updatePosition(self,cameraOffset):

    self.rect.x = (self.startx)*32 - cameraOffset[0]
    self.rect.y = (self.starty)*32 - cameraOffset[1]
  
  def getHeal(self):
    self.kill()
    return self.heal
  
class upgrade(pygame.sprite.Sprite):
  #initialising class
  def __init__(self,image,scale,tilex,tiley):                                         
    super().__init__()
    width = image.get_width()
    height = image.get_height()
    self.originalImage = image
    self.image = image
    self.image = pygame.transform.scale(image,(int(width*scale),int(height*scale)))
    self.rect = self.image.get_rect()
    self.rect.x = tilex*32
    self.rect.y = tiley*32
    self.startx = tilex
    self.starty = tiley
    self.type = random.randint(1,4)

  #call each frame to ensure that it's in the right place. 
  def updatePosition(self,cameraOffset):            
    self.rect.x = (self.startx)*32 - cameraOffset[0]
    self.rect.y = (self.starty)*32 - cameraOffset[1]

  #return which method is supposed to be ran.
  def getType(self):
    self.kill()
    return self.type

class angrydude(pygame.sprite.Sprite):
  def __init__(self,image,scale,difficulty,tilex,tiley,map,number,howMany):
    super().__init__()
    width = image.get_width()
    height = image.get_height()
    self.map = map
    self.originalImage = image
    self.image = image
    self.image = pygame.transform.scale(image,(int(width*scale),int(height*scale)))
    self.rect = self.image.get_rect()
    self.rect.x = tilex*32 +8
    self.rect.y = tiley*32 +8
    self.tilex = tilex
    self.tiley = tilex
    self.startx = tilex
    self.starty = tiley
    self.ticks = number
    self.path = []
    self.targetCoordinates = (None,None)
    self.pathfindTicks = howMany +1
    self.type = "angrydude"
    if difficulty == 2:
      self.health = 12
      self.damage = 4
      self.speed = 2.5
    else:
      self.health = 6
      self.damage = 2
      self.speed = 2

    #pathfinding setup
    #self.currentTileX = tilex
    #self.currentTileY = tiley
  
  def getType(self):
    return self.type
    
  def getTile(self,player,cameraOffset,resolution):
    playerTile = player.getTile(cameraOffset,resolution)
    tileDistance = ((self.rect.x)/32 - resolution[0]/128), ((self.rect.y)/32 - resolution[1]/128)
    self.realTile = [float(playerTile[0] + tileDistance[0]), float(playerTile[1]+ tileDistance[1])]
    self.tile = [int(playerTile[0] + tileDistance[0]), int(playerTile[1]+ tileDistance[1])]
    return self.tile
  
  def updateTicks(self):
    self.ticks += 1

#warning: performance suffers heavily when more than 1 instance of A* is ran in a single frame.
  def pathfind(self,playerTile,matrix,tile):
    searching = False
    if self.ticks >= self.pathfindTicks:                                        #if 1 second has elapsed
      self.ticks = 0                                                            #reset time to 0
      searching = True                                                          #start searching
    while searching:
      y,x = int(playerTile[0]),int(playerTile[1])                               #define target's coordinates
      if y >= 60 or x >= 60:
        break
      if tile[0] >= 60 or tile[1] >=60:
        break
      self.grid = Grid(matrix=matrix)                                           #create matrix for A*,using grid
      self.start = self.grid.node(int(tile[0]),int(tile[1]))                    #define the startpoint
      self.end = self.grid.node(y,x)                                            #use target coordinate as endpoint
      finder = AStarFinder(diagonal_movement=DiagonalMovement.never)           #select A* as the pathfinder, ensure no diagonal movement
      self.path, runs = finder.find_path(self.start,self.end,self.grid)         #find the path
      if self.path != []:
        self.path.pop(0)
      
      #debugging purposes
      #print(self.path)                                                          
      #print(self.grid.grid_str(path=self.path, start=self.start, end=self.end))

      searching = False                                                         #end the loop
  
  def updatePath(self):
    if self.tile == self.targetCoordinates:
      currentReal = (self.realTile[0]-self.tile[0],self.realTile[1]-self.tile[1])
      
    if self.targetCoordinates[0] == None or self.targetCoordinates[1] == None or self.tile ==self.targetCoordinates:  #if no valid next move:
      #print(self.targetCoordinates,self.tile)
      if len(self.path) > 0:                                                                                          #check if there's a next move to make
        self.targetCoordinates = list(self.path.pop(0))
      else:
        return 0                                                                                                      #if there isn't then default to the old one
    if self.path == []:
      self.targetCoordinates =self.tile
      return 0
    self.movex = -(self.speed*(self.targetCoordinates[0] - self.tile[0]))                                             #update the distance that needs to be travelled
    self.movey = -(self.speed*(self.targetCoordinates[1] - self.tile[1]))
    return 1


  def updatePosition(self,cameraOffset,direction):
    x,y=direction[0],direction[1]                                         # x,y representing the x and y distances that the bad dudes move by
    self.startx -= x/32                               
    self.starty -= y/32
    self.rect.x = (self.startx)*32 - cameraOffset[0]  
    self.rect.y = (self.starty)*32 - cameraOffset[1]
  
  def chasePlayer(self,player):
    distance = (player.rect.x - self.rect.x, player.rect.y - self.rect.y) #calculate the length of each component of the vector
    length = math.hypot(*distance)                                        #calculate the length of the vector
    if length == 0.0:
      direction = (0, -1)                                                 #avoid divide by 0 exception
    else:
      direction = (distance[0]/length,distance[1]/length)                 #calculate the direction

    newX = -(self.speed*direction[0])                                     
    newY = -(self.speed*direction[1])
    return (newX,newY)
    #would be used for rotation but it's not working well so i disabled it.
    #angle = math.degrees(math.atan2(direction[1],direction[0]))
    #self.image = pygame.transform.rotate(self.originalImage, -angle)
    #print(angle)
  def takeDamage(self,damage):
    self.health -= damage
    if self.health <= 0:
      self.kill()
      return True
    else:
      return False
    
class Ghost(angrydude):
  def __init__(self,image,scale,difficulty,tilex,tiley,map,number,howMany):
    super().__init__(image,scale,difficulty,tilex,tiley,map,number,howMany)
    self.type = "ghost"
    if difficulty == 2:
      self.health = 6
      self.damage = 2
      self.speed = 1.5
    else:
      self.health = 3
      self.damage = 1
      self.speed = 1.5

  
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y,damage,cameraOffset,penetration):
        super().__init__()
        blue = (125,249,255)
        white = (255,255,255)
        red = (255,0,0)
        if damage >= 666:
          color = red
        elif damage >= 12:
          color = blue
        else:
          color = white
        self.pos = (x/2 + 8, y/2 + 8)
        mx, my = pygame.mouse.get_pos()
        self.dir = (mx - x, my - y)
        length = math.hypot(*self.dir)
        if length == 0.0:
            self.dir = (0, -1)
        else:
            self.dir = (self.dir[0]/length, self.dir[1]/length)
        angle = math.degrees(math.atan2(-self.dir[1], self.dir[0]))

        self.bullet = pygame.Surface((10, 4)).convert_alpha()
        self.bullet.fill(color)
        self.bullet = pygame.transform.rotate(self.bullet, angle)
        self.speed = 15
        self.rect = self.bullet.get_rect(center = self.pos)
        self.rect.x = x
        self.rect.y = y
        self.bulletDamage = damage
        self.initialx = cameraOffset[0]
        self.initialy = cameraOffset[1]
        self.health = penetration
    
    def getHealth(self):
      return self.health

    def getDamage(self):
      return self.bulletDamage
    
    def takeDamage(self):
      self.health -= 1
      if self.health == 0:
        self.kill()

    def update(self,cameraOffset):  
        self.pos = (self.pos[0]+(self.dir[0]*self.speed)-cameraOffset[0] + self.initialx, self.pos[1]+(self.dir[1]*self.speed) - cameraOffset[1] + self.initialy)
        self.rect = self.bullet.get_rect(center = self.pos)
        self.initialx = cameraOffset[0]
        self.initialy = cameraOffset[1]

    def draw(self, surf,camera):
        bullet_rect = self.bullet.get_rect(center = self.pos)
        surf.blit(self.bullet, (bullet_rect))

class gun(Bullet):
  def __init__(self,x, y,image,scale,damage,cameraOffset):
        super().__init__(x,y,damage,cameraOffset,1)
        self.originalImage = image
        width = image.get_width()
        height = image.get_height()
        self.originalImage = pygame.transform.scale(image,(int(width*scale),int(height*scale)))

        self.pos = (x, y)
        mx, my = pygame.mouse.get_pos()
        self.dir = (mx - x, my - y)
        length = math.hypot(*self.dir)
        if length == 0.0:
            self.dir = (0, -1)
        else:
            self.dir = (self.dir[0]/length, self.dir[1]/length)
        angle = math.degrees(math.atan2(-self.dir[1], self.dir[0]))

        self.image = pygame.transform.rotate(self.originalImage, angle)
        self.rect = self.bullet.get_rect(center = self.pos)
        self.rect.x = x
        self.rect.y = y
        self.bulletDamage = 3
  
  def update(self,x,y,image,scale):
    #width,height = image.get_width,image.get_height
    #self.image = pygame.transform.scale(image,(int(width*scale),int(height*scale)))

    self.imageCopy = image
    w,h = self.imageCopy.get_size()
    box = [pygame.math.Vector2(p) for p in [(0, 0), (w, 0), (w, -h), (0, -h)]]
    self.pos = (x,y)
    self.rect.x = x - 10
    self.rect.y = y - 10
    mx, my = pygame.mouse.get_pos()
    self.dir = (mx - x*2, my - y*2)
    length = math.hypot(*self.dir)
    if length == 0.0:
      self.dir = (0, -1)
    else:
      self.dir = (self.dir[0]/length, self.dir[1]/length)
    angle = math.degrees(math.atan2(self.dir[1], -self.dir[0]))
    box = [pygame.math.Vector2(p) for p in [(0, 0), (w, 0), (w, -h), (0, -h)]]
    boxRotate = [p.rotate(angle) for p in box]

    minBox = (min(boxRotate, key=lambda p: p[0])[0], min(boxRotate, key=lambda p: p[1])[1])
    maxBox = (max(boxRotate, key=lambda p: p[0])[0], max(boxRotate, key=lambda p: p[1])[1])
    self.image = pygame.transform.rotate(self.imageCopy, angle)
