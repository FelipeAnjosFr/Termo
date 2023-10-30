from functions.lists import *
from os import system
from time import sleep


# MENUS
def start():
    choice = menu()

    if choice == 1:
        system("cls")
        choice_game = menu_game()
        if choice_game == 1:
            system("cls")
            game1()
        elif choice_game == 2:
            system("cls")
            game2()
        elif choice_game == 3:
            system("cls")
            game3()
    elif choice == 2:
        system("cls")
        rules()
    elif choice == 3:
        system("cls")
        print("Até logo!")
        exit()
    elif choice > 3 or choice_game > 3:
        print("Digite um valor válido")
        sleep(2)
        system("cls")
        start()


def menu():
    print("=" * 80)
    print(" " * 36, "TERMO")
    print("=" * 80)

    print("DIgite para: \n \n[1]| JOGAR \n[2]| COMO JOGAR \n[3]| SAIR \n")

    while True:
        try:
            choice = int(input("Escolha: "))
        except ValueError:
            print("Escolha inválida.")
        else:
            break

    return choice


def menu_game():
    print("=" * 80)
    print(" " * 36, "TERMO")
    print("=" * 80)

    print("DIgite para: \n \n[1]| TERMO \n[2]| DUETO \n[3]| QUARTETO \n")

    while True:
        try:
            choice = int(input("Escolha: "))
        except ValueError:
            print("Escolha inválida.")
        else:
            break

    return choice


# MODOS DE JOGO
def game1():
    cont = 0
    correct = []

    print("=" * 80)
    print(" " * 36, "TERMO")
    print("=" * 80)
    while True:
        while True:
            resp = str(input("-->: "))
            resp = resp.upper()
            if resp not in listwords:
                print("Palavra inválida.")
            else:
                list(resp)
                break

        for c in range(0, 5):
            if resp[c] in word and resp[c] == word[c]:
                correct.append(resp[c])
            elif resp[c] not in word:
                correct.append(resp[c])
            elif resp[c] in word and resp[c] != word[c]:
                correct.append(resp[c])

        print("=" * 22)
        for c in range(0, 5):
            if correct[c] in word and correct[c] == word[c]:
                print(f"| \033[1;32m{correct[c]}\033[m", end=" ")
            elif correct[c] not in word:
                print(f"| \033[1;31m{correct[c]}\033[m", end=" ")
            elif correct[c] in word and correct[c] != word[c]:
                print(f"| \033[1;33m{correct[c]}\033[m", end=" ")
        print("|")
        print("=" * 22)

        if correct == word:
            print("=" * 80)
            print(" " * 32, "VOCÊ GANHOU!!")
            print("=" * 80)
            print("Digite para: \n \n[0]| Voltar ao menu \n")
            choice3 = int(input("Escolha: "))
            if choice3 == 0:
                correct.clear()
                system("cls")
                start()
        if cont == 5:
            print("=" * 80)
            print(" " * 32, "VOCÊ PERDEU!!")
            print("=" * 80)
            print(f"A palavra era: {''.join(word)}\n")
            print("Digite para: \n \n[0]| Voltar ao menu \n")
            choice3 = int(input("Escolha: "))
            if choice3 == 0:
                correct.clear()
                system("cls")
                start()

        cont += 1
        correct.clear()


def game2():
    win = False
    win2 = False
    cont = 0
    correct = []
    correct2 = []

    print("=" * 80)
    print(" " * 36, "DUETO")
    print("=" * 80)
    while True:
        while True:
            resp = str(input("-->: "))
            resp = resp.upper()
            if resp not in listwords:
                print("Palavra inválida.")
            else:
                list(resp)
                break

        for c in range(0, 5):
            if resp[c] in word and resp[c] == word[c]:
                correct.append(resp[c])
            elif resp[c] not in word:
                correct.append(resp[c])
            elif resp[c] in word and resp[c] != word[c]:
                correct.append(resp[c])

        for c in range(0, 5):
            if resp[c] in word2 and resp[c] == word2[c]:
                correct2.append(resp[c])
            elif resp[c] not in word2:
                correct2.append(resp[c])
            elif resp[c] in word2 and resp[c] != word2[c]:
                correct2.append(resp[c])

        print(correct)
        print("=" * 22, end=" ")
        print(" ", end=" ")
        print("=" * 22)
        for c in range(0, 5):
            if correct[c] in word and correct[c] == word[c]:
                print(f"| \033[1;32m{correct[c]}\033[m", end=" ")
            elif correct[c] not in word:
                print(f"| \033[1;31m{correct[c]}\033[m", end=" ")
            elif correct[c] in word and correct[c] != word[c]:
                print(f"| \033[1;33m{correct[c]}\033[m", end=" ")
        print("|", end=" ")
        print("  ", end=" ")
        for c in range(0, 5):
            if correct2[c] in word2 and correct2[c] == word2[c]:
                print(f"| \033[1;32m{correct2[c]}\033[m", end=" ")
            elif correct2[c] not in word2:
                print(f"| \033[1;31m{correct2[c]}\033[m", end=" ")
            elif correct2[c] in word2 and correct2[c] != word2[c]:
                print(f"| \033[1;33m{correct2[c]}\033[m", end=" ")
        print("|")
        print("=" * 22, end=" ")
        print(" ", end=" ")
        print("=" * 22)

        if correct == word:
            win = True
        elif correct2 == word2:
            win2 = True
        if correct == word and correct2 == word2:
            print("=" * 80)
            print(" " * 32, "VOCÊ GANHOU!!")
            print("=" * 80)
            print("Digite para: \n \n[0]| Voltar ao menu \n")
            choice3 = int(input("Escolha: "))
            if choice3 == 0:
                correct.clear()
                correct2.clear()
                system("cls")
                start()
        if cont == 6:
            print("=" * 80)
            print(" " * 32, "VOCÊ PERDEU!!")
            print("=" * 80)
            print(f"As palavras eram: {''.join(word)}, {''.join(word2)}\n")
            print("Digite para: \n \n[0]| Voltar ao menu \n")
            while True:
                try:
                    choice3 = int(input("Escolha: "))
                except ValueError:
                    print("Escolha inválida.")
                else:
                    break

            if choice3 == 0:
                correct.clear()
                correct2.clear()
                system("cls")
                start()

        cont += 1
        if win == False:
            correct.clear()
        if win2 == False:
            correct2.clear()


def game3():
    win = False
    win2 = False
    win3 = False
    win4 = False
    cont = 0
    correct = []
    correct2 = []
    correct3 = []
    correct4 = []

    print("=" * 80)
    print(" " * 36, "QUARTETO")
    print("=" * 80)
    while True:
        while True:
            resp = str(input("-->: "))
            resp = resp.upper()
            if resp not in listwords:
                print("Palavra inválida.")
            else:
                list(resp)
                break

        for c in range(0, 5):
            if resp[c] in word and resp[c] == word[c]:
                correct.append(resp[c])
            elif resp[c] not in word:
                correct.append(resp[c])
            elif resp[c] in word and resp[c] != word[c]:
                correct.append(resp[c])

        for c in range(0, 5):
            if resp[c] in word2 and resp[c] == word2[c]:
                correct2.append(resp[c])
            elif resp[c] not in word2:
                correct2.append(resp[c])
            elif resp[c] in word2 and resp[c] != word2[c]:
                correct2.append(resp[c])

        for c in range(0, 5):
            if resp[c] in word3 and resp[c] == word3[c]:
                correct3.append(resp[c])
            elif resp[c] not in word3:
                correct3.append(resp[c])
            elif resp[c] in word3 and resp[c] != word3[c]:
                correct3.append(resp[c])

        for c in range(0, 5):
            if resp[c] in word4 and resp[c] == word4[c]:
                correct4.append(resp[c])
            elif resp[c] not in word4:
                correct4.append(resp[c])
            elif resp[c] in word4 and resp[c] != word4[c]:
                correct4.append(resp[c])

        print("=" * 22, end=" ")
        print(" ", end=" ")
        print("=" * 22)
        for c in range(0, 5):
            if correct[c] in word and correct[c] == word[c]:
                print(f"| \033[1;32m{correct[c]}\033[m", end=" ")
            elif correct[c] not in word:
                print(f"| \033[1;31m{correct[c]}\033[m", end=" ")
            elif correct[c] in word and correct[c] != word[c]:
                print(f"| \033[1;33m{correct[c]}\033[m", end=" ")
        print("|", end=" ")
        print("  ", end=" ")
        for c in range(0, 5):
            if correct2[c] in word2 and correct2[c] == word2[c]:
                print(f"| \033[1;32m{correct2[c]}\033[m", end=" ")
            elif correct2[c] not in word2:
                print(f"| \033[1;31m{correct2[c]}\033[m", end=" ")
            elif correct2[c] in word2 and correct2[c] != word2[c]:
                print(f"| \033[1;33m{correct2[c]}\033[m", end=" ")
        print("|")
        print("=" * 22, end=" ")
        print(" ", end=" ")
        print("=" * 22)

        print("=" * 22, end=" ")
        print(" ", end=" ")
        print("=" * 22)
        for c in range(0, 5):
            if correct3[c] in word3 and correct3[c] == word3[c]:
                print(f"| \033[1;32m{correct3[c]}\033[m", end=" ")
            elif correct3[c] not in word3:
                print(f"| \033[1;31m{correct3[c]}\033[m", end=" ")
            elif correct3[c] in word3 and correct3[c] != word3[c]:
                print(f"| \033[1;33m{correct3[c]}\033[m", end=" ")
        print("|", end=" ")
        print("  ", end=" ")
        for c in range(0, 5):
            if correct4[c] in word4 and correct4[c] == word4[c]:
                print(f"| \033[1;32m{correct4[c]}\033[m", end=" ")
            elif correct4[c] not in word4:
                print(f"| \033[1;31m{correct4[c]}\033[m", end=" ")
            elif correct4[c] in word4 and correct4[c] != word4[c]:
                print(f"| \033[1;33m{correct4[c]}\033[m", end=" ")
        print("|")
        print("=" * 22, end=" ")
        print(" ", end=" ")
        print("=" * 22)

        if correct == word:
            win = True
        elif correct2 == word2:
            win2 = True
        elif correct3 == word3:
            win3 = True
        elif correct4 == word4:
            win4 = True

        if (correct == word and correct2 == word2 and correct3 == word3 and correct4 == word4):
            print("=" * 80)
            print(" " * 32, "VOCÊ GANHOU!!")
            print("=" * 80)
            print("Digite para: \n \n[0]| Voltar ao menu \n")
            choice3 = int(input("Escolha: "))
            if choice3 == 0:
                correct.clear()
                correct2.clear()
                system("cls")
                start()
        if cont == 6:
            print("=" * 80)
            print(" " * 32, "VOCÊ PERDEU!!")
            print("=" * 80)
            print(
                f"As palavras eram: {''.join(word)}, {''.join(word2)}, {''.join(word3)}, {''.join(word4)}\n"
            )
            print("Digite para: \n \n[0]| Voltar ao menu \n")
            while True:
                try:
                    choice3 = int(input("Escolha: "))
                except ValueError:
                    print("Escolha inválida.")
                else:
                    break

            if choice3 == 0:
                correct.clear()
                correct2.clear()
                system("cls")
                start()

        cont += 1
        if win == False:
            correct.clear()
        if win2 == False:
            correct2.clear()
        if win3 == False:
            correct3.clear()
        if win4 == False:
            correct4.clear()


# REGRAS
def rules():
    print("=" * 80)
    print(" " * 36, "REGRAS")
    print("=" * 80)
    print(
        "\nVocê tem 6 tentativas para acertar a palavra que contém 5 letras. \nAs dicas mostraram o quanto esta perto da solução. \nEscreva todas as palavras sem os seus acentos."
    )
    print(
        " \nDICAS: \n\033[1;32mVERDE\033[m = Letra certa no lugar certo. \n\033[1;33mAMARELO\033[m = Letra está na palavra, porém no lugar errado.\n\033[1;31mVERMELHO\033[m = Letra não está na palavra"
    )
    print("=" * 80)
    print("DIgite para: \n \n[0]|Voltar para o menu \n")

    while True:
        try:
            choice2 = int(input("Escolha: "))
        except ValueError:
            print("Escolha inválida")
        else:
            break

    if choice2 == 0:
        system("cls")
        start()
