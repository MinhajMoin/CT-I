## CT-I Programming Assignment
## Minhaj Ahmed Moin
## hm02896


##Tiles on the Board
##board=[["Pink","Yellow","Red"],["Teal","Orange","DarkBlue"],["Teal","Purple","Gold"]]
##board=[['Pink','Pink','Pink'],['Green','Green','DarkBlue'],['Teal','Teal','Gold']]
##Board 1 simple:
##board=[['LightBlue','LightBlue','LightBlue'],['Green','Green','Orange'],['Teal','Teal','Gold']]
##Board 2 simple:
board2 = [['Yellow', 'LightBlue', 'LightBlue'], ['Orange', 'Orange', 'Orange'], ['Purple', 'Purple', 'Gold']]


## Part 1:

## Q1 of Part 1: getPositions Function
def getPositions(board, color):
    clrocc = []
    for x in range(0, len(board)):
        for i in range(0, len(board[x])):
            if color == board[x][i]:
                clrocc.append((x, i))
    return clrocc


## Q2 of Part 2: isTouching Function
# noinspection PySimplifyBooleanCheck
def isTouching(board, color1, color2, isTrue=True):
    # noinspection PySimplifyBooleanCheck
    if isTrue == False:
        return not (isTouching(board, color1, color2))
    c1 = getPositions(board, color1)
    c2 = getPositions(board, color2)
    for i in range(len(c1)):
        for j in range(len(c2)):
            if c1[i][0] == c2[j][0]:
                if c1[i][1] == c2[j][1] + 1 or c1[i][1] == c2[j][1] - 1:
                    return True
            elif c1[i][1] == c2[j][1]:
                if c1[i][0] == c2[j][0] + 1 or c1[i][0] == c2[j][0] - 1:
                    return True
    return False


## Q3 of Part 1: sameRow Function
def sameRow(board, color1, color2, isTrue=True):
    if not isTrue:
        return not (sameRow(board, color1, color2))
    c1 = getPositions(board, color1)
    c2 = getPositions(board, color2)
    for i in range(0, len(c1)):
        for j in range(0, len(c2)):
            if c1[i][0] == c2[j][0]:
                return True
    return False
                ## Q4 of Part 1: sameColumn Function


def sameColumn(board, color1, color2, isTrue=True):
    if not isTrue:
        return not (sameColumn(board, color1, color2))
    c1 = getPositions(board, color1)
    c2 = getPositions(board, color2)
    for i in range(0, len(c1)):
        for j in range(0, len(c2)):
            if c1[i][1] == c2[j][1]:
                return True
    return False

## Q5 of Part 1: inRow Function
def inRow(board, pos, color, N, isTrue=True):
##    print (board,pos,color,N)
    if isTrue==False:
        return not (inRow(board, pos, color, N))
    pos = pos.lower()
    p = 0
    if pos == 'top':
        for i in range(len(board[0])):
            if color==board[0][i]:
                p=p+1
    if pos == 'middle':
        for i in range(len(board[1])):
            if color==board[1][i]:
                p=p+1
    if pos == 'bottom':
        for i in range(len(board[2])):
            if color==board[2][i]:
                p=p+1
##    print (p)
    if p>=N:
        return True
    return False

def inColumn(board,pos,color,N,isTrue=True):
##    print (board,pos,color,N,isTrue)
    transboard=[list(i) for i in zip(*board)]
##    print (transboard)
    pos = pos.lower()
    if pos=='left':
        return inRow(transboard,'top',color,N,isTrue)
    if pos=='middle':
        return inRow(transboard,'middle',color,N,isTrue)
    if pos=='right':
        return inRow(transboard,'bottom',color,N,isTrue)

## Q7 of Part 1: isBetween Function
def isBetween(board, color, betweencol1, betweencol2, isTrue=True):
    if not isTrue:
        return not (isBetween(board, color, betweencol1, betweencol2))
    btcl1 = getPositions(board, betweencol1)
    btcl2 = getPositions(board, betweencol2)
    cl = getPositions(board, color)
    for i in range(0,len(cl)):
        for j in range(0,len(btcl1)):
            for k in range(0,len(btcl2)):                
                if btcl1[j][0] == cl[i][0] and btcl2[k][0] == cl[i][0]:
                    if (btcl1[j][1] > cl[i][1] > btcl2[k][1]) or (btcl1[j][1] < cl[i][1] < btcl2[k][1]):
                        return True
                elif btcl1[j][1] == cl[i][1] and btcl2[k][1] == cl[i][1]:
                    if (btcl1[j][0] > cl[i][0] > btcl2[k][0]) or (btcl1[j][0] < cl[i][0] < btcl2[k][0]):
                        return True
    return False
    
## Q8 of Part 1: atPlace Function
def atPlace(board, color, row, col, isTrue=True):
    if not isTrue:
        return not (atPlace1(board, color, row, col))
    r = ["top", "middle", "bottom"]
    c = ["left", "middle", "right"]
    clr = getPositions(board, color)
    for i in range(0, len(r)):
        if row == r[i]:
            for z in range(0, len(c)):
                if col == c[z]:
                    for j in range(len(clr)):
                        if clr[j][0] == i and clr[j][1] == z:
                            return True
    return False


## Q9 of Part 1: isTowards Function
def isTowards(board, color, direction, color2, isTrue=True):
    if not isTrue:
        return not (isTowards(board, color, direction, color2))
    Tcl2 = getPositions(board, color)
    Tcl1 = getPositions(board, color2)
    for i in range(0,len(Tcl1)):
        for j in range(0,len(Tcl2)):
            if direction == "under" or direction == "below":
                if sameColumn(board, color, color2):
                    if Tcl1[i][1] == Tcl2[j][1]:
                        if Tcl1[i][0] < Tcl2[j][0]:
                            return True                        
            if direction == "above":
                if sameColumn(board, color, color2):
                    if Tcl1[i][0] > Tcl2[j][0]:
                        return True
            if direction == "right":
                if sameRow(board, color, color2):
                    if Tcl1[i][1] < Tcl2[j][1]:
                        return True
            if direction == "left":
                if sameRow(board, color, color2):
                    if Tcl1[i][1] > Tcl2[j][1]:
                        return True
    return False

## Part 2

## Q1 of Part 2
def getColors(colors):
    colors=colors.strip('\n')
    return colors.split(' ')


## Q2 of Part 2
def getRules(rules):
    rules.replace('.',' ')
    rules = rules.split('\n')
    k=[]
    for i in range(0,len(rules)):
        if rules[i]!='':
            k.append(rules[i])
    return k

## Q3 of Part 2
def inputFromFile(filename):
    fl = open(filename, 'r')
    x = fl.readlines()
    p = x[0]
    p = p.strip('\n')
    p = p.split(' ')
    k = []
    for i in range(2, len(x), 1):
        c = x[i]
        c = c.strip('\n')
        if c!='':
            k.append(c)
    return p, k


## Q4 of Part 2
def isValidBoard(board, colors):
    x = 0
    for j in range(0, len(colors)):
        for i in range(0, len(board)):
            for k in range(0, len(board[i])):
                if colors[j] == board[i][k]:
                    x += 1
                    break
    return x == 9 and len(board) == 3


## Q5 of Part 2
def checkRules(board, rules):
    for i in range(0, len(rules)):
        z = rules[i].split(' ')
        if z[0] == 'col':
            ##            print ('col')
            if z[len(z) - 1] == 'not':
                if inColumn(board, z[3], z[1], z[2], False) == False:
                    return False
            else:
                if inColumn(board, z[3], z[1], int(z[2])) == False:
                    return False
        if z[0] == 'row':
            ##            print ('row')
            if z[len(z) - 1] == 'not':
                if inRow(board, z[3], z[1], z[2], False) == False:
                    return False
            else:
                if inRow(board, z[3], z[1], int(z[2])) == False:
                    return False
        if z[0] == 'place':
                c = z[2].split('.')
##                print(c)
                if len(c)==1:
                    if atPlace(board,z[1],c[0],c[0])==False:
                        return False
                else:
                    if z[len(z) - 1] == 'not':
                        if atPlace(board, z[1], c[0], c[1], False) == False:
                            return False
                    else:
    ##                    if len(z)==3:
    ##                        return atPlace(board,z[1],z[2],z[2])
                        if atPlace(board, z[1], c[0], c[1]) == False:
                            return False
        if z[0] == 'samerow':
            ##            print ('samerow')
            if z[len(z) - 1] == 'not':
                if sameRow(board, z[1], z[2], False) == False:
                    return False
            else:
                if sameRow(board, z[1], z[2]) == False:
                    return False
        if z[0] == 'samecol' or z[0] == 'samecolumn':
            ##            print('samecol')
            if z[len(z) - 1] == 'not':
                if sameColumn(board, z[1], z[2], False)== False:
                    return False
            else:
                if sameColumn(board, z[1], z[2]) == False:
                    return False
        if z[0] == 'touch' or z[0] == 'touches':
            ##            print('touch')
            if z[len(z) - 1] == 'not':
                if isTouching(board, z[1], z[2], False) == False:
                    return False
            else:
                if isTouching(board, z[1], z[2]) == False:
                    return False
        if z[0] == 'towards' or z[0]=='toward':
            if z[len(z) - 1] == 'not':
                if isTowards(board, z[1], z[2],z[3], False) == False:
                    return False
            else:
                if isTowards(board, z[1], z[2],z[3]) == False:
                    return False
    return True

## Part 3

## Q1 of Part 3: MakePermutations Function
def MakePermutations(colors):
    import itertools
    return list(itertools.permutations(colors))

## Q2 of Part 3: GameSolver Function
def GameSolver(filename):
    c = inputFromFile(filename)
##    for i in c:
##        if i == '' :
##            print (i)
##            c.remove(i)
##    print (c)
##    while '' in c:
##        c.remove('')
    m = MakePermutations(c[0])
##    print (c)
    for i in m:
        board = [[i[0], i[1], i[2]], [i[3], i[4], i[5]], [i[6], i[7], i[8]]]
        if checkRules(board, c[1])==True:
            return board
#Exceptional case for GameSolver:
(['Pink', 'Pink', 'Yellow', 'Green', 'Green', 'Orange', 'Teal', 'Purple', 'Gold'], ['towards Green left Orange', 'touch Green Orange', '', 'towards Pink left Orange', 'touch Pink Orange not', '', 'towards Green right Yellow', 'touch Green Yellow', '', 'towards Purple left Green', 'touch Purple Green not', '', 'towards Orange above Green', '', 'place Pink middle', 'touch Pink Green', '', 'towards Teal below Orange', 'touch Teal Orange'])
