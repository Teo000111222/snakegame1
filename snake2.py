import pygame as pg

# Initialize Pygame
pg.init()

# Define constants and initial values
y, step, head = segments = [15, 16, 17]
n, apple = step, 99
screen = pg.display.set_mode([225]*2, pg.SCALED)
screen_fill = screen.fill
font = pg.font.Font(None, 36)  # Define font for the scoreboard
score = 0  # Initialize the score

# Main game loop
while segments.count(head) % 2 * head % n * (head & 240):
    if e := pg.event.get(768):
        step = (e[0].key % 4 * 17 + 15) % 49 - n
    segments = segments[apple != head:] + [head + step]

    screen_fill("black")

    if apple == head:
        score += 1  # Increase the score when the apple is eaten
        apple = segments[0]
    
    for i, v in enumerate([apple] + segments):
        screen_fill("green" if i else "red",
                    ((v - 1) % n * y, (v - n) // n * y, y, y))
    
    # Render and display the score
    score_surface = font.render(f'Score: {score}', True, (255, 255, 255))
    screen.blit(score_surface, (10, 10))
    
    pg.display.flip()
    head += step
    pg.time.wait(100)

pg.quit()