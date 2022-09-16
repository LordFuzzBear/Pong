import pygame

pygame.init()

win = pygame.display.set_mode((1000, 700))

pygame.display.set_caption("Pong")

title_img = pygame.image.load('img/' + 'title' + '.png')

light_yellow = (235, 245, 200)
purple = (170, 0, 255)
blue = (0, 180, 255)
pink = (255, 150, 255)


class Paddle1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([20, 100])
        self.image.fill(pink)
        self.rect = self.image.get_rect()
        self.points = 0


class Paddle2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([20, 100])
        self.image.fill(blue)
        self.rect = self.image.get_rect()
        self.points = 0


class Ball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([30, 30])
        self.image.fill(light_yellow)
        self.rect = self.image.get_rect()
        self.speed = 30
        self.dx = 1
        self.dy = 1


paddle1 = Paddle1()
paddle1.rect.x = 25
paddle1.rect.y = 375

paddle2 = Paddle2()
paddle2.rect.x = 957
paddle2.rect.y = 375

paddle_speed = 50

pong = Ball()
pong.rect.x = 500
pong.rect.y = 375

all_sprites = pygame.sprite.Group()
all_sprites.add(paddle1, paddle2, pong)


def redraw():
    win.fill(purple)

    font = pygame.font.SysFont('Calibri', 50)

    win.blit(title_img, (375, 50))

    p1_score = font.render(str(paddle1.points), False, pink)
    p1rect = p1_score.get_rect()
    p1rect.center = (50, 70)
    win.blit(p1_score, p1rect)

    p2_score = font.render(str(paddle2.points), False, blue)
    p2rect = p2_score.get_rect()
    p2rect.center = (950, 70)
    win.blit(p2_score, p2rect)

    all_sprites.draw(win)
    pygame.display.update()


run = True

while run:

    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    key = pygame.key.get_pressed()
    if key[pygame.K_w]:
        paddle1.rect.y -= paddle_speed
    if key[pygame.K_s]:
        paddle1.rect.y += paddle_speed
    if key[pygame.K_UP]:
        paddle2.rect.y -= paddle_speed
    if key[pygame.K_DOWN]:
        paddle2.rect.y += paddle_speed

    pong.rect.x += pong.speed * pong.dx
    pong.rect.y += pong.speed * pong.dy

    if pong.rect.y > 670:
        pong.dy = -1
    if pong.rect.y < 0:
        pong.dy = 1
    if pong.rect.x > 960:
        pong.rect.x, pong.rect.y = 500, 375
        pong.dx = -1
        paddle1.points += 1
    if pong.rect.x < 10:
        pong.rect.x, pong.rect.y = 500, 375
        pong.dx = 1
        paddle2.points += 1

    if paddle1.rect.colliderect(pong.rect):
        pong.dx = 1
    if paddle2.rect.colliderect(pong.rect):
        pong.dx = -1

    redraw()

pygame.quit()
