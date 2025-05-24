import pygame
import math
from circleshape import *
from constants import PLAYER_RADIUS, PLAYER_SPEED, PLAYER_TURN_SPEED, SHOT_RADIUS, PLAYER_SHOOT_COOLDOWN
from shot import Shot

class Player(CircleShape):
	def __init__(self, x, y):
		super().__init__(x, y, PLAYER_RADIUS)
		self.rotation = 0
		self.shooty_timer = 0
		self.forward = pygame.Vector2(0, 1).rotate(self.rotation)
		self.momentum = pygame.Vector2(0,0)
		self.throttle = 0.05
		self.log_base = 3

	def triangle(self):
		right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
		a = self.position + self.forward * self.radius
		b = self.position - self.forward * self.radius - right
		c = self.position - self.forward * self.radius + right
		return [a, b, c]

	def draw(self, screen):
		pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), 2)
	
	def rotate(self, dt):
		self.rotation += PLAYER_TURN_SPEED * dt
	
	def move(self, dt):
		self.position += self.forward * dt
		self.momentum += self.forward * (dt/abs(dt))
	
	def keep_momentum(self, dt):
		self.position += (self.forward * dt) + (self.momentum * self.throttle)
	
	def shoot(self):
		new_shot = Shot(self.position[0], self.position[1], SHOT_RADIUS, self.rotation)
	
	def update(self, dt):
		self.forward = pygame.Vector2(0, 1).rotate(self.rotation)
		keys = pygame.key.get_pressed()
		
		if keys[pygame.K_a]:
			self.rotate(-dt)
		
		if keys[pygame.K_d]:
			self.rotate(dt)
		
		if keys[pygame.K_w]:
			self.move(dt)
		
		if keys[pygame.K_s]:
			self.move(-dt)
		
		if keys[pygame.K_SPACE] and self.shooty_timer <= 0:
			self.shoot()
			self.shooty_timer = PLAYER_SHOOT_COOLDOWN
		
		self.keep_momentum(dt)
		
		self.shooty_timer -= dt