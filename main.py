# === Flashcard Program! ===
import random


def show_menu():
  print(""" == MENU ==
1. Create Flashcard
2. Remove Flashcard
3. View All Flashcards
4. Randomize!
5. Exit
  """)

  choice = input("Select an option: ")
  while not choice.isnumeric():
    print("Please enter the number associated with your choice!")
    choice = input("Select an option: ")
  return choice

def create_card():
  
  term = input("\nGreat! What is the term?: ")
  definition = input("What is the definition?: ")

  flashcards[term] = definition
  print(flashcards)

  one_more = input("Would you like to make another? (y/n) ")
  one_more = one_more.strip().lower()

  if one_more == 'n':
    return
    
  elif one_more != 'y': 
    print("Please type 'y' or 'n'")
    one_more = input("Would you like to make another? (y/n) ")
    one_more = one_more.strip().lower()
    
  while one_more == 'y':
    term = input("\nGreat! What is the term?: ")
    definition = input("What is the definition?: ")
  
    flashcards[term] = definition
    print(flashcards)

    one_more = input("Would you like to make another? (y/n) \n")
    one_more = one_more.strip().lower()

def remove_card():
  if not flashcards:
    print("There are no cards to remove! \n")
  terms = list(flashcards.keys())
  removal = input(f"Which of the following terms would you like to remove?: {terms} ")
  
  while removal not in flashcards:
    removal = input("That term wasn't found. (Try entering term without quotation marks! ")
    
  flashcards.pop(removal)
  print(flashcards)

def view_cards():
  if not flashcards:
    print("You haven't made any flashcards! \n")
  
  print()
  
  for term in flashcards:
    print(f"""  {term}: {flashcards[term]}""")
    
  print()

def randomize():
  if not flashcards: print("There are no cards to randomize! \n")

  terms = list(flashcards.keys())
  random.shuffle(terms)

  print("Random terms will be shown from all of your flashcards. Type 'q' at any point to quit \n")

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
            print(f"{points} correct so far!\n")
            break
          elif right_wrong == 'n':
            print("Try to review this one!\n")
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
  print(f"You got {round(percentage, 2)}% correct!\n")
  
def exit():
  print("Thank you!")

flashcards = {'hi' : 'hola', 'one': 'uno', 'two' : 'dos'}

while True:
  menu_choices = {1: create_card, 2: remove_card, 3: view_cards, 4: randomize, 5: exit}
  
  choice = int(show_menu())
  if choice in menu_choices:
    menu_choices[choice]()
    if choice == 5:
      break
  else: print("Please enter the number associated with your choice!")

  

