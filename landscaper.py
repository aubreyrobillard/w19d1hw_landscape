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
    if(game_data['money'] < 25):
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

    if(game_data['money'] >= 25):
        user_input = int(input("""
                            would you like to...
                            [1] Use the rusty scissors to cut the grass for $5?
                            [2] Use your teeth to cut the grass for $1?
                            [3] Buy an old-timey push lawnmower for $25?
                            [4] Quit the game?
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
            game_data['money'] -= 25
            print(f"you purchased an old-timey push lawnmower")
            print(f"you have ${game_data['money']} in your pocket")
            break

        if(user_input == 4):
            game_data["quit"] = True

        if(game_data["quit"] == True):
            print(f"game over")
            break

while(True):
    if(game_data['money'] < 250):
        user_input = int(input("""
                            would you like to...
                            [1] Use the old-timey lawnmower to cut the grass for $50?
                            [2] Use the rusty scissors to cut the grass for $5?
                            [3] Use your teeth to cut the grass for $1?
                            [4] Quit the game?
                        """))
        if(user_input == 1):
            game_data['money'] += 50
            print(f"you earned $50")
            print(f"you have $ {game_data['money']} in your pocket")

        if(user_input == 2):
            game_data['money'] += 5
            print(f"you earned $5")
            print(f"you have $ {game_data['money']} in your pocket")

        if(user_input == 3):
            game_data["money"] += 1
            print(f"you earned $1")
            print(f"You have $ {game_data['money']} in your pocket")

        if(user_input == 4):
            game_data["quit"] = True

        if(game_data["quit"] == True):
            print(f"game over")
            break

    if(game_data['money'] >= 250):
        user_input = int(input("""
                            would you like to...
                            [1] Use the old-timey lawnmower to cut the grass for $50?
                            [2] Use the rusty scissors to cut the grass for $5?
                            [3] Use your teeth to cut the grass for $1?
                            [4] Buy a battery-powered lawnmower for $250?
                            [5] Quit the game?
                        """))
        
        if(user_input == 1):
            game_data['money'] += 50
            print(f"you earned $50")
            print(f"you have $ {game_data['money']} in your pocket")

        if(user_input == 2):
            game_data['money'] += 5
            print(f"you earned $5")
            print(f"you have $ {game_data['money']} in your pocket")

        if(user_input == 3):
            game_data["money"] += 1
            print(f"you earned $1")
            print(f"You have $ {game_data['money']} in your pocket")
        
        if(user_input == 4):
            game_data['money'] -= 250
            print(f"you purchased a battery-powered lawnmower")
            print(f"you have ${game_data['money']} in your pocket")
            break

        if(user_input == 5):
            game_data["quit"] = True

        if(game_data["quit"] == True):
            print(f"game over")
            break

while(True):
    if(game_data['money'] < 500):
        user_input = int(input("""
                            would you like to...
                            [1] Use battery-powered lawnmower to cut the grass for $100?
                            [2] Use the old-timey lawnmower to cut the grass for $50?
                            [3] Use the rusty scissors to cut the grass for $5?
                            [4] Use your teeth to cut the grass for $1?
                            [5] Quit the game?
                        """))
        
        if(user_input == 1):
            game_data['money'] += 100
            print(f"you earned $100")
            print(f"you have $ {game_data['money']} in your pocket")

        if(user_input == 2):
            game_data['money'] += 50
            print(f"you earned $50")
            print(f"you have $ {game_data['money']} in your pocket")

        if(user_input == 3):
            game_data['money'] += 5
            print(f"you earned $5")
            print(f"you have $ {game_data['money']} in your pocket")

        if(user_input == 4):
            game_data["money"] += 1
            print(f"you earned $1")
            print(f"You have $ {game_data['money']} in your pocket")

        if(user_input == 5):
            game_data["quit"] = True

        if(game_data["quit"] == True):
            print(f"game over")
            break

    if(game_data['money'] >= 500):
        user_input = int(input("""
                            would you like to...
                            [1] Use battery-powered lawnmower to cut the grass for $100?
                            [2] Use the old-timey lawnmower to cut the grass for $50?
                            [3] Use the rusty scissors to cut the grass for $5?
                            [4] Use your teeth to cut the grass for $1?
                            [5] Hire a team of starving students for $500?
                            [6] Quit the game?
                        """))

        if(user_input == 1):
            game_data['money'] += 100
            print(f"you earned $100")
            print(f"you have $ {game_data['money']} in your pocket")

        if(user_input == 2):
            game_data['money'] += 50
            print(f"you earned $50")
            print(f"you have $ {game_data['money']} in your pocket")

        if(user_input == 3):
            game_data['money'] += 5
            print(f"you earned $5")
            print(f"you have $ {game_data['money']} in your pocket")

        if(user_input == 4):
            game_data["money"] += 1
            print(f"you earned $1")
            print(f"You have $ {game_data['money']} in your pocket")

        if(user_input == 5):
            game_data['money'] -= 500
            print(f"you hired a team of starving students")
            print(f"you have ${game_data['money']} in your pocket")
            break

        if(user_input == 6):
            game_data["quit"] = True

        if(game_data["quit"] == True):
            print(f"game over")
            break

while(True):
    if(game_data['money'] <1000):
        user_input = int(input("""
                            would you like to...
                                [1] Use your team of starving students to cut the grass for $250?
                                [2] Use battery-powered lawnmower to cut the grass for $100?
                                [3] Use the old-timey lawnmower to cut the grass for $50?
                                [4] Use the rusty scissors to cut the grass for $5?
                                [5] Use your teeth to cut the grass for $1?
                                [6] Quit the game?
                                """))

        if(user_input == 1):
            game_data['money'] += 250
            print(f"you earned $250")
            print(f"you have $ {game_data['money']} in your pocket")

        if(user_input == 2):
            game_data['money'] += 100
            print(f"you earned $100")
            print(f"you have $ {game_data['money']} in your pocket")

        if(user_input == 3):
            game_data['money'] += 50
            print(f"you earned $50")
            print(f"you have $ {game_data['money']} in your pocket")

        if(user_input == 4):
            game_data['money'] += 5
            print(f"you earned $5")
            print(f"you have $ {game_data['money']} in your pocket")

        if(user_input == 5):
            game_data["money"] += 1
            print(f"you earned $1")
            print(f"You have $ {game_data['money']} in your pocket")

        if(user_input == 6):
            game_data["quit"] = True

        if(game_data["quit"] == True):
            print(f"game over")
            break

    if(game_data['money'] >= 1000):
        print(f"you've won!")
        print(f"GAME OVER")
        break