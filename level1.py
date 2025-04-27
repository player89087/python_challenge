letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
                   'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


message = []
message_inp = input("The secret message: ")
message.append(message_inp)
codec = input("Type in the codec, by how many letter was the word shifted ?: ")


y = 0
x = len(message)
for i in range (0,x):
    shift = message[y]
    print(shift)
    y += 1
    #shift = message.index(y)
    #if shift  in letter:
    z = letter.index(shift) # should find the index from the letter from the message in the letter list
    print(z)
    codec = int(codec)
    z += codec
    print(letter[z])
