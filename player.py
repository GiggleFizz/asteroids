from circleshape import *
from constants import (PLAYER_TURN_SPEED, PLAYER_RADIUS, PLAYER_SPEED,PLAYER_SHOT_SPEED, PLAYER_SHOOT_COOLDOWN)
from shot import *

class Player(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.rotation = 0
        self.countdown = 0


    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), width = 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
    
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
    
    def shoot(self):
        if self.countdown > 0:
            pass
        else:
            self.countdown = PLAYER_SHOOT_COOLDOWN
            shot = Shot(self.position.x, self.position.y)
            forward = pygame.Vector2(0, 1).rotate(self.rotation)
            velocity = (forward * PLAYER_SHOT_SPEED)
            shot.velocity = velocity

    def update(self, dt):
        if self.countdown > 0:
            self.countdown = max(0, self.countdown - dt)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rotate(- dt)
        if keys[pygame.K_d]:
            self.rotate(+ dt)
        if keys[pygame.K_w]:
            self.move(+ dt)
        if keys[pygame.K_s]:
            self.move(- dt)
        if keys[pygame.K_SPACE]:
            self.shoot()
