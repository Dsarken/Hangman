import random
import time


def word_list_choice(difficulty):
    # Easy level word list with letters of length 3 to 5
    if difficulty == 1:
        easy_word_list = [
            "mux",
            "vex",
            "vox",
            "kex",
            "wax",
            "zag",
            "zebra",
            "fox",
            "fund",
            "ford",
            "base",
            "bear",
            "army",
            "area",
            "blue",
            "jazzy",
            "haji",
            "buzzy",
            "pizza",
            "pzazz",
        ]
        return random.choice(easy_word_list)
    # Medium level word list with letters of length 6 to 8
    if difficulty == 2:
        medium_word_list = [
            "august",
            "battle",
            "camera",
            "bishop",
            "behind",
            "engage",
            "eighth",
            "whizzes",
            "jumbuck",
            "puzzle",
            "quizzing",
            "whizzier",
            "buzzbomb",
            "mosses",
            "guzzle",
            "zigzag",
            "jawbox",
            "whizzo",
            "nozzle",
            "quacky",
        ]
        return random.choice(medium_word_list)
    # Hard level word list with letters of length 10 to 12
    if difficulty == 3:
        hard_word_list = [
            "archetypes",
            "distressed",
            "unfriendly",
            "monophonic",
            "injunctive",
            "kyrgyzstan",
            "permissive",
            "recordable",
            "manuscript",
            "wilderness",
            "loudspeaker",
            "criticality",
            "deliverance",
            "empowerment",
            "collectible",
            "subsidiaries",
            "aerodynamics",
            "cosmopolitan",
            "distillation",
        ]
        return random.choice(hard_word_list)
    # Nightmare word list with letters of length 15 to 20:
    if difficulty == 4:
        nightmare_word_list = [
            "telecommunications",
            "crystallization",
            "implementations",
            "apprenticeships",
            "interoperability",
            "administrations",
            "developmentally",
            "psychopathology",
            "professionalism",
            "autocorrelation",
            "videoconferencing",
            "microcontrollers",
            "fundamentalists",
            "misunderstandings",
            "congratulations",
            "pharmaceuticals",
            "interdisciplinary",
            "environmentalists",
            "synchronization",
            "misunderstanding",
        ]
        return random.choice(nightmare_word_list)


def hangman_pieces(guesses_left):
    if guesses_left == 6:
        level1 = """
             _______
            |/      |
            |
            |
            |
            |
            |
        jgs_|___
        """
        return level1
    if guesses_left == 5:
        level2 = """
             _______
            |/      |
            |       |
            |
            |
            |
            |
        jgs_|___
        """
        return level2
    if guesses_left == 4:
        level3 = """
             _______
            |/      |
            |       |
            |      (_)
            |
            |
            |
        jgs_|___
        """
        return level3
    if guesses_left == 3:
        level4 = """
             _______
            |/      |
            |       |
            |      (_)
            |      \|/
            |
            |
        jgs_|___
        """
        return level4
    if guesses_left == 2:
        level5 = """
             _______
            |/      |
            |       |
            |      (_)
            |      \|/
            |       |
            |
        jgs_|___
        """
        return level5
    if guesses_left == 1:
        level6 = """
             _______
            |/      |
            |       |
            |      (_)
            |      \|/
            |       |
            |      / \\
        jgs_|___
        """
        return level6


def win_loss_tracker(win_loss):
    if win_loss == "win":
        wins = 0
        wins += 1
        return wins
    if win_loss == "loss":
        losses = 0
        losses += 1
        return losses


def main():
    # Variable for player choice and to store new encrypted word in
    global choice
    global guesses
    encrypted_word = ""
    play_again = ""

    while True:
        winning = 0
        losing = 0

        print(
            "-------------------------------------------------------------------------------------------------"
        )
        print(
            "| This is a game of Hangman, the computer will randomly select a word and you have to guess     |"
        )
        print(
            "| each letter, for every incorrectly guessed letter a body part will be drawn if the user types |"
        )
        print(
            "| the correct word then they will win the game instantly. You have 6 guesses                    |"
        )
        print(
            "-------------------------------------------------------------------------------------------------"
        )
        print()
        print("Choose your difficulty:")
        print("1. Easy: Three to 5 letter words")
        print("2. Medium: 6 to 8 letter words")
        print("3. Hard: 10 to 12 letter words")
        print("4. Nightmare: 15 to 20 letter words")
        print()
        while True:
            print("Enter your choice")
            try:
                choice = int(input("> "))
                break
            except ValueError:
                print("Please enter a number to make your choice.")
        stored_word = word_list_choice(choice)
        for _ in stored_word:
            encrypted_word += "_"
        guesses = 6
        while True:
            print(f"Current Wins: {winning}\tCurrent Losses: {losing}")
            print(hangman_pieces(guesses))
            print("==================================================")
            print(f"I am thinking of a {len(stored_word)} letter word")
            print(f"You have {guesses} guesses left")
            for dash in encrypted_word:
                print(dash + " ", end="")
            print("\n")
            while True:

                try:
                    your_guess = input("Enter a letter: ")
                    if your_guess.isalpha():
                        if len(your_guess) == 1:
                            break
                        elif len(your_guess) == len(stored_word):
                            break
                        else:
                            print("Please enter a single letter or the whole word")
                    else:
                        print("Please enter a letter or the whole word")
                except ValueError:
                    print("Please enter a single letter or the whole word")
            if your_guess == stored_word:
                print("You guessed the word correctly!")
                print("You Won!")
                print("Do you want to play again(y or n)? ")
                play_again = input("> ")
                if play_again == "y":
                    encrypted_word = ""
                    for _ in stored_word:
                        encrypted_word += "_"
                    continue

                if play_again == "n":
                    print("Thank you for playing!")
                    exit(0)

            elif your_guess in stored_word:
                print("Correct guess")
                time.sleep(1)
                for index, letter in enumerate(stored_word):
                    for index2, letter2 in enumerate(encrypted_word):
                        if your_guess == letter:
                            if index == index2:
                                encrypted_word = (
                                        encrypted_word[:index2]
                                        + your_guess
                                        + encrypted_word[index2 + 1:]
                                )
                                if encrypted_word == stored_word:
                                    print(
                                        "Congratulations you guessed all the letters correctly!"
                                    )
                                    winning += win_loss_tracker("win")
                                    print("Do you want to play again(y or n)? ")
                                    play_again = input("> ")
                                    if play_again == "y":
                                        encrypted_word = ""
                                        for _ in stored_word:
                                            encrypted_word += "_"
                                        stored_word = word_list_choice(choice)
                                        continue
                                    if play_again == "n":
                                        print("Thank you for playing!")
                                        exit(0)
            elif your_guess not in stored_word:
                guesses -= 1
                print("Incorrect guess")
                time.sleep(1)
                if guesses == 0:
                    print("Sorry you ran out of guesses and died!")
                    losing += win_loss_tracker("loss")
                    print("Do you want to play again(y or n)? ")
                    play_again = input("> ")
                    encrypted_word = ""
                    for _ in stored_word:
                        encrypted_word += "_"
                    if play_again == "y":
                        stored_word = word_list_choice(choice)
                        guesses = 6
                        continue
                    if play_again == "n":
                        print("Thank you for playing!")
                        exit(0)
                    guesses = 6


if __name__ == "__main__":
    main()
