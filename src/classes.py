import pygame
import globalVars as gv

################################################################################
#Classes
################################################################################
#Effects
class Explosion(object):
    def __init__(self, position_x, position_y):
        self.position_x = position_x
        self.position_y = position_y
        self.animation_counter = 0

    def explode(self, window):
        if self.animation_counter > 0 and self.animation_counter < 5:
            window.blit(gv.Explosion_1_IMG, (self.position_x, self.position_y))
        elif self.animation_counter >= 5 and self.animation_counter < 10:
            window.blit(gv.Explosion_2_IMG, (self.position_x, self.position_y))
        elif self.animation_counter >= 5 and self.animation_counter < 10:
            window.blit(Egv.xplosion_3_IMG, (self.position_x, self.position_y))
        elif self.animation_counter >= 10 and self.animation_counter < 15:
            window.blit(gv.Explosion_4_IMG, (self.position_x, self.position_y))
        elif self.animation_counter >= 15 and self.animation_counter < 20:
            window.blit(gv.Explosion_5_IMG, (self.position_x, self.position_y))
        elif self.animation_counter >= 20 and self.animation_counter < 25:
            window.blit(gv.Explosion_6_IMG, (self.position_x, self.position_y))
        else:
            self.animation_counter = 0
            gv.Sound_Explosion.play()
        self.animation_counter += 1


#Tile class
class Tile(object):
    def __init__(self, position_x, position_y):
        self.position_x = position_x
        self.position_y = position_y
        self.hitbox = pygame.Rect(self.position_x, self.position_y, 50, 50)
        self.health = 5

    def draw_tile(self, window):
        if self.position_y > 250:
            if self.health == 5:
                window.blit(gv.Deck_IMG, (self.position_x, self.position_y))
            elif self.health < 5 and self.health > 2:
                window.blit(gv.Deck_Dam_1_IMG, (self.position_x, self.position_y))
            elif self.health <= 2:
                window.blit(gv.Deck_Dam_2_IMG, (self.position_x, self.position_y))
        else:
            if self.health == 5:
                window.blit(gv.Deck_IMG_reversed, (self.position_x, self.position_y))
            elif self.health < 5 and self.health > 2:
                window.blit(gv.Deck_Dam_1_IMG_reversed, (self.position_x, self.position_y))
            elif self.health <= 2:
                window.blit(gv.Deck_Dam_2_IMG_reversed, (self.position_x, self.position_y))

#Projectile class
class Cannonball(object):
    def __init__(self, position_x, position_y):
        self.position_x = position_x
        self.position_y = position_y
        self.hitbox = pygame.Rect(self.position_x, self.position_y, 50, 50)
        self.velocity = 10
        self.animation_counter = 0
        self.isDestroyed = False

    def move_cannonball(self):
        self.position_y -= self.velocity
        self.hitbox = pygame.Rect(self.position_x, self.position_y, 50, 50)

    def draw_cannonball(self, window):
        if self.isDestroyed == 0:
            if self.animation_counter > 11:
                self.animation_counter = 0
            else:
                self.animation_counter += 1

            if self.animation_counter < 3:
                window.blit(gv.CannonBall_IMG, (self.position_x, self.position_y))
            elif self.animation_counter >= 3 and self.animation_counter < 6:
                window.blit(gv.CannonBall_IMG2, (self.position_x, self.position_y))
            elif self.animation_counter >= 6 and self.animation_counter < 9:
                window.blit(gv.CannonBall_IMG3, (self.position_x, self.position_y))
            elif self.animation_counter >= 9:
                window.blit(gv.CannonBall_IMG4, (self.position_x, self.position_y))


#        pygame.draw.rect(window, (255,255,0), self.hitbox)

#Player class
class Player(object):
    def __init__(self, position_x, position_y):
        self.position_x = position_x
        self.position_y = position_y
        self.hitbox = None
        self.isDestroyed = False
        self.cannonball = None
        self.cannonballs = [] #empty list for projectiles
        self.cooldown_timer = 0
        self.velocity = 5
        self.firing = False
        self.animation_counter = 0

    def draw_player(self, window):
#        pygame.draw.rect(window, (255,0,0), self.hitbox)
        if self.firing == True:
            self.animation_counter += 1
            window.blit(gv.CannonFiring_IMG, (self.position_x, self.position_y))
            if self.animation_counter > 10:
                self.animation_counter = 0
                self.cooldown_timer += 1
                self.firing = False
                Cannonball_x = Cannonball(self.position_x, gv.height - 100)
                self.cannonballs.append(Cannonball_x)
                gv.Sound_Fire.play()
        else:
            window.blit(gv.Cannon_IMG, (self.position_x, self.position_y))
            if self.cooldown_timer > 0:
                self.cooldown_timer += 1
                if self.cooldown_timer >= 60:
                    self.cooldown_timer = 0

    def move_player(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] and self.position_x > 0:
            self.position_x -= self.velocity
        if key[pygame.K_RIGHT] and self.position_x < gv.width - 50:
            self.position_x += self.velocity
        if key[pygame.K_SPACE] and self.cooldown_timer == 0:
            self.firing = True

        self.hitbox = pygame.Rect(self.position_x, self.position_y, 50, 50) #update hitbox location


class Enemy(object):
    def __init__(self, position_x, position_y):
        self.position_x = position_x
        self.position_y = position_y
        self.hitbox = None
        self.isDestroyed = False
        self.cannonballs = []
        self.velocity = 3
        self.cooldown_timer = 0
        self.animation_counter = 0
        self.firing = False

    def draw_enemy(self, window):
        if self.firing == True:
            self.animation_counter += 1
            window.blit(gv.CannonFiring_IMG_reversed, (self.position_x, self.position_y))
            if self.animation_counter > 10:
                self.animation_counter = 0
                self.firing = False
                Cannonball_x = Cannonball(self.position_x, 100)
                Cannonball_x.velocity *= -1
                self.cannonballs.append(Cannonball_x)
                gv.Sound_Fire.play()
        else:
            window.blit(gv.Cannon_IMG_reversed, (self.position_x, self.position_y))

    def follow_player(self, player_pos_x):
        if abs(player_pos_x - self.position_x) > 5:
            if player_pos_x < self.position_x:
                self.position_x -= self.velocity
            else:
                self.position_x += self.velocity
        else:
            if self.cooldown_timer == 0:
                self.firing = True
                self.cooldown_timer += 1

    def avoid_cannonball(self, cannonball_pos_x):
            if cannonball_pos_x < self.position_x: #if cannonball is to the left of enemy...
                self.position_x += self.velocity
            else:
                self.position_x -= self.velocity

    def behaviour(self, cannonball_list, player_pos_x):
        if self.position_x < 0:
            self.position_x = 0
        elif self.position_x > gv.width - 50:
            self.position_x = gv.width - 50
        else: #if on screen...
            if len(cannonball_list) == 0: #if player has fired no cannonballs...
                Enemy.follow_player(self, player_pos_x)
            else:
                for cannonball_object in cannonball_list:
                    if abs(cannonball_object.position_x - self.position_x) < 80:
                        Enemy.avoid_cannonball(self, cannonball_object.position_x)
                    else:
                        Enemy.follow_player(self, player_pos_x)

        if self.cooldown_timer > 0:
            self.cooldown_timer += 1
            if self.cooldown_timer >= 90:
                self.cooldown_timer = 0

        self.hitbox = pygame.Rect(self.position_x, self.position_y, 50, 50) #update hitbox location