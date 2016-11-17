BOARD_EDGE_LENGTH = 3
WINNING_ROW_LENGTH = 3

# Changing the board size obviously requires redefining the --+---+-- drawing section in show().
# The winning row may not have to be the BOARD_EDGE_LENGTH so this is built in to the checks.
#
# oxotest.py does not allow lengths greater than 3 currently. I may tweak it to prove it works.
#
# Also would have written as BOARD_HEIGHT and BOARD_WIDTH but the worksheet asks for n * n implying square.


class OxoBoard:
    def __init__(self):
        """ The initialiser. Initialise any fields you need here. """
        self.board = {}
        for x in xrange(BOARD_EDGE_LENGTH):
            for y in xrange(BOARD_EDGE_LENGTH):
                self.board[x, y] = 0

    def get_square(self, x, y):
        """ Return 0, 1 or 2 depending on the contents of the specified square. """
        # Use .get here as later a None return is relied upon for out of bounds x, y coordinates.
        return self.board.get((x, y))

    def set_square(self, x, y, mark):
        """ If the specified square is currently empty (0), fill it with mark and return True.
            If the square is not empty, leave it as-is and return False. """
        if self.get_square(x, y) == 0:
            self.board[x, y] = mark
            return True
        else:
            return False

    def is_board_full(self):
        """ If there are still empty squares on the board, return False.
            If there are no empty squares, return True. """

        #return all(value != 0 for value in self.board.values())
        return 0 not in self.board.values()

    def get_winner(self):
        """Revised get_winner function that looks for winning rows of length WINNING_ROW_LENGTH.
        Clashes with oxotest.py because of the assumed 3x3 grid though."""
        for x in xrange (BOARD_EDGE_LENGTH):
            for y in xrange (BOARD_EDGE_LENGTH):

                current_contents = self.get_square(x, y)

                if current_contents != 0:

                    # Check for vertical in a row
                    for i in xrange (1, WINNING_ROW_LENGTH):
                        if current_contents != self.get_square(x, y + i):
                            break
                    else:
                        return current_contents

                    # Check for three in a row
                    for i in xrange (1, WINNING_ROW_LENGTH):
                        if current_contents != self.get_square(x + i, y):
                            break
                    else:
                        return current_contents

                    # Check for diagonal down right in a row
                    for i in xrange (1, WINNING_ROW_LENGTH):
                        if current_contents != self.get_square(x + i, y + i):
                            break
                    else:
                        return current_contents

                    #  Check for diagonal down left in a row
                    for i in xrange (WINNING_ROW_LENGTH):
                        if current_contents != self.get_square(x + i, y - i):
                            break
                    else:
                        return current_contents
        return 0

    def show(self):
        """ Display the current board state in the terminal. You should not need to edit this. """
        for y in xrange(BOARD_EDGE_LENGTH):
            if y > 0:
                print "--+---+--"
            for x in xrange(BOARD_EDGE_LENGTH):
                if x > 0:
                    print '|',

                # Print a space for empty (0), an O for player 1, or an X for player 2
                print " OX"[self.get_square(x, y)],
            print


def input_square():
    """ Prompt the player to enter a square. You should not need to edit this. """
    while True:
        input = raw_input("Enter x,y where x=0,1,2, y=0,1,2: ")
        if input.count(',') != 1:
            print "Input must contain exactly one comma!"
            continue

        x, y = input.split(',')
        try:
            x = int(x)
            y = int(y)
        except ValueError:
            print "Input must be two numbers separated by a comma!"
            continue

        if x < 0 or x > BOARD_EDGE_LENGTH or y < 0 or y > BOARD_EDGE_LENGTH:
            print "Input is out of bounds!"
            continue

        return x, y

if __name__ == '__main__':
    board = OxoBoard()
    current_player = 1
    while True:
        board.show()
        print "Choose a square, Player", current_player
        x, y = input_square()
        if board.set_square(x, y, current_player):
            # Move was played successfully, so check for a winner
            winner = board.get_winner()
            if winner != 0:
                board.show()
                print "Player", winner, "wins!"
                break  # End the game
            elif board.is_board_full():
                board.show()
                print "It's a draw!"
                break  # End the game
            else:
                # Switch players
                if current_player == 1:
                    current_player = 2
                else:
                    current_player = 1
        else:
            # Move was not played successfully
            print "That square is already filled!"