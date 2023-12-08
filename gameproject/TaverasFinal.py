import pygame
from pygame import mixer

pygame.init()
mixer.init()

#Clock for the keys
clock = pygame.time.Clock()


#Creates the display and caption for the window
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("My Rhythm Game")


#Creates the colors for the background, menu buttons, keys, notes, and counter
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)


#Creates the font
font = pygame.font.Font(None, 36)


class Button(object):
    '''Models the stage buttons
    attributes: x, y, width, height, color, text, action'''
    def __init__(self, x, y, width, height, color, text, action):
        '''Initializes the buttons'''
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.text = text
        self.action = action

    def draw(self):
        '''Draws the buttons'''
        pygame.draw.rect(screen, self.color, self.rect)
        text_surface = font.render(self.text, True, WHITE)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def handle_event(self, event):
        '''Recongnizes the mouse position and when a button is clicked'''
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.action()


class Key(object):
    '''Models the Keys
    attributes: x, y, color1, color2, key'''
    def __init__(self, x, y, color1, color2, key):
        self.rect = pygame.Rect(x, y, 50, 60) #4th value changes the height of the keys
        self.color1 = color1
        self.color2 = color2
        self.key = key
        self.handled = False

#To define load
def load(map, keys):
    '''Loads the music and notes for each stages'''
    rects = []
    pygame.mixer.music.load(f"{map}.mp3") #For the music
    pygame.mixer.music.play()
    with open(f"{map}.txt", 'r') as f: #Reads the notes
        data = f.readlines()

    #Reads the notes
    for y in range(len(data)):
        for x in range(len(data[y])):
            if data[y][x] == '0': #Reads the 0's in the txt file
                rects.append(pygame.Rect(keys[x].rect.centerx - 25, y * -100, 50, 25))
    return rects
    

map_rect = [] #For defining

#Creates keys and assigns the keybind
keys = []
keys.append(Key(100, 500, (255, 0, 0), (220, 0, 0), pygame.K_LSHIFT))
keys.append(Key(200, 500, (0, 255, 0), (0, 220, 0), pygame.K_z))
keys.append(Key(300, 500, (0, 0, 255), (0, 0, 220), pygame.K_SLASH))
keys.append(Key(400, 500, (255, 255, 0), (220, 220, 0), pygame.K_RSHIFT))


#Sets the stage button values
stage1_clicked = False
stage2_clicked = False
buttons_visible = True

#Sets the counter values
stage1_counter = 0
stage2_counter = 0
stage1_counter_visible = False
stage2_counter_visible = False


#Stage 1 map
def load_stage1():
    '''Loads the notes and keys for stage 1'''
    global map_rect, stage1_clicked, stage2_clicked, buttons_visible
    map_rect = []
    map_rect = load("stage1", keys) #Loads the keys
    stage1_clicked = True
    stage2_clicked = False
    buttons_visible = False #Makes the stage buttons vanish

    #Loads the the notes
    with open("stage1.txt", 'r') as f:
        data = f.readlines()
        
    for y in range(len(data)):
        for x in range(len(data[y])):
            if data[y][x] == '0':
                map_rect.append(pygame.Rect(keys[x].rect.centerx - 25, y * -100, 50, 25))

#Creates the Stage 1 button
stage1_button = Button(350, 250, 100, 50, RED, "Stage 1", load_stage1)



#Stage 2 map
def load_stage2():
    '''Loads the notes and keys for stage 2'''
    global map_rect, stage1_clicked, stage2_clicked, buttons_visible
    map_rect = []
    map_rect = load("stage2", keys)  #Loads the keys
    stage1_clicked = False
    stage2_clicked = True
    buttons_visible = False #Makes the stage buttons vanish


    #Loads the the notes
    with open("stage2.txt", 'r') as f:
        data = f.readlines()
    
    for y in range(len(data)):
        for x in range(len(data[y])):
            if data[y][x] == '0':
                map_rect.append(pygame.Rect(keys[x].rect.centerx - 25, y * -100, 50, 25))

#Creates the Stage 2 button
stage2_button = Button(350, 320, 100, 50, BLUE, "Stage 2", load_stage2)


#Creates a game loop (everything in here is while the game running)
while True:
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if buttons_visible:
            if not stage2_clicked:
                stage1_button.handle_event(event)  #Handles events for Stage 1 button

            if not stage1_clicked:
                stage2_button.handle_event(event)  #Handles events for Stage 2 button

    #Draws the Stage 1 and Stage 2 buttons
    if buttons_visible:
        if not stage1_clicked:
            stage1_button.draw()

        if not stage2_clicked:
            stage2_button.draw()
    
    #Creates the counter for Stage 1 and Stage 2
    if stage1_clicked:
        stage1_total = 482  #Total number of notes in Stage 1
        stage1_counter_text = font.render(f"{stage1_counter} / {stage1_total}", True, WHITE)
        screen.blit(stage1_counter_text, (500, 450))

    if stage2_clicked:
        stage2_total = 528  #Total number of notes in Stage 2 (update later)
        stage2_counter_text = font.render(f"{stage2_counter} / {stage2_total}", True, WHITE)
        screen.blit(stage2_counter_text, (500, 450))



    #Loads the keys into the map and light the key 
    if map_rect:
        k = pygame.key.get_pressed()
        for key in keys:
            if k[key.key]:
                pygame.draw.rect(screen, key.color1, key.rect)
                key.handled = False
            if not k[key.key]:
                pygame.draw.rect(screen, key.color2, key.rect)
                key.handled = True

        for rect in map_rect:
            pygame.draw.rect(screen, (200, 0, 0), rect)
            rect.y += 7 #Sets the speed the notes fall
            for key in keys:
                if key.rect.colliderect(rect) and not key.handled:
                    map_rect.remove(rect)
                    key.handled = True
                    
                    #Updates the counters (broken)
                    if stage1_clicked:
                        stage1_counter += 1
                    elif stage2_clicked:
                        stage2_counter += 1
                    break


    pygame.display.update()
    clock.tick(60)