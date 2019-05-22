class Board:
    O = "⭕"
    X = "❌"
    S = "⬜"

    def __init__(self):
        self._cells = [[self.S] * 3 for _ in range(3)]

    def winner(self):
        """
        (Board) -> str
        :return: '⭕' if O-s won, '❌' if X-ses won, 'Draw' if draw, None if it is not a winning position
        """
        # check common lines
        for i in range(3):
            if self._cells[i][0] == self._cells[i][1] == self._cells[i][2] != self.S or \
                    self._cells[0][i] == self._cells[1][i] == self._cells[2][i] != self.S:
                return self._cells[i][i]

        # check_diagonals
        if self._cells[0][0] == self._cells[1][1] == self._cells[2][2] != self.S or \
                self._cells[0][2] == self._cells[1][1] == self._cells[2][0] != self.S:
            return self._cells[1][1]
        draw = True
        for i in range(3):
            for j in range(3):
                if self._cells[i][j] == self.S:
                    draw = False
        if draw:
            return "Draw"
        else:
            return None

    def make_move(self, position, character):
        """
        (Board, tuple(int, int), str) -> Bool
        Place a character on the position
        :param position: position in form (x, y)
        :param character: character to be put
        :return: True if placed successfully else false
        """
        i, j = position
        if not (0 <= i < 3 and 0 <= j < 3):
            return False
        if self._cells[i][j] != self.S:
            return False
        self._cells[i][j] = character
        return True

    @staticmethod
    def check_position(position):
        """
        Check whether position is in right format
        :param position: tuple representing a position
        :return: True if position is in right foemat else False
        """
        if len(position) != 2:
            return False
        if type(position[0]) != str or type(position[1]) != str:
            return False
        if not position[0].isdigit() or not position[1].isdigit():
            return False
        return True

    def possible_moves(self):
        """
        (Board) -> list(tuple(int, int))
        :return: list of tuples of free cells
        """
        res = []
        for i in range(3):
            for j in range(3):
                if self._cells[i][j] == self.S:
                    res.append((i, j))
        return res

    def __str__(self):
        res = ""
        for i in range(3):
            for j in range(3):
                res += self._cells[i][j]
            res += "\n"
        return res
