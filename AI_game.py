import pygame

FPS = 60
WHITE = (255, 255, 255)
GREEN = (102, 205, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
BROWN = (139, 115, 85)
WIDTH = 1000
HEIGHT = 600
# 遊戲初始化 and 創建視窗
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("傳教士過河遊戲")
clock = pygame.time.Clock()

class Coast1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((200, 100))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 500

class Coast2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((200, 100))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = 800
        self.rect.y = 500

class Cannibal1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 40))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = 10
        self.rect.y = 460        

class Cannibal2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 40))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = 40
        self.rect.y = 460 

class Cannibal3(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 40))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = 70
        self.rect.y = 460

class Missionary1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 40))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 460

class Missionary2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 40))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = 130
        self.rect.y = 460

class Missionary3(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 40))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = 160
        self.rect.y = 460

class Boat1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(BROWN)
        self.rect = self.image.get_rect()
        self.rect.x = 220
        self.rect.y = 510

class Boat2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(BROWN)
        self.rect = self.image.get_rect()
        self.rect.x = 290
        self.rect.y = 510


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
    screen.fill(WHITE)
    all_sprites.draw(screen)
    pygame.display.update()
pygame.quit()            
