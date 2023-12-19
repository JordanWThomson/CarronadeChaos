import pygame
import os

pygame.font.init()
pygame.mixer.init()

#Window/Setup
width = 500
height = 500
window = pygame.display.set_mode((width,height))
pygame.display.set_caption("CARRONADE CHAOS")
clock = pygame.time.Clock()
fps = 60

################################################################################
#Images/assets
################################################################################
PixelFontLarge = pygame.font.Font("../assets/PixeloidSans-nR3g1.ttf", 50)
PixelFontSmall = pygame.font.Font("../assets/PixeloidSans-nR3g1.ttf", 40)

titleText = PixelFontLarge.render("CARRONADE CHAOS", True, 'white')
pressEnterToStartText = PixelFontSmall.render("press 'enter'", True, 'white')

dualText = PixelFontSmall.render("Dual", True, 'white')
krakattackText = PixelFontSmall.render("Krak-Attack", True, 'white')

Font_ariel_small = pygame.font.SysFont("ariel", 50) #define the font.
Font_ariel_large = pygame.font.SysFont("ariel", 90)

Text_Title = Font_ariel_large.render("BROADSIDER", 1, (255,255,255))
Text_Press_Enter = Font_ariel_large.render("Press Enter", 1, (255,255,255))
Text_Victory = Font_ariel_small.render("Victory", 1, (255,255,255))
Text_Defeat = Font_ariel_small.render("Defeat", 1, (255,255,255))

Sound_Fire = pygame.mixer.Sound(os.path.join("../assets", "CannonFire.mp3"))
Sound_Explosion = pygame.mixer.Sound(os.path.join("../assets", "CannonExplosion.mp3"))

Background_IMG = pygame.image.load(os.path.join("../assets", "Background.png")).convert_alpha()

Deck_IMG = pygame.image.load(os.path.join("../assets", "DeckTile.png")).convert_alpha()
Deck_Dam_1_IMG = pygame.image.load(os.path.join("../assets", "DeckTileDamaged_1.png")).convert_alpha()
Deck_Dam_2_IMG = pygame.image.load(os.path.join("../assets", "DeckTileDamaged_2.png")).convert_alpha()
Deck_IMG_reversed = pygame.transform.flip(Deck_IMG, False, True)
Deck_Dam_1_IMG_reversed = pygame.transform.flip(Deck_Dam_1_IMG, False, True)
Deck_Dam_2_IMG_reversed = pygame.transform.flip(Deck_Dam_2_IMG, False, True)

Cannon_IMG = pygame.image.load(os.path.join("../assets", "BroadsiderTall.png")).convert_alpha()
Cannon_IMG_reversed = pygame.transform.flip(Cannon_IMG, False, True)
CannonFiring_IMG = pygame.image.load(os.path.join("../assets", "BroadsiderWide.png")).convert_alpha()
CannonFiring_IMG_reversed = pygame.transform.flip(CannonFiring_IMG, False, True)
CannonBall_IMG = pygame.image.load(os.path.join("../assets", "Cannonball.png")).convert_alpha()
CannonBall_IMG2 = pygame.transform.flip(CannonBall_IMG, True, False)
CannonBall_IMG3 = pygame.transform.flip(CannonBall_IMG, True, True)
CannonBall_IMG4 = pygame.transform.flip(CannonBall_IMG, False, True)

Explosion_1_IMG = pygame.image.load(os.path.join("../assets", "Explosion_1.png")).convert_alpha()
Explosion_2_IMG = pygame.image.load(os.path.join("../assets", "Explosion_2.png")).convert_alpha()
Explosion_3_IMG = pygame.image.load(os.path.join("../assets", "Explosion_3.png")).convert_alpha()
Explosion_4_IMG = pygame.image.load(os.path.join("../assets", "Explosion_4.png")).convert_alpha()
Explosion_5_IMG = pygame.image.load(os.path.join("../assets", "Explosion_5.png")).convert_alpha()
Explosion_6_IMG = pygame.image.load(os.path.join("../assets", "Explosion_6.png")).convert_alpha()


pygame.display.set_icon(Cannon_IMG)