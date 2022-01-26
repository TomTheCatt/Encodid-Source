print("Rewriting key. . .")

import random, os, pickle
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()-=_+[]{}\\|;:',<.>/?`~ " + "'" + '"'

#Sets up variables to be rewritten
x, y, dic = list(characters), list(characters), {}
for char in x:
    dic.update({char:0})

#Remakes key
for key in dic:
    a = str("".join([random.choice(y) for i in range(random.randint(4, 22))]))
    if a not in dic:
        dic[key] = a
    else:
        continue

#Stores key
with open(f"{os.getcwd()}\\key.txt", "wb") as file:
    pickle.dump(dic, file)

print("Key rewritten.")
