import random

def play_truth_or_dare():
    """Plays a simple command-line Truth or Dare game."""

    truths = [
        "What is the most embarrassing thing you've ever done?",
        "What is your biggest fear?",
        "If you could change one thing about yourself, what would it be?",
        "What is a secret you've never told anyone?",
        "What is the funniest thing that has happened to you recently?"
    ]

    dares = [
        "Sing a song loudly for 30 seconds.",
        "Do 10 push-ups.",
        "Call a friend and tell them a bad joke.",
        "Let someone else choose your next profile picture.",
        "Eat a spoonful of a lemon."
    ]

    print("Welcome to Truth or Dare!")

    while True:
        choice = input("Enter 'truth' or 'dare' (or 'quit' to exit): ").lower()

        if choice == "truth":
            print(f"\nTruth: {random.choice(truths)}\n")
        elif choice == "dare":
            print(f"\nDare: {random.choice(dares)}\n")
        elif choice == "quit":
            print("Thanks for playing!")
            break
        else:
            print("Invalid input. Please enter 'truth', 'dare', or 'quit'.")

if __name__ == "__main__":
    play_truth_or_dare()
