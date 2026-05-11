# Minigame Medley
#### Video Demo:  <URL HERE>
#### Description:
```
    This is Minigame Medley. It supports three different games: rock, paper, scissors, flappy duck, and a guessing game. The first thing it does is import the libraries system, pygame, and random. After that, the main function calls for input stored in a variable called "game". Then, it checks to see if the variable "game" equals the following: "a", "b", "c" or "d". If "game" does not equal "a", "b", "c", or "d", it re-prompts the user.

    If the user types in "a" for the "game" input, the program loads up the rock, paper, scissors game in a function called rock_paper_scissors(). After that, the computer tells the user to input rock, paper, or scissors. Using the random module, the computer uses random.shuffle and chooses what is at the index. Then, it will check if the computer beat the user or the user beat the computer.

    If you type the letter “b”, it will take you to the guessing game. Then, it will prompt you for a level stored in a variable called “level”. If the user inputs text that is not an integer or the integer is not greater than 1, it will re-prompt the user. If the user correctly inputs a number, it will ask for a number between 1 and the level number for the user to guess stored in a variable called “guess”. If the guess is correct, the computer will print out “Correct!” If the guess is lower than the correct answer, it will print out “Too low!” and re-prompt the user. If the guess is higher than the correct answer, it will print out “Too high!” and re-prompt the user. If the guess is not a number, It will re-prompt the user.

    If you type the letter “c”, it will take you to the flappy duck. Flappy duck is started with pygame.init to initialize the game. Then, it loads the images and hitboxes and will set its position. After that, in a loop, is where the game is initialized. Everything except the duck begins to travel x-1. If you click w, space, or the up arrow, you will jump. If you hit a pipe you will die. If you die and press r, the score resets and the game restarts. To stop playing, you have to x out the window.

    If you type the letter "d", it will exit the program with code 0. Overall, minigame medley is a collection of games you can play offline, at the park, or anywhere else.


```
