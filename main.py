import pygame

# ---- reset ----#
pygame.init()

# ---- color ----#
BLACK = (0, 0, 0)
GRAY = (127, 127, 127)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
xpos = 100
ypos = 100

# ---- screen ----#
screen_size = 640, 640
screen = pygame.display.set_mode(screen_size)
screen.fill(WHITE)

# ---- FPS ----#
FPS = 60
CLOCK = pygame.time.Clock()

# ---- main loop ----#
main = True
while main:
    screen.fill(WHITE)
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                print("위쪽")
                ypos -= 10
            if event.key == pygame.K_DOWN:
                print("아래쪽")
                ypos += 10
            if event.key == pygame.K_RIGHT:
                print("오른쪽")
                xpos += 10
            if event.key == pygame.K_LEFT:
                print("왼쪽")
                xpos -= 10
            if event.key == pygame.K_ESCAPE:
                main = False
        if event.type == pygame.QUIT:
            main = False

    pygame.draw.rect(screen, BLACK, (xpos, ypos, 10, 10))
    pygame.display.update()
    CLOCK.tick(60)

pygame.quit()
