def game():
    number_range = list(range(1,21))
    choice = "wrong"
    within_range = False

    while choice.isdigit() == False or within_range == False:
        choice = input(f"Please enter a number between {number_range[0]} and {number_range[-1]}: ")

        if choice.isdigit() == False:
            print("Sorry that is not a digit")

        if choice.isdigit():
            if int(choice) in number_range:
                within_range = True
            else:
                print("Sorry you are out of acceptable range")
                within_range = False
    
    return int(choice)

game()

# Game 2
def display_game(game_list):
    print("Here is the current list:")
    print(game_list)

def position_choice():
    choice = "wrong"

    while choice not in ['1', '2', '3']:
        choice = input("Pick a position (0,1,2): ")
        
        if choice not in ['1', '2', '3']:
            print("Sorry, invalid choice!") 
    
    return int(choice)

def replacement_choice(game_list, position):
    user_placement = input("Type a string to place at position: ")
    game_list[position] = user_placement

    return game_list

def gameon_choice():
    choice = "wrong"

    while choice not in ['Y', 'N']:
        choice = input("Keep playing? (Y or N) ")
        
        if choice not in ['Y', 'N']:
            print("Please choose Y or N") 
    
    return choice == 'Y'

def play_game():
    game_on = True
    game_list = [0,1,2]

    while game_on:
        display_game(game_list)
        position = position_choice()
        game_list = replacement_choice(game_list, position)
        display_game(game_list)
        game_on = gameon_choice()
