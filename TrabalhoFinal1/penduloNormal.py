import pygame
import math
 
#VARIABLES
width, height = 800, 400   # Tamanho da tela
Out = False                # Estado(byte) que controla se o jogo continua ou nao. Se verdadeiro: jogo encerra.
acceleration = False       # Estado que controla o calculo da dinamica do pendulo
length = 0                 # Comprimento L entre a bola e o rolamento
angle = 0                  # Angulo
vel = 0                    # Velocidade
Aacc = 0                   # Aceleracao
length_draw = 300;

#COLORS
white = (255,255,255)
black = (0,0,0)
gray = (150, 150, 150)
Dark_red = (150, 0, 0)
     

class ball(object):
 
    def __init__(self, XY, radius):  # Set ball coordenates and radius
        self.x = XY[0]
        self.y = XY[1]
        self.radius = radius
 
    def draw(self, bg):  # Draw circle and line based on XY coordinates
        pygame.draw.lines(bg, black, False, [(width/2, 50), (self.x, self.y)], 2)
        pygame.draw.circle(bg, black, (self.x, self.y), self.radius)
        pygame.draw.circle(bg, Dark_red, (self.x, self.y), self.radius - 2)
 
 
def grid():  # Draw a grid behind the pendulum
    for x in range(50, width, 50):
        pygame.draw.lines(background, gray, False, [(x, 0), (x, height)])
        for y in range(50, height, 50):
            pygame.draw.lines(background, gray, False, [(0, y), (width, y)])
    pygame.draw.circle(background, black, (int(width/2), 50), 5)
 
def angle_Length():  # Send back the length and angle at the first click on screen
    length = math.sqrt(math.pow(pendulum.x - width/2, 2) + math.pow(pendulum.y - 50, 2))
    angle = math.asin((pendulum.x - width/2)/ length)
    return (angle, length)
 
def get_path(angle, length): # with angle and length calculate x and y position
    pendulum.x = round(width/2 + length * math.sin(angle))
    pendulum.y = round(50 + length * math.cos(angle))
 
def redraw(): # Clean up the screen and start a new grid and new frame of pendulum with new coordinates
    background.fill(white)
    grid()
    pendulum.draw(background)
    pygame.display.update()
 
#BEFORE START
pygame.init()
background = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

pendulum = ball((int(width / 2),300), 15) # Comeca com o pendulo invisivel equilibrado no meio da tela para cima

 
if __name__ == '__main__': 

    while not Out:
        clock.tick(120)   #FPS
    
        for event in pygame.event.get():  # Coleta de eventos do pygame                 
            if event.type == pygame.QUIT: #Quando fecha a janela                   
                Out = True                                   
            if event.type == pygame.MOUSEBUTTONDOWN:  #Quando clica o mouse em algum local
                pendulum = ball(pygame.mouse.get_pos(), 15)
                angle, length = angle_Length()           
                acceleration = True                          
    
        if acceleration:   # Increase acceleration and damping in the pendulum moviment
            Aacc = -0.005 * math.sin(angle)
            vel += Aacc
            vel *= 0.99  # damping factor
            angle += vel
            get_path(angle, length_draw)
    
        redraw()
        
    pygame.quit()