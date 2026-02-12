import pygame
import random
import math

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
pygame.display.set_caption("Clickable Fireworks")
COLOR_PALETTES = [
    (255, 80, 80),     # red
    (80, 255, 80),     # green
    (80, 80, 255),     # blue
    (255, 255, 80),    # yellow
    (255, 120, 255),   # pink/purple
    (120, 255, 255),   # cyan
    (255, 140, 0),     # orange
    (255, 20, 147),    # deep pink
    (138, 43, 226),    # blue violet
    (0, 191, 255),     # deep sky blue
    (173, 255, 47),    # green yellow
    (255, 105, 180),   # hot pink
    (186, 85, 211),    # medium orchid
    (240, 128, 128),   # light coral
    (255, 215, 0),     # gold
    (64, 224, 208),    # turquoise
    "MIXED"            # Special mixed-color mode
]
class Spark:
    def __init__(self, x, y, base_color):
        # Random direction
        angle = random.uniform(0, 2 * math.pi)
        speed = random.uniform(2, 8)
        self.x = x
        self.y = y

        # Polar
        self.vx = math.cos(angle) * speed
        self.vy = math.sin(angle) * speed

        # Particle life time
        self.life = random.randint(20, 90)
        self.max_life = self.life
        self.color = tuple(
            max(0, min(255, c + random.randint(-40, 40)))
            for c in base_color
        )
        # Render
        self.surface = pygame.Surface((5, 5), pygame.SRCALPHA)
        pygame.draw.circle(self.surface, self.color, (3, 3), 3)

    def update_motion(self):
        # Air resistence
        self.vx *= 0.99

        # Apply gravity
        self.vy = self.vy * 0.99 + 0.1
        
        # Update position
        self.x += self.vx
        self.y += self.vy

        # Change life time
        self.life -= 1

    def draw_spark(self, surface):
        if self.life <= 0:
            return    
        # Transparency control --> linear interpolation
        alpha = int(255 * (self.life / self.max_life))
        s = self.surface.copy()
        s.set_alpha(alpha)
        surface.blit(s, (self.x, self.y))
class Firework:
    def __init__(self, x, y):
        base_color = random.choice(COLOR_PALETTES)
        # Mixed-color starting with high brightness color (150-255)
        if base_color == "MIXED":
            self.sparks = [Spark(x, y,( random.randint(150, 255), random.randint(150, 255), random.randint(150, 255))) for _ in range(140)]
        else:
            # Single-color
            self.sparks = [Spark(x, y, base_color) for _ in range(250)]
    def update_spark(self):
        for s in self.sparks:
            s.update_motion()
        self.sparks = [s for s in self.sparks if s.life > 0]
    def spawn(self, surface):
        for s in self.sparks:
            s.draw_spark(surface)

if __name__ == "__main__": 
    fireworks = [] 
    running = True 
    while running: 
        screen.fill((0, 0, 0)) 
        for event in pygame.event.get(): 
            if event.type == pygame.MOUSEBUTTONDOWN: 
                x, y = pygame.mouse.get_pos() 
                fireworks.append(Firework(x, y))
            if event.type == pygame.QUIT: running = False 
        for fw in fireworks: 
                fw.update_spark() 
                fw.spawn(screen) 
        fireworks = [fw for fw in fireworks if fw.sparks]
        pygame.display.flip() 
        clock.tick(60) 
    pygame.quit()
