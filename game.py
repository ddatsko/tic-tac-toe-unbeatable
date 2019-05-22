import game_tree
from board import Board
import os


class Game:
    def __init__(self, init_board):
        """
        Initialization
        :param board: init board of the game
        """
        self.board = init_board
        self.move = 0
        self.player = None
        self.player_character = None
        self.computer_character = None

    def get_init_info(self):
        """
        Get information from the user before the game starts
        """
        os.system("clear")
        self.player = input("What is your name: ")
        character = input("Would you like to play with X and move first[Y/n]: ")
        if character and character.lower() in "nN":
            self.player_character = self.board.O
            self.computer_character = self.board.X
        else:
            self.computer_character = self.board.O
            self.player_character = self.board.X

    def print_state(self):
        """
        Print the state of the game
        :return:
        """
        os.system("clear")
        print()
        print(self.board)
        print(f"Your move, {self.player}")

    def get_user_input(self):
        """
        Get user input from terminal
        :return: the position user will move to
        """
        position = input("Enter the position to move to (e.g.: 0 2): ").split()
        while not Board.check_position(position) or not self.board.make_move(tuple(map(int, position)),
                                                                             self.player_character):
            position = input("Enter one more time: ").split()

    def make_move_by_computer(self):
        """
        Make move by computer
        :return:None
        """
        tree = game_tree.GameTree(self.board)
        position = tree.build_tree(self.computer_character, self.player_character)[1]
        self.board.make_move(position, self.computer_character)

    def find_winner(self):
        """
        :return: the name of a winner or None otherwise
        """
        winner = self.board.winner()
        if winner == "Draw":
            return "This is a draw"
        if winner == self.player_character:
            return f"{self.player} WON!!!"
        elif winner:
            return f"Computer defeated you, {self.player}"
        return None


if __name__ == "__main__":
    init_board = Board()
    game = Game(init_board)
    game.get_init_info()
    while not game.find_winner():
        if game.player_character == game.board.X:
            game.print_state()
            game.get_user_input()
            if game.find_winner():
                break
            game.make_move_by_computer()
        else:
            if len(game.board.possible_moves()) == 9:
                game.board.make_move((1, 1), game.board.X)
            else:
                game.make_move_by_computer()
            game.print_state()
            if game.find_winner():
                break
            game.get_user_input()
    os.system("clear")
    print()
    print(game.board)
    print(game.find_winner())
