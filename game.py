import pygame
pygame.init()

# Window
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("My First Game")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Player
x, y = 300, 200
speed = 5
clock = pygame.time.Clock()

running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed

    pygame.draw.rect(screen, BLUE, (x, y, 50, 50))
    pygame.display.update()
    clock.tick(60)

pygame.quit()
