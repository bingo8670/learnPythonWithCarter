import pygame, sys
pygame.init()
screen = pygame.display.set_mode([640,480])
screen.fill([255, 255, 255])
pygame.draw.circle(screen, [25,20,10],[320,240], 30, 0)
# rectangle 矩形
pygame.draw.rect(screen, [255,0,0], [250, 150, 300, 200], 0)
pygame.display.flip()
running = True
while running:
  for event in pygame.event.get():
      if event.type == pygame.QUIT:
          running = False
pygame.quit()
