
import random

# 게임에 단어 리스트
words = ["apple", "banana", "orange", "grape", "lemon"]

# 게임 기반 그림
hangman_pics = [
    """
     ------
     |    |
     |
     |
     |
     |
    ---""",
    """
     ------
     |    |
     |    O
     |
     |
     |
    ---""",
    """
     ------
     |    |
     |    O
     |    |
     |
     |
    ---""",
    """
     ------
     |    |
     |    O
     |   /|
     |
     |
    ---""",
    """
     ------
     |    |
     |    O
     |   /|\\
     |
     |
    ---""",
    """
     ------
     |    |
     |    O
     |   /|\\
     |   /
     |
    ---""",
    """
     ------
     |    |
     |    O
     |   /|\\
     |   / \\
     |
    ---""",
]


class HangmanGame:
    def __init__(self):
        self.word = random.choice(words) 
        self.guessed_word = ["_"] * len(self.word) 
        self.attempts = 10

    def display(self):
        print(" ".join(self.guessed_word)) 
    
    def play(self):
        print("행맨 게임을 시작합니다")
        self.display()

        while self.attempts > 0: 
            guess = input("알파벳 하나를 입력하세요: ").lower() 
            while len(guess) != 1: 
                print("잘못된 입력입니다. 한 글자만 입력하세요.")
                guess = input("알파벳 하나를 입력하세요: ").lower() 

            if guess in self.word:                 
                for idx, letter in enumerate(self.word): 
                        self.guessed_word[idx] = guess 
                if "_" not in self.guessed_word: 
                    break
                print("단어를 맞추셨군요. 더 힘내봐요!")
            else: 
                self.attempts -= 1 
                print(f"틀렸습니다. 남은 시도 횟수: {self.attempts}")
                print(hangman_pics[6 - self.attempts]) 
            self.display()

        if "_" not in self.guessed_word: 
            print(f"축하합니다! 단어를 맞추셨습니다: {self.word}")
        else: 
            print(f"끝났습니다. 정답은 {self.word}였습니다.")

if __name__ == "__main__":
    game = HangmanGame()
    game.play()