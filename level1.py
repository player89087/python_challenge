import string 


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

message_inp = input("The secret message: ").lower()
codec = int(input("Type in the codec, by how many letters was the word shifted?: "))

encrypted_message = []

for char in message_inp:
    if char == ' ':
        encrypted_message.append(' ')
    elif char in letters:
        original_pos = letters.index(char)
        new_pos = (original_pos + codec) % 26  
        encrypted_message.append(letters[new_pos])
    else:
        encrypted_message.append(char) 
print("Encrypted message:", ''.join(encrypted_message))

table = string.maketrans(
    "abcdefghijklmnopqrstuvwxyz", "cdefghijklmnopqrstuvwxyzab"
)

int = "abcdefghiklmnopqrstuvwxyz"
out = "cdefghiklmnopqrstuvwxyzab"

trans = string.maketrans(int, out)
b = map # the url 
print(b.translate(trans))