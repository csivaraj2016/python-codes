
dictionary = {'a':500, 'b':5874, 'c': 560,'d':1200,'e':234}


Keymax = max(dictionary, key=dictionary.get)        # dictionary.get used to return the key value of the dictionary(it may max or min)

Keymin = min(dictionary, key=dictionary.get)                # both  object  and  fn will be passed  as the arguement

print("maximum value of the key is ",Keymax)
print(dictionary[Keymax])                           # print the value for the corresponding key
print("minimum val of the key is ",Keymin)
print(dictionary[Keymin])



