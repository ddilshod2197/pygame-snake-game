import pygame
import sys
import random

# Pygame ni ishga tushirish
pygame.init()

# Ekran kattaligi
ekran_kattaligi = (800, 600)

# Ekran yaratish
ekran = pygame.display.set_mode(ekran_kattaligi)

# Sarlavha yaratish
pygame.display.set_caption("Ilon o'yini")

# Ranglar
oq = (255, 255, 255)
qizil = (255, 0, 0)
yashil = (0, 255, 0)

# Ilon uzunligi
ilon_uzunligi = 1

# Ilon joylashuvi
ilon_joylashuvi = [(400, 300)]

# Taom joylashuvi
taom_joylashuvi = (random.randint(0, ekran_kattaligi[0] - 20) // 20 * 20, random.randint(0, ekran_kattaligi[1] - 20) // 20 * 20)

# Ilon harakatini boshlash
harakat = "chapga"

# Frame rate
frame_rate = 10

# Frame rate ni boshlash
clock = pygame.time.Clock()

# O'yin davomiyligi
davomiyligi = True

while davomiyligi:
    # Frame rate ni boshlash
    clock.tick(frame_rate)

    # Kiritilgan tugmalar
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            davomiyligi = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and harakat != "pastga":
                harakat = "yuqoriga"
            elif event.key == pygame.K_DOWN and harakat != "yuqoriga":
                harakat = "pastga"
            elif event.key == pygame.K_LEFT and harakat != "o'nga":
                harakat = "chapga"
            elif event.key == pygame.K_RIGHT and harakat != "chapga":
                harakat = "o'nga"

    # Ilon harakatini o'zgartirish
    if harakat == "yuqoriga":
        ilon_joylashuvi.append((ilon_joylashuvi[-1][0], ilon_joylashuvi[-1][1] - 20))
    elif harakat == "pastga":
        ilon_joylashuvi.append((ilon_joylashuvi[-1][0], ilon_joylashuvi[-1][1] + 20))
    elif harakat == "chapga":
        ilon_joylashuvi.append((ilon_joylashuvi[-1][0] - 20, ilon_joylashuvi[-1][1]))
    elif harakat == "o'nga":
        ilon_joylashuvi.append((ilon_joylashuvi[-1][0] + 20, ilon_joylashuvi[-1][1]))

    # Taom joylashuvi
    if ilon_joylashuvi[-1] == taom_joylashuvi:
        ilon_uzunligi += 1
        taom_joylashuvi = (random.randint(0, ekran_kattaligi[0] - 20) // 20 * 20, random.randint(0, ekran_kattaligi[1] - 20) // 20 * 20)

    # Ilon uzunligi cheklovchi
    if ilon_joylashuvi[-1] in ilon_joylashuvi[:-1]:
        davomiyligi = False

    # Ekranni o'zgartirish
    ekran.fill(oq)
    for joylashuvi in ilon_joylashuvi:
        pygame.draw.rect(ekran, yashil, (joylashuvi[0], joylashuvi[1], 20, 20))
    pygame.draw.rect(ekran, qizil, (taom_joylashuvi[0], taom_joylashuvi[1], 20, 20))

    # Ekranni ko'rsatish
    pygame.display.update()

# O'yin tugashi
pygame.quit()
sys.exit()
