import random


# Rock, paper, scissors game
class Rps:
    options: tuple = 'rock', 'scissors', 'paper'
    rules: dict = {'rock': 'paper',
                   'paper': 'scissors',
                   'scissors': 'rock'}

    def game(self, player_choice: str):
        if player_choice not in self.options:
            print(f'Wrong input: {player_choice}. Should be one of {self.options}')
            exit()

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
    def message(result, option):
        if result == 'lose':
            print(f'Sorry, but the computer chose {option}')
        if result == 'draw':
            print(f'There is a draw {option}')
        if result == 'win':
            print(f'Well done. The computer chose {option} and failed')

def main():
    player_choice = input().strip()
    Rps().game(player_choice)


if __name__ == '__main__':
    main()
