dictionary = {"cat": "animal", "dog": "GreaterAnimal", "phone": "Object"}

for key in dictionary.keys():
    print(key, "->", dictionary[key])
    
for english, french in dictionary.items():
    print(english, "->", french)

for french in dictionary.values():
    print(french)
    
dictionary['swan'] = 'cygne' # Adding new key
print(dictionary)

del dictionary['dog'] # Removing key
print(dictionary)

dictionary.popitem() # Del last item in a dictionary
print(dictionary)