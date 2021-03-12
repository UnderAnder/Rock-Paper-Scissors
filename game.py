import random


# Rock, paper, scissors game
class Rps:
    options: tuple = 'rock', 'scissors', 'paper'
    rules: dict = {'rock': 'paper',
                   'paper': 'scissors',
                   'scissors': 'rock'}

    def game(self, player_choice: str):
        comp_choise = random.choice(self.options)
        result = ''

        if player_choice == comp_choise:
            result = 'draw'
        elif player_choice == self.rules[comp_choise]:
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

def main():
    while True:
        player_choice = input().strip()
        if player_choice in Rps.options:
            Rps().game(player_choice)
        elif player_choice == '!exit':
            print('Bye!')
            exit()
        else:
            # ugly output for hyperskill tests
            # print(f'Wrong input: {player_choice}. Should be one of {Rps.options} or "!exit"')
            print('Invalid input')

if __name__ == '__main__':
    main()
