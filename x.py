import pygame
import random
import sys


pygame.init()


SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 900


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Crossy Road")
clock = pygame.time.Clock()


player_texture = pygame.Surface((40, 40))
player_texture.fill(GREEN)

car_texture = pygame.Surface((40, 20))  # Smaller cars
car_texture.fill(RED)

road_texture = pygame.Surface((SCREEN_WIDTH, 60))
road_texture.fill(BLACK)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_texture
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT - 50)
        self.moving_up = False

    def update(self, keys):
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= 3
            self.moving_up = True
        else:
            self.moving_up = False

        if not self.moving_up:
            if keys[pygame.K_LEFT] and self.rect.left > 0:
                self.rect.x -= 3
            if keys[pygame.K_RIGHT] and self.rect.right < SCREEN_WIDTH:
                self.rect.x += 3


class Car(pygame.sprite.Sprite):
    def __init__(self, x, y, speed, direction):
        super().__init__()
        self.image = car_texture
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
        self.direction = direction  # Left or right

    def update(self):
        self.rect.x += self.speed
        if self.rect.right < 0 and self.direction == "left":
            self.rect.x = SCREEN_WIDTH
        elif self.rect.left > SCREEN_WIDTH and self.direction == "right":
            self.rect.x = -self.rect.width


class Level:
    def __init__(self):
        self.obstacles = pygame.sprite.Group()
        self.generate_cars()

    def generate_cars(self):
        for i in range(1, 9):
            road_y = i * (SCREEN_HEIGHT // 6)
            for _ in range(random.randint(2, 4)):
                car_x = random.randint(0, SCREEN_WIDTH - 40)
                speed = random.choice([-15, -13, 13, 15])
                direction = "left" if speed < 0 else "right"
                car = Car(car_x, road_y, speed, direction)
                self.obstacles.add(car)

    def draw(self):
        for i in range(1, 6):
            road_y = i * (SCREEN_HEIGHT // 6)
            screen.blit(road_texture, (0, road_y - 30))

    def update(self):
        self.obstacles.update()


def main():
    player = Player()
    player_group = pygame.sprite.Group(player)

    level = Level()

    running = True
    while running:
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        player.update(keys)

        level.draw()
        player_group.draw(screen)
        level.obstacles.draw(screen)

        level.update()

        # Check collisions
        if pygame.sprite.spritecollideany(player, level.obstacles):
            print("You lost!")
            running = False

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()






