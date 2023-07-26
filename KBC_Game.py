#  qustion list

qustions = [
["Which of the following corresponds to ek bataa do?",'Pura', 'Sawa','Adha','Pauna',3],
["Which of the following gods is also known as Gauri Nandan?",'Agni','Indra','Hanuman','Ganesha',4],
["n the game of ludo the discs or tokens are of how many colours?",'One','Two','Three','Four',4],
['Which of these are names of national parks located in Madhya Pradesh?','Krishna and Kanhaiya','Kanha and Madhav','Ghanshyam and Murari','Girdhar and Gopal',2],
[' Where was the BRICS summit held in 2014?','Brazil','India','Russia','China',1],
['Who wrote the introduction to the English translation of Rabindranath Tagores Gitanjali?','P.B. Shelley','Alfred Tennyson','W.B. Yeats','T.S. Elliot',3],
['Which of these leaders was a recipient of a gallantry award in 1987 by a state government for saving two girls from drowning?','Anandiben Patel','Vasundhara Raje Scindia','Uma Bharti','Mamata Banerjee',1],
[' The wife of which of these famous sports persons was once captain of Indian volleyball team?',' K.D.Jadav','Dhyan Chand',' Prakash Padukone','Milkha Singh',4],
[' Which of these terms can only be used for women?','Dirghaayu','Suhagan','Chiranjeevi','Sushil',2],
['Which of these sports requires you to shout out a word loudly during play?','Ludo','Kho-kho','Playing cards','Chess',2]
]

#  create amount list

ammount = [0,1000,2000,3000,5000,10000,20000,40000,80000,160000,320000]

# created marks list 

qustionMarks = ['A','B','C','D']

# convet user Answer into num 1 to 4

def usrAswer():
    while True:
        ans = input('Enter Your Answer (A - B - C - D) :- ').upper()
        ansNum=0
        if ans == qustionMarks[0]:
            ansNum = int(1)
            return ansNum
            
        elif ans == qustionMarks[1]:
             ansNum = int(2)
             return ansNum
           
        elif ans == qustionMarks[2]:
             ansNum = int(3)
             return ansNum
            
        elif ans == qustionMarks[3]:
             ansNum = int(4)
             return ansNum
        elif ans == 'Q':
                return 'Q'
        elif ans == '':
            print('Opps !! Please Enter Somthing !! ')
        elif ans != 'A' or ans != "B" or ans != "C" or ans != "D" :
            print (f'Opps !!! You Enter Wrong inpute " {ans} "!!! You can only enter (A TO D) !!! ' )


# check winnig amount 

def checkLastAmount(c):
    a = 0
    if c > 8:
        a = 8
    elif c > 5:
        a = 5
    elif c > 3:
        a = 3
    return a



# check piece qustion

def pieceMony(f,d):
    if f >= 8:
        print(f'!!! This is your piece Qustion amount RS.{d} If you can lose next Qustion Amount You cannot loose all mony!! (.^.) ')
    elif f>=5:
        print(f'!!! This is your piece Qustion amount RS.{d} If you can lose next Qustion Amount You cannot loose all mony!! (.^.) ')
    elif f>=3:
        print(f'!!! This is your piece Qustion amount RS.{d} If you can lose next Qustion Amount You cannot loose all mony!! (.^.) ')



# create variable length of qustion list
qustionsLen = len(qustions) + 1

# set defouat amount price rs.0
q = 1

# Print Welcome lines

print('\n'*100)
print(f'@@@@@@@@@@@@@@@@   Welcome to KBC Game  @@@@@@@@@@@@@@@@')
print('\n'*2)

for qustion in qustions:

    # Qustion Print

    print('\n'*5)
    print(f':###########  Qustion for Rs.{ammount[q]}  ###########:')
    print('\n')

    # Qustion Option print

    print(f'{q}. {qustion[0]}')
    print('\n')
    print(f'{qustionMarks[0]}.{qustion[1]}                           {qustionMarks[1]}.{qustion[2]}')
    print(f'{qustionMarks[2]}.{qustion[3]}                           {qustionMarks[3]}.{qustion[4]}')
    print('\n')

    #  chek if aswer is true or not
    aswer = usrAswer()
    if qustion[-1] == aswer:
        print('\n')
        print(f'Congratulation !!! Your Answer Is Right You WON Rs.{ammount[q]} !!!')
        print('\n')
        # check piece qustion inpute currect qustion no. & currunt amount
        pieceMony(q,ammount[q])
    elif 'Q' == aswer:
        print('\n')
        print(f'Your Winning Amount is Rs.{ammount[checkLastAmount(q)]} ')
        print('\n')
        print (f'Thank You For Playing KBC ////')
        break
        # print()


    else:
        # run amount last 
        b = checkLastAmount(q) + 1
        
        print(f'***** Your Answer is wrong You Won Rs.{ammount[b-1]} **********')
        print('\n')
        print(f'Right Answer is {qustionMarks[qustion[-1]-1]}.{qustion[qustion[-1]]}')
        print('\n')
        print("Thank You For Playing KBC ////")
        print('\n'*5)
        break

    q += 1

    # End of code *****************************************************************************************
