

def show_menu():
    """Displays the main interactive terminal menu."""
    print("\n" + "=" * 30)
    print("   CLI RETRO MUSIC COMPOSER   ")
    print("=" * 30)
    print("1. Play sample song")
    print("2. Enter custom song string")
    print("3. Exit program")
    print("-" * 30)


def get_user_choice():
    """Gets and returns the user's menu selection."""
    choice = input("Enter your choice (1-3): ").strip()
    return choice