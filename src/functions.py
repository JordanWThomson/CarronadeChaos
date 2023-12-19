import pygame

import classes
import globalVars as gv


################################################################################
#General Functions
################################################################################
def draw_title_screen():
    gv.window.fill((0,0,0))
    gv.window.blit(gv.titleText, ((gv.width - gv.titleText.get_width())/2,150))
    gv.window.blit(gv.pressEnterToStartText, ((gv.width - gv.pressEnterToStartText.get_width())/2,250))
    #gv.window.blit(gv.Text_Title, ((gv.width - gv.Text_Title.get_width())/2,150))
    #gv.window.blit(gv.Text_Press_Enter, ((gv.width - gv.Text_Press_Enter.get_width())/2,250))
    pygame.display.update()

def draw_victory_screen():
    gv.window.fill((0,0,0))
    gv.window.blit(gv.Text_Victory, ((gv.width - gv.Text_Victory.get_width())/2,220))
    pygame.display.update()

def draw_defeat_screen():
    gv.window.fill((0,0,0))
    gv.window.blit(gv.Text_Defeat, ((gv.width - gv.Text_Defeat.get_width())/2,220))
    pygame.display.update()

def off_tile_collision(Collision_list, Entity): #keep entity on the tiles.
    for Collision_rect in Collision_list:
        if Entity.hitbox.colliderect(Collision_rect.hitbox):
            if Entity.position_x < Collision_rect.position_x: #collide from right
                Entity.position_x = Collision_rect.position_x - 50
            else: #from left
                Entity.position_x = Collision_rect.position_x + 50

def draw_window(Tile_set_1, Tile_set_2, Cannon_1, Enemy_Cannon, Explosion_set, Collision_set):
    gv.window.blit(gv.Background_IMG, (0,0))

    for Tile in Tile_set_1:
        Tile.draw_tile(gv.window)
    for Tile in Tile_set_2:
        Tile.draw_tile(gv.window)

    for Cannonball_P in Cannon_1.cannonballs:
        Cannonball_P.move_cannonball()
        Cannonball_P.draw_cannonball(gv.window)
        if Cannonball_P.isDestroyed == True:
            Explosion_x = classes.Explosion(Cannonball_P.position_x - 25, Cannonball_P.position_y - 25)
            Explosion_set.append(Explosion_x)
            Cannon_1.cannonballs.pop(Cannon_1.cannonballs.index(Cannonball_P))
        if Cannonball_P.position_y < 0-50:
            Cannon_1.cannonballs.pop(Cannon_1.cannonballs.index(Cannonball_P))
        for Tile in Tile_set_1:
            if Cannonball_P.hitbox.colliderect(Tile.hitbox):
                Cannonball_P.isDestroyed = True
                Tile.health -= 1
                if Tile.health == 0:
                    Collision_set.append(Tile)
                    Tile_set_1.remove(Tile)

    for Cannonball_E in Enemy_Cannon.cannonballs:
        Cannonball_E.move_cannonball()
        Cannonball_E.draw_cannonball(gv.window)
        if Cannonball_E.isDestroyed == True:
            Explosion_x = classes.Explosion(Cannonball_E.position_x - 25, Cannonball_E.position_y - 25)
            Explosion_set.append(Explosion_x)
            Enemy_Cannon.cannonballs.pop(Enemy_Cannon.cannonballs.index(Cannonball_E))
        if Cannonball_E.position_y < 0-50:
            Enemy_Cannon.cannonballs.pop(Enemy_Cannon.cannonballs.index(Cannonball_E))
        for Tile in Tile_set_2:
            if Cannonball_E.hitbox.colliderect(Tile.hitbox):
                Cannonball_E.isDestroyed = True
                Tile.health -= 1
                if Tile.health == 0:
                    Collision_set.append(Tile)
                    Tile_set_2.remove(Tile)

    for Explosions in Explosion_set:
        Explosions.explode(gv.window)
        if Explosions.animation_counter == 25:
            Explosion_set.remove(Explosions)

    Enemy_Cannon.draw_enemy(gv.window)
    Cannon_1.draw_player(gv.window)

    pygame.display.update()