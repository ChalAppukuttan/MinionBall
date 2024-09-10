def menu():
    import pygame
    import time

    pygame.init()

    window_Width = 1000
    window_Height = 478
    game_display = pygame.display.set_mode((window_Width, window_Height))

    font = pygame.font.SysFont("Arial", 36)

    white = (255, 255, 255)
    black = (0, 0, 0)

    bg_image = pygame.image.load("MinionBall.png")


    def draw_menu():
        global start_game_button_rect, quit_button_rect

        # Draw the background
        game_display.blit(bg_image,(0,0))

        # Draw the Start Game button
        start_game_button = font.render("Start Game", True, black)
        start_game_button_rect = start_game_button.get_rect(center=(window_Width / 5.2, 300))
        pygame.draw.rect(game_display, black, (
            start_game_button_rect.left - 10, start_game_button_rect.top - 10, start_game_button_rect.width + 20,
            start_game_button_rect.height + 20), 5)
        game_display.blit(start_game_button, start_game_button_rect)

        # Draw the Quit button
        quit_button = font.render("Quit", True, black)
        quit_button_rect = quit_button.get_rect(center=(window_Width / 1.3, 300))
        pygame.draw.rect(game_display, black, (
            quit_button_rect.left - 10, quit_button_rect.top - 10, quit_button_rect.width + 20,
            quit_button_rect.height + 20),
                         5)
        game_display.blit(quit_button, quit_button_rect)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        game_display.blit(bg_image,(0,0))
        draw_menu()
        pygame.display.update()
        global quit_button_rect, start_game_button_rect
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if quit_button_rect.collidepoint(event.pos):
                    pygame.quit()
                    quit()
        pygame.display.update()

    pygame.quit()

menu()