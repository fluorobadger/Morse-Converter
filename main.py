# Converting Text to Morse Code, or Morse Code to Text


RULES = """
      READING MORSE CODE
      
1. A dot is one unit.
2. A dash is three units.
3. The gap between letters is a space.
4. The gap between words is a slash /.
5. Some symbols may not be translatable.
      """

#dictionary of characters and their equivalent in morse 
ALPHABET = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.', 'h': '....', 'i': '..', 'j': '.---',
            'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-', 
            'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--', 'z': '--..', '0': '-----', '1': '.----', '2': '..---', 
            '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '!': '-.-.--',
            ',': '--..--', '?': '..--..', ':': '---...', '-': '-....-', '"': '.-..-.', '(': '-.--.', '=': '-...-', '&': '.-...',
            '.': '.-.-.-', ';': '-.-.-.', '/': '-..-.', "'": '.----.', '_': '..--.-', ')': '-.--.-', '+': '.-.-.', '@': '.--.-.',' ': '/'} 
 

def convert_to_morse(text):
    """Searches Dictionary for each character, and if its found adds value to list otherwise adds to cant find list. Joins list and returns """
    chars = list(text) #create a list of characters to search for them one at a time
    cant_find = []
    morse_list = []
    for char in chars:
        try:
            morse_list.append(ALPHABET[char]) #find character in dictionary
        except KeyError:
            cant_find.append(char) #do this if it doesn't exist in the dictionary
    morse_string = ' '.join(morse_list)
    return morse_string, cant_find

def convert_to_text(code):
    """Searches Dictionary for each character, and if its found adds key to list, otherwise adds to cant find list. Joins list and returns """
    char_list = code.split() #split into individual morse code letters
    string_list = []
    cant_find = set() #a set so that duplicates aren't added more than once
    for char in char_list:
        found = False #each letter starts out as not found
        for letter, morse in ALPHABET.items():
            if char == morse:
                string_list.append(letter)
                found = True #if its found in dictionary, don't need to do next step
                break
        if not found: #if not found in dictionary do this step next
            cant_find.add(char)
    char_string = ''.join(string_list)
    return char_string, cant_find      
            

running = True
while running is True:
    print("Welcome to the Morse Code Converter\n")   
    try:    #try to provide options from the menu, requires an int as input
        option = int(input("Choose an option:\n1.Convert text to Morse Code.\n2.Convert Morse Code to text.\n3.See the Morse Code Alphabet and Rules.\n4.Quit the Program. \n"))
        
        if option == 1:
            text = input("What do you want converted to Morse Code? \n").lower()
            morse, cant_find_morse = convert_to_morse(text) #see above def function for notes
            print(morse)
            if cant_find_morse != []: #only print this if there are letters that couldn't be found, otherwise isn't required
                print(f"\nThese letters could not be translated: {cant_find_morse}")
            input("\n Press any key to return to menu \n")  
              
        elif option == 2:
            code = input("What do you want converted to text? \n")
            string, cant_find_letter = convert_to_text(code) #see above def function for notes
            print(string)
            if cant_find_letter != set(): #only print this if there are letters that couldn't be found, otherwise isn't required
                print(f"\nThese sections were invalid morse code: {cant_find_letter}")
            input("\n Press any key to return to menu \n")
            
        elif option == 3:
            print(RULES)
            for item in ALPHABET:
                print (item, " : ", ALPHABET[item]) #prints items in a neater way than just the dictionary list
            input("\n Press any key to return to menu \n")
            
        elif option == 4:
            running = False #this is to quit the while loop
            
        else: #do this if an invalid int was provided
            print("\nYou selected an invalid option. Please type either 1, 2, 3, or 4\n")
            input("\n Press any key to return to menu \n")
            
    except ValueError: #do this if any other character was provided
        print("\nYou selected an invalid option. Please type either 1, 2, 3, or 4\n")
        input("\n Press any key to return to menu \n")        
        
print("\nThankyou for using!") #print when option 4 chosen and while loop broken