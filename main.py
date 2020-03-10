from Game import GameManager

if __name__ == "__main__":
    rpc = GameManager()

    # Game loop
    while True:
        # Print stats
        print(rpc.get_score())

        # Get player choice
        player_choice = rpc.get_player_choice()

        # Check if player wants to quit
        if player_choice == "q":
            exit()
        elif player_choice in rpc.choices:
            # Play match and print result
            print(rpc.play(player_choice))
        else:
            print(
                "Invalid player choice, must be either r for rock, p for paper, or s for scissors"
            )

