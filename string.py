
print("hey this a String")
print("hey i m creating a new line \nsee")
print("print a quotation mark but it ends the String so use this \" tadaa!!")
string_variable = "this is string varible"
print(string_variable)
name = "Ronak"; print("my name is " + name)
#lowercase nd uppercase
print(name.lower()+" "+name.upper())
print(name.islower());print(name.isupper())
print(name.upper().isupper())
print("swapped cases : "+name.swapcase())
print("title() : " +string_variable.title())
#length
print(len(name))
#char
print(name[3]);print("First char : "+name[0]);print("last char : "+name[-1])
print(name.index("o"));print(string_variable.index("st"))
print(string_variable.replace("string", "number"));print(name.replace("R", ""))#if string exists it will replace
print(string_variable.replace("s", "blah"))#find all s and replaace with blah
#slice
print("sliced [4:19] : "+string_variable[4:19])
print("sliced [3:-1:2] : "+string_variable[3:-1:2])
#del
del name
#print(name) error name not defined

#setting format of String

string_format = "{3} {1} {0} {2}".format("my", "name", "is", "Ronak");print(string_format)
string_format = "{} {} {} {}".format("my", "name", "is", "Ronak");print(string_format)

#setting format of integers
String1 = "{0:b}".format(13);print(String1)#gives binary of 13
String2 = "{0:.3f}".format(1/6);print(String2)#divide 1/6 and give result in 3points(.3f)

#find
print(string_format.find("name", 2, 5))
print("first occiurnce of n ",string_format.find("n"))
print("last occiurnce of n",string_format.rfind("n")) #last occurence

#count
string_geek = "geeksforgeeks"
print("count : ",string_geek.count("geeks"))

# center(), ljust() and rjust()
str = "geeksforgeeks"

# Printing the string after centering with '-'
print("The string after centering with '-' is : ",end="")
print(str.center(20, '-')) #length u wanna give with character

# Printing the string after ljust()
print("The string after ljust is : ",end="")
print(str.ljust(20, '-'))

# Printing the string after rjust()
print("The string after rjust is : ",end="")
print(str.rjust(20, '-'))

#join
str = "_"
str1 = ("geeks", "for", "geeks")
print(str1[0])

# using join() to join sequence str1 with str
print("The string after joining is : ", end="")
print(str.join(str1))

# strip(), lstrip() and rstrip()
str = "---geeksforgeeks---"
print(str)

# using strip() to delete all '-'
print("String after stripping all '-' is : ", end="")
print(str.strip('-'))

# using lstrip() to delete all trailing '-'
print("String after stripping all leading '-' is : ", end="")
print(str.lstrip('-'))

# using rstrip() to delete all leading '-'
print("String after stripping all trailing '-' is : ", end="")
print(str.rstrip('-'))

# min() and max()
str = "geeksforgeeks"

# using min() to print the smallest character
# prints 'e'
print("The minimum value character is : " + min(str))

# using max() to print the largest character
# prints 's'
print("The maximum value character is : " + max(str))

