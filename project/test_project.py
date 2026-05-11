from project import guessing_game
from project import flappy_duck
from project import rock_paper_scissors
from unittest.mock import Mock, patch

def main():
    test_guessing_game()
    test_flappy_duck()
    test_rock_paper_scissors()

def test_guessing_game():
    assert guessing_game()

def test_flappy_duck():
    assert flappy_duck()

def test_rock_paper_scissors():
    assert rock_paper_scissors()

if __name__ == "__main__":
    main()
