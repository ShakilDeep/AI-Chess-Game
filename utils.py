import pygame

def initialize_game_window():
    """
    Initialize the Pygame window for the chess game.
    
    Returns:
    window (pygame.Surface): The Pygame window surface.
    width (int): The width of the window.
    height (int): The height of the window.
    """
    width, height = 800, 800
    window = pygame.display.set_mode((width, height))
    return window, width, height

def display_evaluation_results(window, move_count_bot1, move_count_bot2, score):
    """
    Display the evaluation results and move counts on the game window.
    
    Parameters:
    window (pygame.Surface): The Pygame window surface.
    move_count_bot1 (int): The total number of moves made by bot 1.
    move_count_bot2 (int): The total number of moves made by bot 2.
    score (int): The current evaluation score of the board.
    """
    font = pygame.font.SysFont(None, 24)
    text_color = (0, 0, 0)  # Black color for text

    # Display move counts
    move_text_bot1 = font.render(f'Bot 1 Moves: {move_count_bot1}', True, text_color)
    move_text_bot2 = font.render(f'Bot 2 Moves: {move_count_bot2}', True, text_color)
    score_text = font.render(f'Score: {score}', True, text_color)

    # Positioning the text on the window
    window.blit(move_text_bot1, (10, 10))
    window.blit(move_text_bot2, (10, 40))
    window.blit(score_text, (10, 70))
