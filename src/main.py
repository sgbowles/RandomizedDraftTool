import secrets
import time
import copy
import random
from twitter import *

consumer_key = ""
consumer_secret = ""
access_key = ""
access_secret = ""

def run_baseball():
    names = ["Temp1", "Temp2", "Temp3", "Temp4", "Temp5", "Temp6", "Temp7", "Temp8", "Temp9"]
    tweet = Twitter(auth = OAuth(access_key, access_secret, consumer_key, consumer_secret))
    #winners = [["Jay Massey", 0], ["Blake Goleman", 0], ["Tim Hrubetz", 0], ["Jon Meisterling", 0], ["Stevan Bowles", 0], ["Jason May", 0], ["Conor Rowe", 0], ["John Ernst", 0], ["Jonathan Gelert", 0] ]
    #runs = int(input("How many runs? "))
    #it_runs = 0
    #while(it_runs < runs):

    #build lottery dict
    lottery = {}
    seed = 1
    for i in range(len(names)):
        #print (names[i])
        protected = False
        if seed < 4:
            protected = True
        nestedList = [names[i], protected]
        lottery[int(seed)] = nestedList
        seed += 1

    lotteryList = []
    it = 0
    for x in lottery:
            #print('Seed {} has the key of {}'.format(x, lottery[x]))
            if x < 4:
                for i in range(8):
                    lotteryList.append(lottery[x])
            elif x < 5:
                for i in range(7):
                    lotteryList.append(lottery[x])
            elif x < 6:
                for i in range(6):
                    lotteryList.append(lottery[x])
            elif x < 7:
                for i in range(5):
                    lotteryList.append(lottery[x])
            elif x < 8:
                for i in range(4):
                    lotteryList.append(lottery[x])
            else:
                for i in range(3):
                    lotteryList.append(lottery[x])
            
    '''
    for l in lotteryList:
        print (l)
        '''
    guarCount = 0
    seedCount = 0
    curWinList = []
    while 1:
        if len(lotteryList) <= 0:
            break
        
        if seedCount < 6:
            if (seedCount - guarCount) == 3:
                guarList = []
                #print("HERE")
                for n in range(len(lotteryList)):
                    if lotteryList[n][1]:
                        guarList.append(lotteryList[n])
                #print(tempList)
                x = secrets.randbelow(len(guarList))
                newName = guarList[x][0]
                
            else:
                #print("NOW HERE 2")
                x = secrets.randbelow(len(lotteryList))
                newName = lotteryList[x][0]
            
        else:
            #print("NOW HERE")
            x = secrets.randbelow(len(lotteryList))
            newName = lotteryList[x][0]
        #print (x)
        #print(lotteryList[x])
        curWinList.append(newName)
        #print ('{}. {}'.format((seedCount+1),newName))
        tempList = []
        #print (len(lotteryList))
        isGuar = False
        for n in range(len(lotteryList)):
            if newName != lotteryList[n][0]:
                tempList.append(lotteryList[n])
            else:
                if lotteryList[n][1]:
                    isGuar = True
        if isGuar:
            guarCount += 1
            isGuar
        #print(guarCount)
        lotteryList = copy.deepcopy(tempList)
        seedCount += 1
        #print(seedCount)
        #print(lotteryList)
        #time.sleep(2)
    #for z in range(len(winners)):
        #if curWinList[0] == winners[z][0]:
            #winners[z][1] += 1
    #it_runs += 1
    #print(it_runs)

            
    curWinList.append("Temp10")
    curWinList.append("Temp11")
    curWinList.append("Temp12")
    print(curWinList)
    '''
    pos = 12
    p_Count = 0
    output_Str = ""
    '''

    count = curWinList.__len__()

    firstNum = count
    secNum = count - 2

    output = "Draft selection results " + str(firstNum) + " - " + str(secNum) + ":\n"

    for teamName in reversed(curWinList):
        output += str(count) + ": " + teamName + "\n"
        if count == secNum:
            results = tweet.statuses.update(status=output)
            firstNum -= 3
            secNum -= 3
            output = "Draft selection results " + str(firstNum) + " - " + str(secNum) + ":\n"
            time.sleep(120)
        count -= 1


        
            
    #for y in range(len(winners)):
        #print ('{}       \twon {} time(s) out of {}'.format((winners[y][0]),winners[y][1], runs))


def run_football():
    #initialize names and Twitter API
    names = ["Wes Maxey", "Stevan Bowles", "Marshall Bowles", "Jason Anderson", "Nick Funk", "Ryan Fish", "Ben Johnson", "Justin Shotgunn", "Jared Harper", "Chase Macarski", "Doug Zola", "Chase Stanton"]
    tweet = Twitter(auth = OAuth(access_key, access_secret, consumer_key, consumer_secret))
    
    #shuffle list 5 times
    for i in range(5):
        random.shuffle(names)
     
    #Inital tweet to indicate the order is coming sleep for 1 min before sending first set
    output = "Post Lockout League Draft Order Selection INCOMING!!!"
    results = tweet.statuses.update(status=output)
    time.sleep(60)
    #print(output)
    
    #initialize count and breaks to only show 3 at a time
    count = names.__len__()
    first = count
    last = first - 2
    
    output = "Draft selection results " + str(first) + " - " + str(last) + ":\n"
    
    #Tweet the list in reverse (i.e. 12 to 1) and in sets of 3 in 2 minute intervals
    for name in reversed(names):
        output += str(count) + ": " + name + "\n"
        if count == last:
            print("Tweet incoming")
            results = tweet.statuses.update(status=output)
            #print(output)
            first -= 3
            last -= 3
            output = "Draft selection results " + str(first) + " - " + str(last) + ":\n"
            time.sleep(120)
        count -= 1
    
    #This prints to my console for me to verify that the order matches with what was tweeted 
    debug_count = 1
    for name in names:
        print ('{}. {}'.format(debug_count,name))
        debug_count += 1


if __name__== "__main__":
    while(1):
        opt = int(input("Options:\n(1)\tBaseball\n(2)\tFootball\n\nEnter Number: "))
        if opt == 1:
            run_baseball()
            break
        elif opt == 2:
            run_football()
            break
        else:
            print("Invalid option, try again!")
