import pygame
import random
import os


os.chdir('/Users/kennylee/code/spaceship')


SCREEN_WIDTH=500
SCREEN_HEIGHT=600
FPS=60

BLACK=(0,0,0)
WHITE=(255,255,255)
GREEN=(0,255,0)
RED=(255,0,0)
YELLOW=(255,255,0)






class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.Surface((50, 40))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH / 2
        self.rect.bottom=SCREEN_HEIGHT-10
        #speed adjust
        self.speed = 8

    def update(self):
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_d]:
            self.rect.x += self.speed
        if key_pressed[pygame.K_a]:  # Use K_LEFT instead of K_RIGHT here
            self.rect.x -= self.speed
        if self.rect.right>SCREEN_WIDTH:
            self.rect.right=SCREEN_WIDTH
        if self.rect.left<0:
            self.rect.left=0
    
    def shoot(self):
        bullet=Bullet(self.rect.centerx,self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)
        
class Rock(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.Surface((30, 40))
        self.image.fill(RED)
        self.rect = self.image.get_rect()

        self.rect.x=random.randrange(0,SCREEN_WIDTH-self.rect.width)
        self.rect.y=random.randrange(-100,-40)
        self.speedx = random.randrange(-3,3)
        self.speedy = random.randrange(1,5)

    def update(self):
        self.rect.y+=self.speedy
        self.rect.x+=self.speedx
        if self.rect.top>SCREEN_HEIGHT or self.rect.left>SCREEN_WIDTH or self.rect.right<0:
            self.rect.x=random.randrange(0,SCREEN_WIDTH-self.rect.width)
            self.rect.y=random.randrange(-100,-40)
            self.speedx = random.randrange(-3,3)
            self.speedy = random.randrange(1,5)
            
class Bullet(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.Surface((10, 20))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()

        self.rect.centerx= x
        self.rect.bottom= y
        
        self.speedy = -10

    def update(self):
        self.rect.y+=self.speedy
        if self.rect.bottom<0:
            self.kill()
        
          
all_sprites=pygame.sprite.Group()
bullets=pygame.sprite.Group()
rocks=pygame.sprite.Group()
spaceship=Player()

all_sprites.add(spaceship)
for i in range(8):
    rock=Rock()
    all_sprites.add(rock)
    rocks.add(rock)






def main():
    

    pygame.init()

    #load photos
    # pygame.image.load()

    clock=pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    pygame.display.set_caption('Space')
    running=True
    
    
    
    #loop
    while running:
        
        clock.tick(FPS)

        #control
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
            elif event.type ==pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    spaceship.shoot()
                
            
                
        
        #update
        all_sprites.update()
        hits=pygame.sprite.groupcollide(rocks,bullets,True,True)#後面bolean用來判斷用不用消失
        for hit in hits:
            rock=Rock()
            all_sprites.add(rock)
            rocks.add(rock)
    
        
        hits=pygame.sprite.spritecollide(spaceship,rocks,False)
        if hits:
            running=False
         

        
        
        #visual
        screen.fill((BLACK))
        all_sprites.draw(screen)
        pygame.display.update() 
        
main()
