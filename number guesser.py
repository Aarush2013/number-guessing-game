import pygame
import sys
import random
import time
pygame.init()
screen_width = 1290
screen_height = 737
running=True

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pygame Basics")
background_color = ('black')
play_button=pygame.Rect(545,268.5,200,50)
exit_button=pygame.Rect(545,268.5+80,200,50)

def number_guessing_game():
    pygame.init()
    screen_width = 1290
    screen_height = 737

    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Pygame Basics")

    background_color = ('white')

    increase_button = pygame.Rect(150, 250, 100, 50)
    decrease_button = pygame.Rect(350, 250, 100, 50)
    submit_button = pygame.Rect(250, 320, 100, 50)

    font = pygame.font.Font(None, 32)

    rand_number = random.randint(1, 10)
    message = ("guess the number between 1 to 10")

    chances = 3
    user_guess = 1

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if increase_button.collidepoint(event.pos) and user_guess < 10:
                    user_guess += 1
                if decrease_button.collidepoint(event.pos) and user_guess > 1:
                    user_guess -= 1
                if submit_button.collidepoint(event.pos):
                    if chances > 0:
                        if user_guess == rand_number:
                            message = 'You Won!!!'
                        elif user_guess > rand_number:
                            message = 'Your guess is to high'
                            chances -= 1

                        elif user_guess < rand_number:
                            message = 'Your guess is too low'
                            chances -= 1

        if chances == 0 and user_guess != rand_number:
            message = f'You lose, The correct answer is {rand_number}'

            # time.sleep(5)
            #
            # running=False

        screen.fill(background_color)

        text1 = font.render('+', True, 'black')

        text2 = font.render('-', True, 'black')

        text3 = font.render('Submit', True, "black")

        game_text = font.render(message, True, 'black')
        screen.blit(game_text, (150, 150))

        guess_text = font.render(f'Your guess : {user_guess}', True, 'black')
        screen.blit(guess_text, (220, 180))

        chance_text = font.render(f'chances : {chances}', True, 'black')
        screen.blit(chance_text, (250, 100))

        pygame.draw.rect(screen, 'blue', increase_button, border_radius=20)
        pygame.draw.rect(screen, 'red', decrease_button, border_radius=20)
        pygame.draw.rect(screen, 'green', submit_button, border_radius=20)

        screen.blit(text1, (increase_button.x + 45, increase_button.y + 10))
        screen.blit(text2, (decrease_button.x + 45, decrease_button.y + 10))
        screen.blit(text3, (submit_button.x + 10, submit_button.y + 10))

        pygame.display.flip()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type==pygame.MOUSEBUTTONDOWN:
            if exit_button.collidepoint(event.pos):
                running=False
            if play_button.collidepoint(event.pos):
                print("play button was clicked")
                number_guessing_game()


    screen.fill(background_color)

    pygame.draw.rect(screen,'green',play_button,border_radius=20)
    pygame.draw.rect(screen,'red',exit_button,border_radius=20)
    font=pygame.font.Font(None,36)

    play_text=font.render("Play",True,'black')
    exit_text=font.render("Exit",True,'black')

    screen.blit(play_text,(play_button.x+75,play_button.y+10))
    screen.blit(exit_text, (exit_button.x+75, exit_button.y+10))

    pygame.display.flip()
