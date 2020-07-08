friends = ["Sandeep", "Dino", "Amal", "Amal", "Terin", "Francis", "Abay", "Adarsh", "Ajith", "Akhil", "Hridik"]
fruits = ["apple", "banana", "orange", "pineapple"]
print("friends :",friends)
print("fruits :",fruits)
print("friends[2:5] :",friends[2:5])
friends.extend(fruits)
print("friends.extend(fruits) : ",friends)
fruits.append("mango")  #atlaaast
fruits.insert(2,"chikoo")   #at some position
print("add chichkoo at 2 and append mango",fruits)
fruits.remove("pineapple")
print("removed pineapple :",fruits)
fruits.pop();print("popped  :",fruits)
#clear() used to cler the list
print("Index of dino",friends.index("Dino"))
print("Count of amal in friends : ",friends.count("Amal"))
friends.sort()
print("sorted list :",friends)
friends.reverse()
print("reversed :",friends)
friends2 = friends.copy()
print("copy : ",friends2)