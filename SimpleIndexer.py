# letter1 = input("input letter here: ").upper()
# letter2 = input("input letter here: ").upper()
# letter3 = input("input letter here: ").upper()
# letter4 = input("input letter here: ").upper()
# letter5 = input("input letter here: ").upper()
# letter6 = input("input letter here: ").upper()
# letter7 = input("input letter here: ").upper()
# Tileset = letter1 + letter2 + letter3 + letter4 + letter5 + letter6 + letter7
Tileset = input("Enter your 7 letters here: ").upper()
# Tileset = Tileset.split()
#Tileset = str(Tileset)
#Tileset = Tileset.translate({ord('['): None})
#Tileset = Tileset.translate({ord(']'): None})
#Tileset = Tileset.translate({ord("'"): None})
print('Your input')
print(Tileset)
print('------')


dictionaryfile = open("dictionary.txt", "r")

for line in dictionaryfile:
    line = line.replace(" ", "")
    if Tileset in line:
        print(line)
        # if len(Tileset) == (len(line)-1):
        #     print(line + '1')