t= int(input())
while t > 0:
    n = int(input())
    List = list(map(int,input().split()))[:n]
    sum = 0
    prev = List[0]
    List.remove(prev)
    for i in List:
        sum += abs(i-prev) - 1
        prev = i
    print(sum)
    t-=1