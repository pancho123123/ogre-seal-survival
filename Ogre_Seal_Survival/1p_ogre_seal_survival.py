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
		self.rect.x = 500
		self.rect.y = 133
		self.speed_x = 0
		self.hp = 100
		self.mana = 100
		
	def update(self):
		self.hp += 0.02
		self.mana += 1/50
		if self.mana < 0:
			self.mana = 0
		if self.mana > 100:
			self.mana = 100
		if self.hp < 0:
			self.hp = 0
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
	if radio != 0:
		x, y = (dx/radio, dy/radio)
	else:
		x, y = (0, 0)
	return x, y

def direction2(a,b):
	#x,y unitary vector from a to b
	dx = b[0] - a.rect.centerx
	dy = b[1] - a.rect.centery
	radio = (dx**2 + dy**2)**(1/2)
	if radio != 0:
		x, y = (dx/radio, dy/radio)
	else:
		x, y = (0, 0)
	return x, y	

class OgreSeal(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = ogre_images[0]
		self.image.set_colorkey(WHITE)
		self.rect = self.image.get_rect()
		self.rect.x = 750
		self.rect.y = 233
		self.hp = 100
		self.counter1 = True
		self.counter2 = False
		self.counter3 = False
		self.n = randint(2000,4000)
		self.start_time1 = pygame.time.get_ticks()
		self.speed = 2
		self.a = 0
		self.b = 0
		self.a = 0
		self.b = 0

	def update(self):
		target = player
		self.image.set_colorkey(WHITE)
		current_time = pygame.time.get_ticks()
		elapsed_time = current_time - self.start_time1
		print(self.counter1)
		print(self.counter2)
		print(self.counter3)
		print(elapsed_time)
		#print(self.a , self.b)
		if self.rect.right > WIDTH:
			self.rect.right = WIDTH
		if self.rect.left < 250:
			self.rect.left = 250
		if self.rect.top < 30:
			self.rect.top = 30
		if self.rect.bottom > 500:
			self.rect.bottom = 500
		
		if self.counter1:
			print("a")
			x,y = direction(self, target)
			if x > 0 and y > 0:
				self.image = ogre_images[3]
			elif x < 0 and y < 0:
				self.image = ogre_images[7]
			elif x > 0 and y < 0:
				self.image = ogre_images[1]
			elif x < 0 and y > 0:
				self.image = ogre_images[5]
			elif x < 0 and y == 0:
				self.image = ogre_images[6]
			elif x > 0 and y == 0:
				self.image = ogre_images[10]
			elif x == 0 and y > 0:
				self.image = ogre_images[4]
			#elif x == 0 and y < 0:
			else:
				self.image = ogre_images[9]
			self.rect.centerx += self.speed*x
			self.rect.centery += self.speed*y
			if elapsed_time >= self.n:
				self.counter1 = False
				self.n = 1000
				self.a, self.b = target.rect.centerx, target.rect.centery
				self.counter2 = True
				self.start_time1 = pygame.time.get_ticks()

		elif self.counter2:
			print("b")
			if elapsed_time >= self.n:
				self.counter2 = False
				self.c, self.d = randint(250,WIDTH), randint(30,500)
				self.n = 2000
				self.counter3 = True
				self.start_time1 = pygame.time.get_ticks()

		elif self.counter3:
			print("d")
			if self.a == self.rect.centerx and self.b == self.rect.centery:
				x,y = direction2(self,(self.c, self.d))
				if x > 0 and y > 0:
					self.image = ogre_images[3]
				elif x < 0 and y < 0:
					self.image = ogre_images[7]
				elif x > 0 and y < 0:
					self.image = ogre_images[1]
				elif x < 0 and y > 0:
					self.image = ogre_images[5]
				elif x < 0 and y == 0:
					self.image = ogre_images[6]
				elif x > 0 and y == 0:
					self.image = ogre_images[10]
				elif x == 0 and y > 0:
					self.image = ogre_images[4]
				#elif x == 0 and y < 0:
				else:
					self.image = ogre_images[9]
				self.rect.centerx += self.speed*x*15
				self.rect.centery += self.speed*y*15
			else:
				x,y = direction2(self,(self.a, self.b))
				if x > 0 and y > 0:
					self.image = ogre_images[3]
				elif x < 0 and y < 0:
					self.image = ogre_images[7]
				elif x > 0 and y < 0:
					self.image = ogre_images[1]
				elif x < 0 and y > 0:
					self.image = ogre_images[5]
				elif x < 0 and y == 0:
					self.image = ogre_images[6]
				elif x > 0 and y == 0:
					self.image = ogre_images[10]
				elif x == 0 and y > 0:
					self.image = ogre_images[4]
				#elif x == 0 and y < 0:
				else:
					self.image = ogre_images[9]
				self.rect.centerx += self.speed*x*15
				self.rect.centery += self.speed*y*15
			if elapsed_time >= self.n:
				self.counter3 = False
				self.n = randint(2000,4000)
				self.counter1 = True
				self.start_time1 = pygame.time.get_ticks()
				
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
		

def show_go_screen():
	screen.fill(BLACK)
	draw_text1(screen, "Ogre Seal Survival", 65, WIDTH // 2, HEIGHT // 4)
	draw_text1(screen, "Avoid getting crushed by the Ogre Seal", 20, WIDTH // 2, HEIGHT // 2)
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

ogre_images = []
ogre_list = ["img/no.png", "img/2.png", "img/3.png", "img/5.png", "img/6.png", "img/7.png", "img/9.png", "img/10.png", "img/11.png", "img/12.png", "img/33.png"]
for img in ogre_list:
	ogre_images.append(pygame.transform.scale(pygame.image.load(img).convert(),(150,150)))

def show_game_over_screen():
	screen.fill(BLACK)
	#draw_text1(screen, "Qop", 65, WIDTH // 2, HEIGHT // 4)
	draw_text1(screen, "Record: " + str(score) + " segundos", 80, WIDTH // 2, 250)
	draw_text1(screen, "Game Over", 20, WIDTH // 2, 400)
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
game_over = False
running = True
start = True
while running:
	if game_over:
		show_game_over_screen()
		screen.blit(background,(0,0))
		game_over = False
		counter1 = True
		counter2 = True
		counter3 = True
		counter4 = True
		counter5 = True
		counter6 = True
		all_sprites = pygame.sprite.Group()
		ogre_list = pygame.sprite.Group()
		player = Player()
		all_sprites.add(player)
		start_time = pygame.time.get_ticks()
		score = 0
	
	if start:
		show_go_screen()
		start = False
		all_sprites = pygame.sprite.Group()
		ogre_list = pygame.sprite.Group()
		player = Player()
		all_sprites.add(player)
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
	if counter2:
		if now == 21:
			counter2 = False
			ogre2 = OgreSeal2()
			all_sprites.add(ogre2)
			ogre_list.add(ogre2)
	if counter3:
		if now == 38:
			counter3 = False
			ogre3 = OgreSeal3()
			all_sprites.add(ogre3)
			ogre_list.add(ogre3)
	if counter4:
		if now == 52:
			counter4 = False
			ogre4 = OgreSeal4()
			all_sprites.add(ogre4)
			ogre_list.add(ogre4)
	if counter5:
		if now == 64:
			counter5 = False
			ogre5 = OgreSeal5()
			all_sprites.add(ogre5)
			ogre_list.add(ogre5)
	if counter6:
		if now == 76:
			counter6 = False
			ogre6 = OgreSeal6()
			all_sprites.add(ogre6)
			ogre_list.add(ogre6)
	
	if player.hp <= 0:
		game_over = True
		score += now
	
	all_sprites.update()
	
	# Checar colisiones - jugador - ogre seal 
	for o in ogre_list:
		if pygame.sprite.collide_rect(player,o):
			if o.counter3:
				player.hp -= 0.8

	screen.blit(background, [0, 0])

	all_sprites.draw(screen)

	# Escudo.
	draw_text1(screen, "P1", 20, 500, 6)
		
	draw_hp_bar(screen, 520, 5, player.hp)
	draw_text2(screen, str(int(player.hp)) + "/100", 10, 545, 6)
	draw_hp_bar(screen, player.rect.x, player.rect.y - 10, player.hp)

	draw_mana_bar(screen, 520, 15, player.mana)
	draw_text1(screen, str(int(player.mana))+ "/100", 10, 545, 16)

	#reloj
	draw_text1(screen, str((((pygame.time.get_ticks() - start_time)//60000)+(60))%(60))+":" + str((((pygame.time.get_ticks() - start_time)//1000)+(60))%(60)), 30, 570, 50)
	
	pygame.display.flip()
pygame.quit()