from game import Game

def get_user_menu_choice():
    """Display the menu and get user's choice."""
    print("\nMenu:")
    print("1. Play a new game")
    print("2. Show scores")
    print("3. Quit")
    
    while True:
        choice = input("Enter your choice (1/2/3): ").strip()
        if choice in ["1", "2", "3"]:
            return choice
        print("Invalid choice. Please select 1, 2, or 3.")

def print_results(results):
    """Print the summary of game results."""
    print("\nGame Summary:")
    print(f"🏆 Wins: {results.get('win', 0)}")
    print(f"❌ Losses: {results.get('loss', 0)}")
    print(f"🤝 Draws: {results.get('draw', 0)}")
    print("Thank you for playing!")

def main():
    """Main function to run the game loop."""
    results = {"win": 0, "loss": 0, "draw": 0}
    
    while True:
        choice = get_user_menu_choice()
        
        if choice == "1":
            game = Game()
            result = game.play()
            results[result] += 1
            
        elif choice == "2":
            print_results(results)
            
        elif choice == "3":
            print_results(results)
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
