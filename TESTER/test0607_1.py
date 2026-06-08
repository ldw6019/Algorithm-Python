def mincoin(coins, v):
    count = []
    for i in range(len(coins)):
        cnt = v // coins[i]
        count.append(cnt)
        v -= cnt * coins[i]
    return count

coins = [500, 100, 50, 10, 1]
v= 580
print(mincoin(coins, v))


