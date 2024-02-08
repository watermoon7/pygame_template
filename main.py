import pygame
pygame.init()

width = 800
height = 600
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
fps = 30

pygame.mixer.music.load("test.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play()

pos = [100, 100]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if pygame.Rect(pos[0], pos[1], 50, 50).collidepoint(mouse_pos):
                print('clicked the box')

    dt = clock.tick(fps)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        pos[1] -= 5
    elif keys[pygame.K_s]:
        pos[1] += 5
    if keys[pygame.K_a]:
        pos[0] -= 5
    elif keys[pygame.K_d]:
        pos[0] += 5

    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (0, 255, 0), (pos[0], pos[1], 50, 50))
    pygame.display.update()


pygame.quit()
