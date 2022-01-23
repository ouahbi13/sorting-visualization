'''
    This is the first project of the Algo Cell,
    Don't hesitate to ask me about any difficulties or parts you didn't understand.

    IMPORTANT:
        This project is still incomplete and here comes your part,
        try to implement one (or more if you can) of the other sorting algorithms,
        and submit a pull request to the project (you should fork it first),
        this will help you get in the open source.
        If you don't know how to submit a pull request, don't worry we will do a git/github session sooner,
        and for now, you can send me the code (implementation of the sorting algorithm) so we can discuss it together.
'''

import pygame
import math
import random
pygame.init()

class Window:
    '''
        Window is just an abstraction class,
        and the actual window that shows when executing the code is the self.screen attribute
    '''
    BG_COLOR = 255, 255, 255
    BLACK = 0, 0, 0
    BLUE = 0, 100, 150
    RED = 255, 0, 0
    GREEN = 0, 255, 0

    SIDE_MARGIN = 140 #Sum of right margin and left margin
    TOP_MARGIN = 200 #The top margin (where to write titles and instructions)

    FONT = pygame.font.SysFont('Montserrat Thin', 30)
    LARGE_FONT = pygame.font.SysFont('Montserrat Thin', 40)

    def __init__(self, width, height, array):
        self.array = array
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))

        self.min =  min(array)
        self.max = max(array)
        self.bar_width = round( (self.width - self.SIDE_MARGIN) / len(self.array) ) # the width of each bar
        self.height_unit = math.floor((self.height - self.TOP_MARGIN) / (self.max - self.min)) # the height unit that will be multiplied by the element's value to calculate the height of the bar    
        self.start_x = self.SIDE_MARGIN // 2 # the x position where the drawing of the bars starts

def create_array(n, min, max):
    arr = []
    for i in range(n):
        arr.append(random.randint(min, max)) # append to the array a random integer betwen the min and max values
    return arr

def draw(window, algorithm_name, color_dict={}):
    '''
        This function draws the array to the screen after it was updated by one loop of the sorting algorithm,
        color_dict argument stores indexes that should be colored, 
        it changes with every iteration of the sorting algorithm.
    '''
    window.screen.fill(window.BG_COLOR) #in each drawing, first reset the screen by filling its bg color

    title = window.LARGE_FONT.render(f"{algorithm_name}", 1, window.BLACK)
    window.screen.blit(title, (window.width/2 - title.get_width()/2 , 5))
    
    reset = window.FONT.render("R - Press R to Reset", 1, window.BLACK)
    window.screen.blit(reset, (window.width/2 - reset.get_width()/2 , 45))
    space = window.FONT.render("P - Press P to Start", 1, window.BLACK)
    window.screen.blit(space, (window.width/2 - space.get_width()/2 , 80))
    sorts_1 = window.FONT.render("B - Bubble Sort | I - Insertion Sort | S - Selection Sort", 1, window.BLACK)
    window.screen.blit(sorts_1, (window.width/2 - sorts_1.get_width()/2 , 115))

    sorts_2 = window.FONT.render("M - Merge Sort | Q - Quick Sort | H - Heap Sort", 1, window.BLACK)
    window.screen.blit(sorts_2, (window.width/2 - sorts_2.get_width()/2 , 150))

    array = window.array
    n = len(array)

    for i in range(n):
        x = window.start_x + i * window.bar_width
        bar_height = (array[i] - window.min) * window.height_unit
        y = window.height - bar_height

        color = window.BLUE
        if i in color_dict:
            color = color_dict[i]
        pygame.draw.rect(window.screen, color, (x, y, window.bar_width, bar_height))
    pygame.display.update()

def bubble_sort(window, algorithm_name):
    array = window.array
    n = len(array)
    for i in range(n):
        for j in range(n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                draw(window, algorithm_name, {j: window.GREEN, j + 1: window.RED}) # when two elements have switched places in the array, draw the whole array again
                yield True # remember this is not a function, it is a generator: it returns an iterator
    return array



def main():
    run = True
    sorting = False
    n, min, max = 50, 0, 100
    array = create_array(n,  min, max)
    window = Window(800, 600, array)

    sorting_algorithm = bubble_sort
    algorithm_name = "Bubble Sort"
    sorting_algorithm_generator = None

    clock = pygame.time.Clock()
    draw(window, algorithm_name)

    while run:
        clock.tick(40) # this is the framerate: 40 frames per second

        if sorting:
            try:
                next(sorting_algorithm_generator)
            except StopIteration: # when an iterator ends it returns a StopIteration exception
                sorting = False
        else:
            draw(window, algorithm_name)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type != pygame.KEYDOWN:
                continue
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    # when resetting, the sorting stops, a new array is created, and attributed to window
                    sorting = False
                    array = create_array(n, min, max)
                    window.array = array
                    draw(window, algorithm_name)
                if event.key == pygame.K_p and not sorting:
                    sorting = True
                    sorting_algorithm_generator = sorting_algorithm(window, algorithm_name)
                if event.key == pygame.K_b and not sorting:
                    sorting_algorithm = bubble_sort
                    algorithm_name = "Bubble Sort"
                if event.key == pygame.K_i and not sorting:
                    algorithm_name = "Insertion Sort"
                if event.key == pygame.K_q and not sorting:
                    algorithm_name = "Quick Sort"
                if event.key == pygame.K_h and not sorting:
                    algorithm_name = "Heap Sort"
                if event.key == pygame.K_s and not sorting:
                    algorithm_name = "Selection Sort"

    pygame.quit()

if __name__ == '__main__':
    main()
