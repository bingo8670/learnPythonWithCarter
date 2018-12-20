import pygame, sys
# 初始化 Pygame 和 mixer
pygame.init()
pygame.mixer.init()

# 创建一个 Pygame 窗口 等 1 秒钟让 mixer 完成初始化
screen = pygame.display.set_mode([640,480])
pygame.time.delay(1000)


# 播放声音 创建声音对象
pygame.mixer.music.load("bg_music.mp3")
pygame.mixer.music.set_volume(0.30)
pygame.mixer.music.play()

splat = pygame.mixer.Sound("splat.wav")
splat.set_volume(0.50)
splat.play()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
