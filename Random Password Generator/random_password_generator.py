import random
import string
CHOICES = [string.ascii_uppercase, string.ascii_lowercase, string.punctuation, string.digits]


def generate_password(pw_length):
    """
    :param pw_length: Length to generate password to accordingly
    :return: Returns randomly generated password
    """
    generated_password = ""

    for i in range(pw_length):
        generated_password += random.choice(random.choice(CHOICES))

    # Writes password to "password.txt"
    with open("password.txt", "w") as file:
        file.write(generated_password)
        file.close()

    return generated_password


def generate_passphrase():
    """
    :return: Returns random generated passphrase
    """
    with open("nouns.txt", "r") as subject_file:
        subject_list = subject_file.read()
        subject_list = subject_list.split()
        subject_file.close()

    with open("adjectives.txt", "r") as adjectives_file:
        adjectives_list = adjectives_file.read()
        adjectives_list = adjectives_list.split()
        adjectives_file.close()

    with open("verbs.txt", "r") as verbs_file:
        verbs_list = verbs_file.read()
        verbs_list = verbs_list.split()
        verbs_file.close()

    passphrase = random.choice(adjectives_list) + "-" + random.choice(subject_list) + "-" + random.choice(verbs_list) + str(random.randint(0, 9999))

    # Writes passphrase to "passphrase.txt"
    with open("passphrase.txt", "w") as file:
        file.write(passphrase.lower())
        file.close()

    return passphrase.lower()


def test():
    pass


def main():
    test()

    valid_flag = 0
    while valid_flag == 0:
        print("Select your choice (Input '1' or '2')")
        print("(1) Password")
        print("(2) Passphrase")
        choice_input = input("Generate password or passphrase?: ")

        if choice_input.isdigit():
            if 1 <= int(choice_input) <= 2:
                if choice_input == 1:
                    user_input = input("Enter a password length: ")
                    if user_input.isdigit() and 8 <= int(user_input) <= 16:
                        user_input = int(user_input)
                        print(f"Password: {generate_password(user_input)}")
                        valid_flag = 1
                    else:
                        print("Input an integer for your password length. (8-16)")
                        continue
                else:
                    print(f"Passphrase: {generate_passphrase()}")
                    valid_flag = 1
            else:
                print("Enter 1 or 2.")
                continue
        else:
            print("Enter 1 or 2.")
            continue


if __name__ == "__main__":
    main()
