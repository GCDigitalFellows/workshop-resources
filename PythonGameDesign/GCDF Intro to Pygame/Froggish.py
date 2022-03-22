# Basic Frogger-style game in Python

# import library
import pygame

# initialize pygame
pygame.init()

# size of our screen and caption
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Froggish"
# screen color in RGB
WHITE_COLOR = (255, 255, 255)
BLACK_COLOR = (0, 0, 0)

# clock to handle FPS
clock = pygame.time.Clock()
TICK_RATE = 60
pygame.font.init()
font = pygame.font.SysFont('comicsans', 75)

class Game:
    def __init__(self, image_path, title, width, height):
        self.title = title
        self.width = width
        self.height = height

        # create window of specified size
        self.game_screen = pygame.display.set_mode((width, height))
        # set the game window color to white
        self.game_screen.fill(WHITE_COLOR)
        pygame.display.set_caption(title)

        background_image = pygame.image.load(image_path)
        self.scaled_bkg = pygame.transform.scale(background_image, (width, height))
        
    def runGame(self, level_speed):
        isGameOver = False
        did_win = False
        direction = 0

        player_character = PlayerCharacter('frog.png', 375, 700, 50, 50)
        
        enemy_0 = EnemyCharacter('enemy.png', 20, 600, 50, 50)
        enemy_0.SPEED *= level_speed

        enemy_1 = EnemyCharacter('enemy.png', self.width - 40, 400, 50, 50)
        enemy_1.SPEED *= level_speed 

        enemy_2 = EnemyCharacter('enemy.png', 20, 200, 50, 50)
        enemy_2.SPEED *= level_speed        

        treasure = GameObjects('treasure.png', 375, 50, 50, 50)

       # set up game loop - game loops (often 'while' loops) repeat our code and update the game state (movement, display, etc) 
        while not isGameOver:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:   # if event type is a quit event
                    isGameOver = True
                # detect when key is pressed
                direction = pygame.key.get_pressed()
                print(event)
            
            self.game_screen.fill(WHITE_COLOR)
            self.game_screen.blit(self.scaled_bkg, (0, 0))
            treasure.draw(self.game_screen)
            
            player_character.move(direction, self.height)
            player_character.draw(self.game_screen)

            # demonstrates drawing
            # pygame.draw.rect(game_screen, BLACK_COLOR, (350, 350, 100, 100)) # surface, color, (x, y, width, height)
            # pygame.draw.circle(game_screen, BLACK_COLOR, (400, 300), 50)
            # game_screen.blit(player_image, (375, 375))

            enemy_0.move(self.width)
            enemy_0.draw(self.game_screen)

            # add more enemies based on current level
            if level_speed > 2:
                enemy_1.move(self.width)
                enemy_1.draw(self.game_screen)

            # add more enemies based on current level
            if level_speed > 4:
                enemy_2.move(self.width)
                enemy_2.draw(self.game_screen)

            # endgame logic / collision detection for enemies and treasure
            if player_character.detect_collision(enemy_0) or player_character.detect_collision(enemy_1) or player_character.detect_collision(enemy_2):
                isGameOver = True
                did_win = False
                text = font.render('Game Over :(', True, BLACK_COLOR)
                self.game_screen.blit(text, (200, 350))
                pygame.display.update()
                clock.tick(1)
                break
            elif player_character.detect_collision(treasure):
                isGameOver = True
                did_win = True
                text = font.render('You won :D', True, BLACK_COLOR)
                self.game_screen.blit(text, (200, 350))
                pygame.display.update()
                clock.tick(1)
                break
            # update the graphics
            pygame.display.update()
            # tick our clock and render next frame
            clock.tick(TICK_RATE)

        # call quit function and exit the program
        #pygame.quit()
        #quit()
        if did_win:
            self.runGame(level_speed + 0.5)
        else:
            return


# Generic class for all game objects
class GameObjects:
        def __init__(self, image_path, x, y, width, height):
            self.x_pos = x
            self.y_pos = y
            self.width = width
            self.height = height

            # get each object's image and scale it
            object_image = pygame.image.load(image_path)
            self.image = pygame.transform.scale(object_image, (width, height))
            
        def draw(self, background):
            background.blit(self.image, (self.x_pos, self.y_pos))


class PlayerCharacter(GameObjects):
    SPEED = 10
    
    def __init__(self, image_path, x, y, width, height):
        super().__init__(image_path, x, y, width, height)

    def move(self, direction, max_height):
        # move player based on direction pressed
        if direction[pygame.K_UP]:
            self.y_pos -= self.SPEED
        elif direction[pygame.K_DOWN]:
            self.y_pos += self.SPEED
        elif direction[pygame.K_LEFT]:
            self.x_pos -= self.SPEED
        elif direction[pygame.K_RIGHT]:
            self.x_pos += self.SPEED
        
        # prevent player from moving below the screen (subtracting the image's height from the screen height)
        if self.y_pos >= max_height - self.height:
            self.y_pos = max_height - self.height

    def detect_collision(self, other_body):
        # if below enemy
        if self.y_pos > other_body.y_pos + other_body.height:
            return False
        # if above enemy
        elif self.y_pos + self.height < other_body.y_pos:
            return False
        # if we're to the right of enemy
        if self.x_pos > other_body.x_pos + other_body.width:
            return False
        # if we're to the left of enemy
        elif self.x_pos + self.width < other_body.x_pos:
            return False
        return True

class EnemyCharacter(GameObjects):
    SPEED = 5
    
    def __init__(self, image_path, x, y, width, height):
        super().__init__(image_path, x, y, width, height)
        self.image_path = image_path

    def move(self, max_width):
        if self.x_pos <= 20:
            self.SPEED = abs(self.SPEED)
        elif self.x_pos >= max_width - (20 + self.width):
            self.SPEED = -abs(self.SPEED)
        self.x_pos += self.SPEED


new_game = Game('frogger_bkg.png', SCREEN_TITLE, SCREEN_WIDTH, SCREEN_HEIGHT)
new_game.runGame(1)



