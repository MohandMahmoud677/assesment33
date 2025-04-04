def get_player_choice(player_num):
    while True:
        choice = input(f"Player {player_num}, enter your choice (rock, paper, scissors): ").lower()
        if choice in ["rock", "paper", "scissors"]:
            return choice
        print("Invalid choice. Please enter rock, paper, or scissors.")

def determine_winner(player1_choice, player2_choice):
    if player1_choice == player2_choice:
        return "It's a tie!"
    elif (player1_choice == "rock" and player2_choice == "scissors") or \
         (player1_choice == "paper" and player2_choice == "rock") or \
         (player1_choice == "scissors" and player2_choice == "paper"):
        return "Player 1 wins!"
    else:
        return "Player 2 wins!"

def play_game():
    print("Welcome to Rock-Paper-Scissors!")
    player1_choice = get_player_choice(1)
    player2_choice = get_player_choice(2)

    print(f"\nPlayer 1 chose: {player1_choice}")
    print(f"Player 2 chose: {player2_choice}")
    
    winner = determine_winner(player1_choice, player2_choice)
    print(winner)

if '_name_' == "_main_":
    play_game()