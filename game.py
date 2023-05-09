"""
Aqui é onde fica a lógica de interação com player:
Isso com certeza será melhorado com o tempo.

Para jogar digite: python3 game.py
"""
import main

if __name__ == "__main__":
    choosed_word, shuffled_word = main.shuffled(main.WORDS)
    print(f"A palavra é: {shuffled_word}")
    user_guesses = main.guesses()
    main.game_result(choosed_word, user_guesses)
