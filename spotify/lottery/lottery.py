from math import ceil

def choose(n, k):
    ''' calculate the binomial coefficient '''
    combos = 1

    if n < k:
        return 0

    for i in range(1, int(k+1)):
        combos *= (n - (k - i)) / i

    return combos

def chance_to_win(participants, winners, tickets_per_win, friends):
    required_wins = int(ceil(friends / tickets_per_win))
    total_combos = choose(participants, winners)

    lose_combos = 0
    competitors = participants - friends
    for i in range(required_wins):
        lose_combos += choose(competitors, winners - i) * choose(friends, i)

    chance_to_lose = lose_combos / total_combos

    return 1 - chance_to_lose
    
if __name__ == "__main__":
    m, n, t, p = (float(num) for num in raw_input().split())

    print "%.10f" % chance_to_win(m, n, t, p)
