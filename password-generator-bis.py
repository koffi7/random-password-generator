import random

def password_generator(digits, letters, sp_chr):
    # Main program
    while True:
        print('\n-- Password Generator --')
        print('Choose an option\n\n1-Generate a password\n2-Exit the program')
        usr_choice = input('\nYour choice: ')

        if usr_choice == '1':
            while True:
                try:
                    psswd_lgth = int(input('Provide password length: '))
                    if psswd_lgth > 0:
                        break
                    else:
                        print('Provide an integer greater than 0')
                except ValueError:
                    print('Please enter a correct value')

            upper_str = input('Use uppercase letters? y/n: ')
            lower_str = input('Use lowercase letters? y/n: ')
            use_digit = input('Use digit? (y/n): ')
            use_sp_char = input('Use special characters? (y/n): ')

            password = []

            while len(password) < psswd_lgth:
                if upper_str == 'y':
                    password.append(random.choice(letters).upper())
                if lower_str == 'y':
                    password.append(random.choice(letters))
                if use_digit == 'y':
                    password.append(random.choice(digits))
                if use_sp_char == 'y':
                    password.append(random.choice(sp_chr))

            password = password[:psswd_lgth]  

            random.shuffle(password)  
            print('The generated password is:', ''.join(password)) 

        elif usr_choice == '2':
            print('Bye')
            break
        else:
            print('Enter a correct value')
            usr_choice = input('\nYour choice: ')

password_generator([str(d) for d in range(10)], [chr(l) for l in range(ord('a'), ord('z') + 1)], list('!#$%&()*+,-./:;<=>?@_{|}~'))
