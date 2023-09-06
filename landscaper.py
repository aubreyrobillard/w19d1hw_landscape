# store data in a dictionary
game_data= {
    "money": 0,
    "quit": False
}

while(True):
    user_input = int(input("""
                        would you like to...
                        [1] Use your teeth to cut the grass and earn $1?
                        [2] Quit the game?
                    """))
    if(user_input == 1):
        game_data["money"] += 1
        print(f"You have $ {game_data['money']} in your pocket")

    if(user_input == 2):
        game_data["quit"] = True

    if(game_data["quit"] == True):
        print(f"game over")
        break
