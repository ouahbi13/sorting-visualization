# from os import close
import pygame
import random
import math
pygame.init()



class Window:
    BLACK = 0, 0, 0
    BLUE = 52, 222, 235
    GREEN = 0, 255, 0
    RED = 255, 0, 0
    BG_COLOR = 255, 255, 255

    FONT = pygame.font.SysFont('Montserrat Thin', 30)
    LARGE_FONT = pygame.font.SysFont('Montserrat Thin', 40)

    SIDE_MARGIN = 140
    TOP_MARGIN = 170

    def __init__(self, width, height, array):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode( (width, height) )
        pygame.display.set_caption("Sorting Algorithms Visualization")
        
        self.array = array
        self.min = min(array)
        self.max = max(array)
        self.bar_width = round( (self.width - self.SIDE_MARGIN) / len(array) ) # The width of each bar
        self.height_unit = math.floor( (self.height - self.TOP_MARGIN) / (self.max - self.min) )
        self.start_x = self.SIDE_MARGIN // 2

def create_array(n, min, max):
    array = []
    for i in range(n):
        val = random.randint(min, max)
        array.append(val)
    return array

def draw(window,algorithm_name):
    window.screen.fill(window.BG_COLOR)

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


    
    draw_array(window)
    pygame.display.update()

def draw_array(window, color_dict = {}, clear_bg = False):
    array = window.array

    if clear_bg:
        clear_surface = (window.start_x, window.TOP_MARGIN,
                             window.width, window.height - window.TOP_MARGIN)
        pygame.draw.rect(window.screen, window.BG_COLOR , clear_surface)

    for i, val in enumerate(array):
        x = window.start_x + i * window.bar_width
        bar_height = (val - window.min) * window.height_unit
        y = window.height - bar_height

        color = window.BLUE

        if i in color_dict:
            color = color_dict[i]

        pygame.draw.rect(window.screen, color, (x, y, window.bar_width, bar_height))
    
    if clear_bg:
        pygame.display.update()

def bubble_sort(window, arr):
    array = window.array
    n = len(array)
    for i in range(n):
        for j in range(n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                draw_array(window, {j: window.GREEN, j + 1: window.RED}, True)
                yield True
    return array




def main():
    run = True
    clock = pygame.time.Clock() # Create an object to help track time
    
    n, min, max = 50, 0, 100
    array = create_array(n, min, max)
    window = Window(800, 600, array)

    sorting = False

    sorting_algorithm = bubble_sort
    algorithm_name = "Bubble Sort"
    sorting_algorithm_generator = None

    draw(window, algorithm_name)

    while run:
        clock.tick(40)
        if sorting:
            try:
                next(sorting_algorithm_generator)
            except StopIteration:
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
                    sorting = False
                    array = create_array(n, min, max)
                    window.array = array
                    draw(window, algorithm_name)
                if event.key == pygame.K_SPACE and not sorting:
                    sorting = True
                    sorting_algorithm_generator = sorting_algorithm(window, array)
                if event.key == pygame.K_b and not sorting:
                    sorting_algorithm = bubble_sort
                    algorithm_name = "Bubble Sort"
                if event.key == pygame.K_i and not sorting:
                    algorithm_name = "Insertion Sort"
                if event.key == pygame.K_s and not sorting:
                    algorithm_name = "Selection Sort"
                if event.key == pygame.K_m and not sorting:
                    algorithm_name = "Merge Sort"
                    # sorting_algorithm =  merge_sort
                if event.key == pygame.K_q and not sorting:
                    algorithm_name = "Quick Sort"
                if event.key == pygame.K_h and not sorting:
                    algorithm_name = "Heap Sort"
                
                  
    pygame.quit()



if __name__ == "__main__":
    main()








# def merge(window, arr, L, R):
#     i = j = k = 0
#     while i < len(L) and j < len(R):
#         if L[i] < R[j]:
#             arr[k] = L[i]
#             i += 1
#             # draw_array(window, {i: window.GREEN, k: window.RED}, True)
#             # yield True
#         else:
#             arr[k] = R[i]
#             j += 1
#             # draw_array(window, {j: window.GREEN, k: window.RED}, True)
#             # yield True
#         k += 1    
#     while j < len(R):
#         arr[k] = R[j]
#         j += 1
#         k += 1
#         # yield True
    
#     while i < len(L):
#         arr[k] = L[i]
#         i += 1
#         k += 1
#         # draw_array(window, {i: window.GREEN, k: window.RED}, True)
#         # yield True
#     # window.array = arr
#     yield True
#     # draw_array(window, {}, True)

# def merge_sort(window, arr):
#     # arr = window.array
#     n = len(arr)
#     if n > 1:
#         q =  n//2
#         L = arr[:q]
#         R = arr[q:]
#         draw_array(window, {}, True)
#         yield from merge_sort(window, L)
#         draw_array(window, {}, True)
#         yield from merge_sort(window, R)
#         draw_array(window, {}, True)
#         yield from merge(window, arr, L, R)
