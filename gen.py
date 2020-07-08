def TopTensq(): #using generator
    n =1
    while n <= 10:
        sq = n*n
        yield sq    #bsic diff btw yield and return is return woulh terminate func while yield wont
        n+=1


values = TopTensq()
for i in values:
    print(i)