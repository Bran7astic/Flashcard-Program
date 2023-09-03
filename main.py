# === Study Sprites! ===
from termcolor import colored
import random

def show_menu():
  print("""     == MENU ==
1. Create Flashcard
2. Remove Flashcard
3. Edit Flashcard
4. View All Flashcards
5. Randomize!
6. Exit
  """)

  choice = input("Select an option: ")
  while not choice.isnumeric():
    print(colored("Please enter the number associated with your choice!", 'red'))
    choice = input("Select an option: ")
  return choice

def create_card(): # 1
  
  term = input("\nGreat! What is the term?: ")
  definition = input("What is the definition?: ")

  flashcards[term] = definition
  print("\n--Updated List--")
  for key, value in flashcards.items():
    print("{} - {}".format(key, value))
  print()

  one_more = input("Would you like to make another? (y/n) ")
  one_more = one_more.strip().lower()

  if one_more == 'n':
    print()
    return
    
  elif one_more != 'y': 
    print("Please type 'y' or 'n'")
    one_more = input("Would you like to make another? (y/n) ")
    one_more = one_more.strip().lower()
    
  while one_more == 'y':
    term = input("\nGreat! What is the term?: ")
    definition = input("What is the definition?: ")
  
    flashcards[term] = definition
    print("\n--Updated List--")
    for key, value in flashcards.items():
      print("{} - {}".format(key, value))
    print()

    one_more = input("Would you like to make another? (y/n) \n")
    one_more = one_more.strip().lower()
    print()


def remove_card(): # 2
  if not flashcards:
    print(colored("There are no cards to remove! \n", 'red'))
  terms = list(flashcards.keys())
  removal = input(f"Which of the following terms would you like to remove? (Type 'q' to quit): {terms} ")
  if removal == 'q': return
  
  while removal not in flashcards:
    removal = input(colored("That term wasn't found. (Try entering term without quotation marks! ", 'red'))
    terms = list(flashcards.keys())
    removal = input(f"Which of the following terms would you like to remove?: {terms} ")
    if removal == 'q': break
    
  flashcards.pop(removal)
  print(f"Flashcard with the term {removal} has been removed")

  print()

def edit_cards(): # 3

  if not flashcards: 
    print(colored("There are no flashcards to edit! \n", 'red'))
    return

  print(f"\nTerms: {list(flashcards.keys())}") 
  term = input("What is the term you would like to edit?  ")
    
  
  while term not in flashcards:
    print(colored("Sorry but this term does not exist, please check your spelling and try again!", 'red'))
    term = input ("What is the term you would like to edit?  ")
    print()
  else:
    new_def = input("Please enter the new defention here: ")
    flashcards[term] = new_def
    print("\n--Updated List--")
    print()
    for key, value in flashcards.items():
     print("{} - {}".format(key, value))

     print()

def view_cards(): # 4
  if not flashcards:
    print("You haven't made any flashcards! \n")
  
  print()
  
  for num, term in enumerate(flashcards):
    print(f"""  {num+1}. {term} - {flashcards[term]}""")
    
  print()

def randomize(): # 5
  if not flashcards: print(colored("There are no cards to randomize! \n", 'red'))

  terms = list(flashcards.keys())
  random.shuffle(terms)

  print(colored("Random terms will be shown from all of your flashcards. Type 'q' at any point to quit \n", 'yellow'))

  points = 0
  
  for term in terms:
    while True:
      print()
      print(f"\nTerm: {term}")
      
      flip_or_quit = input("Type 'f' to flip the card. Type 'quit' to quit: ")
      flip_or_quit = flip_or_quit.strip().lower()

      if flip_or_quit == 'f':
        print()
        print(f"\nTerm: {term}")
        print(f"Definition: {flashcards[term]} \n")
        
        while True:
          right_wrong = input("Did you get this term right? (y/n) ")
          if right_wrong == 'y':
            points += 1
            print(colored(f"{points} correct so far!\n", 'green'))
            break
          elif right_wrong == 'n':
            print(colored("Try to review this one!\n", 'red'))
            break 
          elif right_wrong == 'quit':
            break
          else: 
            print("Please type 'y' or 'n'. ")
            
        break
        
      elif flip_or_quit == 'quit':
        break
      else: 
        print("Please type 'f' to flip or 'quit' to quit \n")

  percentage = (points/len(flashcards)) * 100
  print(colored(f"You got {round(percentage, 2)}% correct!\n", 'green'))

def exit(): # 6
  print(colored("Thank you!", 'blue'))

print(colored("Welcome to Study Sprites!!\n", 'green'))
  
flashcards = {}

while True:
  menu_choices = {1: create_card, 2: remove_card, 3: edit_cards, 4: view_cards, 5: randomize, 6:exit}
  
  choice = int(show_menu())
  if choice in menu_choices:
    menu_choices[choice]()
    if choice == 6:
      break
  else: print(colored("Please enter the number associated with your choice!\n", 'red'))