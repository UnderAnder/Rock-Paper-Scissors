import random


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
            for line in file:
                name, score = line.split()
                if name == self.name:
                    return int(score)
        return 0

    def add_score(self, score):
        self.score += score


# Rock, paper, scissors, etc game
class Rps:
    shapes: tuple = 'rock', 'fire', 'scissors', 'snake', 'human', 'tree', 'wolf', 'sponge', \
         'paper', 'air', 'water', 'dragon', 'devil', 'lightning', 'gun'

    def __init__(self, user: Users, options: tuple):
        self.user = user
        self.options = options
        self.rules = {v: (self.shapes[i+1:]+self.shapes[:i])[:(len(self.shapes)//2)] for i, v in enumerate(self.shapes)}


    def game(self, player_choice: str):
        comp_choice = random.choice(self.options)

        if player_choice == comp_choice:
            self.user.add_score(50)
            result = 'draw'
        elif comp_choice in self.rules.get(player_choice):
            self.user.add_score(100)
            result = 'win'
        else:
            result = 'lose'

        self.message(result, comp_choice)

    def message(self, result: str, option: str):
        if result == 'lose':
            print(f'Sorry, but the computer chose {option}')
            print(f'Your rating: {self.user.score}')
        if result == 'draw':
            print(f'There is a draw {option}')
            print(f'Your rating incresed by 50: {self.user.score}')
        if result == 'win':
            print(f'Well done. The computer chose {option} and failed')
            print(f'Your rating incresed by 100: {self.user.score}')


def main():
    user_name = input('Enter your name:')
    user = Users(user_name)

    options = tuple(input('Options, separated by comma, e.g. rock,paper,scissors,human,tree:').strip().split(','))
    if options == ('',):  # empty input
        options = 'rock', 'scissors', 'paper'
    print('Okay, let\'s start')

    rps = Rps(user, options)  # Create game session
    while True:
        player_choice = input('Pick one:').strip()
        if player_choice in options:
            rps.game(player_choice)
        elif player_choice == '!rating':
            print(f'Your rating: {user.score}')
        elif player_choice == '!exit':
            print('Bye!')
            exit()
        else:
            print(f'Wrong input: {player_choice}. Should be one of {options}, "!rating" or "!exit"')


if __name__ == '__main__':
    main()
