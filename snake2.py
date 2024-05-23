import pygame as pg

# Inicializacija Pygame
pg.init()


y, step, head = segments = [15, 16, 17] # Začetna lokacija kače
n, apple = step, 99 # Nastavitev velikosti igralne površine in začetno lokacijo jabolka
screen = pg.display.set_mode([225]*2, pg.SCALED)
screen_fill = screen.fill
font = pg.font.Font(None, 36) 
score = 0  

# glavna zanka igre
while segments.count(head) % 2 * head % n * (head & 240): # Preveri in obdelaj dogodke tipkovnice
    if e := pg.event.get(768):
        step = (e[0].key % 4 * 17 + 15) % 49 - n # Določi smer premika kače
    segments = segments[apple != head:] + [head + step]  # Premakni kačo

    screen_fill("black")
# Preveri, če je kača pojedla jabolko
    if apple == head:
        score += 1 
        apple = segments[0] # Premakni jabolko na mesto prvega segmenta kače
    # Narisaj kačo in jabolko na zaslon
    for i, v in enumerate([apple] + segments):
        screen_fill("green" if i else "red",
                    ((v - 1) % n * y, (v - n) // n * y, y, y))
    
    # Prikaži rezultat na zaslonu
    score_surface = font.render(f'Score: {score}', True, (255, 255, 255))
    screen.blit(score_surface, (10, 10))
    
    pg.display.flip()  # Prikazi spremembe na zaslonu
    head += step # Premakni glavo kače
    pg.time.wait(100)

pg.quit()
