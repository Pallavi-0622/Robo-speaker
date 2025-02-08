import os

if __name__ == "__main__":
    print("Welcome to Robospeaker 1.1. created by LoharPallavi")

    while True:
        x = input("Enter what you want me to speak: ")

        if x == "q":
            os.system('espeak "Bye bye friend"')
            break

        command = f'espeak "{x}"'
        os.system(command)
