import keys

def _f(ballot, name, position, or_abstained=False):
    temp = position in ballot and ballot[position].startswith(name)
    if or_abstained:
        temp = temp or (position in ballot and ballot[position].startswith('Abstain'))
    return temp

#President
def _pres(ballot, name):
    return _f(ballot, name, 'President')

def votedMadina(ballot):
    return 'President' in ballot and ballot['President'].startswith('Madina')

def votedJasmine(ballot):
    return 'President' in ballot and ballot['President'].startswith('Jasmine')

def abstainedPresident(ballot):
    return _pres(ballot, 'Abstain')

#VPCL
def _vpcl(ballot, name):
    return _f(ballot, name, 'Vice-President, Campus Life')

def votedShahinFirst(ballot):
    return _vpcl(ballot, 'Shahin')

def votedLeraFirst(ballot):
    return _vpcl(ballot, 'Lera')

def votedAlessiaFirst(ballot):
    return _vpcl(ballot, 'Alessia')

def abstainedVPCL(ballot):
    return _vpcl(ballot, 'Abstain')


#VPEQ
def _vpeq(ballot, name):
    return _f(ballot, name, 'Vice-President, Equity')

def votedFarah(ballot):
    return _vpeq(ballot, 'Farah')

def votedMalkeet(ballot):
    return _vpeq(ballot, 'Malkeet')

def abstainedVPEQ(ballot):
    return _vpeq(ballot, 'Abstain')


#VPEX
def _vpex(ballot, name):
    return _f(ballot, name, 'Vice-President, External')

def votedLucinda(ballot):
    return _vpex(ballot, 'Lucinda')

def votedAndre(ballot):
    return _vpex(ballot, 'Andre')

def abstainedVPEX(ballot):
    return _vpex(ballot, 'Abstain')

#VPIS
def _vpis(ballot, name):
    return _f(ballot, name, 'Vice-President, Internal and Services')

def votedMathias(ballot):
    return _vpis(ballot, 'Mathias')

def votedCarina(ballot):
    return _vpis(ballot, 'Carina')

def votedOnlyCarina(ballot):
    return votedCarina(ballot) and (_coreExecAbstensions(ballot) == 1)

def abstainedVPIS(ballot):
    return _vpis(ballot, 'Abstain')


#VPPF
def _vppf(ballot, name):
    return _f(ballot, name, 'Vice-President, Professional Faculties')

def votedRyan(ballot):
    return _vppf(ballot, 'Ryan')

def votedCharlotte(ballot):
    return _vppf(ballot, 'Charlotte')

def isProfac(ballot):
    return 'Vice-President, Professional Faculties' in ballot

def abstainedVPPF(ballot):
    return _vppf(ballot, 'Abstain')


#VPUA
def _vpua(ballot, name):
    return _f(ballot, name, 'Vice-President, University Affairs')

def votedShawn(ballot):
    return _vpua(ballot, 'Shawn')

def votedAndy(ballot):
    return _vpua(ballot, 'Andy')

def abstainedVPUA(ballot):
    return _vpua(ballot, 'Abstain')


#Voted Slates
def _hello(ballot):
    if (votedJasmine(ballot) and votedFarah(ballot) and votedLucinda(ballot) and
        votedMathias(ballot) and votedShawn(ballot)):

        if (isProfac(ballot) and votedRyan(ballot)):
            return True

    return False

def votedHello(ballot):
    return _hello(ballot) and votedShahinFirst(ballot)

def votedHelloAndAlessia(ballot):
    return _hello(ballot) and votedAlessiaFirst(ballot)

def _one(ballot):
    if (votedMadina(ballot) and votedMalkeet(ballot) and votedAndre(ballot) and
        votedCarina(ballot) and votedAndy(ballot)):

        if (isProfac(ballot) and votedCharlotte(ballot)):
            return True

    return False

def votedOne(ballot):
    return _one(ballot) and votedLeraFirst(ballot)

def votedOneAndAlessia(ballot):
    return _one(ballot) and votedAlessiaFirst(ballot)


def fullAbstension(ballot):
    for key in ballot:
        if ballot[key] != 'Abstain':
            return False
    return True

def onlyAsian(ballot):
    return (abstainedPresident(ballot) and abstainedVPEQ(ballot) and abstainedVPEX(ballot) and
            votedCarina(ballot) and abstainedVPUA(ballot) and abstainedVPCL(ballot))


#Academics
def isCS(ballot):
    return keys.CS in ballot

def yesCS(ballot):
    return isCS(ballot) and ballot[keys.CS] == 'Yes'

def isLifeSci(ballot):
    return keys.LIFE_SCI in ballot

def isSocialSci(ballot):
    return keys.SOCIAL_SCI in ballot

def isHumanities(ballot):
    return keys.HUMANITIES in ballot

def isMPS(ballot):
    return keys.MPS in ballot

def isRotman(ballot):
    return keys.ROTMAN in ballot

def noAcademics(ballot):
    return not (isHumanities(ballot) or isLifeSci(ballot) or isSocialSci(ballot) or
                isCS(ballot) or isMPS(ballot) or isRotman(ballot))

#Colleges
def isVic(ballot):
    return keys.VIC in ballot

def isUC(ballot):
    return keys.UC in ballot

def isWW(ballot):
    return keys.WW in ballot


def couldVoteForAnyDirectors(ballot):
    return (isHumanities(ballot) or isLifeSci(ballot) or isSocialSci(ballot) or
            isVic(ballot) or isUC(ballot) or isWW(ballot) or
            isCS(ballot) or isMPS(ballot) or isRotman(ballot))


def isArtsci(ballot):
    return not isUTM(ballot) and not isProfac(ballot)


#UTM

def isUTM(ballot):
    return len(ballot) == 7

#other
def _coreExecAbstensions(ballot):
    count = 0

    if abstainedPresident(ballot):
        count += 1
    if abstainedVPCL(ballot):
        count += 1
    if abstainedVPEQ(ballot):
        count += 1
    if abstainedVPEX(ballot):
        count += 1
    if abstainedVPIS(ballot):
        count += 1
    if abstainedVPUA(ballot):
        count += 1

    return count
