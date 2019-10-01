import pygame
import pygame.draw as draw
import pygame.display as display

'''
This file defines the "Main" class, which handles most of the annoying graphics stuff,
like buttons and redrawing everything every frame.
Includes some freebies like a simple color list (colors) and a function that displays
on-screen text (disp).
See example.py to get started.
'''

class colors(object): #look what you made me do
    white = (255,255,255)
    black = (0, 0, 0)
    gray = (90, 90, 90)
    bg = (218, 218, 200)
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    yellow = (255, 255, 0)
    cyan = (0, 255, 255)
    purple = (255, 0, 255)
#end

class Button(object):
    def __init__(self, pos, size, text, colorDefault, colorOver, action):
        self.pos = pos
        self.size = size
        self.text = text
        self.colorDefault = colorDefault
        self.colorOver = colorOver
        self.action = action
        self.mouseOver = False
        self.master = None
    #end

    def draw(self, main):
        col = self.colorDefault
        if self.mouseOver:
            col = self.colorOver
        #end
        main.mainDisplay.fill(col, rect=(self.pos[0], self.pos[1], self.size[0], self.size[1]))
        main.disp(self.text, pos=(self.pos[0]+self.size[0]/2.0, self.pos[1]+self.size[1]/2.0))
    #end

    def hoverCheck(self, mouse):
        self.mouseOver = ((self.pos[0] <= mouse[0] <= self.pos[0] + self.size[0]) and (self.pos[1] <= mouse[1] <= self.pos[1] + self.size[1]))
    #end

    def clickCheck(self):
        if self.mouseOver:
            self.action(self)
        #end
    #end

    def remove(self):
        if self.master:
            self.master.removeButton(self)
        #end
    #end
#end

class ButtonHandler(object):
    def __init__(self):
        self.buttons = []
    #end


#end

class Main(object):
    def __init__(self, title, size=(800,800), fps=10, bg=colors.bg):
        self.title = title
        self.W = size[0]
        self.H = size[1]
        self.fps = fps
        self.bg = bg
        self.modules = []
        self.buttons = []
    #end

    def quit(self):
        self.running = False
    #end

    def addModule(self, m):
        self.modules += [m]
        m.setup(self)
    #end

    def addButton(self, pos, size, text, colorDefault, colorOver, action):
        but = Button(pos, size, text, colorDefault, colorOver, action)
        self.buttons += [but]
        return but
    #end

    def drawButtons(self):
        for b in self.buttons:
            b.draw(self)
        #end
    #end

    def hoverCheck(self, mouse):
        for b in self.buttons:
            b.hoverCheck(mouse)
        #end
    #end

    def clickCheck(self):
        for b in self.buttons:
            b.clickCheck()
        #end
    #end

    def removeButton(self, but):
        r = 0
        for i in range(len(self.buttons)):
            if self.buttons[i] == but:
                r = i
                break
            #end
        #end
        self.buttons = self.buttons[:r] + self.buttons[r:]
    #end

    def disp(self, msg, pos=(0,0), col=colors.black, size=25):
        font = pygame.font.SysFont(None, size)
        t = font.render(msg, True, col)
        self.mainDisplay.blit(t, pos)
    #end

    def run(self):
        pygame.init()
        clock = pygame.time.Clock()
        self.mainDisplay = display.set_mode((int(self.W), int(self.H)))
        display.set_caption(self.title)

        self.running = True

        while self.running:
            self.mainDisplay.fill(self.bg)
            mouse = pygame.mouse.get_pos()
            events = pygame.event.get() #calling this seems to empty the event list
            for event in events:
                if event.type == pygame.QUIT:
                    self.running = False
                    break
                elif event.type == pygame.MOUSEMOTION:
                    self.hoverCheck(mouse)
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.clickCheck()
                    #end
                #end
            #end
            self.drawButtons()

            for m in self.modules:
                m.dispatch(events, mouse)

            display.update()
            clock.tick(self.fps)
        #end

        pygame.quit()
        quit()
    #end
#end

class Module(object):
    '''
    A helpfull baseclass that reminds you to implement base functionality to fully
    take advantage of the Main class's facilities.
    '''
    def dispatch(self, events, mouse):
        print("You forgot to override your module's dispatch method.")
    #end

    def setup(self, main):
        print("You forgot to override your module's setup method.")
    #end

    def mouseButtonDown(self, pos):
        return
    #end

    def mouseMove(self, pos):
        return
    #end

    def keyPress(self, key):
        return
    #end
#end
