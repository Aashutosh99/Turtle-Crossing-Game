import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Set up the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)  # Turn off automatic screen updates

# Create player, car manager, and scoreboard objects
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

# Listen for key events
screen.listen()
screen.onkey(player.move_turtle, "Up")  # Player moves up on pressing "Up" arrow key

game_is_on = True
while game_is_on:
    time.sleep(0.1)  # Introduce a slight delay for smooth animation
    screen.update()  # Update the screen manually

    # Generate new cars and move existing ones
    car_manager.create_car()
    car_manager.move_cars()

    # Check if player has reached the top of the screen
    if player.ycor() == 280:
        player.got_to_start()  # Reset player position
        scoreboard.increase_score()  # Increase score
        scoreboard.update_scoreboard()  # Update scoreboard display
        car_manager.level_up()  # Increase car speed or add more cars

    # Check collision with cars
    for car in car_manager.all_cars:
        if player.distance(car) < 20:  # Check distance between player and cars
            player.color("Red")  # Change player color on collision
            car.color("black")  # Change car color on collision
            player.shapesize(3, 1)  # Modify player size on collision
            screen.bgcolor("maroon")  # Change background color on collision
            screen.update()  # Update screen to show collision effects
            scoreboard.game_over()  # Display game over message
            game_is_on = False  # End the game loop

# Exit game on screen click
screen.exitonclick()
