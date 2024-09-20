import pygame
import random
import os

os.chdir('/Users/kennylee/code/spaceship')

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 600
FPS = 60

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 40))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH / 2
        self.rect.bottom = SCREEN_HEIGHT - 10
        self.speed = 8

    def update(self):
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_d]:
            self.rect.x += self.speed
        if key_pressed[pygame.K_a]:
            self.rect.x -= self.speed
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
    
    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)

class Rock(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 40))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedx = random.randrange(-3, 3)
        self.speedy = random.randrange(1, 5)

    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.top > SCREEN_HEIGHT or self.rect.left > SCREEN_WIDTH or self.rect.right < 0:
            self.rect.x = random.randrange(0, SCREEN_WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedx = random.randrange(-3, 3)
            self.speedy = random.randrange(1, 5)

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 20))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speedy = -10

    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()

def draw_text(surface, text, size, color, x, y):
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    surface.blit(text_surface, text_rect)

def show_start_screen():
    screen.fill(BLACK)
    draw_text(screen, "Space Game", 64, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4)
    draw_text(screen, "Press Enter to Start", 36, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    pygame.display.flip()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    waiting = False

def show_game_over_screen(score):
    screen.fill(BLACK)
    draw_text(screen, "Game Over", 64, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4)
    draw_text(screen, f"Score: {score}", 36, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    draw_text(screen, "Press R to Retry or E to Exit", 36, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT * 3 // 4)
    pygame.display.flip()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    waiting = False
                if event.key == pygame.K_e:
                    pygame.quit()
                    exit()

def main():
    global screen
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Space')

    while True:
        # Show the start screen
        show_start_screen()
        
        # Game loop
        score = 0
        global all_sprites, bullets, rocks
        all_sprites = pygame.sprite.Group()
        bullets = pygame.sprite.Group()
        rocks = pygame.sprite.Group()
        spaceship = Player()
        
        all_sprites.add(spaceship)
        for i in range(8):
            rock = Rock()
            all_sprites.add(rock)
            rocks.add(rock)

        running = True
        
        while running:
            clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        spaceship.shoot()  # Only shoot on space key press

            all_sprites.update()
            
            # Check for collisions
            hits = pygame.sprite.groupcollide(rocks, bullets, True, True)
            for hit in hits:
                score += 1
                rock = Rock()
                all_sprites.add(rock)
                rocks.add(rock)
        
            hits = pygame.sprite.spritecollide(spaceship, rocks, False)
            if hits:
                running = False

            # Visual
            screen.fill(BLACK)
            all_sprites.draw(screen)
            draw_text(screen, f'Score: {score}', 36, WHITE, 50, 20)  # Render score
            
            pygame.display.update()
        
        # Show game over screen
        show_game_over_screen(score)

    pygame.quit()

main()
