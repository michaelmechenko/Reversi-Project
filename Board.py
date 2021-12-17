class Board:
    """a class representing a board"""
    def __init__(self, board_size):
        """initializes a board object"""
        if not isinstance(board_size, int):
            raise TypeError('The arguments must be of type Int')
        self.board_size = board_size
        self.matrix = []
    
    def create_board(self):
        """given a board, creates a matrix to hold information
        :param: Board
        :return: none"""
        for i in range(self.board_size):
            self.matrix.append([" "] * self.board_size)
    
    def reset_board(self):
        """empties the board and initializes its spaces again
        :param: Board
        :return: none"""
        for rows in range(self.board_size):
            for cols in range(self.board_size):
                self.matrix[rows][cols] = " "
        
        if (self.board_size % 2 == 0):
            s = int((self.board_size / 2) - 1)
        else:
            s = int(((self.board_size + 1) / 2) - 1)

        self.matrix[s][s] = 'X'
        self.matrix[s + 1][s + 1] = 'X'
        self.matrix[s][s + 1] = 'O'
        self.matrix[s + 1][s] = 'O'

    def draw_board(self):
        """draws the board onto the screen
        :param: Board
        :return: none"""
        h_line = "----" * (self.board_size + 1)
        v_line = "|   "

        print(' | ', end='')
        for i in range(1, self.board_size + 1):
            if (i == self.board_size):
                print(f'{i} | ', end='\n')
            else:
                print(f'{i} | ', end="")
        print(h_line[0:(5 * self.board_size) - 5])

        for cols in range(self.board_size):
            print(cols + 1, end="")
            for rows in range(self.board_size):
                if (rows == self.board_size):
                    print(f'| {self.matrix[rows][cols]}', end="")
                else:
                    print(f'| {self.matrix[rows][cols]}', end=" ")
            print(v_line)
            print(h_line[0:(5 * self.board_size) - 5])