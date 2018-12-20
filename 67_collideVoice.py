import pygame, sys
from pygame.locals import *
pygame.mixer.init()
hit = pygame.mixer.Sound("hit_paddle.wav")
hit.set_volume(0.4)
hit_wall = pygame.mixer.Sound("hit_wall.wav")
hit_wall.set_volume(0.4)
get_point = pygame.mixer.Sound("get_point.wav")
get_point.set_volume(0.2)
splat = pygame.mixer.Sound("splat.wav")
splat.set_volume(0.6)
new_life = pygame.mixer.Sound("new_life.wav")
new_life.set_volume(0.5)
bye = pygame.mixer.Sound("game_over.wav")
bye.set_volume(0.6)

class MyBallClass(pygame.sprite.Sprite):
    def __init__(self, image_file, speed, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        self.speed = speed

    def move(self):
        global score, score_font, score_surf
        self.rect = self.rect.move(self.speed)
        # 碰到两边的墙
        if self.rect.left < 0 or self.rect.right > screen.get_width():
            self.speed[0] = -self.speed[0]
            hit_wall.play()

        # 碰到顶端的墙
        if self.rect.top <= 0 :
            self.speed[1] = -self.speed[1]
            score = score + 2
            score_surf = score_font.render(str(score), 1, (0, 0, 0))
            get_point.play()

class MyPaddleClass(pygame.sprite.Sprite):
    def __init__(self, location = [0, 0]):
        # 为球拍创建一个表面
        pygame.sprite.Sprite.__init__(self)
        image_surface = pygame.surface.Surface([100, 20])
        image_surface.fill([0,0,0])
        self.image = image_surface.convert()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

pygame.init()
screen = pygame.display.set_mode([640, 480])
clock = pygame.time.Clock()
myBall = MyBallClass('wackyball.bmp', [10, 5], [50, 50])
ballGroup = pygame.sprite.Group(myBall)
paddle = MyPaddleClass([270, 400])

# 创建积分字体
lives = 3
score = 1
score_font = pygame.font.Font(None, 50)
score_surf = score_font.render(str(score), 1, (0, 0, 0))
score_pos  = [10, 10]
done = False

running = True
while running:
    clock.tick(30)
    screen.fill([255, 255, 255])
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == pygame.MOUSEMOTION:
            paddle.rect.centerx = event.pos[0]

    if pygame.sprite.spritecollide(paddle, ballGroup, False):
        myBall.speed[1] = -myBall.speed[1]
        hit.play()
    myBall.move()
    if not done:
        screen.blit(myBall.image, myBall.rect)
        screen.blit(paddle.image, paddle.rect)
        screen.blit(score_surf, score_pos)
        for i in range(lives):
            width = screen.get_rect().width
            screen.blit(myBall.image, [width - 40 * i, 20])
        pygame.display.flip()

    # 碰到底部
    if myBall.rect.top >= screen.get_rect().bottom:
        if not done:
            splat.play(1)
        lives = lives - 1
        if lives == 0:
            if not done:
                bye.play(1)
            final_text1 = "Game Over"
            final_text2 = "Your final score is:  " + str(score)
            ft1_font    = pygame.font.Font(None, 70)
            ft1_surf    = ft1_font.render(final_text1, 1, (0, 0, 0))
            ft2_font    = pygame.font.Font(None, 50)
            ft2_surf    = ft2_font.render(final_text2, 1, (0, 0, 0))
            screen.blit(ft1_surf, [screen.get_width()/2 - \
                    ft1_surf.get_width()/2, 100])
            screen.blit(ft2_surf, [screen.get_width()/2 - \
                    ft2_surf.get_width()/2, 100])
            pygame.display.flip()
            done = True
        else:   # wait 2 seconds, then start the next ball
            pygame.time.delay(1000)
            new_life.play()
            myBall.rect.topleft = [50, 50]
            screen.blit(myBall.image, myBall.rect)
            pygame.display.flip()
            pygame.time.delay(1000)
pygame.quit()

