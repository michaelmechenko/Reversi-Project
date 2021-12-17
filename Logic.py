import random
from Board import Board

class Logic(Board):
    """class handling the logic of the game"""
    def is_on_board(self, x, y):
        """returns whether the selection is on the board
        :param: int, int
        :return: boolean"""
        return x >= 0 and x <= super.board_size and y >= 0 and y <= super.board_size
    
    def is_corner(self, x, y):
        """returns true if the selection is a corner of the board
        :param: int, int
        :return: boolean"""
        return (x == 0 and y == 0) or (x == super.board_size + 1 and y == 0) or (x == 0 and y == super.board_size + 1) or (x == super.board_size + 1 and y == super.board_size + 1)

    def is_valid_move(self, board, tile, x_start, y_start):
        """returns false if the starting position is invalid,
        returns a list of possible moves otherwise
        :param: Board, str, int, int
        :return: Boolean, List"""
        if (board.matrix[x_start][y_start] != ' ' or not self.is_on_board(x_start, y_start)):
            return False

        board.matrix[x_start][y_start] = tile

        if (tile == 'X'):
            other_tile = 'O'
        else:
            other_tile = 'X'

        tiles_to_flip = []

        for xdir, ydir in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:
            x, y = x_start, y_start
            x += xdir
            y += ydir
            if self.is_on_board(x, y) and board.matrix[x][y] == other_tile:
                x += xdir
                y += ydir
                if not self.is_on_board(x, y):
                    continue
                while board.matrix[x][y] == other_tile:
                    x += xdir
                    y += ydir
                    if not self.is_on_board(x, y):
                        break
                if not self.is_on_board(x, y):
                        continue
                if board.matrix[x][y] == tile:
                    while True:
                        x -= xdir
                        y -= ydir
                        if x == x_start and y == y_start:
                            break
                        tiles_to_flip.append([x, y])

        board.matrix[x_start][y_start] = ' '
        if len(tiles_to_flip) == 0:
            return False
        return tiles_to_flip

    def board_valid_moves(self, board, tile):
        """returns a board showcasing the possible valid moves with a *
        :param: Board, str
        :return: Board"""

        board_copy = board
        for x, y in self.get_valid_moves(board_copy, tile):
            board_copy.matrix[x][y] = '*'
        return board_copy

    def get_valid_moves(self, board, tile):
        """returns a list of valid moves
        :param: Board, str
        :return: list"""
        valid_moves = []

        for x in range(board.board_size):
            for y in range(board.board_size):
                if self.is_valid_move(board, tile, x, y) != False:
                    valid_moves.append([x, y])
        return valid_moves
    
    def get_score(self, board):
        x_score = 0
        o_score = 0

        for x in range(board.board_size):
            for y in range(board.board_size):
                if board.matrix[x][y] == 'X':
                    x_score += 1
                if board.matrix[x][y] == 'O':
                    o_score += 1
        return {'X':x_score, 'O':o_score}
    
    def player_tile(self):
        """input to choose what tile the player wants to be
        returns a list of the player's tile and the opposing player's tile
        :param: none
        :return: list"""
        tile = ''
        while not (tile == 'X' or tile == 'O'):
            print('Which tile do you want to be? Input either "X" or "O".')
            tile = input().upper()
        
        if tile == 'X':
            return ['X', 'O']
        else:
            return ['O', 'X']
    
    def first_turn(self):
        """randomly chooses who the first turn will be given to
        :param: none
        :return: str"""
        if random.randint(0, 1) == 1:
            return 'player'
        else:
            return 'computer'

    def make_move(self, board, tile, x_start, y_start):
        """places the tile on the board at the given position and flips any
        opposing pieces. returns true if the move is valid
        :param: Board, str, int, int
        :return: boolean"""
        tiles_to_flip = self.is_valid_move(board, tile, x_start, y_start)

        if tiles_to_flip == False:
            return False
        
        board.matrix[x_start][y_start] = tile
        for x, y in tiles_to_flip:
            board.matrix[x][y] = tile
        return True

    def get_player_move(self, board, player_tile):
        """allows the player to make their move; returns the move as a list
        :param: Board, str
        :return: list"""
        board_size_list = []
        for i in range(board.board_size):
            board_size_list.append(i)

        while True:
            print("Input your move as two integers with nothing separating them.")
            move = input().lower()
            if len(move) == 2 and move[0] in board_size_list and move[1] in board_size_list:
                x = int(move[0]) - 1
                y = int(move[1]) - 1
                if self.is_valid_move(board, player_tile, x, y) == False:
                    continue
                else:
                    break
            else:
                print("That is not a valid move.")
        return [x, y]
    
    def get_computer_move(self, board, comp_tile):
        """returns one possible computer move
        :param: Board, str
        :return: list"""
        possible_moves = self.get_valid_moves(board, comp_tile)
        random.shuffle(possible_moves)
        
        for x, y in possible_moves:
            if self.is_corner(x, y):
                return[x, y]
        
        best_score = -1
        for x, y in possible_moves:
            board_copy = board
            self.make_move(board_copy, comp_tile, x, y)
            score = self.get_score(board_copy)[comp_tile]
            if score > best_score:
                best_move = [x, y]
                best_score = score
            return best_move
        
    def show_points(self, board, player_tile, comp_tile):
        """prints the current score of the board
        :param: str, str
        :return: none"""
        score = self.get_score(board)
        print('You have %s points. The computer has %s points.' % (score[player_tile], score[comp_tile]))
