
def s_o_d(n):
    sum = 0
    while n > 0:
        sum += int(n%10)
        n = int(n / 10)
    return sum


t = int(input())
while t > 0:
    n = int(input())
    win = [0, 0]
    count = 0
    while n > 0:
        n -= 1
        a, b = input().split()
        if s_o_d(int(a)) > s_o_d(int(b)):
            win[0] += 1
            print("in 0", win[0])
        elif s_o_d(int(a)) < s_o_d(int(b)):
            win[1] += 1
            print("in 1", win[1])
        else:
            print("same")

    if win[0] > win[1]:
        print("0", win[0])
    elif win[0] < win[1]:
        print("1", win[1])
    else:
        print("2", win[0])
    t -= 1