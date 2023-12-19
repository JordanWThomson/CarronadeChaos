import pygame
import sys

import classes
import functions
import globalVars as gv

def main():
################################################################################
#Main Setup
################################################################################
    game_run = False

    Tile_set_1 = []
    for i in range(0,10):
        Tile_x_1 = classes.Tile(i*50,0)
        Tile_set_1.append(Tile_x_1)
    Tile_set_2 = []
    for i in range(0,10):
        Tile_x_2 = classes.Tile(i*50,gv.height-50)
        Tile_set_2.append(Tile_x_2)

    Collision_set = [] #add destroyed tiles to this list, block movement.
    Explosion_set = []

    Cannon_1 = classes.Player(100, 440)
    Enemy_Cannon = classes.Enemy(400, 10)

    countertitle = 0
################################################################################
#Main Loop
################################################################################
    while True:
        gv.clock.tick(gv.fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: #Suicide
                    if game_run:
                        Cannon_1.isDestroyed = True
                        game_run = False

        if not game_run: #handle all screens
            if not Cannon_1.isDestroyed and not Enemy_Cannon.isDestroyed:
                key = pygame.key.get_pressed()
                if key[pygame.K_RETURN]:
                    game_run = True
                functions.draw_title_screen()
            elif Cannon_1.isDestroyed:
                functions.draw_defeat_screen()
                countertitle += 1
                if countertitle >= 180:
                    main()
            elif Enemy_Cannon.isDestroyed:
                functions.draw_victory_screen()
                countertitle += 1
                if countertitle >= 180:
                    main()
        else: #main game
            Enemy_Cannon.behaviour(Cannon_1.cannonballs, Cannon_1.position_x)
            Cannon_1.move_player()
            functions.off_tile_collision(Collision_set, Enemy_Cannon)
            functions.off_tile_collision(Collision_set, Cannon_1)
            functions.draw_window(Tile_set_1, Tile_set_2, Cannon_1, Enemy_Cannon, Explosion_set, Collision_set)
            for Projectile in Cannon_1.cannonballs:
                if Projectile.hitbox.colliderect(Enemy_Cannon.hitbox):
                    Enemy_Cannon.isDestroyed = True
                    game_run = False
            for Projectile in Enemy_Cannon.cannonballs:
                if Projectile.hitbox.colliderect(Cannon_1.hitbox):
                    Cannon_1.isDestroyed = True
                    game_run = False


if __name__ == "__main__":
    main()
