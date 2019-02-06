from os import system
import pygame
import pygame.gfxdraw
import sys
import random
import time

block_size = 10
height_of_arena = 50 * block_size
width_of_arena = 50 * block_size
size_of_arena = (width_of_arena, height_of_arena)
food_radious = int(block_size / 2 - 1)

food_position = []
score = 0

pygame.init()
largeText = pygame.font.Font('freesansbold.ttf',45)
smallText = pygame.font.Font('freesansbold.ttf',15)
screen = pygame.display.init()
pygame.display.set_caption("Snake")



class Snake():
	def __init__(self):
		self.position = [250, 250]
		self.body = [[250, 250], [240, 250], [230, 250]]
		self.direction = "RIGHT"

	def change_direction_to(self, dir):
		if dir == "RIGHT" and self.direction != "LEFT":
			self.direction = "RIGHT"
		elif dir == "LEFT" and self.direction != "RIGHT":
			self.direction = "LEFT"
		elif dir == "UP" and self.direction != "DOWN":
			self.direction = "UP"
		elif dir == "DOWN" and self.direction != "UP":
			self.direction = "DOWN"

	def move(self, ):
		global score
		if self.direction == "RIGHT":
			self.position[0] += block_size
		elif self.direction == "LEFT":
			self.position[0] -= block_size
		elif self.direction == "UP":
			self.position[1] -= block_size
		elif self.direction == "DOWN":
			self.position[1] += block_size
		self.body.insert(0, list(self.position))
		if self.position == food_position:
			generate_food()
			score += 1
			return
		else:
			self.body = self.body[:-1]						
			
	def defeat(self, ):
		if self.position[0] > (height_of_arena - block_size) or self.position[0] < block_size:
			return True
		elif self.position[1] > (width_of_arena - block_size) or self.position[1] < block_size:
			return True
		for body_part in self.body[1:]:
			if self.position == body_part:
				return True
	def get_position(self, ):
		return self.position

	def get_body(self, ):
		return self.body
		

def main_screan():
	global screen
	screen = pygame.display.set_mode(size_of_arena)
	fps = pygame.time.Clock()
	score = 0
	snake = Snake()
	generate_food()
	while True:
		for event in pygame.event.get():
			if event.type ==pygame.QUIT:
				sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RIGHT:
				    snake.change_direction_to("RIGHT")
				elif event.key == pygame.K_UP:
				    snake.change_direction_to("UP")
				elif event.key == pygame.K_DOWN:
				    snake.change_direction_to("DOWN")
				elif event.key == pygame.K_LEFT:
				    snake.change_direction_to("LEFT")																
		snake.move()
		display_arena(snake)
		fps.tick(20)
		if snake.defeat():
			game_over(snake)
			


def generate_food():
	global food_position
	food_position = [random.randint(0, 49) * block_size, random.randint(0, 49) * block_size]

def display_arena(snake):
	screen.fill((0, 0, 0))
	for body_part in snake.get_body():
		pygame.draw.rect(screen, (89, 152, 47), (body_part[0], body_part[1], block_size, block_size))
	pygame.draw.rect(screen, (0,128,0), (snake.position[0], snake.position[1], block_size, block_size))
	pygame.gfxdraw.aacircle(screen, int(food_position[0]+block_size/2), int(food_position[1]+block_size/2),food_radious,(225, 0, 0))
	pygame.gfxdraw.filled_circle(screen, int(food_position[0]+block_size/2), int(food_position[1]+block_size/2),food_radious,(225, 0, 0))
	pygame.display.update()
	

def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

def game_over(snake):
	for i in range(7):
		if i % 2 != 0:
			screen.fill((0, 0, 0))
			pygame.display.update()
		else:
			display_arena(snake)
		time.sleep(0.35)

	screen.fill((0, 0, 0))
	TextSurf, TextRect = text_objects("SNAKE", largeText, (255,255,255))
	TextRect.center = ((width_of_arena/2),int(30))
	screen.blit(TextSurf, TextRect)

	TextSurf, TextRect = text_objects(" Score : " + str(score), largeText, (255,255,255))
	TextRect.center = ((width_of_arena/2),(height_of_arena/2))
	screen.blit(TextSurf, TextRect)

	TextSurf, TextRect = text_objects("Wait for 2 seconds", smallText, (255,255,255))
	TextRect.center = ((width_of_arena/2),(height_of_arena-10))
	screen.blit(TextSurf, TextRect)

	pygame.display.update()

	time.sleep(2)

	pygame.quit()
	sys.exit()


if __name__ == "__main__":
	main_screan()