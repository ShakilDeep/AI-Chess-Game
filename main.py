import pygame
import chess
import chess.engine
from game_logic import draw_board, evaluate_board
from gui import display_game_result

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def main():
    pygame.init()
    window = pygame.display.set_mode((480, 520))  # Increased height for text display
    pygame.display.set_caption("Chess")

    board = chess.Board()
    engine_path = "./stockfish.exe"  # Ensure this path is correct
    engine = chess.engine.SimpleEngine.popen_uci(engine_path)

    selected_square = None
    move_count_white = 0
    move_count_black = 0

    font = pygame.font.SysFont(None, 24)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if y < 480:  # Only consider clicks within the board area
                    col = x // 60
                    row = 7 - (y // 60)
                    square = chess.square(col, row)

                    if selected_square is None:
                        if board.piece_at(square) is not None and board.piece_at(square).color == chess.WHITE:
                            selected_square = square
                    else:
                        move = chess.Move(selected_square, square)
                        if move in board.legal_moves:
                            board.push(move)
                            move_count_white += 1
                            selected_square = None

                            # AI makes a move
                            if not board.is_game_over():
                                result = engine.play(board, chess.engine.Limit(time=0.1))
                                board.push(result.move)
                                move_count_black += 1
                        else:
                            selected_square = None

        # Draw the board and pieces
        draw_board(window, board, 480, 480)

        # Calculate points
        white_points, black_points = evaluate_board(board)

        # Render text
        current_player = "White" if board.turn == chess.WHITE else "Black"
        text_surface = font.render(f"Current Player: {current_player}", True, BLACK)
        move_count_surface = font.render(f"Moves - White: {move_count_white} Black: {move_count_black}", True, BLACK)
        points_surface = font.render(f"Points - White: {white_points} Black: {black_points}", True, BLACK)

        window.blit(text_surface, (10, 480))
        window.blit(move_count_surface, (10, 500))
        window.blit(points_surface, (250, 500))

        # Check for game over and display result
        if board.is_game_over():
            if board.is_checkmate():
                result = "White wins" if board.turn == chess.BLACK else "Black wins"
            elif board.is_stalemate():
                result = "Draw"
            else:
                result = "No result"

            display_game_result(window, result)
            running = False  # Stop the game loop

        pygame.display.flip()

    engine.quit()
    pygame.quit()

if __name__ == "__main__":
    main()
