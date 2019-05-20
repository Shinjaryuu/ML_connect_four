from classes.connect_four_game import ConnectFourGame

g = ConnectFourGame()
players = {1:1, -1:2}
while True:
    g.print_board()
    print("Current player: {}".format(players[g.current_player]))
    move_input = input()
    try:
        next_move = int(move_input)
    except:
        print('You must enter an integer between 0 and 6.')
        continue
    if next_move < 0 or next_move > 6 or next_move != float(move_input):
        print('You must enter an integer between 0 and 6.')
        continue
    if not g.move(next_move):
        print('That column is full.')
    else:
        winner = g.connected_four()
        if winner != 0:
            print("Congratulations! Player {} won!".format(players[winner]))
            break
