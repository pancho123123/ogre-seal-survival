import pygame, random
from random import randint

WIDTH = 1200
HEIGHT = 700
BLACK = (0, 0, 0)
WHITE = ( 255, 255, 255)
GREEN = (0, 255, 0)
RED = (255,0,0)
BLUE = (0,0,255)
BROWN = (50,20,30)

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ogre Seal Survival")
clock = pygame.time.Clock()

def draw_text1(surface, text, size, x, y):
	font = pygame.font.SysFont("serif", size)
	text_surface = font.render(text, True, WHITE)
	text_rect = text_surface.get_rect()
	text_rect.midtop = (x, y)
	surface.blit(text_surface, text_rect)

def draw_text2(surface, text, size, x, y):
	font = pygame.font.SysFont("serif", size)
	text_surface = font.render(text, True, BLACK)
	text_rect = text_surface.get_rect()
	text_rect.midtop = (x, y)
	surface.blit(text_surface, text_rect)

def draw_hp_bar(surface, x, y, percentage):
	BAR_LENGHT = 50
	BAR_HEIGHT = 10
	fill = (percentage / 100) * BAR_LENGHT
	border = pygame.Rect(x, y, BAR_LENGHT, BAR_HEIGHT)
	fill = pygame.Rect(x, y, fill, BAR_HEIGHT)
	pygame.draw.rect(surface, GREEN, fill)
	pygame.draw.rect(surface, WHITE, border, 2)

def draw_hp_bar2(surface, x, y, percentage):
	BAR_LENGHT = 50
	BAR_HEIGHT = 10
	fill = (percentage / 100) * BAR_LENGHT
	border = pygame.Rect(x, y, BAR_LENGHT, BAR_HEIGHT)
	fill = pygame.Rect(x, y, fill, BAR_HEIGHT)
	pygame.draw.rect(surface, BROWN, fill)
	pygame.draw.rect(surface, BROWN, border, 2)

def draw_mana_bar(surface, x, y, percentage):
	BAR_LENGHT = 50
	BAR_HEIGHT = 10
	fill = (percentage / 100) * BAR_LENGHT
	border = pygame.Rect(x, y, BAR_LENGHT, BAR_HEIGHT)
	fill = pygame.Rect(x, y, fill, BAR_HEIGHT)
	pygame.draw.rect(surface, BLUE, fill)
	pygame.draw.rect(surface, WHITE, border, 2)

class Player(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.transform.scale(pygame.image.load("img/venge.png").convert(),(50,65))
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
		self.speed_x = 0
		self.hp = 100
		self.mana = 100

class Player1(Player):
	def __init__(self):
		super().__init__()
		self.rect.x = 500
		self.rect.y = 133
		
	def update(self):
		self.hp += 0.02
		self.mana += 1/50
		if self.mana < 0:
			self.mana = 0
		if self.mana > 100:
			self.mana = 100
		if self.hp < 0:
			self.hp = 0
		if self.hp == 0:
			self.kill()
		if self.hp > 100:
			self.hp = 100
		self.speed_x = 0
		self.speed_y = 0
		keystate = pygame.key.get_pressed()
		if keystate[pygame.K_a]:
			self.speed_x = -3
		if keystate[pygame.K_d]:
			self.speed_x = 3
		self.rect.x += self.speed_x
		if keystate[pygame.K_w]:
			self.speed_y = -3
		if keystate[pygame.K_s]:
			self.speed_y = 3
		self.rect.y += self.speed_y
		if self.rect.right > WIDTH:
			self.rect.right = WIDTH
		if self.rect.left < 300:
			self.rect.left = 300
		if self.rect.top < 50:
			self.rect.top = 50
		if self.rect.bottom > 550:
			self.rect.bottom = 550

class Player2(Player):
	def __init__(self):
		super().__init__()
		self.rect.x = 900
		self.rect.y = 133
		
	def update(self):
		self.hp += 0.02
		self.mana += 1/50
		if self.mana < 0:
			self.mana = 0
		if self.mana > 100:
			self.mana = 100
		if self.hp < 0:
			self.hp = 0
		if self.hp == 0:
			self.kill()
		if self.hp > 100:
			self.hp = 100
		self.speed_x = 0
		self.speed_y = 0
		keystate = pygame.key.get_pressed()
		if keystate[pygame.K_LEFT]:
			self.speed_x = -3
		if keystate[pygame.K_RIGHT]:
			self.speed_x = 3
		self.rect.x += self.speed_x
		if keystate[pygame.K_UP]:
			self.speed_y = -3
		if keystate[pygame.K_DOWN]:
			self.speed_y = 3
		self.rect.y += self.speed_y
		
		if self.rect.right > WIDTH:
			self.rect.right = WIDTH
		if self.rect.left < 300:
			self.rect.left = 300
		if self.rect.top < 50:
			self.rect.top = 50
		if self.rect.bottom > 550:
			self.rect.bottom = 550

class Player3(Player):
	def __init__(self):
		super().__init__()
		self.rect.x = 500
		self.rect.y =  366
		
	def update(self):
		self.hp += 0.02
		self.mana += 1/50
		if self.mana < 0:
			self.mana = 0
		if self.mana > 100:
			self.mana = 100
		if self.hp < 0:
			self.hp = 0
		if self.hp == 0:
			self.kill()
		if self.hp > 100:
			self.hp = 100
		self.speed_x = 0
		self.speed_y = 0
		keystate = pygame.key.get_pressed()
		if keystate[pygame.K_f]:
			self.speed_x = -3
		if keystate[pygame.K_h]:
			self.speed_x = 3
		self.rect.x += self.speed_x
		if keystate[pygame.K_t]:
			self.speed_y = -3
		if keystate[pygame.K_g]:
			self.speed_y = 3
		self.rect.y += self.speed_y
		
		if self.rect.right > WIDTH:
			self.rect.right = WIDTH
		if self.rect.left < 300:
			self.rect.left = 300
		if self.rect.top < 50:
			self.rect.top = 50
		if self.rect.bottom > 550:
			self.rect.bottom = 550


def distance(a,b):
	#pitagoras distance between a and b
	dx = b.rect.centerx - a.rect.centerx
	dy = b.rect.centery - a.rect.centery
	return (dx**2 + dy**2)**(1/2)

def direction(a,b):
	#x,y unitary vector from a to b
	dx = b.rect.centerx - a.rect.centerx
	dy = b.rect.centery - a.rect.centery
	radio = (dx**2 + dy**2)**(1/2)
	return dx/radio, dy/radio

def direction2(a,b):
	#x,y unitary vector from a to b
	dx = b[0] - a.rect.centerx
	dy = b[1] - a.rect.centery
	radio = (dx**2 + dy**2)**(1/2)
	return dx/radio, dy/radio

class OgreSeal(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = ogre_images[0]
		self.image.set_colorkey(WHITE)
		self.rect = self.image.get_rect()
		self.rect.x = 750
		self.rect.y = 233
		self.hp = 100
		self.target_list = [player1, player2, player3]
		self.target = random.choice(self.target_list)
		self.counter1 = True
		self.counter2 = False
		self.counter3 = False
		self.counter4 = False
		self.counter5 = False
		self.counter6 = False
		self.counter7 = False
		self.speed = 1
		self.time1 = 0
		self.time2 = 0
		self.time3 = 0
		self.n = 1000
		self.start_time1 = pygame.time.get_ticks()
		self.a = 0
		self.b = 0

	def update(self):
		current_time = pygame.time.get_ticks()
		elapsed_time = current_time - self.start_time1
		self.target_list = [t for t in self.target_list if t.hp >0]
		self.image.set_colorkey(WHITE)
		
		if self.rect.right > WIDTH:
			self.rect.right = WIDTH
		if self.rect.left < 250:
			self.rect.left = 250
		if self.rect.top < 30:
			self.rect.top = 30
		if self.rect.bottom > 500:
			self.rect.bottom = 500

		if self.counter1:
			if (self.target.rect.centerx - self.rect.centerx) == 0:
				if self.target.rect.centery > self.rect.centery:
					self.image = ogre_images[4]
					self.rect.centery += self.speed 
				elif self.rect.centery > self.target.rect.centery:
					self.image = ogre_images[9]
					self.rect.centery -= self.speed
				else:
					self.rect.centery += 0
			elif (self.target.rect.centerx - self.rect.centerx) != 0:
				x,y = direction(self, self.target)
				if x > 0 and y > 0:
					self.image = ogre_images[3]
				if x < 0 and y < 0:
					self.image = ogre_images[7]
				if x > 0 and y < 0:
					self.image = ogre_images[1]
				if x < 0 and y > 0:
					self.image = ogre_images[5]
				if x < 0 and y == 0:
					self.image = ogre_images[6]
				if x > 0 and y == 0:
					self.image = ogre_images[10]
				self.rect.centerx += self.speed*x
				self.rect.centery += self.speed*y
			if elapsed_time >= self.n:
				self.counter1 = False
				self.counter2 = True
				self.start_time1 = pygame.time.get_ticks()
				self.target = random.choice(self.target_list)
			
		if self.counter2:
			if (self.target.rect.centerx - self.rect.centerx) == 0:
				if self.target.rect.centery > self.rect.centery:
					self.image = ogre_images[4]
					self.rect.centery += self.speed 
				elif self.rect.centery > self.target.rect.centery:
					self.image = ogre_images[9]
					self.rect.centery -= self.speed
				else:
					self.rect.centery += 0
			elif (self.target.rect.centerx - self.rect.centerx) != 0:
				x,y = direction(self, self.target)
				if x > 0 and y > 0:
					self.image = ogre_images[3]
				if x < 0 and y < 0:
					self.image = ogre_images[7]
				if x > 0 and y < 0:
					self.image = ogre_images[1]
				if x < 0 and y > 0:
					self.image = ogre_images[5]
				if x < 0 and y == 0:
					self.image = ogre_images[6]
				if x > 0 and y == 0:
					self.image = ogre_images[10]
				self.rect.centerx += self.speed*x
				self.rect.centery += self.speed*y
			if elapsed_time >= self.n:
				self.counter2 = False
				self.counter3 = True
				self.start_time1 = pygame.time.get_ticks()
				self.target = random.choice(self.target_list)

		if self.counter3:
			if (self.target.rect.centerx - self.rect.centerx) == 0:
				if self.target.rect.centery > self.rect.centery:
					self.image = ogre_images[4]
					self.rect.centery += self.speed 
				elif self.rect.centery > self.target.rect.centery:
					self.image = ogre_images[9]
					self.rect.centery -= self.speed
				else:
					self.rect.centery += 0
			elif (self.target.rect.centerx - self.rect.centerx) != 0:
				x,y = direction(self, self.target)
				if x > 0 and y > 0:
					self.image = ogre_images[3]
				if x < 0 and y < 0:
					self.image = ogre_images[7]
				if x > 0 and y < 0:
					self.image = ogre_images[1]
				if x < 0 and y > 0:
					self.image = ogre_images[5]
				if x < 0 and y == 0:
					self.image = ogre_images[6]
				if x > 0 and y == 0:
					self.image = ogre_images[10]
				self.rect.centerx += self.speed*x
				self.rect.centery += self.speed*y
			if elapsed_time >= self.n:
				self.counter3 = False
				self.counter4 = True
				self.start_time1 = pygame.time.get_ticks()
				self.target = random.choice(self.target_list)


		if self.counter4:
			if (self.target.rect.centerx - self.rect.centerx) == 0:
				if self.target.rect.centery > self.rect.centery:
					self.image = ogre_images[4]
					self.rect.centery += self.speed 
				elif self.rect.centery > self.target.rect.centery:
					self.image = ogre_images[9]
					self.rect.centery -= self.speed
				else:
					self.rect.centery += 0
			elif (self.target.rect.centerx - self.rect.centerx) != 0:
				x,y = direction(self, self.target)
				if x > 0 and y > 0:
					self.image = ogre_images[3]
				if x < 0 and y < 0:
					self.image = ogre_images[7]
				if x > 0 and y < 0:
					self.image = ogre_images[1]
				if x < 0 and y > 0:
					self.image = ogre_images[5]
				if x < 0 and y == 0:
					self.image = ogre_images[6]
				if x > 0 and y == 0:
					self.image = ogre_images[10]
				self.rect.centerx += self.speed*x
				self.rect.centery += self.speed*y
			if elapsed_time >= self.n:
				self.counter4 = False
				self.counter5 = True
				self.start_time1 = pygame.time.get_ticks()
				self.target = random.choice(self.target_list)

		if self.counter5:
			if (self.target.rect.centerx - self.rect.centerx) == 0:
				if self.target.rect.centery > self.rect.centery:
					self.image = ogre_images[4]
					self.rect.centery += self.speed 
				elif self.rect.centery > self.target.rect.centery:
					self.image = ogre_images[9]
					self.rect.centery -= self.speed
				else:
					self.rect.centery += 0
			elif (self.target.rect.centerx - self.rect.centerx) != 0:
				x,y = direction(self, self.target)
				if x > 0 and y > 0:
					self.image = ogre_images[3]
				if x < 0 and y < 0:
					self.image = ogre_images[7]
				if x > 0 and y < 0:
					self.image = ogre_images[1]
				if x < 0 and y > 0:
					self.image = ogre_images[5]
				if x < 0 and y == 0:
					self.image = ogre_images[6]
				if x > 0 and y == 0:
					self.image = ogre_images[10]
				self.rect.centerx += self.speed*x
				self.rect.centery += self.speed*y
			if elapsed_time >= self.n:
				self.counter5 = False
				self.counter6 = True
				self.start_time1 = pygame.time.get_ticks()
				self.a , self.b = self.target.rect.centerx , self.target.rect.centerx

		if self.counter6:
			if elapsed_time >= self.n:
				self.counter6 = False
				self.counter7 = True
				self.start_time1 = pygame.time.get_ticks()
				a, b = randint(250,WIDTH), randint(30,500)
				self.n = 2000

		if self.counter7:
			if (self.a - self.rect.centerx) == 0:
				if self.b > self.rect.centery:
					self.image = ogre_images[4]
					self.rect.centery += self.speed*20
				elif self.rect.centery > self.b:
					self.image = ogre_images[9]
					self.rect.centery -= self.speed*20
				else:
					self.rect.centery += 0
			elif (self.a - self.rect.centerx) != 0:
				x,y = direction2(self,(self.a, self.b))
				if x > 0 and y > 0:
					self.image = ogre_images[3]
				if x < 0 and y < 0:
					self.image = ogre_images[7]
				if x > 0 and y < 0:
					self.image = ogre_images[1]
				if x < 0 and y > 0:
					self.image = ogre_images[5]
				if x < 0 and y == 0:
					self.image = ogre_images[6]
				if x > 0 and y == 0:
					self.image = ogre_images[10]
				self.rect.centerx += self.speed*x*20
				self.rect.centery += self.speed*y*20
			if elapsed_time >= self.n:
				self.counter7 = False
				self.counter1 = True
				self.start_time1 = pygame.time.get_ticks()
				self.target = random.choice(self.target_list)
				self.n = 1000

class OgreSeal1(OgreSeal):
	def __init__(self):
		super().__init__()
		
class OgreSeal2(OgreSeal):
	def __init__(self):
		super().__init__()
		
class OgreSeal3(OgreSeal):
	def __init__(self):
		super().__init__()
		
class OgreSeal4(OgreSeal):
	def __init__(self):
		super().__init__()
		
class OgreSeal5(OgreSeal):
	def __init__(self):
		super().__init__()
		
class OgreSeal6(OgreSeal):
	def __init__(self):
		super().__init__()

class Borde1(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.transform.scale(pygame.image.load("img/borde.png").convert(),(1000,1))
		self.image.set_colorkey(WHITE)
		self.rect = self.image.get_rect()
		self.rect.x = 290
		self.rect.y = 80

class Borde2(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.transform.scale(pygame.image.load("img/borde.png").convert(),(1000,1))
		self.image.set_colorkey(WHITE)
		self.rect = self.image.get_rect()
		self.rect.x = 290
		self.rect.y = 550

class Borde3(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.transform.scale(pygame.image.load("img/borde.png").convert(),(1,550))
		self.image.set_colorkey(WHITE)
		self.rect = self.image.get_rect()
		self.rect.x = 300
		self.rect.y = 0

class Borde4(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.transform.scale(pygame.image.load("img/borde.png").convert(),(1,550))
		self.image.set_colorkey(WHITE)
		self.rect = self.image.get_rect()
		self.rect.x = WIDTH
		self.rect.y = 0

def show_go_screen():
	
	screen.fill(BLACK)#(background, [0,0])
	draw_text1(screen, "Ogre Seal Survival", 65, WIDTH // 2, HEIGHT // 4)
	draw_text1(screen, "Avoid getting crushed by the Ogre Seal", 20, WIDTH // 2, HEIGHT // 2)
	draw_text1(screen, "Press Q", 20, WIDTH // 2, HEIGHT * 3/4)
	#draw_text(screen, "Created by: Francisco Carvajal", 10,  60, 625)
	
	pygame.display.flip()
	waiting = True
	while waiting:
		clock.tick(60)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					waiting = False

ogre_images = []
ogre_list = ["img/no.png", "img/2.png", "img/3.png", "img/5.png", "img/6.png", "img/7.png", "img/9.png", "img/10.png", "img/11.png", "img/12.png", "img/33.png"]
for img in ogre_list:
	ogre_images.append(pygame.transform.scale(pygame.image.load(img).convert(),(150,150)))

def show_game_over_screenp1():
	screen.fill(BLACK)
	#draw_text1(screen, "Qop", 65, WIDTH // 2, HEIGHT // 4)
	draw_text1(screen, "Record: " + str(score) + " segundos", 80, WIDTH // 2, 250)
	draw_text1(screen, "Player 1 WINS", 20, WIDTH // 2, 400)
	draw_text1(screen, "Press Q", 20, WIDTH // 2, HEIGHT * 3/4)

	pygame.display.flip()
	waiting = True
	while waiting:
		clock.tick(60)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					waiting = False

def show_game_over_screenp2():
	screen.fill(BLACK)
	#draw_text1(screen, "Qop", 65, WIDTH // 2, HEIGHT // 4)
	draw_text1(screen, "Record: " + str(score) + " segundos", 80, WIDTH // 2, 250)
	draw_text1(screen, "Player 2 WINS", 20, WIDTH // 2, 400)
	draw_text1(screen, "Press Q", 20, WIDTH // 2, HEIGHT * 3/4)

	pygame.display.flip()
	waiting = True
	while waiting:
		clock.tick(60)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					waiting = False

def show_game_over_screenp3():
	screen.fill(BLACK)
	#draw_text1(screen, "Qop", 65, WIDTH // 2, HEIGHT // 4)
	draw_text1(screen, "Record: " + str(score) + " segundos", 80, WIDTH // 2, 250)
	draw_text1(screen, "Player 3 WINS", 20, WIDTH // 2, 400)
	draw_text1(screen, "Press Q", 20, WIDTH // 2, HEIGHT * 3/4)

	pygame.display.flip()
	waiting = True
	while waiting:
		clock.tick(60)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					waiting = False

background = pygame.transform.scale(pygame.image.load("img/fond.png").convert(), (1300,700))

counter1 = True
counter2 = True
counter3 = True
counter4 = True
counter5 = True
counter6 = True
game_over1 = False
game_over2 = False
game_over3 = False
running = True
start = True
while running:
	if game_over1:
		show_game_over_screenp1()
		borde1 = Borde1()
		borde2 = Borde2()
		borde3 = Borde3()
		borde4 = Borde4()
		screen.blit(background,(0,0))
		game_over1 = False
		counter1 = True
		counter2 = True
		counter3 = True
		counter4 = True
		counter5 = True
		counter6 = True
		all_sprites = pygame.sprite.Group()
		all_sprites.add(borde1, borde2, borde3, borde4)
		ogre_list = pygame.sprite.Group()
		ogre1_list = pygame.sprite.Group()
		ogre2_list = pygame.sprite.Group()
		ogre3_list = pygame.sprite.Group()
		ogre4_list = pygame.sprite.Group()
		ogre5_list = pygame.sprite.Group()
		ogre6_list = pygame.sprite.Group()
		player1 = Player1()
		all_sprites.add(player1)
		player2 = Player2()
		all_sprites.add(player2)
		player3 = Player3()
		all_sprites.add(player3)
		
		start_time = pygame.time.get_ticks()
		score = 0

	if game_over2:
		show_game_over_screenp2()
		borde1 = Borde1()
		borde2 = Borde2()
		borde3 = Borde3()
		borde4 = Borde4()
		screen.blit(background,(0,0))
		game_over2 = False
		counter1 = True
		counter2 = True
		counter3 = True
		counter4 = True
		counter5 = True
		counter6 = True
		all_sprites = pygame.sprite.Group()
		all_sprites.add(borde1, borde2, borde3, borde4)
		ogre_list = pygame.sprite.Group()
		ogre1_list = pygame.sprite.Group()
		ogre2_list = pygame.sprite.Group()
		ogre3_list = pygame.sprite.Group()
		ogre4_list = pygame.sprite.Group()
		ogre5_list = pygame.sprite.Group()
		ogre6_list = pygame.sprite.Group()
		player1 = Player1()
		all_sprites.add(player1)
		player2 = Player2()
		all_sprites.add(player2)
		player3 = Player3()
		all_sprites.add(player3)
		
		start_time = pygame.time.get_ticks()
		score = 0

	if game_over3:
		show_game_over_screenp3()
		borde1 = Borde1()
		borde2 = Borde2()
		borde3 = Borde3()
		borde4 = Borde4()
		screen.blit(background,(0,0))
		game_over3 = False
		counter1 = True
		counter2 = True
		counter3 = True
		counter4 = True
		counter5 = True
		counter6 = True
		all_sprites = pygame.sprite.Group()
		all_sprites.add(borde1, borde2, borde3, borde4)
		ogre_list = pygame.sprite.Group()
		ogre1_list = pygame.sprite.Group()
		ogre2_list = pygame.sprite.Group()
		ogre3_list = pygame.sprite.Group()
		ogre4_list = pygame.sprite.Group()
		ogre5_list = pygame.sprite.Group()
		ogre6_list = pygame.sprite.Group()
		player1 = Player1()
		all_sprites.add(player1)
		player2 = Player2()
		all_sprites.add(player2)
		player3 = Player3()
		all_sprites.add(player3)
		
		start_time = pygame.time.get_ticks()
		score = 0

	if start:
		show_go_screen()
		borde1 = Borde1()
		borde2 = Borde2()
		borde3 = Borde3()
		borde4 = Borde4()
		start = False
		all_sprites = pygame.sprite.Group()
		all_sprites.add(borde1, borde2, borde3, borde4)
		ogre_list = pygame.sprite.Group()
		ogre1_list = pygame.sprite.Group()
		ogre2_list = pygame.sprite.Group()
		ogre3_list = pygame.sprite.Group()
		ogre4_list = pygame.sprite.Group()
		ogre5_list = pygame.sprite.Group()
		ogre6_list = pygame.sprite.Group()
		player1 = Player1()
		all_sprites.add(player1)
		player2 = Player2()
		all_sprites.add(player2)
		player3 = Player3()
		all_sprites.add(player3)
		
		start_time = pygame.time.get_ticks()
		score = 0
		
	clock.tick(60)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
			pygame.quit()
			sys.exit()
	
	now = (pygame.time.get_ticks() - start_time)//1000
	
	if counter1:
		if now == 2:
			counter1 = False
			ogre1 = OgreSeal1()
			all_sprites.add(ogre1)
			ogre_list.add(ogre1)
			ogre1_list.add(ogre1)
	if counter2:
		if now == 21:
			counter2 = False
			ogre2 = OgreSeal2()
			all_sprites.add(ogre2)
			ogre_list.add(ogre2)
			ogre2_list.add(ogre2)

	if counter3:
		if now == 38:
			counter3 = False
			ogre3 = OgreSeal3()
			all_sprites.add(ogre3)
			ogre_list.add(ogre3)
			ogre3_list.add(ogre3)
	if counter4:
		if now == 52:
			counter4 = False
			ogre4 = OgreSeal4()
			all_sprites.add(ogre4)
			ogre_list.add(ogre4)
			ogre4_list.add(ogre4)
	if counter5:
		if now == 64:
			counter5 = False
			ogre5 = OgreSeal5()
			all_sprites.add(ogre5)
			ogre_list.add(ogre5)
			ogre5_list.add(ogre5)
	if counter6:
		if now == 76:
			counter6 = False
			ogre6 = OgreSeal6()
			all_sprites.add(ogre6)
			ogre_list.add(ogre6)
			ogre6_list.add(ogre6)
	
	if player1.hp <= 0 and player2.hp <= 0:
		game_over3 = True
		score += now
	if player2.hp <= 0 and player3.hp <= 0:
		game_over1 = True
		score += now
	if player1.hp <= 0 and player3.hp <= 0:
		game_over2 = True
		score += now
	
	all_sprites.update()
	
	# Checar colisiones - jugador1 - ogre seal 1
	hits = pygame.sprite.spritecollide(player1, ogre1_list, False)
	for hit in hits:
		if ogre1.counter6:
			player1.hp -= 0.8

	# Checar colisiones - jugador2 - ogre seal 1
	hits = pygame.sprite.spritecollide(player2, ogre1_list, False)
	for hit in hits:
		if ogre1.counter6:
			player2.hp -= 0.8

	# Checar colisiones - jugador3 - ogre seal 1
	hits = pygame.sprite.spritecollide(player3, ogre1_list, False)
	for hit in hits:
		if ogre1.counter6:
			player3.hp -= 0.8

	# Checar colisiones - jugador1 - ogre seal 2
	hits = pygame.sprite.spritecollide(player1, ogre2_list, False)
	for hit in hits:
		if ogre2.counter6:
			player1.hp -= 0.8

	# Checar colisiones - jugador2 - ogre seal 2
	hits = pygame.sprite.spritecollide(player2, ogre2_list, False)
	for hit in hits:
		if ogre2.counter6:
			player2.hp -= 0.8

	# Checar colisiones - jugador3 - ogre seal 2
	hits = pygame.sprite.spritecollide(player3, ogre2_list, False)
	for hit in hits:
		if ogre2.counter6:
			player3.hp -= 0.8

	# Checar colisiones - jugador1 - ogre seal 3
	hits = pygame.sprite.spritecollide(player1, ogre3_list, False)
	for hit in hits:
		if ogre3.counter6:
			player1.hp -= 0.8

	# Checar colisiones - jugador2 - ogre seal 3
	hits = pygame.sprite.spritecollide(player2, ogre3_list, False)
	for hit in hits:
		if ogre3.counter6:
			player2.hp -= 0.8

	# Checar colisiones - jugador3 - ogre seal 3
	hits = pygame.sprite.spritecollide(player3, ogre3_list, False)
	for hit in hits:
		if ogre3.counter6:
			player3.hp -= 0.8

	# Checar colisiones - jugador1 - ogre seal 4
	hits = pygame.sprite.spritecollide(player1, ogre4_list, False)
	for hit in hits:
		if ogre4.counter6:
			player1.hp -= 0.8

	# Checar colisiones - jugador2 - ogre seal 4
	hits = pygame.sprite.spritecollide(player2, ogre4_list, False)
	for hit in hits:
		if ogre4.counter6:
			player2.hp -= 0.8

	# Checar colisiones - jugador3 - ogre seal 4
	hits = pygame.sprite.spritecollide(player3, ogre4_list, False)
	for hit in hits:
		if ogre4.counter6:
			player3.hp -= 0.8

	# Checar colisiones - jugador1 - ogre seal 5
	hits = pygame.sprite.spritecollide(player1, ogre5_list, False)
	for hit in hits:
		if ogre5.counter6:
			player1.hp -= 0.8

	# Checar colisiones - jugador2 - ogre seal 5
	hits = pygame.sprite.spritecollide(player2, ogre5_list, False)
	for hit in hits:
		if ogre5.counter6:
			player2.hp -= 0.8

	# Checar colisiones - jugador3 - ogre seal 5
	hits = pygame.sprite.spritecollide(player3, ogre5_list, False)
	for hit in hits:
		if ogre5.counter6:
			player3.hp -= 0.8

	# Checar colisiones - jugador1 - ogre seal 6
	hits = pygame.sprite.spritecollide(player1, ogre6_list, False)
	for hit in hits:
		if ogre6.counter6:
			player1.hp -= 0.8

	# Checar colisiones - jugador2 - ogre seal 6
	hits = pygame.sprite.spritecollide(player2, ogre6_list, False)
	for hit in hits:
		if ogre6.counter6:
			player2.hp -= 0.8

	# Checar colisiones - jugador3 - ogre seal 6
	hits = pygame.sprite.spritecollide(player3, ogre6_list, False)
	for hit in hits:
		if ogre6.counter6:
			player3.hp -= 0.8

	screen.blit(background, [0, 0])

	all_sprites.draw(screen)

		
	# Escudo.
	draw_text1(screen, "P1", 20, 10, 6)
	draw_text1(screen, "P2", 20, 400, 6)
	draw_text1(screen, "P3", 20, 800, 6)
	
	draw_hp_bar(screen, 20, 5, player1.hp)
	draw_text2(screen, str(int(player1.hp)) + "/100", 10, 45, 6)
	if player1.hp > 0:
		draw_hp_bar(screen, player1.rect.x, player1.rect.y - 10, player1.hp)

	draw_hp_bar(screen, 415, 5, player2.hp)
	draw_text2(screen, str(int(player2.hp))+ "/100", 10, 440, 6)
	if player2.hp > 0:
		draw_hp_bar(screen, player2.rect.x, player2.rect.y - 10, player2.hp)

	draw_hp_bar(screen, 815, 5, player3.hp)
	draw_text2(screen, str(int(player3.hp))+ "/100", 10, 840, 6)
	if player3.hp > 0:
		draw_hp_bar(screen, player3.rect.x, player3.rect.y - 10, player3.hp)

	
	draw_mana_bar(screen, 20, 15, player1.mana)
	draw_text1(screen, str(int(player1.mana))+ "/100", 10, 45, 16)

	draw_mana_bar(screen, 415, 15, player2.mana)
	draw_text1(screen, str(int(player2.mana))+ "/100", 10, 440, 16)

	draw_mana_bar(screen, 815, 15, player3.mana)
	draw_text1(screen, str(int(player3.mana))+ "/100", 10, 840, 16)

	#reloj
	draw_text1(screen, str((((pygame.time.get_ticks() - start_time)//60000)+(60))%(60))+":" + str((((pygame.time.get_ticks() - start_time)//1000)+(60))%(60)), 30, 570, 50)
	
	

	pygame.display.flip()
pygame.quit()