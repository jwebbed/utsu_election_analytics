import csv
import pprint

import filters
import helpers
import keys
from ballot import Ballot


pp = pprint.PrettyPrinter(indent=2, compact=True)

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
        ballots.append(Ballot(hold))

    return set(ballots)

def sfilter(f, s):
    return set(filter(f, s))


if __name__ == '__main__':
    ballots = getBallots()

    artsci = set(filter(filters.isArtsci, ballots))
    profac = set(filter(filters.isProfac, ballots))
    utm = set(filter(filters.isUTM, ballots))
    utsg = artsci | profac

    print('Voter turnout Artsci: '  + str(len(artsci)))
    print('Voter turnout Profacs: '  + str(len(profac)))
    print('Voter turnout UTSG: '  + str(len(utsg)))
    print('Voter turnout UTM: '  + str(len(utm)))

    no_academics = sfilter(filters.noAcademics, artsci)
    print('')
    print('Percentage of artsci students with no academics: ' + str(round((len(no_academics) / len(artsci)) * 100, 2)) + '%')




    #farah = 'HXMX'
    #abdulla = 'FWV6'






    #voted_one_m = set(filter(filters.votedOne, utm))


    #print('Voted 1UofT at UTM: '  + str(len(voted_one_m)))






#print(total / count)

#print(yes)
#print(no)

#percent = no / (yes + no)
#print(percent)
