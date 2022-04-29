# Author: SMR (AMDG) 04/29/22

# Initial Import
from string import ascii_uppercase

# Functions
def cipher_key(shift):
    original_letters = ascii_uppercase
    shifted_letters = ascii_uppercase[int(shift):] + ascii_uppercase[:int(shift)]

    return dict(zip(original_letters, shifted_letters))
def shifting_line(line, dict_key):
    # Blank space for new lines
    new_line = ""
    
    # Have to create a for loop here in order to translate correctly for every character
    for character in line: 
        if character == " ":
            new_line += " "
            continue
       
        elif character == "\n":
         
         # Need a new line in order to keep the indents in place 
            new_line += "\n" 
            continue
       
       #Then need another elif statement to  keep punctuation in check for later
        elif character == "!" or character == "," or character == "'": 
            new_line += character
            continue
        
        # Convert each character (letter) to uppercase
        character = character.upper() 
       
       # Then the blankspace variable from above gets filled in with new information
        new_line = new_line + dict_key[character] 
    return new_line

def encrypt_message(filename, dict_key):
# creating blank space for list    
    lst = [] 
   # creating blank space for final statement
    last_statement = "" 
    it = open(filename)
    with it as file:
        for l in file: 
        # adds the list to the line that shifted    
            lst += shifting_line(l,dict_key)
        for lines in lst: 
            end += lines
        file = open("new_file.txt","w")
   # Final Write statement to store in new file     
        file.write(last_statement) 
        file.close()

# Input statements prompting user to enter the file as well as shift value. Once this occurs, stores information as variable.
user_file = input("Please enter a file to be encrypted: ")
shift_value = input("Please enter a shift value: ")

key = cipher_key(shift_value)

encrypt_message(user_file, key)
