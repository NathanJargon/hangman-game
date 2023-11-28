"""
Copyright 2023 Synochrina 

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), 
to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, 
and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER 
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS 
IN THE SOFTWARE.
"""

import pygame
import random
import string
import os
import sys
import time

pygame.init()

width = 800
height = 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Hangman: Computer Science Edition by Nash")
start_time = None
keyboard_pressed = False
 
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

font = pygame.font.Font(None, 55)
timefont = pygame.font.Font(None, 25)
hint_font = pygame.font.Font(None, 32)
madefont = pygame.font.Font(None, 15)
text = font.render("Press Anything to Start Playing", True, (255, 255, 255))

word_hint_dict = {
    "cryptography": "Hint: The science of keeping information secure",
    "pygame": "Hint: A popular library for creating games in Python!",
    "systems_architect": "Hint: Computer systems analysts, creates the hardware, software, and network systems.",
    "depth_first_search": "Hint: An algorithm for traversing or searching tree or graph data structures.",
    "brent's_algorithm": "Hint: An algorithm that finds a cycle in function value iterations using only two iterators.",
    "dijkstra's_algorithm": "Hint: An algorithm that computes shortest paths in a graph with non-negative edge weights.",
    "greedy_algorithm": "Hint: It is an algorithm that picks the best immediate choice and never reconsiders its choices.",
    "scratch": "Hint: A programming language and website aimed primarily at children as an educational tool.",
    "algorithm": "Hint: A step-by-step procedure to solve a problem or perform a task!",
    "debugging": "Hint: The process of finding and fixing errors in code!",
    "variable": "Hint: A named container that stores data in a program!",
    "function": "Hint: A reusable block of code that performs a specific task!",
    "boolean": "Hint: A data type representing true or false values!",
    "inheritance": "Hint: A concept where a class inherits properties from another class!",
    "polymorphism": "Hint: The ability of objects to take on different forms based on context!",
    "database": "Hint: A structured collection of data stored on a computer!",
    "encryption": "Hint: The process of transforming plaintext into coded, unintelligible text for secure storage.",
    "recursion": "Hint: A programming technique where a function calls itself to solve a problem!",
    "variable_scope": "Hint: The region where a variable is accessible in a program!",
    "abstraction": "Hint: The process of simplifying complex reality by modeling classes and objects!",
    "encapsulation": "Hint: The bundling of data and methods that operate on the data into a single unit!",
    "modularity": "Hint: The practice of breaking down a program into smaller, manageable components!",
    "namespace": "Hint: A container that holds a set of identifiers, preventing naming conflicts!",
    "thread": "Hint: A lightweight process that enables multitasking in a program!",
    "stack_data": "Hint: A data structure that follows the Last In First Out (LIFO) principle!",
    "queue_data": "Hint: A data structure that follows the First In First Out (FIFO) principle!",
    "hashing": "Hint: A technique to convert data into a fixed-size value, often used in dictionaries!",
    "exception": "Hint: An event that disrupts the normal flow of a program's execution!",
    "compiler": "Hint: A software that translates high-level programming code into machine code!",
    "interpreter": "Hint: A program that directly executes high-level programming code line by line!",
    "ciphertext": "Hint: The text in its encrypted form.",
    "substitution_cipher": "Hint: A cipher in which one letter is consistently substituted for another. The ROT13 cipher are examples.",
    "binary_search": "Hint: A search algorithm that finds the position of a target value within a sorted array.",
    "merge_sort": "Hint: An efficient, general-purpose, and comparison-based sorting algorithm.",
    "bubble_sort": "Hint: An algorithm that is based on a repeated swap between adjacent elements if they are in wrong order.",
    "selection_sort": "Hint: An algorithm that works by taking the smallest element in an unsorted array and bringing it to the front.",
    "counting_sort": "Hint: An algorithm for sorting a collection of objects according to keys that are small positive integers.",
    "breadth_first_search": "Hint: An algorithm for searching a tree data structure for a node that satisfies a given property.", 
    "bucket_sort": "Hint: A sorting algorithm that works by distributing the elements of an array into a number of buckets.",
    "computing_systems": "Hint: A set of integrated devices that input, output, process, and store data and information.",
}

def generate_random_word():
    return random.choice(list(word_hint_dict.keys()))

word_to_guess = generate_random_word()
guessed_letters = []
points = 0
health = 10 
game_time_limit = 120

def draw_health_bar(health):
    health_bar_width = 150
    health_bar_height = 20
    x = (width - health_bar_width) // 2
    y = 10
    pygame.draw.rect(window, red, (x-60, y, health_bar_width * health / 5, health_bar_height))

running = True 
game = False 

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type in (pygame.KEYDOWN, pygame.MOUSEBUTTONDOWN):
            game = True
            running = False
            start_time = pygame.time.get_ticks()

    window.fill((0, 0, 0))
    window.blit(text, ((width / 2) - 235, (height / 2) - 25))

    pygame.display.flip()


while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        elif event.type == pygame.KEYDOWN:
            if event.unicode.isalpha():
                if event.unicode.lower() not in guessed_letters:
                    guessed_letters.append(event.unicode.lower())
                    if event.unicode.lower() not in word_to_guess:
                        health -= 1
    
    
    elapsed_time = (pygame.time.get_ticks() - start_time) // 1000

    if elapsed_time >= game_time_limit:
        game = False


    window.fill(black)

    timer_text = timefont.render(f"Time: {elapsed_time} seconds", True, white)
    window.blit(timer_text, (10, 10))

    point_text = timefont.render(f"Points: {points}", True, white)
    window.blit(point_text, (width-100, 10))


    made_by = madefont.render(f"Made by Nash Andrew Bondoc", True, white)
    window.blit(made_by, (10, 580))

    draw_health_bar(health) 

    display_word = ""
    for letter in word_to_guess:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    if word_to_guess == display_word.replace(" ", ""):
        points += 5
        word_to_guess = generate_random_word()
        guessed_letters = []
        game_time_limit = max(0, game_time_limit - 15)

    if health <= 0:
        points = 0
        health = 10
        word_to_guess = generate_random_word()
        guessed_letters = []
        start_time = pygame.time.get_ticks()

    text = font.render(display_word, True, white)
    text_x = (width - text.get_width()) / 2
    text_y = (height - text.get_height()) / 2
    window.blit(text, (text_x, text_y))

    health_text = timefont.render(f"{health}", True, white)
    window.blit(health_text, (width/2, 12))

    hint_text = hint_font.render(word_hint_dict.get(word_to_guess, "Hint: No hint available"), True, white)
    hint_max_width = width - 40 
    if hint_text.get_width() > hint_max_width:
        hint_text = pygame.transform.scale(hint_text, (hint_max_width, hint_text.get_height()))
    hint_x = (width - hint_text.get_width()) / 2
    hint_y = text_y + text.get_height() + 20 
    window.blit(hint_text, (hint_x, hint_y))

    pygame.display.flip()

pygame.quit()
sys.exit()
