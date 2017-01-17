import string
import random

def password_secure_generator(size=20, chars=string.ascii_letters +
                              string.punctuation):
    return ''.join(random.SystemRandom().choice(chars) for i in range(size))

def repeat_question(number_for_input):
    answer = input("Are you happy with that answer? (y/n) ").lower()
    while answer != 'y':
        print("\n\n" + password_secure_generator(int(number_for_input)))
        answer = input("\nAre you happy with that answer? (y/n) ").lower()

def main():
    while True:
        try:
            number_for_input = int(input("Enter a number for the password" +
                                    " secure generator "))
            if int(number_for_input):
                print(password_secure_generator(int(number_for_input)))
                repeat_question(number_for_input)                
                break    
        except ValueError as e:
            print("I'm sorry I can't do that")
            print(e)

main()

input("\n\nEnjoy a securer day\n\nPress the enter key to exit.")

