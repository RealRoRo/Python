

friends = open("use_file.txt", "r")
print(friends.readable())
print(friends.readline())
#print(friends.readlines())
for friend in friends.readlines():
    print(friend)

friends.close()
friends = open("use_file.txt", "a")

friends.write("\nKelly - bombay")
friends.close()
friends = open("use_file.txt", "w")
friends.write("\n ellm poyi")
'''
Ronak - Cherpu
Dino - Irilajhakuda
amal - panithadam
abay - mundur
terin - Chavakad
Akhil - Erumapetti
Kelly - bombay
'''
friends.close()
friends2 = open("use_file2.txt", "w")
friends2.write("Ronak - Cherpu\nDino - Irilajhakuda\namal - panithadam\nabay - mundur\nterin - Chavakad\nAkhil - Erumapetti")
friends2.close()