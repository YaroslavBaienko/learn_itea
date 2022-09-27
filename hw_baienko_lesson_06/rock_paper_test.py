def generate_key():
    import string
    import secrets
    alphabet = string.ascii_letters + string.digits
    while True:
        key = ''.join(secrets.choice(alphabet) for i in range(64))
        if (any(c.islower() for c in key)
                and any(c.isupper() for c in key)
                and sum(c.isdigit() for c in key) >= 3):
            break
    return key.upper()


def give_hmac(key, params):
    import hmac
    import hashlib
    secret_key = b"key"
    total_params = b"params"
    hmac = hmac.new(secret_key, total_params, hashlib.sha256).hexdigest().upper()
    return hmac


def name_to_number(name):
    if name == "rock":
        return 1
    elif name == "Spock":
        return 2
    elif name == "paper":
        return 3
    elif name == "lizard":
        return 4
    elif name == "scissors":
        return 5


def number_to_name(number):
    if number == '1':
        return "rock"
    elif number == '2':
        return "Spock"
    elif number == '3':
        return "paper"
    elif number == '4':
        return "lizard"
    elif number == '5':
        return "scissors"
    elif number == '0':
        return '0'
    elif number == '?':
        return '?'


def rock_paper_game(player_choice, key):
    import random
    if player_choice in ('rock', 'paper', 'scissors', 'Spock', 'lizard'):
        print("")
        print("Your move: " + player_choice)
        player_number = name_to_number(player_choice)
        comp_number = random.randrange(1, 6)
        comp_choice = number_to_name(str(comp_number))
        print("Computer move: " + comp_choice)

        if comp_number - player_number > 0:
            if comp_number - player_number > 2:
                print("Player wins")
                print(f'HMAC key: {give_hmac(key, params=comp_number)}')
            elif comp_number - player_number <= 2:
                print("Computer wins")
                print(f'HMAC key: {give_hmac(key, params=comp_number)}')
        elif comp_number - player_number < 0:
            if (comp_number - player_number) % 5 > 2:
                print("Player wins")
                print(f'HMAC key: {give_hmac(key, params=comp_number)}')
            elif comp_number - player_number <= 2:
                print("Computer wins")
                print(f'HMAC key: {give_hmac(key, params=comp_number)}')
        elif comp_number == player_number:
            print("Player and computer tie!")
            print(f'HMAC key: {give_hmac(key, params=comp_number)}')
    elif player_choice == '0':
        exit()
    elif player_choice == '?':
        print('Game produced by Yaroslav Baienko')


def main():
    while True:
        key = generate_key()
        print(f'HMAC: {key}')
        print("""Available moves:
        1 - rock
        2 - paper
        3 - scissors
        4 - lizard
        5 - Spock
        0 - exit
        ? - help""")
        player_choice = input('Enter your move: ')
        if player_choice not in ['1', '2', '3', '4', '5', '0', '?']:
            continue
        else:
            rock_paper_game(number_to_name(player_choice), key=key)
            break


if __name__ == '__main__':
    main()
