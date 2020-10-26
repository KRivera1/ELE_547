import pygame
import numpy as np

## Neural Network

eta = 0.01

def sigmoid(x):
	return 1.0/(1 + np.exp(-x))

def sigmoid_derivative(x):
	return x * (1.0 - x)

class NeuralNetwork:
	def __init__(self, x, y):
		self.input	  = x
		self.weights1   = np.random.rand(self.input.shape[1],8) 
		self.weights2   = np.random.rand(8,2)				 
		self.y		  = y
		self.output	 = np.zeros(self.y.shape)

	def feedforward(self):
		self.layer1 = sigmoid(np.dot(self.input, self.weights1))
		self.output = sigmoid(np.dot(self.layer1, self.weights2))

	def backprop(self):
		# application of the chain rule to find derivative of the loss function with respect to weights2 and weights1
		d_weights2 = np.dot(self.layer1.T, (eta*(self.y - self.output) * sigmoid_derivative(self.output)))
		d_weights1 = np.dot(self.input.T,  (np.dot(eta*(self.y - self.output) * sigmoid_derivative(self.output), self.weights2.T) * sigmoid_derivative(self.layer1)))

		# update the weights with the derivative (slope) of the loss function
		self.weights1 += d_weights1
		self.weights2 += d_weights2

	def predict(self, testx):
		self.layer1 = sigmoid(np.dot(testx, self.weights1))
		return (sigmoid(np.dot(self.layer1, self.weights2)))

	def learn(self, newx, newy):
		self.layer1_learn = sigmoid(np.dot(newx, self.weights1))
		self.output_learn = sigmoid(np.dot(self.layer1_learn, self.weights2))
		# application of the chain rule to find derivative of the loss function with respect to weights2 and weights1
		d_weights2 = np.dot(self.layer1_learn.T, (eta*(newy - self.output_learn) * sigmoid_derivative(self.output_learn)))
		d_weights1 = np.dot(newx.T,  (np.dot(eta*(newy - self.output_learn) * sigmoid_derivative(self.output_learn), self.weights2.T) * sigmoid_derivative(self.layer1_learn)))

		self.weights1 += d_weights1
		self.weights2 += d_weights2

	def reset(self, w1, w2):
		self.weights1 = np.zeros([self.input.shape[1],8]) 
		self.weights2 = np.zeros([8,2])
		self.weights1 = np.add(self.weights1, w1)
		self.weights2 = np.add(self.weights2, w2)


## GUI

def draw_grid(screen, color, position, mouse, value):
	if (position[0] + position[2] > mouse[0] > position[0]) and (position[1] + position[3] > mouse[1] > position[1]):
		Button = pygame.draw.rect(screen, color, position)
	else:
		if value:
			Button = pygame.draw.rect(screen, BLUE, position)
		else:
			Button = pygame.draw.rect(screen, BLACK, position)
	return Button

def draw_progress(screen, color, position):
	return pygame.draw.rect(screen, color, position)


def draw_button(screen, color, position):
	return pygame.draw.rect(screen, color, position)

def draw_truefalse(screen, color, position_true, position_false, pattern_output):
	if pattern_output[0][0]:
		Button_true = pygame.draw.rect(screen, BLUE, position_true)
		Button_false = pygame.draw.rect(screen, BLACK, position_false)
		return Button_true, Button_false
	else:
		Button_true = pygame.draw.rect(screen, BLACK, position_true)
		Button_false = pygame.draw.rect(screen, BLUE, position_false)
		return Button_true, Button_false

def draw_gridline(screen, color):
	line1 = pygame.draw.line(screen, color, (60, 60), (60,420)) 
	line2 = pygame.draw.line(screen, color, (150, 60), (150,420)) 
	line3 = pygame.draw.line(screen, color, (240, 60), (240,420)) 
	line4 = pygame.draw.line(screen, color, (330, 60), (330,420)) 
	line5 = pygame.draw.line(screen, color, (420, 60), (420,420)) 
	line6 = pygame.draw.line(screen, color, (60, 60), (420,60)) 
	line7 = pygame.draw.line(screen, color, (60, 150), (420,150)) 
	line8 = pygame.draw.line(screen, color, (60, 240), (420,240)) 
	line9 = pygame.draw.line(screen, color, (60, 330), (420,330)) 
	line10 = pygame.draw.line(screen, color, (60, 420), (420,420))

def draw_buttonline(screen, color):
	pygame.draw.line(screen, color, (700, 40), (700,220))
	pygame.draw.line(screen, color, (770, 40), (770,220))
	pygame.draw.line(screen, color, (700, 40), (770,40))
	pygame.draw.line(screen, color, (700, 130), (770,130))
	pygame.draw.line(screen, color, (700, 220), (770,220))
	pygame.draw.line(screen, color, (700, 350), (700,430))
	pygame.draw.line(screen, color, (700, 430), (770,430))
	pygame.draw.line(screen, color, (700, 350), (770,350))
	pygame.draw.line(screen, color, (770, 350), (770,430))
	pygame.draw.line(screen, color, (520, 350), (620,350))
	pygame.draw.line(screen, color, (520, 350), (520,430))
	pygame.draw.line(screen, color, (520, 430), (620,430))
	pygame.draw.line(screen, color, (620, 350), (620,430))

def show_progress(progress):
	draw_progress(screen, GREEN, (500,150,120*progress[0][0],40))
	draw_progress(screen, RED, (500+120*progress[0][0],150,120*(1-progress[0][0]),40))
	draw_progress(screen, GREEN, (500,260,120*(progress[0][1]),40))
	draw_progress(screen, RED, (500+120*(progress[0][1]),260,120*(1-progress[0][1]),40))

def main(pattern_output):
	pygame.init()
	screen = pygame.display.set_mode((800, 480))
	size = width, height = 800, 480

	move = 0
	move1 = width

	font = pygame.font.Font('freesansbold.ttf', 32) 
	
	text = font.render('nothing', True, WHITE, BLACK)  
	textRect = text.get_rect()  
	textRect.center = (800 // 2, 480 // 2) 

	while True:
		screen.fill(BLACK)
		# pygame.display.flip()
		mouse = pygame.mouse.get_pos() 

		Grid1 = draw_grid(screen, (66,244,238), (60,60,90,90), mouse, pattern[0][0])
		Grid2 = draw_grid(screen, (66,244,238), (150,60,90,90), mouse, pattern[0][1])
		Grid3 = draw_grid(screen, (66,244,238), (240,60,90,90), mouse, pattern[0][2])
		Grid4 = draw_grid(screen, (66,244,238), (330,60,90,90), mouse, pattern[0][3])
		Grid5 = draw_grid(screen, (66,244,238), (60,150,90,90), mouse, pattern[0][4])
		Grid6 = draw_grid(screen, (66,244,238), (150,150,90,90), mouse, pattern[0][5])
		Grid7 = draw_grid(screen, (66,244,238), (240,150,90,90), mouse, pattern[0][6])
		Grid8 = draw_grid(screen, (66,244,238), (330,150,90,90), mouse, pattern[0][7])
		Grid9 = draw_grid(screen, (66,244,238), (60,240,90,90), mouse, pattern[0][8])
		Grid10 = draw_grid(screen, (66,244,238), (150,240,90,90), mouse, pattern[0][9])
		Grid11 = draw_grid(screen, (66,244,238), (240,240,90,90), mouse, pattern[0][10])
		Grid12 = draw_grid(screen, (66,244,238), (330,240,90,90), mouse, pattern[0][11])
		Grid13 = draw_grid(screen, (66,244,238), (60,330,90,90), mouse, pattern[0][12])
		Grid14 = draw_grid(screen, (66,244,238), (150,330,90,90), mouse, pattern[0][13])
		Grid15 = draw_grid(screen, (66,244,238), (240,330,90,90), mouse, pattern[0][14])
		Grid16 = draw_grid(screen, (66,244,238), (330,330,90,90), mouse, pattern[0][15])

		draw_gridline(screen, WHITE)

		text = font.render(str(pattern_output), True, WHITE, BLACK) 
		# screen.blit(text, textRect)

		# use nn result here
		progress = nn.predict(pattern)
		draw_progress(screen, GREEN, (500,150,120*progress[0][0],40))
		draw_progress(screen, RED, (500+120*progress[0][0],150,120*(1-progress[0][0]),40))
		draw_progress(screen, GREEN, (500,260,120*(progress[0][1]),40))
		draw_progress(screen, RED, (500+120*(progress[0][1]),260,120*(1-progress[0][1]),40))

		# Button_true = draw_button(screen, BLACK, (700,40,70,90))
		# Button_false = draw_button(screen, BLACK, (700,130,70,90))
		Button_true, Button_false = draw_truefalse(screen, BLACK,(700,40,70,90),(700,130,70,90), pattern_output)
		Button_learn = draw_button(screen, BLACK, (700,350,70,80))
		Button_reset = draw_button(screen, BLACK, (520,350,100,80))

		text_true = font.render('T', True, WHITE, BLACK) 
		text_false = font.render('F', True, WHITE, BLACK)

		text_Learn = font.render('L', True, WHITE, BLACK) 
		text_Reset = font.render('Reset', True, WHITE, BLACK) 

		tr_true = text_true.get_rect()
		tr_true.center = (735, 85)

		tr_false = text_false.get_rect()
		tr_false.center = (735, 175)

		tr_learn = text_Learn.get_rect()
		tr_learn.center = (735, 390)

		tr_reset = text_Reset.get_rect()
		tr_reset.center = (570, 390)

		screen.blit(text_true, tr_true)
		screen.blit(text_false, tr_false)
		screen.blit(text_Learn, tr_learn)
		screen.blit(text_Reset, tr_reset)

		draw_buttonline(screen, WHITE)

		pygame.display.update()
		for event in pygame.event.get():
			if event.type == pygame.MOUSEBUTTONUP:
				pos = pygame.mouse.get_pos()

				g1_click = Grid1.collidepoint(pos)
				g2_click = Grid2.collidepoint(pos)
				g3_click = Grid3.collidepoint(pos)
				g4_click = Grid4.collidepoint(pos)
				g5_click = Grid5.collidepoint(pos)
				g6_click = Grid6.collidepoint(pos)
				g7_click = Grid7.collidepoint(pos)
				g8_click = Grid8.collidepoint(pos)
				g9_click = Grid9.collidepoint(pos)
				g10_click = Grid10.collidepoint(pos)
				g11_click = Grid11.collidepoint(pos)
				g12_click = Grid12.collidepoint(pos)
				g13_click = Grid13.collidepoint(pos)
				g14_click = Grid14.collidepoint(pos)
				g15_click = Grid15.collidepoint(pos)
				g16_click = Grid16.collidepoint(pos)

				b_true = Button_true.collidepoint(pos)
				b_false = Button_false.collidepoint(pos)
				b_learn = Button_learn.collidepoint(pos)
				b_reset = Button_reset.collidepoint(pos)

				##  1 xor 1 = 0, 0 xor 1 = 1, we have exactly flip effect
				if g1_click:
					pattern[0][0] = np.logical_xor(pattern[0][0], 1)
				if g2_click:
					pattern[0][1] = np.logical_xor(pattern[0][1], 1)
				if g3_click:
					pattern[0][2] = np.logical_xor(pattern[0][2], 1)
				if g4_click:
					pattern[0][3] = np.logical_xor(pattern[0][3], 1)
				if g5_click:
					pattern[0][4] = np.logical_xor(pattern[0][4], 1)
				if g6_click:
					pattern[0][5] = np.logical_xor(pattern[0][5], 1)
				if g7_click:
					pattern[0][6] = np.logical_xor(pattern[0][6], 1)
				if g8_click:
					pattern[0][7] = np.logical_xor(pattern[0][7], 1)
				if g9_click:
					pattern[0][8] = np.logical_xor(pattern[0][8], 1)
				if g10_click:
					pattern[0][9] = np.logical_xor(pattern[0][9], 1)
				if g11_click:
					pattern[0][10] = np.logical_xor(pattern[0][10], 1)
				if g12_click:
					pattern[0][11] = np.logical_xor(pattern[0][11], 1)
				if g13_click:
					pattern[0][12] = np.logical_xor(pattern[0][12], 1)
				if g14_click:
					pattern[0][13] = np.logical_xor(pattern[0][13], 1)
				if g15_click:
					pattern[0][14] = np.logical_xor(pattern[0][14], 1)
				if g16_click:
					pattern[0][15] = np.logical_xor(pattern[0][15], 1)

				step = 50
				if b_true:
					pattern_output = np.array([[1, 0]])
					step = 50
				if b_false:
					pattern_output = np.array([[0, 1]])
					step = 50
				if b_learn:
					for i in range(50):
						nn.learn(pattern, pattern_output)
				if b_reset:
					print('reset')
					print(nn.weights1)
					nn.reset(init_weight1,init_weight2)
					print('done')
					print(init_weight1)

			if event.type == pygame.QUIT:
				pygame.display.quit()
				pygame.quit()
				exit()
	quit()

if __name__ == '__main__':
	## Neural Network
	X = np.array([[ 1, 1, 0, 0, 
					1, 1, 0, 0, 
					0, 0, 0, 0, 
					0, 0, 0, 0],   #True

				  [ 0, 0, 0, 0, 
					1, 1, 0, 0, 
					1, 1, 0, 0, 
					0, 0, 0, 0],   #True

				  [ 0, 0, 0, 0, 
					0, 1, 1, 0, 
					0, 1, 1, 0, 
					0, 0, 0, 0],   #True

				  [ 0, 0, 0, 0, 
					0, 0, 0, 0, 
					0, 0, 1, 1, 
					0, 0, 1, 1],   #True

				  [ 1, 1, 1, 0, 
					0, 1, 0, 0, 
					0, 0, 0, 0, 
					0, 0, 0, 0],   #False

				  [ 0, 0, 0, 0, 
					1, 1, 1, 1, 
					0, 0, 0, 0, 
					0, 0, 0, 0]])  #False

	y = np.array([[1, 0],[1, 0],[1, 0],[1, 0],[0, 1],[0, 1]])

	nn = NeuralNetwork(X,y)

	for i in range(9500):
		nn.feedforward()
		nn.backprop()

	print(nn.output)
	print(nn.weights1)
	print(nn.weights2)

	init_weights1  = np.zeros([X.shape[1],8])
	init_weights2  = np.zeros([8,2])				 

	init_weight1 = np.add(nn.weights1, init_weights1)
	init_weight2 = np.add(nn.weights2, init_weights2)

	TESTX = np.array([[ 0, 0, 0, 0, 
						0, 1, 1, 0, 
						0, 1, 1, 0, 
						0, 0, 0, 0]])

	print(nn.predict(TESTX))

	# GUI

	WHITE = (255,255,255)
	BLACK = (0,0,0)
	BLUE = (0,0,255)
	RED=(255,0,0)
	GREEN=(0,255,0)
	YELLOW=(255,255,0)
	PURPLE=(128,0,128)
	pattern_output = np.array([[1, 0]])

	print(pattern_output)

	pattern = np.array([[1, 1, 0, 0, 
						 1, 1, 0, 0, 
						 0, 0, 0, 0, 
						 0, 0, 0, 0]])
	
	main(pattern_output)
