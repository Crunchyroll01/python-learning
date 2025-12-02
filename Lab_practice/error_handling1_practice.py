def practice_1_basic_exceptions():
    """
    Practice identifying and handling common exceptions
    """
    print("\n" + "="*50)
    print("EXERCISE 1: Handle the Exceptions")
    print("="*50)
    # TODO 1: Fix division by zero
    def safe_divide(a, b):
        """Return a/b or None if division by zero"""
        # Add try-except block here
        try:
            return a / b
        except ZeroDivisionError:
            print ("Error: Division by zero is not allowed.")
            return None
    # Test your function
    print(f"10 / 2 = {safe_divide(10, 2)}")
    print(f"10 / 0 = {safe_divide(10, 0)}")
practice_1_basic_exceptions()
def practice_2_exception_hierarchy():
    """
    Practice with exception hierarchy
    """
    print("\n" + "="*50)
    print("EXERCISE 2: Exception Hierarchy")
    print("="*50)
    # TODO 1: Catch multiple related exceptions efficiently
    def access_data(data_structure, key):
        """
        Access data[key] whether data is list or dict.
        Return None if key doesn't exist.
        """
        try:
            return data_structure[key]
        except (KeyError, IndexError): # TODO: Replace with appropriate parent exception
            return None
    # Test with different data structures
    test_list = [10, 20, 30]
    test_dict = {"a": 1, "b": 2}
    print(f"List[1]: {access_data(test_list, 1)}")
    print(f"List[10]: {access_data(test_list, 10)}")
    print(f"Dict['a']: {access_data(test_dict, 'a')}")
    print(f"Dict['z']: {access_data(test_dict, 'z')}")
practice_2_exception_hierarchy()

'''
def practice_5_custom_exceptions():
    """
    Practice creating and using custom exceptions
    """
    print("\n" + "="*50)
    print("EXERCISE 5: Custom Exceptions")
    print("="*50)
    # TODO 1: Create custom exceptions
    class GameError(Exception):
        """Base class for game exceptions."""
        pass
    class InvalidMoveError(GameError):
        """Invalid game move."""
        def __init__(self, position, reason):
            self.position = position
            self.reason = reason
    class GameOverError(GameError):
        """Game has ended."""
        def __init__(self, winner):
            self.winner = winner
# TODO 2: Use custom exceptions
class TicTacToe:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        self.game_over = False
    def make_move(self, row, col):
        # TODO: Raise GameOverError if game_over is True
        # TODO: Raise InvalidMoveError if position is taken
        # TODO: Raise InvalidMoveError if position is out of bounds
        if self.game_over:
            raise GameOverError("Game is already over.")
        if not (0 <= row < 3 and 0 <= col < 3):
            raise InvalidMoveError((row, col), "Position is out of bounds.")
        if self.board[row][col] != ' ':
            raise InvalidMoveError((row, col), "Position is already taken.")
        self.board[row][col] = self.current_player
    # Test the game
    game = TicTacToe()
    test_moves = [
        (0, 0), # Valid
        (0, 0), # Already taken
        (5, 5), # Out of bounds
    ]
    for row, col in test_moves:
        try:
            game.make_move(row, col)
            print(f"✅ Move ({row}, {col}) successful")
        except InvalidMoveError as e:
            print(f"❌ Invalid move: {e}")
        except GameOverError as e:
            print(f"🏁 Game over: {e}")
practice_5_custom_exceptions()
'''