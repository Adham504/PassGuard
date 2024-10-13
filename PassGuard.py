# this project to check password strength
import math

def password_user_input():
    password = input("enter your password to check: ")
    if not password:
        print("\npassword can not be empty")
        main()
    return password


def password_strength(password):
    total_score = 0
    special_characters = {'`', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '+', '=', '{', '[', '}', '}', '|', '\'', ',', ':', ';', '"', '>', '.', '?', '/'}
    upper_check = False
    lower_check = False
    num_check = False
    special_characters_check = False
    password_len_check = False

    upper_check_warning = "your password is should include uppercase letter!! "
    lower_check_warning = "your password is should include lowercase letter!! "
    num_check_warning = "your password is should include digits!! "
    special_characters_warning = "your password is should include special_characters!!"
    pass_len_warning = "your password length must be more than 7 chars "

    for char in password:
        if char.isupper():
            upper_check = True

        if char.islower():
            lower_check = True

        if char.isdigit():
            num_check = True

        if char in special_characters:
            special_characters_check = True

    if len(password) > 7:
        password_len_check = True

    if not upper_check:
        print(upper_check_warning)
    else:
        total_score +=1

    if not lower_check:
        print(lower_check_warning)
    else:
        total_score +=1

    if not num_check:
        print(num_check_warning)
    else:
        total_score +=1

    if not special_characters_check:
        print(special_characters_warning)
    else:
        total_score +=1

    if not password_len_check:
        print(pass_len_warning)
        total_score = total_score

    if total_score:
        print(f"your password meets {total_score}/4 conditions\n")



def calculate_entropy(password): # yet to complete
    charset_size = 0

    if any(char.islower() for char in password):
        charset_size += 26

    if any(char.isupper() for char in password):
        charset_size += 26

    if any(char.isdigit() for char in password):
        charset_size += 10

    if any(char in '`~!@#$%^&*()-_=+[{]}|;:\'",<.>/?' for char in password):
        charset_size += 32

    if charset_size > 0:
        entropy = math.log(charset_size)*len(password)
    else:
        entropy = 0

    print(f"Password entropy: {entropy:.2f} bits")
    if entropy >= 80:
        print("Entropy feedback: Your password is very strong!")
    elif entropy >= 60:
        print("Entropy feedback: Your password is moderately strong, but adding more character variety or length could help.")
    else:
        print("Entropy feedback: Your password is weak. Consider using a longer password with more character variety.")

    return entropy

def main():
    print("\n*********************************************")
    print("Welcome to password strength check , you ready ? ")
    print("*********************************************")
    while True:
        print("\nto enter you password press 1")
        print("to exit press 2")
        user_option = input(":")
        if user_option == '1':
            password = password_user_input()
            password_strength(password)
            calculate_entropy(password)
        elif user_option == '2':
            exit()
        else:
            print("wrong input")
            print("#############\n")


if __name__ == '__main__':
    main()
