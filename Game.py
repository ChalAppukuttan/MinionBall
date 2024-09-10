def mrwgame():
    import pygame
    import random
    import math

    pygame.init()

    # Screen width and height
    window_Width = 800
    window_Height = 600
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    BUTTON_COLOR = (0, 255, 0)  # Green color for the button
    BUTTON_HOVER_COLOR = (0, 200, 0)  # Darker green for hover effect
    BUTTON_POSITION = (window_Width // 2 - 100, window_Height // 2)
    BUTTON_SIZE = (200, 50)

    # Game controls
    game_display = pygame.display.set_mode((window_Width, window_Height))

    tfont = pygame.font.SysFont('Arial', 48)
    tText = tfont.render('Game Title', True, WHITE)
    rText = tText.get_rect(center=(window_Width // 2, 50))

    # Button function
    def start_game():
        game = Game()
        game.run()

    # Function to draw the button
    def draw_button(surface, color, rect):
        pygame.draw.rect(surface, color, rect)
        button_text = pygame.font.SysFont('Arial', 24).render('Start Game', True, BLACK)
        text_rect = button_text.get_rect(center=rect.center)
        surface.blit(button_text, text_rect)

    # Game Class
    class Game:
        def __init__(self):
            self.screen = pygame.display.set_mode((window_Width, window_Height))
            pygame.display.set_caption("My Game")
            self.background = pygame.image.load('images/bckgrnd.png')
            self.icon = pygame.image.load('images/player.png')
            pygame.display.set_icon(self.icon)

            self.playerImg = pygame.image.load('images/player.png')
            self.playerX = 370
            self.playerY = 480
            self.playerX_chng = 0

            self.monsterImg = pygame.image.load('images/target.png')
            self.monsterX = random.randint(0, 800)
            self.monsterY = 50
            self.monsterX_chng = 0.3
            self.monsterY_chng = 0

            self.bulletImg = pygame.image.load('images/bullet.png')
            self.bulletX = 0
            self.bulletY = 480
            self.bulletX_chng = 0
            self.bulletY_chng = 5
            self.bullet_state = "ready"

        def player(self, x, y):
            self.screen.blit(self.playerImg, (x, y))

        def monster(self, x, y):
            self.screen.blit(self.monsterImg, (x, y))

        def fire_bullet(self, x, y):
            self.bullet_state = "fire"

        def isCollision(self, monsterX, monsterY, bulletX, bulletY):
            distance = math.sqrt(math.pow(monsterX - bulletX, 2) + math.pow(monsterY - bulletY, 2))
            return distance < 27

        def run(self):
            running = True
            while running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT:
                            self.playerX_chng = -0.3
                        if event.key == pygame.K_RIGHT:
                            self.playerX_chng = 0.3
                        if event.key == pygame.K_SPACE:
                            if self.bullet_state == "ready":
                                self.bulletX = self.playerX
                                self.bulletY = self.playerY
                                self.fire_bullet(self.bulletX, self.bulletY)

                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                            self.playerX_chng = 0

                # Player movement
                self.playerX += self.playerX_chng
                if self.playerX <= 0:
                    self.playerX = 0
                elif self.playerX >= 768:
                    self.playerX = 768

                # Monster movement
                self.monsterX += self.monsterX_chng
                if self.monsterX <= 0:
                    self.monsterX_chng = 0.3
                elif self.monsterX >= 768:
                    self.monsterX_chng = -0.3

                # Bullet movement
                if self.bullet_state == "fire":
                    self.screen.blit(self.bulletImg, (self.bulletX + 16, self.bulletY))  # Draw the bullet
                    self.bulletY -= self.bulletY_chng
                    if self.bulletY <= 0:
                        self.bulletY = 480
                        self.bullet_state = "ready"

                # Check collision
                collision = self.isCollision(self.monsterX, self.monsterY, self.bulletX, self.bulletY)
                if collision:
                    self.bulletY = 480
                    self.bullet_state = "ready"
                    self.monsterX = random.randint(0, 800)
                    self.monsterY = random.randint(50, 150)

                # Drawing everything
                self.screen.fill((130, 100, 20))
                self.screen.blit(self.background, (0, 0))
                self.player(self.playerX, self.playerY)
                self.monster(self.monsterX, self.monsterY)
                pygame.display.update()

            pygame.quit()

    # Main loop
    running = True
    while running:
        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        button_rect = pygame.Rect(BUTTON_POSITION, BUTTON_SIZE)
        if button_rect.collidepoint(mouse_pos):
            button_color = BUTTON_HOVER_COLOR
            if mouse_click[0]:  # Left mouse button clicked
                start_game()
        else:
            button_color = BUTTON_COLOR

        game_display.fill(WHITE)
        game_display.blit(tText, rText)
        draw_button(game_display, button_color, button_rect)
        pygame.display.update()

    pygame.quit()

mrwgame()
