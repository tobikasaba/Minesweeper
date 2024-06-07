# lets create a board object to represent the minesweeper game
# this is so that we can just say "create a new board object", or
# "dig here", or "render this game for this object"
class Board:
    def __init__(self, dim_size, num_bombs):
        # keeping track of these parameters. Theyll be helpful later on
        self.dim_size = dim_size
        self.num_bombs = num_bombs

        # creating the board
        self.board = self.make_new_board()  # plant the bombs

        # initialise a set to keep track of which locations we've uncovered]
        # we'll save (row, col) tuples into this set
        self.dug = set()

    def make_new_board(self):
        # construct a new board based on the dim size and num bombs
        # we should construct the list of lists here (or whatever representation you prefer,
        # but since we have a 2-D board, list of lists is most natural)

        # generate a new board
        board = [[None for i in range(self.dim_size)]
                 for j in range(self.dim_size)]
        # this creates an array like this:
        # [[None, None, ....., None]，
        # [None, None, ....., None]
        # [....                   ]
        # [None, None, ....., None]]，
        # hence this represents a board!
        return True


# play the game
def play(dim_size=10, num_bombs=10):
    # Step 1: create the board and plant the bombs
    # Step 2: show the user the bpard and ask where they want to dig
    # Step 3a: if location is a bomb, show game over message
    # Step 3b: if location is not a bomb, dig recursively until each square is at least next to a bomb
    # Step 4: repeat steps 2 and 3a/b until there are no places to dig -> VICTORY!
    pass

