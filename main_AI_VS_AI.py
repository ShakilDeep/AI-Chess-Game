import pygame
import chess
import chess.engine
from game_logic import draw_board, evaluate_board

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)


def main():
    pygame.init()
    window = pygame.display.set_mode((480, 520))  # Increased height for text display
    pygame.display.set_caption("Chess")

    board = chess.Board()
    engine_path = "stockfish.exe"  # Ensure this path is correct
    engine = chess.engine.SimpleEngine.popen_uci(engine_path)

    move_count_white = 0
    move_count_black = 0

    font = pygame.font.SysFont(None, 24)
    large_font = pygame.font.SysFont(None, 48)  # Large font for winner message

    running = True
    game_over = False
    winner_text = ""

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if not game_over:
            if not board.is_game_over():
                # AI makes a move
                result = engine.play(board, chess.engine.Limit(time=0.1))
                board.push(result.move)
                if board.turn == chess.WHITE:
                    move_count_black += 1
                else:
                    move_count_white += 1
            else:
                game_over = True
                if board.is_checkmate():
                    winner = "White" if board.turn == chess.BLACK else "Black"
                    winner_text = f"Winner: {winner}"
                elif board.is_stalemate():
                    winner_text = "Game over: Stalemate"
                elif board.is_insufficient_material():
                    winner_text = "Game over: Insufficient material"
                elif board.is_seventyfive_moves():
                    winner_text = "Game over: 75-move rule"
                elif board.is_fivefold_repetition():
                    winner_text = "Game over: Fivefold repetition"
                elif board.is_variant_draw():
                    winner_text = "Game over: Variant draw"
                else:
                    winner_text = "Game over: Draw"

        # Draw the board and pieces
        draw_board(window, board, 480, 480)

        # Calculate points
        white_points, black_points = evaluate_board(board)

        # Render text
        current_player = "White" if board.turn == chess.WHITE else "Black"
        text_surface = font.render(f"Current Player: {current_player}", True, BLACK)
        move_count_surface = font.render(f"Moves - White: {move_count_white} Black: {move_count_black}", True, BLACK)
        points_surface = font.render(f"Points - White: {white_points} Black: {black_points}", True, BLACK)

        window.fill(WHITE)  # Clear the screen
        draw_board(window, board, 480, 480)  # Redraw the board and pieces

        window.blit(text_surface, (10, 485))
        window.blit(move_count_surface, (10, 505))
        window.blit(points_surface, (250, 485))

        if game_over:
            winner_surface = large_font.render(winner_text, True, RED)
            window.blit(winner_surface, (10, 485))

        pygame.display.flip()

    engine.quit()
    pygame.quit()


if __name__ == "__main__":
    main()
