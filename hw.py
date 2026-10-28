
import pygame

def main():
    pygame.init()
    screen_width, screen_height = 500, 400
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Mini Sprite Adventure")

    x, y = 50, 50
    speed = 4
    size = 60

    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    BLUE = (0, 125, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    YELLOW = (255, 255, 0)

    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]: x -= speed
        if keys[pygame.K_RIGHT]: x += speed
        if keys[pygame.K_UP]: y -= speed
        if keys[pygame.K_DOWN]: y += speed

        x = max(0, min(x, screen_width - size))
        y = max(0, min(y, screen_height - size))

        color = WHITE
        if x == 0: color = BLUE
        elif x == screen_width - size: color = YELLOW
        elif y == 0: color = RED
        elif y == screen_height - size: color = GREEN

        screen.fill(BLACK)
        pygame.draw.circle(screen, GREEN, (420, 320), 35)
        pygame.draw.circle(screen, BLUE, (80, 320), 35, 4)
        pygame.draw.rect(screen, color, (x, y, size, size))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
