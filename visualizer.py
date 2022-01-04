import pygame
import math
import random
pygame.init()

class Window:

    BG_COLOR = 255, 255, 255
    BLACK = 0, 0, 0
    BLUE = 0, 100, 150
    RED = 255, 0, 0
    GREEN = 0, 255, 0

    SIDE_MARGIN = 140
    TOP_MARGIN = 200

    def __init__(self, width, height, array):
        self.array = array
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))

        self.min =  min(array)
        self.max = max(array)
        self.bar_width = round( (self.width - self.SIDE_MARGIN) / len(self.array) )
        self.height_unit = math.floor((self.height - self.TOP_MARGIN) / (self.max - self.min))       
        self.start_x = self.SIDE_MARGIN // 2

def create_array(n, min, max):
    arr = []
    for i in range(n):
        arr.append(random.randint(min, max))
    return arr

def draw(window, color_dict={}):
    window.screen.fill(window.BG_COLOR)

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

def bubble_sort(window, arr):
    array = window.array
    n = len(array)
    for i in range(n):
        for j in range(n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                draw(window, {j: window.GREEN, j + 1: window.RED}, True)
                yield True
    return array

def main():
    run = True
    n, min, max = 50, 0, 100
    array = create_array(n,  min, max)
    window = Window(800, 600, array)

    clock = pygame.time.Clock()
    draw(window)

    while run:
        clock.tick(40)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    array = create_array(n, min, max)
                    window.array = array
                    draw(window)
    pygame.quit()

if __name__ == '__main__':
    main()