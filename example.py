from main import Main, colors, Module
import pygame, math, random

main = Main("Example", bg=(210,210,210), fps=10)

class ExampleModule(Module):
    def __init__(self):
        self.buttons = []
    #end

    def dispatch(self, events, mouse):
        for e in events:
            if e.type == pygame.KEYDOWN and e.key == pygame.K_q:
                print("pressed q")
                main.quit()
            #end
        #end
    #end

    def setup(self, main):
        self.buttons += [main.addButton((400, 400), (120, 50), "start game", colors.blue, colors.green, lambda x: print(x))]
    #end
#end

main.addModule(ExampleModule())
main.run()
