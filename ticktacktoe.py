"""
Author: Porter Mecham

Stretch challenge:
    Completely Dynamic spaces and board size
"""

board_size = 3

total_board_spaces = (board_size * board_size) + 1


def get_board():
    """Create equal rows and columns of board size"""
    board = []

    for i in range(1, total_board_spaces + 1):
        if i != total_board_spaces:
            board.append(i)

    return board


def get_board_size():
    b_size = input("What size would you like the board?: ")
    return int(b_size)


def print_board(board):
    """takes a board and prints it to the console

    Args:
        board : list of numbers
    """
    # the number of digits
    digit_size = len(str(len(board)))

    # if the number are larger than one digit then they need more space on the board

    for number in range(1, total_board_spaces):
        n_digit_size = len(str(number))
        # If number is the end number
        if ((number - 1) % board_size) == (board_size - 1):
            print(" " * (digit_size - n_digit_size) + str(board[number - 1]))
        else:
            print(
                " " * (digit_size - n_digit_size) + str(board[number - 1]) + "|",
                end="",
            )
        # if end of row
        if number % board_size == 0 and number != total_board_spaces - 1:
            print("-" * digit_size + ("+" + "-" * digit_size) * (board_size - 1))


def get_move(is_x_turn) -> int:
    """asks player what move they want to make

    Args:
        is_x_turn (bool): whos turn is it

    Returns:
        int: the place they want to move to
    """

    if is_x_turn:
        print("x", end="")
    else:
        print("o", end="")

    print(f"'s turn to choose a square (1-{total_board_spaces - 1}): ", end="")
    move = input()
    return int(move)


def change_board(board, is_x_turn: bool, move: int) -> list[str]:
    """Takes the move and changes that piece on the board

    Args:
        board (list): board list
        is_x_turn (bool): whos turn is it
        move (int): the place the player wants to move to

    Returns:
        list[str]: board list
    """

    if is_x_turn:
        board[move - 1] = "x"
    else:
        board[move - 1] = "o"

    return board


def check_for_win(board):
    """Checks if there is three in a row

    Args:
        board (list): board list

    Returns:
        tuple: (bool,"winning mark")
    """
    item_counter = 0

    for num in range(1, total_board_spaces):
        if board[num - 1] == "x" or board[num - 1] == "o":
            mark = board[num - 1]

            # if beginning of row
            if ((num - 1) % board_size) == 0:
                # if on top left
                if num - board_size < 1:
                    continue
                # if on bottom left
                elif num + board_size > total_board_spaces:
                    continue
                else:
                    if check_vertical_row(board, mark, num):
                        return (True, mark)
            # if on the end of the row
            elif ((num - 1) % board_size) == (board_size - 1):
                # if on top right
                if num - board_size < 1:
                    continue
                # if on bottom right
                elif num + board_size > total_board_spaces:
                    continue
                # if in top middle
                else:
                    if check_vertical_row(board, mark, num):
                        return (True, mark)

                continue
            # if on the top row and not beginning or end
            elif num - board_size < 1:
                if check_horizontal_row(board, mark, num):
                    return (True, mark)
            # if on the bottom row and not beginning or end
            elif num + board_size > total_board_spaces:
                if check_horizontal_row(board, mark, num):
                    return (True, mark)
            # if surrounded on all sides
            else:
                if (
                    check_horizontal_row(board, mark, num)
                    or check_vertical_row(board, mark, num)
                    or check_diagonal_ur_row(board, mark, num)
                    or check_diagonal_ul_row(board, mark, num)
                ):
                    return (True, mark)

    return (False, " ")


def check_vertical_row(board, mark, num):
    """ check for vertical row """
    num -= 1
    return board[num - board_size] == mark and board[num + board_size] == mark


def check_horizontal_row(board, mark, num):
    """ check for horizontal row """
    num -= 1
    return board[num - 1] == mark and board[num + 1] == mark


def check_diagonal_ur_row(board, mark, num):
    """ check for diagonal / row """
    return board[num - board_size + 1] == mark and board[num + board_size - 2] == mark


def check_diagonal_ul_row(board, mark, num):
    """ check for diagonal \\ row """
    return board[num - board_size - 2] == mark and board[num + board_size] == mark


def board_is_full(board):
    """Checks the board for any open places

    Args:
        board (list): board list

    Returns:
        bool: True or false
    """

    for i in board:
        if isinstance(board, int):
            return True
    return False


def main():
    is_x_turn = True

    global board_size
    global total_board_spaces
    board_size = get_board_size()
    total_board_spaces = (board_size * board_size) + 1

    # Get Grid
    board = get_board()
    print_board(board)

    game_over = False
    while not game_over:
        # Get Player Move
        move = get_move(is_x_turn)

        # Change Board
        board = change_board(board, is_x_turn, move)

        # Switch Player Turn
        is_x_turn = not is_x_turn

        # Check If Win
        winner = check_for_win(board)

        # Check if Game Is Over
        if winner[0]:
            game_over = True
            print(winner[1], "is the winner")
        else:
            if board_is_full(board):
                game_over = True
                print("Game is Draw")

        # Print Grid
        print_board(board)


if __name__ == "__main__":
    main()"""
Solo Checkpoint 02
Author: Porter Mecham

Stretch challenge:
    Completely Dynamic spaces and board size
"""

board_size = 3

total_board_spaces = (board_size * board_size) + 1


def get_board():
    """Create equal rows and columns of board size"""
    board = []

    for i in range(1, total_board_spaces + 1):
        if i != total_board_spaces:
            board.append(i)

    return board


def get_board_size():
    b_size = input("What size would you like the board?: ")
    return int(b_size)


def print_board(board):
    """takes a board and prints it to the console

    Args:
        board : list of numbers
    """
    # the number of digits
    digit_size = len(str(len(board)))

    # if the number are larger than one digit then they need more space on the board

    for number in range(1, total_board_spaces):
        n_digit_size = len(str(number))
        # If number is the end number
        if ((number - 1) % board_size) == (board_size - 1):
            print(" " * (digit_size - n_digit_size) + str(board[number - 1]))
        else:
            print(
                " " * (digit_size - n_digit_size) + str(board[number - 1]) + "|",
                end="",
            )
        # if end of row
        if number % board_size == 0 and number != total_board_spaces - 1:
            print("-" * digit_size + ("+" + "-" * digit_size) * (board_size - 1))


def get_move(is_x_turn) -> int:
    """asks player what move they want to make

    Args:
        is_x_turn (bool): whos turn is it

    Returns:
        int: the place they want to move to
    """

    if is_x_turn:
        print("x", end="")
    else:
        print("o", end="")

    print(f"'s turn to choose a square (1-{total_board_spaces - 1}): ", end="")
    move = input()
    return int(move)


def change_board(board, is_x_turn: bool, move: int) -> list[str]:
    """Takes the move and changes that piece on the board

    Args:
        board (list): board list
        is_x_turn (bool): whos turn is it
        move (int): the place the player wants to move to

    Returns:
        list[str]: board list
    """

    if is_x_turn:
        board[move - 1] = "x"
    else:
        board[move - 1] = "o"

    return board


def check_for_win(board):
    """Checks if there is three in a row

    Args:
        board (list): board list

    Returns:
        tuple: (bool,"winning mark")
    """
    item_counter = 0

    for num in range(1, total_board_spaces):
        if board[num - 1] == "x" or board[num - 1] == "o":
            mark = board[num - 1]

            # if beginning of row
            if ((num - 1) % board_size) == 0:
                # if on top left
                if num - board_size < 1:
                    continue
                # if on bottom left
                elif num + board_size > total_board_spaces:
                    continue
                else:
                    if check_vertical_row(board, mark, num):
                        return (True, mark)
            # if on the end of the row
            elif ((num - 1) % board_size) == (board_size - 1):
                # if on top right
                if num - board_size < 1:
                    continue
                # if on bottom right
                elif num + board_size > total_board_spaces:
                    continue
                # if in top middle
                else:
                    if check_vertical_row(board, mark, num):
                        return (True, mark)

                continue
            # if on the top row and not beginning or end
            elif num - board_size < 1:
                if check_horizontal_row(board, mark, num):
                    return (True, mark)
            # if on the bottom row and not beginning or end
            elif num + board_size > total_board_spaces:
                if check_horizontal_row(board, mark, num):
                    return (True, mark)
            # if surrounded on all sides
            else:
                if (
                    check_horizontal_row(board, mark, num)
                    or check_vertical_row(board, mark, num)
                    or check_diagonal_ur_row(board, mark, num)
                    or check_diagonal_ul_row(board, mark, num)
                ):
                    return (True, mark)

    return (False, " ")


def check_vertical_row(board, mark, num):
    """ check for vertical row """
    num -= 1
    return board[num - board_size] == mark and board[num + board_size] == mark


def check_horizontal_row(board, mark, num):
    """ check for horizontal row """
    num -= 1
    return board[num - 1] == mark and board[num + 1] == mark


def check_diagonal_ur_row(board, mark, num):
    """ check for diagonal / row """
    return board[num - board_size + 1] == mark and board[num + board_size - 2] == mark


def check_diagonal_ul_row(board, mark, num):
    """ check for diagonal \\ row """
    return board[num - board_size - 2] == mark and board[num + board_size] == mark


def board_is_full(board):
    """Checks the board for any open places

    Args:
        board (list): board list

    Returns:
        bool: True or false
    """

    for i in board:
        if isinstance(board, int):
            return True
    return False


def main():
    is_x_turn = True

    global board_size
    global total_board_spaces
    board_size = get_board_size()
    total_board_spaces = (board_size * board_size) + 1

    # Get Grid
    board = get_board()
    print_board(board)

    game_over = False
    while not game_over:
        # Get Player Move
        move = get_move(is_x_turn)

        # Change Board
        board = change_board(board, is_x_turn, move)

        # Switch Player Turn
        is_x_turn = not is_x_turn

        # Check If Win
        winner = check_for_win(board)

        # Check if Game Is Over
        if winner[0]:
            game_over = True
            print(winner[1], "is the winner")
        else:
            if board_is_full(board):
                game_over = True
                print("Game is Draw")

        # Print Grid
        print_board(board)


if __name__ == "__main__":
    main()
