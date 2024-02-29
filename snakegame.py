import pygame
import random

# Colors
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Dimensions
WIDTH = 800
HEIGHT = 600
GRID_SIZE = 20

# Initialize Pygame
pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()

# Snake class
class Snake:
    def __init__(self):
        self.body = [(WIDTH // 2, HEIGHT // 2)]
        self.direction = "right"

    def move(self):
        head = self.body[0]
        x, y = head
        if self.direction == "right":
            x += GRID_SIZE
        elif self.direction == "left":
            x -= GRID_SIZE
        elif self.direction == "up":
            y -= GRID_SIZE
        elif self.direction == "down":
            y += GRID_SIZE
        self.body.insert(0, (x, y))
        self.body.pop()

    def draw(self):
        for segment in self.body:
            pygame.draw.rect(window, GREEN, (segment[0], segment[1], GRID_SIZE, GRID_SIZE))

# Food class
class Food:
    def __init__(self):
        self.x = random.randint(0, (WIDTH - GRID_SIZE) // GRID_SIZE) * GRID_SIZE
        self.y = random.randint(0, (HEIGHT - GRID_SIZE) // GRID_SIZE) * GRID_SIZE

    def draw(self):
        pygame.draw.rect(window, RED, (self.x, self.y, GRID_SIZE, GRID_SIZE))

# Create instances of Snake and Food
snake = Snake()
food = Food()

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake.direction != "down":
                snake.direction = "up"
            elif event.key == pygame.K_DOWN and snake.direction != "up":
                snake.direction = "down"
            elif event.key == pygame.K_LEFT and snake.direction != "right":
                snake.direction = "left"
            elif event.key == pygame.K_RIGHT and snake.direction != "left":
                snake.direction = "right"

    # Update snake position
    snake.move()

    # Check for collision with food
    if snake.body[0][0] == food.x and snake.body[0][1] == food.y:
        # Generate new position for the food
        food.x = random.randint(0, (WIDTH - GRID_SIZE) // GRID_SIZE) * GRID_SIZE
        food.y = random.randint(0, (HEIGHT - GRID_SIZE) // GRID_SIZE) * GRID_SIZE
        # Extend the length of the snake
        snake.body.append(snake.body[-1])

    # Check for collision with window edges
    if (
        snake.body[0][0] < 0
        or snake.body[0][0] >= WIDTH
        or snake.body[0][1] < 0
        or snake.body[0][1] >= HEIGHT
    ):
        running = False

    # Draw elements on the game window 
    window.fill(BLACK)
    snake.draw()
    food.draw()
    pygame.display.update()
    clock.tick(10)  

# Quit the game
pygame.quit()