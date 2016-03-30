import csv
import pprint
from math import sqrt

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

def percentStr(l1, l2):
    return str(round(len(l1) / len(l2) * 100, 2)) + '%'


if __name__ == '__main__':
    ballots = getBallots()

    artsci = set(filter(filters.isArtsci, ballots))
    profac = set(filter(filters.isProfac, ballots))
    utm = set(filter(filters.isUTM, ballots))
    utsg = artsci | profac

    print('-- Turnout --')
    print('Voter turnout Artsci: '  + str(len(artsci)))
    print('Voter turnout Profacs: '  + str(len(profac)))
    print('Voter turnout UTSG: '  + str(len(utsg)))
    print('Voter turnout UTM: '  + str(len(utm)))

    no_academics = sfilter(filters.noAcademics, artsci)
    print('')
    print('Percentage of artsci students with no academics: ' + percentStr(no_academics, artsci))


    print('')
    print('-- Slates --')

    voted_all_hello = sfilter(filters.votedHello, ballots)
    voted_all_hello_except_alessia = sfilter(filters.votedHelloAndAlessia, ballots)

    print('Voted all of Hello: ' + str(len(voted_all_hello)) + '/' + percentStr(voted_all_hello, ballots))
    print('Voted all of Hello except for Alessia: ' + str(len(voted_all_hello_except_alessia)) + '/' + percentStr(voted_all_hello_except_alessia, ballots))

    voted_all_one = sfilter(filters.votedOne, ballots)
    voted_all_one_except_alessia = sfilter(filters.votedOneAndAlessia, ballots)

    print('Voted all of One: ' + str(len(voted_all_one)) + '/' + percentStr(voted_all_one, ballots))
    print('Voted all of One except for Alessia: ' + str(len(voted_all_one_except_alessia)) + '/' + percentStr(voted_all_one_except_alessia, ballots))

    lens = []
    # Voted for only 1
    print('')
    print('-- Voted for only 1 Core Candidate (execs ignoring profacs), rest abstensions --')

    voted_only_jasmine = sfilter(filters.votedOnlyJasmine, ballots)
    print('Voted only for Jasmine, rest abstensions: ' + str(len(voted_only_jasmine)) + '/' + percentStr(voted_only_jasmine, ballots))
    lens.append(len(voted_only_jasmine))

    voted_only_madina = sfilter(filters.votedOnlyMadina, ballots)
    print('Voted only for Madina, rest abstensions: ' + str(len(voted_only_madina)) + '/' + percentStr(voted_only_madina, ballots))
    lens.append(len(voted_only_madina))

    print('')

    voted_only_mathias = sfilter(filters.votedOnlyMathias, ballots)
    print('Voted only for Mathias, rest abstensions: ' + str(len(voted_only_mathias)) + '/' + percentStr(voted_only_mathias, ballots))
    lens.append(len(voted_only_mathias))

    voted_only_carina = sfilter(filters.votedOnlyCarina, ballots)
    print('Voted only for Carina, rest abstensions: ' + str(len(voted_only_carina)) + '/' + percentStr(voted_only_carina, ballots))
    lens.append(len(voted_only_carina))

    print('')

    voted_only_shahin = sfilter(filters.votedOnlyShahin, ballots)
    print('Voted only for Shahin, rest abstensions: ' + str(len(voted_only_shahin)) + '/' + percentStr(voted_only_shahin, ballots))
    lens.append(len(voted_only_shahin))

    voted_only_lera = sfilter(filters.votedOnlyLera, ballots)
    print('Voted only for Lera, rest abstensions: ' + str(len(voted_only_lera)) + '/' + percentStr(voted_only_lera, ballots))
    lens.append(len(voted_only_lera))

    voted_only_alessia = sfilter(filters.votedOnlyAlessia, ballots)
    print('Voted only for Alessia, rest abstensions: ' + str(len(voted_only_alessia)) + '/' + percentStr(voted_only_alessia, ballots))
    lens.append(len(voted_only_alessia))

    print('')

    voted_only_farah = sfilter(filters.votedOnlyFarah, ballots)
    print('Voted only for Farah, rest abstensions: ' + str(len(voted_only_farah)) + '/' + percentStr(voted_only_farah, ballots))
    lens.append(len(voted_only_farah))

    voted_only_malkeet = sfilter(filters.votedOnlyMalkeet, ballots)
    print('Voted only for Malkeet, rest abstensions: ' + str(len(voted_only_malkeet)) + '/' + percentStr(voted_only_malkeet, ballots))
    lens.append(len(voted_only_malkeet))

    print('')

    voted_only_lucinda = sfilter(filters.votedOnlyLucinda, ballots)
    print('Voted only for Lucinda, rest abstensions: ' + str(len(voted_only_lucinda)) + '/' + percentStr(voted_only_lucinda, ballots))
    lens.append(len(voted_only_lucinda))

    voted_only_andre = sfilter(filters.votedOnlyAndre, ballots)
    print('Voted only for Andre, rest abstensions: ' + str(len(voted_only_andre)) + '/' + percentStr(voted_only_andre, ballots))
    lens.append(len(voted_only_andre))

    print('')

    voted_only_shawn = sfilter(filters.votedOnlyShawn, ballots)
    print('Voted only for Shawn, rest abstensions: ' + str(len(voted_only_shawn)) + '/' + percentStr(voted_only_shawn, ballots))
    lens.append(len(voted_only_shawn))

    voted_only_andy = sfilter(filters.votedOnlyAndy, ballots)
    print('Voted only for Andy, rest abstensions: ' + str(len(voted_only_andy)) + '/' + percentStr(voted_only_andy, ballots))
    lens.append(len(voted_only_andy))

    print('')

    total = 0
    for i in lens:
        total += i

    average = total / len(lens)
    print('Average individual votes: ' + str(round(average, 2)))

    squared_diff = 0
    for i in lens:
        squared_diff += (i - average) ** 2

    squared_diff /= len(lens)
    std_dev = sqrt(squared_diff)
    print('Standard deviation: ' + str(round(std_dev, 2)))

    number_of_std_dev = (len(voted_only_carina) - average) / std_dev
    print('Carinas standard deviations from the mean: ' + str(round(number_of_std_dev, 2)))

    number_of_std_dev_alessia = (len(voted_only_alessia) - average) / std_dev
    print('Alessias standard deviations from the mean: ' + str(round(number_of_std_dev_alessia, 2)))

    number_of_std_dev_jasmine = (len(voted_only_jasmine) - average) / std_dev
    print('Jasmines standard deviations from the mean: ' + str(round(number_of_std_dev_jasmine, 2)))

    number_of_std_dev_mathias = abs(len(voted_only_mathias) - average) / std_dev
    print('Mathias standard deviations from the mean: ' + str(round(number_of_std_dev_mathias, 2)))


    uc_ballots = sfilter(filters.isUC, ballots)
    uc_ballots_jasmine = sfilter(filters.votedJasmine, uc_ballots)

    vic_ballots = sfilter(filters.isVic, ballots)
    vic_ballots_jasmine = sfilter(filters.votedJasmine, vic_ballots)
    vic_ballots_madina = sfilter(filters.votedMadina, vic_ballots)

    print(len(vic_ballots_jasmine))
    print(len(vic_ballots_madina))
