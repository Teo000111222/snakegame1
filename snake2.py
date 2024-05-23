import pygame as pg

# Nastavimo Pygame, da bo delal svoje fore
pg.init()

# Tle shranimo začetno pozicijo kače in kako daleč se bo premikala
y, step, head = segments = [15, 16, 17] 
# Velikost naše igralske površine in kje je sprva jabolko
n, apple = step, 99 
# Ekran, na katerem se bo vse odvijalo
screen = pg.display.set_mode([225]*2, pg.SCALED)
# Zapolnimo ekran z barvo
screen_fill = screen.fill
# Pisava za prikaz rezultata
font = pg.font.Font(None, 36)
# Rezultat
score = 0  

# Glavna zanka igre
while segments.count(head) % 2 * head % n * (head & 240): 
    # Če se je nekaj pritisnilo na tipkovnici...
    if events := pg.event.get(pg.KEYDOWN):
        # ...ugotovimo, kam naj gre kača
        step = (events[0].key % 4 * 17 + 15) % 49 - n 
    # Premaknemo kačo za en korak
    segments = segments[apple != head:] + [head + step]  
    
    # Pozadje ekrana naredimo črno
    screen_fill("black")
    
    # Če je kača pojedla jabolko...
    if apple == head:
        score += 1 
        # ...premaknemo jabolko na novo mesto
        apple = segments[0] 
    
    # Narišemo kačo in jabolko na ekran
    for i, v in enumerate([apple] + segments):
        # Jabolko je zeleno, kača pa rdeča
        screen_fill("green" if i else "red",
                    ((v - 1) % n * y, (v - n) // n * y, y, y))
    
    # Prikaz rezultata na ekranu
    score_surface = font.render(f'Score: {score}', True, (255, 255, 255))
    screen.blit(score_surface, (10, 10))
    
    # Pokažemo, kaj smo naredili na ekranu
    pg.display.flip()  
    # Premaknemo glavo kače za en korak
    head += step 
    # Pocakamo trenutek preden nadaljujemo
    pg.time.wait(100)

# Končamo s Pygame
pg.quit()
