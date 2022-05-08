

import pygame
import random
from vectorlib import Vector2D

pygame.init()

WIDTH, HEIGHT = 800, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Window")

YELLOW = (255, 255, 0)


class Ball:
    def __init__(self, x, y, radius, color):
        self.position = Vector2D(x, y)
        self.radius = radius
        self.color = color
        self.speed = Vector2D(0, 0)
        self.acceleration = Vector2D(0, 0)
        self.bounce_coeff = 0.9
        self.traction = 0.95

    def distance(self, ball):
        return self.position.distance(ball.position)

    def setSpeed(self, x, y):
        self.speed = Vector2D(x, y)

    def setAcceleration(self, x, y):
        self.acceleration = Vector2D(x, y)

    def update(self, balls):
        if self.atBottom():
            self.position = Vector2D(self.position.x, HEIGHT-self.radius)
            self.speed = self.speed * Vector2D(1, -self.bounce_coeff)
            self.speed = self.speed * Vector2D(self.traction, 1)

        if self.atTop():
            self.position = Vector2D(self.position.x, self.radius)
            self.speed = self.speed * Vector2D(1, -self.bounce_coeff)

        if self.atLeft():
            self.position = Vector2D(self.radius, self.position.y)
            self.speed = self.speed * Vector2D(-self.bounce_coeff, 1)

        if self.atRight():
            self.position = Vector2D(WIDTH-self.radius, self.position.y)
            self.speed = self.speed * Vector2D(-self.bounce_coeff, 1)

        self.hitHandler(balls)
        self.speed += self.acceleration
        self.position += self.speed

    def atBottom(self):
        if self.position.y+self.radius >= HEIGHT:
            return True
        return False

    def atTop(self):
        if self.position.y-self.radius <= 0:
            return True
        return False

    def atLeft(self):
        if self.position.x-self.radius <= 0:
            return True
        return False

    def atRight(self):
        if self.position.x+self.radius >= WIDTH:
            return True
        return False

    def draw(self, win):
        pygame.draw.circle(
            win, self.color, self.position.tuple(), self.radius)

    def hitHandler(self, balls):
        for ball in balls:
            if self.position == ball.position:
                continue
            if self.distance(ball) < self.radius+ball.radius:
                self.speed = self.speed*-1


def main():
    run = True
    clock = pygame.time.Clock()
    balls = []

    for _ in range(10):
        ball = Ball(random.randint(0, WIDTH), random.randint(0, HEIGHT), random.randint(
            10, 20), (25*random.randint(0, 10), 25 * random.randint(0, 10), 25*random.randint(0, 10)))
        ball.setSpeed(random.randint(1, 5), 1)
        ball.setAcceleration(0, 0.3)
        balls.append(ball)

    while run:
        clock.tick(60)
        WIN.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        for ball in balls:
            ball.update(balls)
            ball.draw(WIN)

        pygame.display.update()

    pygame.quit()


main()
