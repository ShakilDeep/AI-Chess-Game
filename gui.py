import pygame

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT_BROWN = (240, 217, 181)
DARK_BROWN = (181, 136, 99)

def initialize_game_window():
    width, height = 800, 800
    window = pygame.display.set_mode((width, height))
    return window, width, height

def display_evaluation_results(window, move_count_bot1, move_count_bot2, score):
    font = pygame.font.SysFont(None, 24)
    text_color = BLACK

    move_text_bot1 = font.render(f'Bot 1 Moves: {move_count_bot1}', True, text_color)
    move_text_bot2 = font.render(f'Bot 2 Moves: {move_count_bot2}', True, text_color)
    window.blit(move_text_bot1, (10, 10))
    window.blit(move_text_bot2, (10, 40))

    score_text = font.render(f'Board Evaluation: {score}', True, text_color)
    window.blit(score_text, (10, 70))

def display_game_result(window, result):
    font = pygame.font.SysFont(None, 36)
    text_color = (255, 0, 0)  # Red color
    width, height = window.get_size()

    result_text = font.render(result, True, text_color)
    text_rect = result_text.get_rect(center=(width // 2, height - 30))
    window.blit(result_text, text_rect)
    pygame.display.flip()
