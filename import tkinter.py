
import tkinter 
import random #We imported the tkinter and random modules to make our code

ROWS = 25
COLUMNS = 25
TILE_SIZE = 25 #These were the amount of rows, coloums and the tile size we c

WINDOW_WIDTH = TILE_SIZE * ROWS
WINDOW_HEIGHT = TILE_SIZE * COLUMNS #Here we created the window with and window height by using the tile size, column, and rows

class Tile:
    def __init__(self, x, y):
        self.x = x
        self.y = y  #here we created a tile class which has x and y  since the tiles on the grid will have x and y coordinate 

#  Here we created the game window using tkinter, we titled  the game, and made it so that window can not be adjusted by anyone and has a fixed position
window = tkinter.Tk()
window.title("Snake Game")
window.resizable(False, False)

canvas = tkinter.Canvas(window, bg="grey", width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
canvas.pack() #Here we created the canvas also using tkinter and we made the colour brown and we made the canvas width equal to the window width that we defined earlier in the code and we did the same with height 

# starting the  game (steps to start)
## the snake's starting position at the coordinates 10,10 on the grid, and the food positioning at 5,5. 
#The velocity x and velocity y make sure that the snake does not move in the beginning.
# The game over variable will be used to see if the game has ended or not  and the score is set at 0 in the beginning of the game.

snake = Tile(10 * TILE_SIZE, 10 * TILE_SIZE)  # single tile. snake's head
food = Tile(5 * TILE_SIZE, 5 * TILE_SIZE)  # food tile, food that the snake will eat
snake_body = []
velocityX = 0
velocityY = 0
game_over = False
score = 0      


def change_direction(e): #Here we have the block which determines how the snake moves, depending on what key we press the x and y velocity updates if we move up and down the y velocity updates and if we move side to side the x velocity updates. 
    global velocityX, velocityY, game_over
    if game_over:
        return

    if (e.keysym == "Up" and velocityY != 1):
        velocityX = 0
        velocityY = -1
    elif (e.keysym == "Down" and velocityY != -1):
        velocityX = 0
        velocityY = 1
    elif (e.keysym == "Left" and velocityX != 1):
        velocityX = -1
        velocityY = 0
    elif (e.keysym == "Right" and velocityX != -1):
        velocityX = 1
        velocityY = 0

def move(): # #In this code block we have the logic of the game, this part detects collisions with canvas walls, and it updates the snakes positioning on the grid, it updates the snakes body and the game score when it eats the food. After the positioning updates the code calls the draw function to update the canvas
    global snake, food, snake_body, game_over, score
    if game_over:
        return

    if (snake.x < 0 or snake.x >= WINDOW_WIDTH or snake.y < 0 or snake.y >= WINDOW_HEIGHT):
        game_over = True
        return

    for tile in snake_body: #For example, here we have a condition that ends the game if  snake.x is less than 0 or if the snake. x is less or equal to the window width this same condition is with snake.y which ends the code.
        if (snake.x == tile.x and snake.y == tile.y):
            game_over = True
            return

    
    if (snake.x == food.x and snake.y == food.y): #This condition checks if the snake x coordinate is the same as the food x coordinate, and if the snake y coordinate is the same as the food y coordinate and if these are the same it means that the snake and food collided
        snake_body.append(Tile(food.x, food.y))# this creates a new tile for the snake, which grows the snake
        food.x = random.randint(0, ROWS - 1) * TILE_SIZE  #This generates a new x coordinate for the food tile
        food.y = random.randint(0, COLUMNS - 1) * TILE_SIZE #this generates a new y coordinate for the food tile
        score += 1 #the score increases as 1 because the snake ate the food



    for i in range(len(snake_body) - 1, -1, -1): #This code organizes the tiles in the body so the tiles from the tail to the head all take the position of the tiles in front of it. 
        tile = snake_body[i]
        if (i == 0):
            tile.x = snake.x
            tile.y = snake.y
        else:
            prev_tile = snake_body[i - 1]
            tile.x = prev_tile.x
            tile.y = prev_tile.y

    snake.x += velocityX * TILE_SIZE
    snake.y += velocityY * TILE_SIZE

    draw()  # Call draw function here to update the canvas after moving the snake.

def draw():
    global snake, food, snake_body, game_over, score
    canvas.delete("all")

    
    # Here we created the food with the color being red which shows on the grid 

    canvas.create_rectangle(food.x, food.y, food.x + TILE_SIZE, food.y + TILE_SIZE, fill="yellow")

     # Here we created the snake with the color being lime green which shows on the grid
    canvas.create_rectangle(snake.x, snake.y, snake.x + TILE_SIZE, snake.y + TILE_SIZE, fill="pink")

    for tile in snake_body: #Here we created the tiles that are inside the snake body 
        canvas.create_rectangle(tile.x, tile.y, tile.x + TILE_SIZE, tile.y + TILE_SIZE, fill="pink")

    if game_over: #Here we have the creation of the game, over pop up that happens if the game is finished
        canvas.create_text(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, font="Arial 20", text=f"Game Over: {score}", fill="white")
    else: #Here we just have the code where the score updates when the game continues
        canvas.create_text(30, 20, font="Arial 12", text=f"Score: {score}", fill="white")

    window.after(100, move)   # Here is the scheduling of the movement function and it is called after 100 milliseconds after the input to create the movement.


window.bind("<KeyRelease>", change_direction) # Here we show that the direction can be changed when the user pressed the arrow keys which is why we have <KeyRelease>, change direction
draw()  #  Here we have the draw function to render the game graphics and it is called to start the game
window.mainloop() #The main loop is here to keep start the tkinter window which keeps the game responsive to user inputs 

