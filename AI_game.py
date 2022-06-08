import pygame
import os

FPS = 60
WHITE = (255, 255, 255)
GREEN = (102, 205, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
BROWN = (139, 115, 85)
LightSkyBlue = (135, 206, 250)
WIDTH = 1000
HEIGHT = 600
# 遊戲初始化 and 創建視窗
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("傳教士過河遊戲")
clock = pygame.time.Clock()

# 載入圖片
boat_img = pygame.image.load(os.path.join("img", "boat.png")).convert()
coast_left_img = pygame.image.load(os.path.join("img", "coast_left.png")).convert()
coast_right_img = pygame.image.load(os.path.join("img", "coast_right.png")).convert()
missionary_img = pygame.image.load(os.path.join("img", "missionaries.png")).convert()
cannibal_img = pygame.image.load(os.path.join("img", "cannibals.png")).convert()

class Coast1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(coast_left_img, (500, 368))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 232

class Coast2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(coast_right_img, (500, 368))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = 500
        self.rect.y = 232

class Cannibal1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(cannibal_img, (80,80))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = 920
        self.rect.y = 435        

class Cannibal2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(cannibal_img, (80,80))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = 870
        self.rect.y = 435

class Cannibal3(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(cannibal_img, (80,80))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = 820
        self.rect.y = 435

class Missionary1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(missionary_img, (80,80))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = 770
        self.rect.y = 435

class Missionary2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(missionary_img, (80,80))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = 720
        self.rect.y = 435

class Missionary3(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(missionary_img, (80,80))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = 670
        self.rect.y = 435

class Boat1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(boat_img, (180,180))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = 600
        self.rect.y = 440

class Boat2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(boat_img, (180,180))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = 540
        self.rect.y = 350


all_sprites = pygame.sprite.Group() 
coast1 = Coast1()
coast2 = Coast2()
cannibal1 = Cannibal1()
cannibal2 = Cannibal2()
cannibal3 = Cannibal3()
missionary1 = Missionary1()
missionary2 = Missionary2()
missionary3 = Missionary3()
boat1 = Boat1()
boat2 = Boat2()
all_sprites.add(coast1)
all_sprites.add(coast2)
all_sprites.add(cannibal1)
all_sprites.add(cannibal2)
all_sprites.add(cannibal3)
all_sprites.add(missionary1)
all_sprites.add(missionary2)
all_sprites.add(missionary3)
all_sprites.add(boat1)
all_sprites.add(boat2)

# 遊戲迴圈
running = True
while running:
    clock.tick(FPS)
    # 取得輸入
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 更新遊戲
    # all_sprites.update()

    # 畫面顯示
    screen.fill(LightSkyBlue)
    # screen.blit(coast_left_img, (10, 460))
    # screen.blit(coast_right_img, (10, 460))
    # screen.blit(cannibal_img, (10, 460))
    all_sprites.draw(screen)
    pygame.display.update()
pygame.quit()             
