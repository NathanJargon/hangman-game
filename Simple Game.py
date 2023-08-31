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
