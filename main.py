# === Flashcard Program! ===

# Test


def create_card():
    response = input("Would you like to create a flashcard?(y/n)  ")

    while response != 'y' and response != 'n':
        print("Please response with 'y' or 'n'")
        response = input("Would you like to create a flashcard? (y/n)")
    
    if response == 'n':
        return
    

create_card()