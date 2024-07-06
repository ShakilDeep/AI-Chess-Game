import chess
import chess.engine

def get_best_move(board, engine):
    """
    Get the best move for the current board state using the given engine.
    
    Parameters:
    board (chess.Board): The current state of the chess board.
    engine (chess.engine.SimpleEngine): The chess engine to use for move calculation.
    
    Returns:
    chess.Move: The best move determined by the engine.
    """
    # Set a time limit for the engine to think
    limit = chess.engine.Limit(time=0.1)
    
    # Get the best move from the engine
    result = engine.play(board, limit)
    
    return result.move
