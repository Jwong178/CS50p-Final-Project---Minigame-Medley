#Minigame Medley

import sys
import random
import pygame

def main():
    while True:
        print()
        game = input("What game do you want to play (a - Rock, paper, scissors, b - guessing game, c - flappy duck, or d - quit)? ").strip().lower()
        if game == "a":
            object = input("Rock, paper, or scissors? ").strip().lower().capitalize()
            rock_paper_scissors(object)
        elif game == "b":
            guessing_game()
        elif game == "c":
            flappy_duck()
        elif game == "d":
            print()
            sys.exit()
        else:
            print()
            print("Invalid game")

def rock_paper_scissors(i):
    print()
    while True:
        ai_selection = ["Rock", "Paper", "Scissors"]
        random.shuffle(ai_selection)
        print()
        print(f"Jerry picked: {ai_selection[0]}")
        print()
        if ai_selection[0] == "Rock" and i == "Paper":
            print("You(paper) beat Jerry(rock).")
            break
        elif ai_selection[0] == "Scissors" and i == "Rock":
            print("You(rock) beat Jerry(scissors).")
            break
        elif ai_selection[0] == "Paper" and i == "Scissors":
            print("You(scissors) beat Jerry(paper).")
            break
        elif ai_selection[0] == "Scissors" and i == "Paper":
            print("Jerry(scissors) beat you(paper).")
            break
        elif ai_selection[0] == "Paper" and i == "Rock":
            print("Jerry(paper) beat you(rock).")
            break
        elif ai_selection[0] == "Rock" and i == "Scissors":
            print("Jerry(rock) beat you(scissors).")
            break
        elif ai_selection[0] == i:
            print("Tie!")
            break
        else:
            print(f"Make sure you input rock, paper or scissors, not {i}")
            print()

def flappy_duck():
    pygame.init()

    font = pygame.font.Font(None, 100)
    font2 = pygame.font.Font(None, 40)
    font3 = pygame.font.Font(None, 60)

    def display_score():
        current_time = int(pygame.time.get_ticks() / 100) - start_time
        score_text = font3.render(f"Score: {current_time}", False, "black")
        score_text_rect = score_text.get_rect(bottomleft=(0, 600))
        pygame.draw.rect(screen, "skyblue", score_text_rect, False, 10)
        screen.blit(score_text, score_text_rect)

    start_time = 0
    game_over_text = font.render("You Died!", False, "black")
    game_over_text_rect = game_over_text.get_rect(center=(500, 400))

    r_text = font2.render('Click "r" to restart', False, "black")
    r_text_rect = r_text.get_rect(center=(500, 500))

    screen = pygame.display.set_mode((1000, 600))
    clock = pygame.time.Clock()
    running = True
    pygame.display.set_caption("Flappy Duck")

    ground = pygame.image.load("ground.png").convert()
    ground_x = -400
    ground2_x = 0
    ground3_x = 400
    ground4_x = 800
    ground5_x = 1200

    duck_picture = pygame.image.load("duck_2.png").convert_alpha()
    flip_duck = pygame.transform.flip(duck_picture, True, False)
    duck = pygame.transform.scale(flip_duck, (50, 50))
    duck_rect = duck.get_rect(midbottom=(500, 915))
    duck_gravity = 0

    duck_end = pygame.transform.scale(flip_duck, (200, 200))
    duck_end_rect = duck_end.get_rect(center=(500, 200))

    pipe_picture = pygame.image.load("pipe.png").convert_alpha()
    pipe_rotation = pygame.transform.scale(pipe_picture, (75, 500))
    pipe = pygame.transform.flip(pipe_rotation, False, True)

    pipe_rect = pipe.get_rect(bottomright=(800, 915))
    pipe_rect2 = pipe.get_rect(bottomright=(1200, 915))
    pipe_rect3 = pipe.get_rect(bottomright=(1600, 915))
    pipe_rect4 = pipe.get_rect(bottomright=(2000, 915))
    pipe_rect5 = pipe.get_rect(bottomright=(2400, 915))

    down_pipe = pipe_rotation

    down_pipe_rect = down_pipe.get_rect(topright=(800, 915))
    down_pipe_rect2 = down_pipe.get_rect(topright=(1200, 915))
    down_pipe_rect3 = down_pipe.get_rect(topright=(1600, 915))
    down_pipe_rect4 = down_pipe.get_rect(topright=(2000, 915))
    down_pipe_rect5 = down_pipe.get_rect(topright=(2400, 915))

    pipe_rect.y = random.randint(-500, -200)
    down_pipe_rect.y = pipe_rect.y + 700

    pipe_rect2.y = random.randint(-500, -200)
    down_pipe_rect2.y = pipe_rect2.y + 700

    pipe_rect3.y = random.randint(-500, -200)
    down_pipe_rect3.y = pipe_rect3.y + 700

    pipe_rect4.y = random.randint(-500, -200)
    down_pipe_rect4.y = pipe_rect4.y + 700

    pipe_rect5.y = random.randint(-500, -200)
    down_pipe_rect5.y = pipe_rect5.y + 700

    game_active = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            keys = pygame.key.get_pressed()

            if game_active == True:
                if event.type == pygame.KEYDOWN:
                    if keys[pygame.K_UP] or keys[pygame.K_SPACE] or keys[pygame.K_w]:
                        duck_gravity = -7
                        pygame.mixer.init()
                        jump_sound = pygame.mixer.Sound("bird_flap.mp3")
                        jump_sound.play()
                        pygame.mixer.stop

        if game_active == True:
            clock.tick(60)
            screen.fill("skyblue")

            screen.blit(ground, (ground_x, 515))
            screen.blit(ground, (ground2_x, 515))
            screen.blit(ground, (ground3_x, 515))
            screen.blit(ground, (ground4_x, 515))
            screen.blit(ground, (ground5_x, 515))

            if ground_x < -400:
                ground_x = 1200

            if ground2_x < -400:
                ground2_x = 1200

            if ground3_x < -400:
                ground3_x = 1200

            if ground4_x < -400:
                ground4_x = 1200

            screen.blit(duck, duck_rect)

            if duck_rect.colliderect(pipe_rect):
                game_active = False
            elif duck_rect.colliderect(down_pipe_rect):
                game_active = False
            elif duck_rect.colliderect(pipe_rect2):
                game_active = False
            elif duck_rect.colliderect(down_pipe_rect2):
                game_active = False
            elif duck_rect.colliderect(pipe_rect3):
                game_active = False
            elif duck_rect.colliderect(down_pipe_rect3):
                game_active = False
            elif duck_rect.colliderect(pipe_rect4):
                game_active = False
            elif duck_rect.colliderect(down_pipe_rect4):
                game_active = False
            elif duck_rect.colliderect(pipe_rect5):
                game_active = False
            elif duck_rect.colliderect(down_pipe_rect5):
                game_active = False
            else:
                ground_x -= 1
                ground2_x -= 1
                ground3_x -= 1
                ground4_x -= 1
                ground5_x -= 1
                pipe_rect.x -= 1
                down_pipe_rect.x -= 1
                pipe_rect2.x -= 1
                down_pipe_rect2.x -= 1
                pipe_rect3.x -= 1
                down_pipe_rect3.x -= 1
                pipe_rect4.x -= 1
                down_pipe_rect4.x -= 1
                pipe_rect5.x -= 1
                down_pipe_rect5.x -= 1
                duck_gravity += 0.55
                duck_rect.y += duck_gravity

                if pipe_rect.x <= 0:
                    pipe_rect.x = 2000
                    pipe_rect.y = random.randint(-500, -200)
                elif down_pipe_rect.x <= 0:
                    down_pipe_rect.x = 2000
                    down_pipe_rect.y = pipe_rect.y + 700

                if pipe_rect2.x <= 0:
                    pipe_rect2.x = 2000
                    pipe_rect2.y = random.randint(-500, -200)
                elif down_pipe_rect2.x <= 0:
                    down_pipe_rect2.x = 2000
                    down_pipe_rect2.y = pipe_rect2.y + 700

                if pipe_rect3.x <= 0:
                    pipe_rect3.x = 2000
                    pipe_rect3.y = random.randint(-500, -200)
                elif down_pipe_rect3.x <= 0:
                    down_pipe_rect3.x = 2000
                    down_pipe_rect3.y = pipe_rect3.y + 700

                if pipe_rect4.x <= 0:
                    pipe_rect4.x = 2000
                    pipe_rect4.y = random.randint(-500, -200)
                elif down_pipe_rect4.x <= 0:
                    down_pipe_rect4.x = 2000
                    down_pipe_rect4.y = pipe_rect4.y + 700

                if pipe_rect5.x <= 0:
                    pipe_rect5.x = 2000
                    pipe_rect5.y = random.randint(-500, -200)
                elif down_pipe_rect5.x <= 0:
                    down_pipe_rect5.x = 2000
                    down_pipe_rect5.y = pipe_rect5.y + 700

                if duck_rect.bottom >= 515:
                    duck_rect.bottom = 515
                if duck_rect.top <= 0:
                    duck_rect.top = 0

                screen.blit(pipe, pipe_rect)
                screen.blit(down_pipe, down_pipe_rect)
                screen.blit(pipe, pipe_rect2)
                screen.blit(down_pipe, down_pipe_rect2)
                screen.blit(pipe, pipe_rect3)
                screen.blit(down_pipe, down_pipe_rect3)
                screen.blit(pipe, pipe_rect4)
                screen.blit(down_pipe, down_pipe_rect4)
                screen.blit(pipe, pipe_rect5)
                screen.blit(down_pipe, down_pipe_rect5)

                display_score()

                pygame.display.update()

        if game_active == False:
            screen.fill("cornflowerblue")
            screen.blit(duck_end, duck_end_rect)
            screen.blit(game_over_text, game_over_text_rect)
            screen.blit(r_text, r_text_rect)
            if keys[pygame.K_r]:
                print("hello")
                pipe_rect.y = random.randint(-500, -200)
                down_pipe_rect.y = pipe_rect.y + 700

                pipe_rect2.y = random.randint(-500, -200)
                down_pipe_rect2.y = pipe_rect2.y + 700

                pipe_rect3.y = random.randint(-500, -200)
                down_pipe_rect3.y = pipe_rect3.y + 700

                pipe_rect4.y = random.randint(-500, -200)
                down_pipe_rect4.y = pipe_rect4.y + 700

                pipe_rect5.y = random.randint(-500, -200)
                down_pipe_rect5.y = pipe_rect5.y + 700

                pipe_rect.x = 800
                pipe_rect2.x = 1200
                pipe_rect3.x = 1600
                pipe_rect4.x = 2000
                pipe_rect5.x = 2400
                down_pipe_rect.x = 800
                down_pipe_rect2.x = 1200
                down_pipe_rect3.x = 1600
                down_pipe_rect4.x = 2000
                down_pipe_rect5.x = 2400
                game_active = True
                start_time = int(pygame.time.get_ticks() / 100)

        pygame.display.update()

    pygame.quit()

def guessing_game():
    while True:
        try:
            print()
            level = int(input("Level: "))
            number = random.randrange(1, level)
            while True:
                try:
                    print()
                    guess = int(input(f"I am thinking of a number between 1 and {level}: ").strip())
                    if guess == number:
                        print()
                        print("Correct!")
                        main()
                    elif guess > number:
                        print()
                        print("Too big!")
                    elif guess < number:
                        print()
                        print("Too small!")
                except ValueError:
                    print()
                    print("Must be an integer!")
        except ValueError or number < 2:
            print()
            print("Must be an integer and greater than 1")

if __name__ == "__main__":
    main()
