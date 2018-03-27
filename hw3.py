sentence = input('Please type anything:\n')

dictionary = dict()


for word in sentence:
    if (word in dictionary):
        dictionary[word]=(dictionary[word]+1)
    else:
        dictionary[word]=1
alphabat = dictionary.keys()
numbers = dictionary.values()
for item in dictionary.items():
    alphabat,numbers = item
    print("'" + alphabat + "'",':',numbers)
