from collections import defaultdict
def change_greedy(amount, coinage):
    counts = defaultdict(int)
    result_list = []
    while amount > 0:
        current_coin = 0
        for coin in coinage:
            if coin > current_coin and coin <= amount:
                current_coin = coin
        counts[current_coin] += 1
        amount -= current_coin
        if current_coin == 0:
            return None
    for count in counts:
        result_list.append((counts[count], count))
    return result_list

print(change_greedy(68, [1, 20, 50]))