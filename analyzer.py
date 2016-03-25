import csv
import filters

def getBallots():
    f = open('./Results.csv', 'r')
    reader = csv.reader(f)
    raw_ballots = [row for row in reader]
    header = raw_ballots[0]

    ballots = []

    for ballot in raw_ballots[1:]:
        hold = {}
        for i in range(len(ballot)):
            if ballot[i] != '':
                hold[header[i]] = ballot[i]
        ballots.append(hold)

    return ballots


if __name__ == '__main__':
    ballots = getBallots()

    shawn_ballots = list(filter(filters.votedShawn, ballots))

    print(len(shawn_ballots))



#print(total / count)

#print(yes)
#print(no)

#percent = no / (yes + no)
#print(percent)
