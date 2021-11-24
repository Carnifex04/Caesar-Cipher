#importing modules
from additionals import logo
from additionals import alphabet

#printing logo
print("Welcome to")
print(logo)

# a function cypher, which takes arguments the input text, the shift number, and the cipher direction
def caesar_cypher (input_text, shift_amt, encoding):
  #initializing an empty cipher string
  cipher = ""

  #if the user wants to decrpt a message, we change the shift number sign to move backwards in the alphabet
  if encoding == "decode":
    shift_amt *= -1

  for letter in input_text:
    #if statement for skipping symbols, numbers and spaces
    if letter not in alphabet:
      cipher += letter
      continue
    else:
      index = alphabet.index(letter)         #finding the index of letter in the alphabet
      shifted_index = index + shift_amt      #finding the shifted index of letter 
      final_index = shifted_index % 26       #finding the final index of letter in the alphabet
      final_letter = alphabet[final_index]   #finding the final letter at the final index
      cipher += final_letter                 #adding the letter to the cipher string

  print(f"The {encoding}d text is: \n{cipher}\n")

continue_game = "yes"
while continue_game == "yes":
  #taking input the cipher direction, the text to be encrypted or decrypted, and the shift number
  cipher_direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  caesar_cypher(text, shift, cipher_direction)

  continue_game = input("Type 'yes' if you want to go again. Otherwise type 'no'\n").lower()

print("See you again!!!")



