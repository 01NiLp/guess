import random


def play():
    print("**********************************")
    print("Welcome to the Guessing Game!")
    print("**********************************")

    secret_number = random.randrange(1, 101)  # 0~100
    score = 100

    print("Choose a level of Dificulty: ")
    print("(1) Easy (2) Medium (3) Hard")

    level = int(input("Choose a Level: "))

    if level == 1:
        number_of_tries = 20
    elif level == 2:
        number_of_tries = 10
    else:
        number_of_tries = 5

    for rodada in range(1, number_of_tries + 1):
        print("Attempt {} of {}".format(rodada, number_of_tries))

        try_str = input("Type a number between 1 and 100: ")
        print("You typed: ", try_str)
        Try = int(try_str)

        if (Try < 1 or Try > 100):
            print("You should type a number between 1 and 100!")
            continue

        right = Try == secret_number
        higher = Try > secret_number
        lower = Try < secret_number

        if (right):
            print("You guessed and made {} score!".format(score))
            break
        else:
            if (higher):
                print("Wrong! Your guess was higher than the number")
            elif (lower):
                print("Wrong! Your guess was lower than the number")
            lost_points = abs(secret_number - Try)
            score -= lost_points

    print("End of Game!")


if (__name__ == "__main__"):
    play()
