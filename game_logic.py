import pygame
import chess

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT_BROWN = (240, 217, 181)
DARK_BROWN = (181, 136, 99)

# Load images with the new filenames
PIECE_IMAGES = {
    'K': pygame.image.load('images/white_king.png'),
    'Q': pygame.image.load('images/white_queen.png'),
    'R': pygame.image.load('images/white_rook.png'),
    'B': pygame.image.load('images/white_bishop.png'),
    'N': pygame.image.load('images/white_knight.png'),
    'P': pygame.image.load('images/white_pawn.png'),
    'k': pygame.image.load('images/black_king.png'),
    'q': pygame.image.load('images/black_queen.png'),
    'r': pygame.image.load('images/black_rook.png'),
    'b': pygame.image.load('images/black_bishop.png'),
    'n': pygame.image.load('images/black_knight.png'),
    'p': pygame.image.load('images/black_pawn.png'),
}

def draw_board(window, board, width, height):
    square_size = width // 8
    for row in range(8):
        for col in range(8):
            color = LIGHT_BROWN if (row + col) % 2 == 0 else DARK_BROWN
            pygame.draw.rect(window, color, pygame.Rect(col * square_size, row * square_size, square_size, square_size))
            piece = board.piece_at(chess.square(col, 7 - row))
            if piece:
                piece_image = PIECE_IMAGES[piece.symbol()]
                piece_image = pygame.transform.scale(piece_image, (square_size, square_size))
                window.blit(piece_image, pygame.Rect(col * square_size, row * square_size, square_size, square_size))

def evaluate_board(board):
    # Simple evaluation function: material count
    material_values = {
        'P': 1, 'N': 3, 'B': 3, 'R': 5, 'Q': 9, 'K': 0,
        'p': -1, 'n': -3, 'b': -3, 'r': -5, 'q': -9, 'k': 0
    }
    white_score = 0
    black_score = 0
    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if piece:
            value = material_values[piece.symbol()]
            if piece.color == chess.WHITE:
                white_score += value
            else:
                black_score += value
    return white_score, black_score
