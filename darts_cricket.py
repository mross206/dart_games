import pygame
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cricket Dart Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Fonts
font = pygame.font.SysFont(None, 40)
small_font = pygame.font.SysFont(None, 30)

# Game variables
players = ["Player 1", "Player 2"]
scores = {player: {i: 0 for i in range(15, 21)} for player in players}
total_scores = {player: 0 for player in players}
current_player = 0
input_value = ""

def draw_scoreboard():
    screen.fill(WHITE)
    
    # Draw headers
    header = font.render("Cricket Dart Game", True, BLACK)
    screen.blit(header, (WIDTH // 2 - header.get_width() // 2, 20))
    
    # Draw player names and total scores
    for i, player in enumerate(players):
        player_text = font.render(player, True, BLACK)
        total_score_text = font.render(f"Total Score: {total_scores[player]}", True, BLACK)
        screen.blit(player_text, (100 + i * 400, 100))
        screen.blit(total_score_text, (100 + i * 400, 140))
    
    # Draw score labels
    for i, score in enumerate(range(15, 21)):
        score_label = small_font.render(str(score), True, BLACK)
        screen.blit(score_label, (WIDTH // 2 - score_label.get_width() // 2, 200 + i * 50))
        
        # Draw player scores
        for j, player in enumerate(players):
            player_score = scores[player][score]
            x_center = 120 + j * 400
            y_center = 210 + i * 50

            if player_score >= 1:
                # Draw first segment of the "X"
                x1, y1 = x_center - 20, y_center - 20
                x2, y2 = x_center + 20, y_center + 20
                pygame.draw.line(screen, BLACK, (x1, y1), (x2, y2), 2)
            
            if player_score >= 2:
                # Draw second segment of the "X"
                x3, y3 = x_center - 20, y_center + 20
                x4, y4 = x_center + 20, y_center - 20
                pygame.draw.line(screen, BLACK, (x3, y3), (x4, y4), 2)
            
            if player_score >= 3:
                # Draw a circle around the "X"
                pygame.draw.circle(screen, BLACK, (x_center, y_center), 25, 2)
            else:
                player_score_text = small_font.render(str(player_score), True, BLACK)
                screen.blit(player_score_text, (100 + j * 400, 200 + i * 50))

def switch_player():
    global current_player
    current_player = (current_player + 1) % 2

def update_score(score):
    player = players[current_player]
    opponent = players[(current_player + 1) % 2]
    if score in scores[player]:
        if scores[player][score] < 3:
            scores[player][score] += 1
        elif scores[opponent][score] < 3:
            total_scores[player] += score

def handle_input(key):
    global input_value
    if key == pygame.K_RETURN:
        if input_value.isdigit():
            score = int(input_value)
            if 15 <= score <= 20:
                update_score(score)
        input_value = ""
    elif key == pygame.K_BACKSPACE:
        input_value = input_value[:-1]
    elif key in range(pygame.K_0, pygame.K_9 + 1):
        input_value += pygame.key.name(key)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                switch_player()
            else:
                handle_input(event.key)
    
    draw_scoreboard()

    # Display input value with player prompt
    player_prompt = f"{players[current_player]} - Enter your scores: {input_value}"
    input_text = font.render(player_prompt, True, BLACK)
    screen.blit(input_text, (WIDTH // 2 - input_text.get_width() // 2, HEIGHT - 50))

    pygame.display.flip()

pygame.quit()
sys.exit()
