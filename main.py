import pygame
import sys
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, ASTEROID_MAX_RADIUS, ASTEROID_MIN_RADIUS, ASTEROID_MED_RADIUS
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print(f"Starting Asteroids with pygame verison: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    Clock = pygame.time.Clock()
    dt = 0

    score = 0


    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    asteroids = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    
    AsteroidField.containers = (updatable)
    asteroidfield = AsteroidField()

    shots = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)
    

    while True:
        log_state()

        for event in pygame.event.get():
            if event.type  == pygame.QUIT:
                return

        screen.fill("black")
        
        updatable.update(dt)
        
        for asteroid in asteroids:
            if asteroid.collides_with(player) == True:
                log_event("player_hit")

                print("Game over!")

                sys.exit()

        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collides_with(shot) == True:
                    log_event("asteroid_shot")
                    shot.kill()

                    if asteroid.radius <= ASTEROID_MIN_RADIUS:
                        score += 500

                    if asteroid.radius <= ASTEROID_MED_RADIUS and asteroid.radius > ASTEROID_MIN_RADIUS:
                        score += 300

                    if asteroid.radius > ASTEROID_MED_RADIUS:
                        score += 100

                    print(score)
                    asteroid.split()
                    


        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        Clock.tick(60) 
        dt = Clock.tick(60) / 1000






















if __name__ == "__main__":
    main()
