# Importiere das Pygame-Modul
import pygame

# Initialisiere Pygame
pygame.init()

# Definiere einige Konstanten für das Spiel
SCREEN_WIDTH = 800 # Die Breite des Bildschirms
SCREEN_HEIGHT = 600 # Die Höhe des Bildschirms
PADDLE_WIDTH = 20 # Die Breite der Schläger
PADDLE_HEIGHT = 100 # Die Höhe der Schläger
BALL_RADIUS = 10 # Der Radius des Balls
MAX_SCORE = 10 # Die maximale Punktzahl, um das Spiel zu gewinnen
BLACK = (0, 0, 0) # Die Farbe Schwarz
WHITE = (255, 255, 255) # Die Farbe Weiß
FONT_SIZE = 32 # Die Schriftgröße für den Punktestand

# Erstelle ein Fenster, um das Spiel anzuzeigen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Setze den Titel des Fensters
pygame.display.set_caption("Pong Spiel in Python")

# Erstelle eine Uhr, um die Bildwiederholrate zu steuern
clock = pygame.time.Clock()

# Erstelle eine Schriftart, um den Punktestand anzuzeigen
font = pygame.font.SysFont("Arial", FONT_SIZE)

# Definiere einige Variablen für das Spiel
left_score = 0 # Die Punktzahl des linken Spielers
right_score = 0 # Die Punktzahl des rechten Spielers
left_paddle_y = SCREEN_HEIGHT / 2 - PADDLE_HEIGHT / 2 # Die Y-Position des linken Schlägers
right_paddle_y = SCREEN_HEIGHT / 2 - PADDLE_HEIGHT / 2 # Die Y-Position des rechten Schlägers
ball_x = SCREEN_WIDTH / 2 # Die X-Position des Balls
ball_y = SCREEN_HEIGHT / 2 # Die Y-Position des Balls
ball_dx = -4 # Die X-Richtung des Balls
ball_dy = 4 # Die Y-Richtung des Balls
left_up = False # Ob die W-Taste gedrückt ist
left_down = False # Ob die S-Taste gedrückt ist
right_up = False # Ob die Pfeiltaste nach oben gedrückt ist
right_down = False # Ob die Pfeiltaste nach unten gedrückt ist
game_over = False # Ob das Spiel zu Ende ist

# Definiere eine Funktion, um das Spiel zu aktualisieren
def update():
    # Greife auf die globalen Variablen zu
    global left_score, right_score, left_paddle_y, right_paddle_y, ball_x, ball_y, ball_dx, ball_dy, left_up, left_down, right_up, right_down, game_over

    # Bewege die Schläger entsprechend den gedrückten Tasten
    if left_up:
        left_paddle_y -= 5
    if left_down:
        left_paddle_y += 5
    if right_up:
        right_paddle_y -= 5
    if right_down:
        right_paddle_y += 5

    # Begrenze die Schläger innerhalb des Bildschirms
    if left_paddle_y < 0:
        left_paddle_y = 0
    if left_paddle_y > SCREEN_HEIGHT - PADDLE_HEIGHT:
        left_paddle_y = SCREEN_HEIGHT - PADDLE_HEIGHT
    if right_paddle_y < 0:
        right_paddle_y = 0
    if right_paddle_y > SCREEN_HEIGHT - PADDLE_HEIGHT:
        right_paddle_y = SCREEN_HEIGHT - PADDLE_HEIGHT

    # Bewege den Ball entsprechend seiner Richtung
    ball_x += ball_dx
    ball_y += ball_dy

    # Prüfe, ob der Ball die Wände berührt
    if ball_y < BALL_RADIUS:
        # Der Ball berührt die obere Wand
        ball_y = BALL_RADIUS
        ball_dy = -ball_dy
    if ball_y > SCREEN_HEIGHT - BALL_RADIUS:
        # Der Ball berührt die untere Wand
        ball_y = SCREEN_HEIGHT - BALL_RADIUS
        ball_dy = -ball_dy

    # Prüfe, ob der Ball die Schläger berührt
    if ball_x < PADDLE_WIDTH + BALL_RADIUS:
        # Der Ball ist auf der linken Seite
        if ball_y > left_paddle_y and ball_y < left_paddle_y + PADDLE_HEIGHT:
            # Der Ball berührt den linken Schläger
            ball_x = PADDLE_WIDTH + BALL_RADIUS
            ball_dx = -ball_dx * 1.1 # Erhöhe die Geschwindigkeit des Balls
            ball_dy = ball_dy * 1.1 + (pygame.math.Vector2(ball_dx, ball_dy).reflect(pygame.math.Vector2(0, 1)).y - ball_dy) / 2 # Ändere die Richtung des Balls
        else:
            # Der Ball geht am linken Schläger vorbei
            right_score += 1 # Erhöhe die Punktzahl des rechten Spielers
            reset_ball() # Setze den Ball zurück
    if ball_x > SCREEN_WIDTH - PADDLE_WIDTH - BALL_RADIUS:
        # Der Ball ist auf der rechten Seite
        if ball_y > right_paddle_y and ball_y < right_paddle_y + PADDLE_HEIGHT:
            # Der Ball berührt den rechten Schläger
            ball_x = SCREEN_WIDTH - PADDLE_WIDTH - BALL_RADIUS
            ball_dx = -ball_dx * 1.1 # Erhöhe die Geschwindigkeit des Balls
            ball_dy = ball_dy * 1.1 + (pygame.math.Vector2(ball_dx, ball_dy).reflect(pygame.math.Vector2(0, 1)).y - ball_dy) / 2 # Ändere die Richtung des Balls
        else:
            # Der Ball geht am rechten Schläger vorbei
            left_score += 1 # Erhöhe die Punktzahl des linken Spielers
            reset_ball() # Setze den Ball zurück

    # Prüfe, ob das Spiel zu Ende ist
    if left_score == MAX_SCORE or right_score == MAX_SCORE:
        # Ein Spieler hat die maximale Punktzahl erreicht
        game_over = True # Setze das Spiel auf beendet

# Definiere eine Funktion, um das Spiel zu zeichnen
def draw():
    # Greife auf die globalen Variablen zu
    global left_score, right_score, left_paddle_y, right_paddle_y, ball_x, ball_y, game_over

    # Lösche den Bildschirm
    screen.fill(BLACK)

    # Zeichne die Schläger
    pygame.draw.rect(screen, WHITE, (0, left_paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.rect(screen, WHITE, (SCREEN_WIDTH - PADDLE_WIDTH, right_paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT))

    # Zeichne den Ball
    pygame.draw.circle(screen, WHITE, (int(ball_x), int(ball_y)), BALL_RADIUS)

    # Zeichne den Punktestand
    score_text = font.render(str(left_score) + " : " + str(right_score), True, WHITE)
    score_rect = score_text.get_rect(center=(SCREEN_WIDTH / 2, FONT_SIZE / 2))
    screen.blit(score_text, score_rect)

    # Zeichne eine Nachricht, wenn das Spiel zu Ende ist
    if game_over:
        game_over_text = font.render("Das Spiel ist zu Ende. Der Gewinner ist " + ("links" if left_score == MAX_SCORE else "rechts") + ".", True, WHITE)
        game_over_rect = game_over_text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        screen.blit(game_over_text, game_over_rect)

    # Aktualisiere den Bildschirm
