
def abstensions(ballot):
    count = 0
    for key in ballot:
        if ballot[key] == 'Abstain':
            count += 1
    return count / len(ballot)

def averageAbstention(votes):
    count = 0
    for i in map(abstensions, votes):
        count += i

    return count / len(votes)
