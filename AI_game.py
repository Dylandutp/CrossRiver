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
pygame.mixer.init
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("傳教士過河遊戲")
clock = pygame.time.Clock()

# 載入圖片
boat_img = pygame.image.load(os.path.join("img", "boat.png")).convert()
coast_left_img = pygame.image.load(os.path.join("img", "coast_left.png")).convert()
coast_right_img = pygame.image.load(os.path.join("img", "coast_right.png")).convert()
missionary_img = pygame.image.load(os.path.join("img", "missionaries.png")).convert()
cannibal_img = pygame.image.load(os.path.join("img", "cannibals.png")).convert()

#載入音樂
pygame.mixer.music.load(os.path.join("sound", "BGM.mp3"))
pygame.mixer.music.set_volume(0.4)

font_name = os.path.join("font.ttf")
def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.centerx = x
    text_rect.top = y
    surf.blit(text_surface, text_rect)

def draw_init():
    draw_text(screen, '傳教士過河!', 64, WIDTH/2, HEIGHT/4)
    draw_text(screen, '按任意鍵開始!!', 18, WIDTH/2, HEIGHT/2)
    pygame.display.update()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYUP:
                waiting = False 


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

    def update(self):
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_y]:
            self.rect.x += 2
        if key_pressed[pygame.K_t]:
            self.rect.x -= 2   
        if key_pressed[pygame.K_u]:
            self.rect.y -= 2
        if key_pressed[pygame.K_i]:
            self.rect.y += 2

class Cannibal2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(cannibal_img, (80,80))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = 870
        self.rect.y = 435

    def update(self):
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_h]:
            self.rect.x += 2
        if key_pressed[pygame.K_g]:
            self.rect.x -= 2   
        if key_pressed[pygame.K_j]:
            self.rect.y -= 2
        if key_pressed[pygame.K_k]:
            self.rect.y += 2

class Cannibal3(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(cannibal_img, (80,80))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = 820
        self.rect.y = 435

    def update(self):
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_n]:
            self.rect.x += 2
        if key_pressed[pygame.K_b]:
            self.rect.x -= 2   
        if key_pressed[pygame.K_m]:
            self.rect.y -= 2
        if key_pressed[pygame.K_l]:
            self.rect.y += 2

class Missionary1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(missionary_img, (80,80))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = 770
        self.rect.y = 435

    def update(self):
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_w]:
            self.rect.x += 2
        if key_pressed[pygame.K_q]:
            self.rect.x -= 2   
        if key_pressed[pygame.K_e]:
            self.rect.y -= 2
        if key_pressed[pygame.K_r]:
            self.rect.y += 2         

class Missionary2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(missionary_img, (80,80))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = 720
        self.rect.y = 435

    def update(self):
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_s]:
            self.rect.x += 2
        if key_pressed[pygame.K_a]:
            self.rect.x -= 2   
        if key_pressed[pygame.K_d]:
            self.rect.y -= 2
        if key_pressed[pygame.K_f]:
            self.rect.y += 2

class Missionary3(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(missionary_img, (80,80))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = 670
        self.rect.y = 435

    def update(self):
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_x]:
            self.rect.x += 2
        if key_pressed[pygame.K_z]:
            self.rect.x -= 2   
        if key_pressed[pygame.K_c]:
            self.rect.y -= 2
        if key_pressed[pygame.K_v]:
            self.rect.y += 2

class Boat1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(boat_img, (180,180))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = 600
        self.rect.y = 440

    def update(self):
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_RIGHT]:
            self.rect.x += 2
        if key_pressed[pygame.K_LEFT]:
            self.rect.x -= 2

class Boat2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(boat_img, (180,180))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = 540
        self.rect.y = 350

    def update(self):
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_p]:
            self.rect.x += 2
        if key_pressed[pygame.K_o]:
            self.rect.x -= 2


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
pygame.mixer.music.play(-1)

# 遊戲迴圈
show_init = True
running = True
while running:
    if show_init:
        draw_init()
        show_init = False

    clock.tick(FPS)
    # 取得輸入
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 更新遊戲
    all_sprites.update()

    # 畫面顯示
    screen.fill(LightSkyBlue)
    # screen.blit(coast_left_img, (10, 460))
    # screen.blit(coast_right_img, (10, 460))
    # screen.blit(cannibal_img, (10, 460))
    all_sprites.draw(screen)
    pygame.display.update()
pygame.quit()             
