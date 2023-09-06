# store data in a dictionary
game_data= {
    "money": 0,
    "quit": False
}

while(True):
    if(game_data['money'] < 5):
        user_input = int(input("""
                        would you like to...
                        [1] Use your teeth to cut the grass and earn $1?
                        [2] Quit the game?
                    """))
        if(user_input == 1):
            game_data["money"] += 1
            print(f"you earned $1")
            print(f"you have $ {game_data['money']} in your pocket")

        if(user_input == 2):
            game_data["quit"] = True

        if(game_data["quit"] == True):
            print(f"game over")
            break

    if(game_data['money'] >= 5):
        user_input = int(input("""
                            would you like to...
                            [1] Use your teeth to cut the grass and earn $1?
                            [2] Buy a pair of rusty scissors for $5?
                            [3] Quit the game?
                        """))
        if(user_input == 1):
            game_data["money"] += 1
            print(f"you earned $1")
            print(f"you have $ {game_data['money']} in your pocket")

        if(user_input == 2):
            game_data['money'] -= 5
            print(f"you purchased a pair of rusty scissors")
            print(f"you have ${game_data['money']} in your pocket")
            break

        if(user_input == 3):
            game_data["quit"] = True

        if(game_data["quit"] == True):
            print(f"game over")
            break

while(True):
    user_input = int(input("""
                            would you like to...
                            [1] Use the rusty scissors to cut the grass for $5?
                            [2] Use your teeth to cut the grass for $1?
                            [3] Quit the game?
                        """))

    if(user_input == 1):
        game_data['money'] += 5
        print(f"you earned $5")
        print(f"you have $ {game_data['money']} in your pocket")

    if(user_input == 2):
        game_data["money"] += 1
        print(f"you earned $1")
        print(f"You have $ {game_data['money']} in your pocket")

    if(user_input == 3):
        game_data["quit"] = True

    if(game_data["quit"] == True):
        print(f"game over")
        break