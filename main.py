import pygame
import random

from particle import Particle

pygame.init()

WIDTH = 800
HEIGHT = 800
window = pygame.display.set_mode((WIDTH, HEIGHT))

BLACK = (51, 51, 51)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)


def main():
    attractors = []
    particles = []
    clock = pygame.time.Clock()
    running = True

    while running:
        window.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                attractors.append(pygame.Vector2(mx, my))

        particles.append(Particle(random.randint(0, WIDTH), random.randint(0, HEIGHT)))

        if len(particles) > 100:
            particles.pop(0)

        for attractor in attractors:
            pygame.draw.circle(window, GREEN, (int(attractor.x), int(attractor.y)), 4)

        for particle in particles:
            for attractor in attractors:
                particle.attracted(attractor)
            particle.update()
            particle.show(window)

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()


if __name__ == "__main__":
    main()
