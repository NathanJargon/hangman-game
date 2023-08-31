import pygame
import random
import string
import os
import sys
import time

pygame.init()

window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Hangman: Computer Science Edition by Nash")
start_time = None
keyboard_pressed = False
 
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

font = pygame.font.Font(None, 85)
timefont = pygame.font.Font(None, 25)
hint_font = pygame.font.Font(None, 35)
madefont = pygame.font.Font(None, 15)

word_hint_dict = {
    "hangman": "Hint: A word often associated with guessing games!",
    "pygame": "Hint: A popular library for creating games in Python!",
    "developer": "Hint: Someone who writes code to create software!",
    "algorithm": "Hint: A step-by-step procedure to solve a problem or perform a task!",
    "syntax": "Hint: The set of rules that dictate how code is written in a programming language!",
    "debugging": "Hint: The process of finding and fixing errors in code!",
    "variable": "Hint: A named container that stores data in a program!",
    "loop": "Hint: A control structure that repeats a block of code until a condition is met!",
    "function": "Hint: A reusable block of code that performs a specific task!",
    "boolean": "Hint: A data type representing true or false values!",
    "array": "Hint: A data structure that holds a collection of elements!",
    "string": "Hint: A sequence of characters, often used to represent text!",
    "class": "Hint: A blueprint for creating objects in object-oriented programming!",
    "inheritance": "Hint: A concept where a class inherits properties from another class!",
    "polymorphism": "Hint: The ability of objects to take on different forms based on context!",
    "database": "Hint: A structured collection of data stored on a computer!",
    "API": "Hint: A set of rules for building software applications and enabling interactions!",
    "git": "Hint: A distributed version control system for tracking code changes!",
    "IDE": "Hint: An Integrated Development Environment used for coding and testing!",
    "recursion": "Hint: A programming technique where a function calls itself to solve a problem!",
    "variable_scope": "Hint: The region where a variable is accessible in a program!",
    "abstraction": "Hint: The process of simplifying complex reality by modeling classes and objects!",
    "encapsulation": "Hint: The bundling of data and methods that operate on the data into a single unit!",
    "modularity": "Hint: The practice of breaking down a program into smaller, manageable components!",
    "namespace": "Hint: A container that holds a set of identifiers, preventing naming conflicts!",
    "thread": "Hint: A lightweight process that enables multitasking in a program!",
    "stack": "Hint: A data structure that follows the Last In First Out (LIFO) principle!",
    "queue": "Hint: A data structure that follows the First In First Out (FIFO) principle!",
    "hashing": "Hint: A technique to convert data into a fixed-size value, often used in dictionaries!",
    "exception": "Hint: An event that disrupts the normal flow of a program's execution!",
    "sorting": "Hint: The process of arranging elements in a specific order!",
    "searching": "Hint: The process of finding a specific element in a collection of data!",
    "compiler": "Hint: A software that translates high-level programming code into machine code!",
    "interpreter": "Hint: A program that directly executes high-level programming code line by line!",
    "CPU": "Hint: The Central Processing Unit, the \"brain\" of a computer that executes instructions!",
    "memory": "Hint: The storage area where data and instructions are stored during program execution!",
}

def generate_random_word():
    return random.choice(list(word_hint_dict.keys()))

word_to_guess = generate_random_word()
guessed_letters = []
points = 0
health = 5 

def draw_health_bar(health):
    health_bar_width = 150
    health_bar_height = 20
    x = (window_width - health_bar_width) // 2
    y = 10
    pygame.draw.rect(window, red, (x, y, health_bar_width * health / 5, health_bar_height))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.unicode.isalpha():
                if event.unicode.lower() not in guessed_letters:
                    guessed_letters.append(event.unicode.lower())
                    if event.unicode.lower() not in word_to_guess:
                        health -= 1

    if start_time is None:
        start_time = pygame.time.get_ticks()

    elapsed_time = (pygame.time.get_ticks() - start_time) // 1000

    window.fill(black)

    timer_text = timefont.render(f"Time: {elapsed_time} seconds", True, white)
    window.blit(timer_text, (10, 10))

    point_text = timefont.render(f"Points: {points}", True, white)
    window.blit(point_text, (window_width-100, 10))

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

    if health <= 0:
        points = 0
        health = 5
        word_to_guess = generate_random_word()
        guessed_letters = []

    text = font.render(display_word, True, white)
    text_x = (window_width - text.get_width()) / 2
    text_y = (window_height - text.get_height()) / 2
    window.blit(text, (text_x, text_y))

    hint_text = hint_font.render(word_hint_dict.get(word_to_guess, "Hint: No hint available"), True, white)
    hint_max_width = window_width - 40 
    if hint_text.get_width() > hint_max_width:
        hint_text = pygame.transform.scale(hint_text, (hint_max_width, hint_text.get_height()))
    hint_x = (window_width - hint_text.get_width()) / 2
    hint_y = text_y + text.get_height() + 20 
    window.blit(hint_text, (hint_x, hint_y))

    pygame.display.flip()

pygame.quit()
sys.exit()
