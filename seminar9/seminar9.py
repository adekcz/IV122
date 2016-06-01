import sys, os, inspect
cmd_folder = os.path.realpath(os.path.abspath(os.path.split(inspect.getfile( inspect.currentframe() ))[0]))
parent = "/".join(cmd_folder.split("/")[0:-1])
parent += "/commonScripts"
sys.path.insert(0,parent)

import IV122Graphics
import Commons
import random


def alwaysSwitch():
    return True
def alwaysDontSwitch():
    return False
def switchRandomly():
    return random.randint(0,1) == 0

def montyHallSimulation(n, strategy):
    succesCount = 0
    for i in range(n):
        carLocation = random.randint(0,2)
        firstChoice = random.randint(0,2)
        switchForSecondChoice = strategy()
        
        if (firstChoice == carLocation and switchForSecondChoice == False):
            succesCount += 1
        if (firstChoice != carLocation and switchForSecondChoice == True):
            succesCount += 1
    return succesCount

def montyHallEval():
    n = 1000
    print("n: " + str(n))
    print("succesCount with alwaysSwitch: " + str(montyHallSimulation(n, alwaysSwitch)))
    print("succesCount with alwaysDontSwitch: " + str(montyHallSimulation(n, alwaysDontSwitch)))
    print("succesCount with switchRandomly: " + str(montyHallSimulation(n, switchRandomly)))
    
    


def frequencyAnalysis(numbers):
    choices = [0 for x in range(6)]
    for num in numbers:
        choices[num-1] = choices[num-1] + 1
    return choices


def countSeq(numbers, seq):
    count = 0
    for i in range(0, len(numbers) - len(seq), len(seq)):
        for j in range(len(seq)):
            if(numbers[i+j] != seq[j]):
                break
            if (j == len(seq) -1):
                count = count +1
    return count


def frequencyOfSequencesAnalysis(numbers): #v nahodnem vzorku by frekvence sekvenci delky vetsi nez 1 mela odpovidat pravdepodobnosti..
    result = []

    sampleSequences = [(x,y) for x in range(1,6) for y in range(1,6)]
    print  "\texpected absolute: ", len(numbers)*(1.0/36.0)/2,  "ratio: ",1/36.0
    for seq in sampleSequences:
        count = countSeq(numbers, seq) #pocita neprekrivajici se dvojce, (takze polovicni celkovy pocet vzorku), kdyby se to prekrivalo, tak to asi neni nezavisle a ma to jinou pravdepodobonst
        print "\t",  seq, ":", count, "->", count / (float(len(numbers))/2)


def chiKvadratTest(numbers):
    expected = len(numbers)/6
    
    choices = frequencyAnalysis(numbers)

    S = 0
    for i  in range(6):
        S = S + (choices[i] - expected)**2 / float(choices[i])

    return S


def analyseFile(name):
    data = [int(x) for x in open(name).readlines()[0].split(" ")]
    print "_----_--------------------------------//----//////__"
    print "analysing file: ", name, "rolls: ", len(data)
    print "frequency Analysis"
    choices = frequencyAnalysis(data)
    for i in range(6):
        print "\t",  i+1, ":", choices[i], " -> ", choices[i] / float(len(data))

    print "chi square"
    S =chiKvadratTest(data) 
    
    if (S > 2.34):
        print "\t with more then 20 percent is not random"
    elif (S > 1.61):
        print "\t with 10 percent is not random"
    elif (S > 1.14):
        print "\t with 5 percent is not random (still quite random)"
    else:
        print "\t probably random"

    print "frequency seq"
    frequencyOfSequencesAnalysis(data)


def diceUpper(): #probablity weighted by number
    choice = random.randint(1,21)
    for i in range(1,7):
        if (choice <= i):
            return i
        choice = choice - i
    return 

def diceLower():
    return 7 - diceUpper()

def tossRandomDice():
    return randomDice()()

def randomDice():
    if random.randint(0,1) %2==0:
        return diceUpper
    return diceLower

def cltExperiment(n, dice):
    avgs = []
    for i in range(n):
        suma = 0
        for j in range(n): 
            suma = suma + dice()

        avgs.append(float(suma)/n)
    return avgs
    
def processExperiment(avgs):
    avg = sum(avgs)/len(avgs)
    sigma = 0
    for i in avgs:
        sigma = (avg - i)**2
    sigma = (sigma/len(avgs))**0.5
    print "average:", avg, "sigma:", sigma

    return
def centralLimitTheorem(n):
    print "Experiment1 - weighted by number"
    
    avgs = cltExperiment(n, diceUpper)
    processExperiment(avgs)

    print "Experiment2 - each toss random dice"
    
    avgs = cltExperiment(n, tossRandomDice)
    processExperiment(avgs)

    print "Experiment3 - choose dice randomly"
    
    avgs = cltExperiment(n, randomDice())
    processExperiment(avgs)






if __name__ == "__main__":
    #montyHallEval()

    #for i in range(1,6):
    #    analyseFile("randomSequences/random" + str(i) +".txt")

    centralLimitTheorem(1000)
