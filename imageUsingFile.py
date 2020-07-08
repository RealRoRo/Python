
f1 = open("Screenshot (7).png","rb")

f2 = open("my pic.png","wb")

for i in f1:
    f2.write(i)

f1.close()
f2.close()