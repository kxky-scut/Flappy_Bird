import pygame
import sys
import random

WIDTH, HEIGHT = 400, 600
FPS = 60


class Bird:
    def __init__(self):
        self.x = 100
        self.y = HEIGHT // 2
        self.velocity = 0
        self.gravity = 0.5
        self.flap_strength = -10
        self.width = 40
        self.height = 30

    def flap(self):
        self.velocity = self.flap_strength

    def update(self):
        self.velocity += self.gravity
        self.y += self.velocity

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 0), self.get_rect())


class Pipe:
    GAP = 160
    WIDTH = 70
    SPEED = -3

    def __init__(self, x):
        self.x = x
        self.gap_y = random.randint(100, HEIGHT - 100 - self.GAP)
        self.scored = False

    def update(self):
        self.x += self.SPEED

    def is_offscreen(self):
        return self.x + self.WIDTH < 0

    def get_rects(self):
        top = pygame.Rect(self.x, 0, self.WIDTH, self.gap_y)
        bottom = pygame.Rect(self.x, self.gap_y + self.GAP, self.WIDTH, HEIGHT - self.gap_y - self.GAP)
        return top, bottom

    def draw(self, screen):
        top, bottom = self.get_rects()
        pygame.draw.rect(screen, (0, 255, 0), top)
        pygame.draw.rect(screen, (0, 255, 0), bottom)


class Game:
    STATE_START = 0
    STATE_PLAYING = 1
    STATE_GAME_OVER = 2

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Flappy Bird")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont(None, 48)
        self.small_font = pygame.font.SysFont(None, 24)
        self.reset()

    def reset(self):
        self.bird = Bird()
        self.pipes = []
        self.score = 0
        self.state = self.STATE_START
        self.frame_count = 0

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                if self.state == self.STATE_START:
                    self.state = self.STATE_PLAYING
                elif self.state == self.STATE_PLAYING:
                    self.bird.flap()
                elif self.state == self.STATE_GAME_OVER:
                    self.reset()
        return True

    def update(self):
        if self.state != self.STATE_PLAYING:
            return

        self.bird.update()
        self.frame_count += 1

        if self.frame_count % 90 == 0:
            self.pipes.append(Pipe(WIDTH))

        for pipe in self.pipes:
            pipe.update()

        self.pipes = [p for p in self.pipes if not p.is_offscreen()]

        bird_rect = self.bird.get_rect()
        for pipe in self.pipes:
            for p_rect in pipe.get_rects():
                if bird_rect.colliderect(p_rect):
                    self.state = self.STATE_GAME_OVER
                    return
            if not pipe.scored and pipe.x + Pipe.WIDTH < self.bird.x:
                pipe.scored = True
                self.score += 1

        if self.bird.y <= 0 or self.bird.y + self.bird.height >= HEIGHT:
            self.state = self.STATE_GAME_OVER

    def render(self):
        self.screen.fill((135, 206, 235))

        for pipe in self.pipes:
            pipe.draw(self.screen)
        self.bird.draw(self.screen)

        # ground line
        pygame.draw.line(self.screen, (0, 100, 0), (0, HEIGHT - 1), (WIDTH, HEIGHT - 1), 2)

        if self.state == self.STATE_START:
            title = self.font.render("Flappy Bird", True, (255, 255, 255))
            hint = self.small_font.render("Press SPACE to start", True, (255, 255, 255))
            self.screen.blit(title, (WIDTH // 2 - title.get_width() // 2, HEIGHT // 3))
            self.screen.blit(hint, (WIDTH // 2 - hint.get_width() // 2, HEIGHT // 2))
        elif self.state == self.STATE_GAME_OVER:
            over = self.font.render("Game Over", True, (255, 0, 0))
            score_text = self.small_font.render(f"Score: {self.score}", True, (255, 255, 255))
            restart = self.small_font.render("Press SPACE to restart", True, (255, 255, 255))
            self.screen.blit(over, (WIDTH // 2 - over.get_width() // 2, HEIGHT // 3))
            self.screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, HEIGHT // 2))
            self.screen.blit(restart, (WIDTH // 2 - restart.get_width() // 2, HEIGHT // 2 + 40))

        if self.state == self.STATE_PLAYING:
            score_text = self.font.render(str(self.score), True, (255, 255, 255))
            self.screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, 30))

        pygame.display.flip()

    def run(self):
        running = True
        while running:
            running = self.handle_events()
            self.update()
            self.render()
            self.clock.tick(FPS)
        pygame.quit()
        sys.exit()


def main():
    game = Game()
    game.run()


if __name__ == "__main__":
    main()
