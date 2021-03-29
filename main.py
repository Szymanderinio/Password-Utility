# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import random
from string import punctuation

colors = {"black": "\033[0;37;40m", "white": "\033[0;37;47m",
          "yellow_txt": "\033[0;33;40m", "white_txt": "\033[1;37;40m", "red_txt_black_bgr": "\033[1;31;40m",
          "red_txt_white_bgr": "\033[1;31;47m", "blue_txt_black_bgr": "\033[1;36;40m",
          "blue_txt_white_bgr": "\033[1;36;47m", "green_txt": "\033[1;32;40m"}


# sp_char_id = {}

def show_menu():
    print("Choose an {}option{} from below: ".format
          (colors["blue_txt_black_bgr"], colors["white_txt"])
          + "\n{}1{}. Check how {}strong{} you password is".format
          (colors["blue_txt_black_bgr"], colors["white_txt"], colors["red_txt_black_bgr"], colors["white_txt"])
          + "\n{}2{}. {}Encrypt{} your password".format
          (colors["blue_txt_black_bgr"], colors["white_txt"], colors["yellow_txt"], colors["white_txt"])
          + "\n{}3{}. {}Decrypt{} your password".format
          (colors["blue_txt_black_bgr"], colors["white_txt"], colors["green_txt"], colors["white_txt"])
          + "\n{}4{}. Exit a program".format(colors["blue_txt_black_bgr"], colors["white_txt"]))


def password_strongmeter():
    print("tu cos bedzie")


def password_encrypt():
    password_to_encrypt = str(input("Type your password below:\n"))
    password_encrypted = ""
    offset = random.randrange(1, 26)
    for char in password_to_encrypt:
        value_of_char = ord(char) + offset
        password_encrypted += chr(value_of_char % 128)
    print("Your key: {}{}{}".format(colors["yellow_txt"], offset, colors["white_txt"]))
    print("Your encrypted password: {}{}{}".format(colors["yellow_txt"], password_encrypted, colors["white_txt"]))
    return password_encrypted


def password_decrypt():
    password_to_decrypt = str(input("Type your password below:\n"))
    password_decrypted = ""
    offset = int(input("Type offset: \n"))
    for char in password_to_decrypt:
        value_of_char = ord(char) - offset
        password_decrypted += chr(value_of_char % 128)  # 128 cause of ascii
    print("Your decrypted password: {}{}{}".format(colors["yellow_txt"], password_decrypted, colors["white_txt"]))


# def load_special_characters():
#    for char in punctuation:
#        sp_char_id[char] = ord(char)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # load_special_characters()
    print(colors["white_txt"])
    while True:
        show_menu()
        decision = int(input())

        if decision in range(1, 5):
            if decision == 1:
                password_strongmeter()
            if decision == 2:
                password_encrypt()
            if decision == 3:
                password_decrypt()
            if decision == 4:
                break
            # if decision == 5:
            #    for i in range(1, 26):
            #        password_decrypt(password_encrypt("!@#asd123ASD*()", i), i)
