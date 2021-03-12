import random


# Rock, paper, scissors game
class Rps:
    options: tuple = 'rock', 'scissors', 'paper'
    rules: dict = {'rock': 'paper',
                   'paper': 'scissors',
                   'scissors': 'rock'}

    def __init__(self, user):
        self.user = user

    def game(self, player_choice: str):
        comp_choise = random.choice(self.options)

        if player_choice == comp_choise:
            self.user.add_score(50)
            result = 'draw'
        elif player_choice == self.rules[comp_choise]:
            self.user.add_score(100)
            result = 'win'
        else:
            result = 'lose'

        self.message(result, comp_choise)

    @staticmethod
    def message(result: str, option: str):
        if result == 'lose':
            print(f'Sorry, but the computer chose {option}')
        if result == 'draw':
            print(f'There is a draw {option}')
        if result == 'win':
            print(f'Well done. The computer chose {option} and failed')

class Users:
    def __init__(self, name: str):
        if not name:
            print('Invalid name')
            exit()
        self.name = name
        self.score = self.get_score()

        print(f'Hello, {self.name}')

    def get_score(self) -> int:
        with open('rating.txt', 'r') as file:
            for line in self.generate_lines_start_with(self.name, file):
                return int(line.removeprefix(self.name))
        return 0

    def add_score(self, score):
        self.score += score

    @staticmethod
    def generate_lines_start_with(string, file):
        for line in file:
            if line.startswith(string):
                yield line

def main():
    user_name = input('Enter your name:')
    user = Users(user_name)

    while True:
        player_choice = input('Pick one: rock, paper, scissors:').strip()
        if player_choice in Rps.options:
            Rps(user).game(player_choice)
        elif player_choice == '!rating':
            print(f'Your rating: {user.score}')
        elif player_choice == '!exit':
            print('Bye!')
            exit()
        else:
            # ugly output for hyperskill tests
            # print(f'Wrong input: {player_choice}. Should be one of {Rps.options} or "!exit"')
            print('Invalid input')

if __name__ == '__main__':
    main()
