"""
A partir desse estágio tive a idéia de fazer um game usando IA. No momemto da
aplicação temos um código que recebe uma lista de palavras, escolhe uma dentre
elas e embaralha.

O jogador tem 3 chances de acerto, após essas 3 chances ele perde.

A idéia é alimentar essas palavras com o chat gpt para ele trazer essas
palavras e interagir com o jogador, dependendo sas respostas ele será legal ou
não com o player e a dificuldade vai almentar conforme o player for acertando.
Após essa etapa vai entrar um front-end para o jogo ficar mais intuitivo e
legal.

Esse é um projeto para brincar com o potencial da IA no aprendizado de uma
nova linguagem
"""

import random


WORDS = ["Fone", "monitor", "teclado", "mouse"]
MAX = 3


def shuffled(word: list[str]) -> str:
    """
    Escolhe uma palavra na lista para embaralhar e retorna duas variaveis,
    uma contendo a palavra escolhida normal e outra embaralhada
    """
    choosed_word = random.choice(word)
    shuffled_word = "".join(random.sample(choosed_word, len(choosed_word)))

    return choosed_word, shuffled_word


def guesses() -> str:
    """
    Cria uma lista vazia e adiciona as tentativas do usuario e retorna essa
    lista
    """
    user_guesses = []

    for _ in range(MAX):
        guess = input("Adivinhe a palavra: ")
        user_guesses.append(guess)

    return user_guesses


def game_result(choosed_word: str, user_guesses: str):
    """
    compara a lista com as respostas do usuario e se alguma das respostas
    estiver correta diz se ele acertou ou errou no game
    """
    if choosed_word in user_guesses:
        print(f"Você acertou! Parabéns, a palavra é {choosed_word}!")
    else:
        print(f"Você perdeu. A palavra certa é: { choosed_word}")
