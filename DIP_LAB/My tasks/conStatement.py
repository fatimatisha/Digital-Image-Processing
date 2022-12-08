words = []
game = "play"
while game == "play":
    new = input("Enter a 3-letter word: ")
    if len(new) > 3 or len(new) < 3:
        print("That’s not a 3-letter word.")
    else: 
        if new in words: 
            game = "over"
            print("You already said that word. Game over.")
            print("You know", len(words), "3-letter words.")
        else:
            print("Nice one.") 
            words.append(new)
