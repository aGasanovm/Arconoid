import pygame
import sys
import time

pygame.init()

back = (200, 255, 255)
green = (0, 200, 0)
mw = pygame.display.set_mode((800, 800))
mw.fill(back)
clock = pygame.time.Clock()

racket_x = 20
racket_y = 650

dx = 3
dy = 3



class Area():
    def __init__(self, x=0, y=0, width=10, height=10, color=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.fill_color = back
        if color:
            self.fill_color = color

    def color(self, new_color):
        self.fill_color = new_color

    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)

    def colliderect(self, rect):
        return self.rect.collidepoint(rect)

    def fill(self):
        pygame.draw.rect(mw, self.fill_color, self.rect)


class Picture(Area):
    def __init__(self, filename, x=0, y=0, width=10, height=10):
        Area.__init__(self, x=x, y=y, width=width, height=height, color=None)
        self.image = pygame.transform.scale(pygame.image.load(filename), (width, height))


    def draw(self):
        mw.blit(self.image, (self.rect.x, self.rect.y))

class Label(Area):
    def set_text(self, text, fsize, text_color):
        self.image = pygame.font.SysFont('verdana', fsize).render(text, True, text_color)

    def draw(self, shift_x, shift_y):
        self.fill()
        mw.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))




ball = Picture('ball.png', 90, 500, 90, 90)
platform = Picture('img.png', racket_x, racket_y, 300, 100)
start_x = 5
start_y = 5
count = 9
monsters = []
for j in range(3):
    y = start_y + (90 * j)

    x = start_x + (85 * j)
    for i in range (count):
        Mon = Picture('monster.png', x, y, 90, 90)
        monsters.append(Mon)
        x = x + 80
    count = count - 1
game_over = True

while True:
    if game_over:
        ball.fill()
        platform.fill()
        for event in pygame.event.get():
            #if event.type == pygame.KEYDOWN:
                #if event.type == pygame.K_RIGHT:
                    #platform.rect.x += 6
                #if event.type == pygame.K_LEFT:
                    #platform.rect.x -= 6


            if event.type == pygame.QUIT:
                sys.exit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            platform.rect.x += 5
        if keys[pygame.K_LEFT]:
            platform.rect.x -= 5

        ball.rect.x += dx
        ball.rect.y += dy
        if ball.rect.y < 0:
            dy *= -1
        if ball.rect.colliderect(platform.rect):
            dy *= -1
        if ball.rect.x > 800 or ball.rect.x < 0:
            dx *= -1

        if ball.rect.y > 780:
            game_over = False
            if game_over == False:
                time_text = Label(150, 320, 50, 50, back)
                time_text.set_text('Ты ЛОХ!', 60, (255, 0, 0))
                time_text.draw(10, 10)
        ball.draw()
        platform.draw()
        for m in monsters:
            m.draw()
            if m.rect.colliderect(ball.rect):
                monsters.remove(m)
                m.fill()
                dy *= -1
        if len(monsters) == 0:
            game_over = False
            if game_over == False:
                time_text = Label(150, 320, 50, 50, back)
                time_text.set_text('Молодец!', 60, (0, 200, 0))
                time_text.draw(10, 10)

    else:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
    pygame.display.update()
    clock.tick(120)