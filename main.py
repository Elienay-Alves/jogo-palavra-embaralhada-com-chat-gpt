"""
Aqui é onde fica a lógica de interação com player:
Isso com certeza será melhorado com o tempo.

Para jogar digite: python3 game.py
"""
import src.setup

if __name__ == "__main__":
    choosed_word, shuffled_word = src.setup.shuffled(src.setup.WORDS)
    print(f"A palavra é: {shuffled_word}")
    user_guesses = src.setup.guesses()
    src.setup.game_result(choosed_word, user_guesses)
