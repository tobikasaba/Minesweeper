import random


# let's create a board object to represent the minesweeper game
# this is so that we can just say "create a new board object", or
# "dig here", or "render this game for this object"
class Board:
    def __init__(self, dim_size, num_bombs):
        # keeping track of these parameters. They'll be helpful later on
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
        board = [[None for i in range(self.dim_size)] for j in range(self.dim_size)]
        # this creates an array like this:
        # [[None, None, ....., None]，
        # [None, None, ....., None]
        # [....                   ]
        # [None, None, ....., None]]，
        # hence this represents a board!

        # plant the bombs
        bombs_planted = 0
        while bombs_planted < self.num_bombs:
            loc = random.randint(0, self.dim_size ** 2 - 1)  # return a random integer N such that a <= N <= b
            row = loc // self.dim_size  # tells us the number of times dim_size goes into loc us what row to look at
            col = loc % self.dim_size  # we want the remainder to tell us what index in that row to look at

            if board[row][col] == "*":
                # this means we've planted a bomb there already so keep going
                continue
            board[row][col] = "*"  # plant the bomb
            bombs_planted += 1
        return board


# play the game
def play(dim_size=10, num_bombs=10):
    # Step 1: create the board and plant the bombs
    # Step 2: show the user the board and ask where they want to dig
    # Step 3a: if location is a bomb, show game over message
    # Step 3b: if location is not a bomb, dig recursively until each square is at least next to a bomb
    # Step 4: repeat steps 2 and 3a/b until there are no places to dig -> VICTORY!
    pass
