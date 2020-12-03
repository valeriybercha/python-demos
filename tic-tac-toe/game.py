# TIC-TAC-TOE game
# Language: Python
# Author: Valeriy B.


# App messages display
def game_messages(msg):
    if msg == "hello":
        print("========= TIC-TAC-TOE game ==========")
    elif msg == "bye":
        print("Good bye!")
    elif msg == "no_one":
        print("No one wins. Play again!")
    elif msg == "win":
        print("You won!!!")
        print("Great! Play again!")


# Info message display
def info_message():
    with open("readme.txt") as f:
        info = f.read()
        return info
        

# Player selection display message
def player_message(number):
    return f"'Player {number}' enter a number from the grid: "


# App inputs
def input_commands(msg):
    commands_dict = {
        "end": ["end", "quit", "q", "exit"],
        "info": ["info", "i"]
    }
    return commands_dict[msg]


# Creating a list of 9 elements
def game_list():
   return [str(i) for i in range(1, 10)]


# Displaying 3x3 grid to play
def game_output(game_grid):
    print("")
    print(game_grid[0] + " | " + game_grid[1] + " | " + game_grid[2])
    print("-" * 9)
    print(game_grid[3] + " | " + game_grid[4] + " | " + game_grid[5])
    print("-" * 9)
    print(game_grid[6] + " | " + game_grid[7] + " | " + game_grid[8])
    print("")


# Game win logic
def game_win(arr):
    count = 0
    
    # Verifying x grid axis
    win_x = 0
    win_o = 0
    for i in arr[:3]:
        if i == "X":
            win_x += 1
        elif i == "O":
            win_o += 1
    if (win_x == 3) or (win_o == 3):
        return "win"
    
    win_x = 0
    win_o = 0
    for i in arr[3:6]:
        if i == "X":
            win_x += 1
        elif i == "O":
            win_o += 1
    if (win_x == 3) or (win_o == 3):
        return "win"
    
    win_x = 0
    win_o = 0
    for i in arr[6:]:
        if i == "X":
            win_x += 1
        elif i == "O":
            win_o += 1
    if (win_x == 3) or (win_o == 3):
        return "win"

        
    # Verifying y grid axis
    win_x = 0
    win_o = 0
    for i in arr[::3]:
        if i == "X":
            win_x += 1
        elif i == "O":
            win_o += 1
    if (win_x == 3) or (win_o == 3):
        return "win"
    
    win_x = 0
    win_o = 0
    for i in arr[1::3]:
        if i == "X":
            win_x += 1
        elif i == "O":
            win_o += 1
    if (win_x == 3) or (win_o == 3):
        return "win"
    
    win_x = 0
    win_o = 0
    for i in arr[2::3]:
        if i == "X":
            win_x += 1
        elif i == "O":
            win_o += 1
    if (win_x == 3) or (win_o == 3):
        return "win"

    # Verifying diagonal axis
    win_x = 0
    win_o = 0
    if (arr[0] == "X") and (arr[4] == "X") and (arr[8] == "X"):
        win_x = 3
    elif (arr[2] == "X") and (arr[4] == "X") and (arr[6] == "X"):
        win_x = 3
    elif (arr[0] == "O") and (arr[4] == "O") and (arr[8] == "O"):
        win_o = 3
    elif (arr[2] == "O") and (arr[4] == "O") and (arr[6] == "O"):
        win_o = 3
    if (win_x == 3) or (win_o == 3):
        return "win"


# Main app logic
def tic_tac_toe(user_input):
    game_messages("hello")
    
    count = 0

    # Initializing a new list with grid numbers
    game_grid = game_list()
    
    # Start the game
    while not (user_input.lower() in input_commands("end") or (count == 10)):

        # Verifying win situation
        if game_win(game_grid) == "win":
            game_messages("win")
            break
        else:
                        
            # Select 'X' or 'O' variable to play with
            if count == 0:
                user_input = input("Type 'X' or 'O' to start the game. Type 'info' for detailed information: ")
                if user_input.lower() in input_commands("info"):
                    print(info_message())
                    user_input = input("Type 'X' or 'O' to start the game: ")
                    print(user_input)
                
                x_o = user_input.lower()
                game_output(game_grid)
                count += 1
        
            # Player variables 'X', 'O' assignment
            x_o_l = ["X", "O"]
            if x_o == "x":
                player_select = x_o_l
            elif x_o == "o":
                player_select = x_o_l[::-1]

            # Inputs for players
            if count % 2 != 0:
                user_input = input(player_message("1"))

                for i in game_grid:
                    if user_input == i:
                        game_grid.remove(i)
                        game_grid.insert(int(user_input) - 1, player_select[0])
                count += 1
            
            else:
                user_input = input(player_message("2"))
                
                for i in game_grid:
                    if user_input == i:
                        game_grid.remove(i)
                        game_grid.insert(int(user_input) - 1, player_select[1])
                count += 1
            print(count)
            
            game_output(game_grid)
    
    # Game end messages
    if count == 10:
        game_messages("no_one")
    else:
        game_messages("bye")
    

tic_tac_toe('')
