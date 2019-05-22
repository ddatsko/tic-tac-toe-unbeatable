import copy


class TreeNode:
    def __init__(self, board=None):
        self.board = board
        self.sons = []

    def add_son(self, son):
        """
        add son to the node
        """
        self.sons.append(son)


class GameTree:
    def __init__(self, board=None):
        self.init_board = TreeNode(board)

    def build_tree(self, player_character, other_character):
        """
        Build tree from given board ad decide what move is the best
        :return: the position of the best move
        """

        def recurse(top, depth):
            """
            recursive tree traversal and counting winning positions
            :param top: top vertex of subtree to count winning positions on
            :param depth: depth of the node
            :return: coefficient representing how good the position is
            """
            if top.board.winner() == player_character:
                return 1, 1
            if top.board.winner() == "Draw":
                return 0, 0
            if top.board.winner():
                return -1, 0
            if depth % 2 == 0:
                character = player_character
                current_state = -1
            else:
                current_state = 1
                character = other_character

            moves = top.board.possible_moves()
            winning = 0
            for move in moves:
                new_board = copy.deepcopy(top.board)
                new_board.make_move(move, character)
                rec = recurse(TreeNode(new_board), depth + 1)
                winning += rec[1]
                if depth % 2 == 0:
                    current_state = max(rec[0], current_state)
                else:
                    current_state = min(rec[0], current_state)

            return current_state, winning

        possible_moves = self.init_board.board.possible_moves()
        res = []
        for move in possible_moves:
            new_board = copy.deepcopy(self.init_board.board)
            new_board.make_move(move, player_character)
            res.append((recurse(TreeNode(new_board), 1), move))
        res.sort(key=lambda x: (-x[0][0], -x[0][1]))
        if res:
            return res[0]
