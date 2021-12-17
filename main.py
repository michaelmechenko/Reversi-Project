from Board import Board
from Logic import Logic

# Michael Mechenko - Northeastern University Fall 2021 

print("Welcome to the game. You are the 'X' tile.")
while True:
    board_size = int(input("Please input the size of the board you want to play on. "))
    main_board = Board(board_size)
    game = Logic(board_size)
    main_board.create_board()
    main_board.reset_board()
    main_board.draw_board()
    player_tile, computer_tile = ['X', 'O']
    turn = game.first_turn()
    print('The ' + turn + ' will go first.')

    while True:
        if turn == 'player':
            main_board.draw_board
            game.show_points(main_board, player_tile, computer_tile)
            move = game.get_player_move(main_board, player_tile)
            game.make_move(main_board, player_tile, move[0], move[1])
            if game.get_valid_moves(main_board, computer_tile) == []:
                break
            else:
                turn = 'computer'

        else:
            main_board.draw_board
            game.show_points(main_board)
            input("Press enter to continue.")
            x, y = game.get_computer_move(main_board, computer_tile)
            game.make_move(main_board, computer_tile, x, y)
            if game.get_valid_moves(main_board, player_tile) == []:
                break
            else:
                turn = 'player'

    main_board.draw_board
    scores = game.get_score(main_board)
    print('X scored %s points. O scored %s points.' % (scores['X'], scores['O']))
