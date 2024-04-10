def get_alphabet():  
  # lowercase_alphabet = [chr(letter) for letter in range(ord('a'), ord('z') + 1)]  
  # uppercase_alphabet = [chr(letter) for letter in range(ord('A'), ord('Z') + 1)]
  ukrainian_alphabet_lower = ' абвгдеєжзиіїйклмнопрстуфхцчшщьюя'
  return ukrainian_alphabet_lower


def get_data():
  with open("data.txt", 'r') as file:
    return file.readline()[:-1], file.readline()


def vigenere_decrypt(ciphertext, keyword, alphabet):
  decrypted_text = ''
  key = keyword  
  while ciphertext:    
    block = ciphertext[:len(key)]
    ciphertext = ciphertext[len(key):]
    for i, j in zip(block, key):            
      decrypted_char = alphabet[(alphabet.index(i) - alphabet.index(j) + len(alphabet)) % len(alphabet)]
      decrypted_text += decrypted_char                      
    key = decrypted_text[-len(key):]
    
  return decrypted_text


def print_data(input, key, input_with_key, alphabet, numbers_for_dividing, result_numbers, result_characters, decrypted_text):
  print("\033[1;32mInput:                \033[0m", "\033[1;33m{}\033[0m".format(input))
  print("\033[1;32mKey:                  \033[0m", "\033[1;33m{}\033[0m".format(key))
  print("\033[1;32mInput with Key:       \033[0m", "\033[1;33m{}\033[0m".format(input_with_key))
  print("\033[1;32mAlphabet:             \033[0m", "\033[1;33m{}\033[0m".format(alphabet))
  print("\033[1;32mNumbers for Dividing: \033[0m", "\033[1;33m{}\033[0m".format(numbers_for_dividing))
  print("\033[1;32mResult Numbers:       \033[0m", "\033[1;33m{}\033[0m".format(result_numbers))
  print("\033[1;32mResult Characters:    \033[0m", "\033[1;33m{}\033[0m".format(''.join(result_characters)))
  print("\033[1;32mDecoded Text:         \033[0m", "\033[1;33m{}\033[0m".format(decrypted_text))


def main():
  input, key = get_data()  
  input_with_key = key + input[:-len(key)]
  alphabet = get_alphabet()
  numbers_for_dividing = [alphabet.index(x) + alphabet.index(y) for x, y in zip(input, input_with_key)] 
  result_numbers = [el % len(alphabet) for el in numbers_for_dividing]  
  result_characters = [alphabet[i] for i in result_numbers]  
  decrypted_text = vigenere_decrypt(result_characters, key, alphabet)
  print_data(input, key, input_with_key, alphabet, numbers_for_dividing, result_numbers, result_characters, decrypted_text)
  

if __name__ == "__main__":
  main()