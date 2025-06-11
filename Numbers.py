import random
import time
import sys

def typewriter_print(text, delay=0.03):
    """Print text with typewriter effect."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # New line at the end

def generate_random_list(size, min_val=1, max_val=100):
    """Generate a list of random integers."""
    return [random.randint(min_val, max_val) for _ in range(size)]

def separate_even_odd(numbers):
    """Separate even and odd numbers from a list and print both lists."""
    even_numbers = sorted([num for num in numbers if num % 2 == 0])
    odd_numbers = sorted([num for num in numbers if num % 2 != 0])
    
    typewriter_print("Even numbers: " + str(even_numbers))
    typewriter_print("Odd numbers: " + str(odd_numbers))

def get_valid_list_size():
    """Get a valid list size from user (1-100)."""
    while True:
        try:
            print()
            size = int(input("How big should the list be? "))
            if 1 <= size <= 100:
                return size
            else:
                typewriter_print("Please choose a number between 1-100")
        except ValueError:
            typewriter_print("Please enter a valid number between 1-100")

def generate_mode(lists):
    """Handle list generation."""
    size = get_valid_list_size()
    
    print()
    typewriter_print(f"Generating random list of {size} numbers.")
    
    # Find next available letter
    list_identity = "A"
    while list_identity in lists:
        list_identity = chr(ord(list_identity) + 1)
    
    # Generate and store the list
    lists[list_identity] = generate_random_list(size)
    typewriter_print(f"Saved as 'List {list_identity}'")

def show_available_lists(lists):
    """Show all available lists to user."""
    if not lists:
        print()
        typewriter_print("No lists available. Generate some first!")
        return False
    
    # Sort lists alphabetically (A, B, C, etc.)
    list_names = sorted(lists.keys())
    print()
    typewriter_print(f"You have {len(lists)} list(s) to choose from: {', '.join([f'List {name}' for name in list_names])}")
    return True

def separation_mode(lists):
    """Handle list separation mode."""
    while True:
        if not show_available_lists(lists):
            return
        
        print()
        choice = input("Which list do you want to use? (Enter the letter): ").upper()
        
        if choice in lists:
            result = list_menu(lists, choice)
            if result == "exit":
                return "exit"
            elif result == "back":
                continue  # Go back to show_available_lists and list selection
            else:
                break  # Normal completion, exit separation mode
        else:
            typewriter_print("Invalid choice. Please enter a valid list letter.")

def list_menu(lists, list_identity):
    """Menu for a specific list - view or separate."""
    while True:
        print()
        typewriter_print(f"List {list_identity} options:")
        action = input("Do you want to 'View' the list or 'Separate' it? ").lower()
        
        if action == "view":
            print()
            sorted_list = sorted(lists[list_identity])
            typewriter_print(f"List {list_identity}: {', '.join(map(str, sorted_list))}")
            
            print()
            next_action = input(f"Are you ready to separate List {list_identity}? (Yes/No) or type 'Back' to choose a different list: ").lower()
            if next_action == "yes":
                print()
                separate_even_odd(lists[list_identity])
                result = post_separation_menu(lists)
                if result == "exit":
                    return "exit"
                break
            elif next_action == "back":
                return "back"  # Signal to go back to list selection
            # If "no", continue the loop to ask view/separate again
            
        elif action == "separate":
            print()
            separate_even_odd(lists[list_identity])
            result = post_separation_menu(lists)
            if result == "exit":
                return "exit"
            break
        else:
            typewriter_print("Please enter 'View' or 'Separate'")

def post_separation_menu(lists):
    """Menu after separating a list."""
    while True:
        print()
        typewriter_print("What would you like to do next?")
        choice = input("'Separate' another list, 'Generate' more lists, or 'Exit': ").lower()
        
        if choice == "separate":
            result = separation_mode(lists)
            if result == "exit":
                return "exit"
            break
        elif choice == "generate":
            break  # Will return to main loop
        elif choice == "exit":
            typewriter_print("Goodbye!")
            return "exit"
        else:
            typewriter_print("Please enter 'Separate', 'Generate', or 'Exit'")

def main():
    """Main program loop."""
    lists = {}  # Dictionary to store all lists
    
    typewriter_print("Welcome to the number separator!")
    
    # Initial choice
    print()
    initial_choice = input("Would you like to generate a random list? Please reply 'Yes' or 'No': ").lower()
    if initial_choice != "yes":
        typewriter_print("Ok then. Goodbye.")
        return
    
    # Generate first list (with user input for size)
    generate_mode(lists)
    
    # Main loop
    while True:
        print()
        typewriter_print("What would you like to do next?")
        choice = input("'Generate' another list, 'Separate' a list, or 'Exit': ").lower()
        
        if choice == "generate" or choice == "another":
            generate_mode(lists)
            
        elif choice == "separate" or choice == "move on":
            result = separation_mode(lists)
            if result == "exit":
                break
            
        elif choice == "exit":
            typewriter_print("Goodbye!")
            break
            
        else:
            typewriter_print("Please enter 'Generate', 'Separate', or 'Exit'")

if __name__ == "__main__":
    main()
