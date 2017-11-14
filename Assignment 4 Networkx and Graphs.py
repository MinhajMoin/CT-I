##----------------------------------##
## Name: Minhaj Ahmed Moin          ##
##----------------------------------##
## ID: hm02896                      ##
##----------------------------------##

## Import Modules
from __future__ import division
import csv
import networkx as nt
import matplotlib.pyplot as plt
##-----------------------------------
## Helper Functions
def listOfNodes(g): return g.nodes()
def listOfEdges(g): return g.edges()
def adjacencyMatrix(g): return nt.adjacency_matrix(g).todense()
def adjacencyList(g): return [tuple(x.split(' ')) for x in list(nt.generate_adjlist(g))]
def drawGraph(g):nt.draw(g,with_labels=True)
def dnd(g):
    for i in listOfNodes(g):
        print (i,':\n')
        print ('Neighbors:',nt.neighbors(g,i))
        print ('In Degrees:',g.in_degree(i))
        print ('Out Degrees:',g.out_degree(i),'\n')
def printNeighboursAndDegrees(g):
    for i in listOfNodes(g):
        print (i,'\nNeighbors:',nt.neighbors(g,i))
        print ('Degree:',g.degree(i),'\n')
def printInDegreeOutDegree(g):
    for i in listofNodes(g):
        print (i,'\nIn Degrees:\n',g.in_degree(i),'\nOut Degrees:\n',g.out_degree(i),'\n')
def addWeightedEdges(g,lst):
    for i in lst:
        g.add_edge(i[0],i[1],weight=i[2])
def sumInDegrees(g):
    in_count=0
    v=listOfNodes(g)
    for i in v:
        in_count+=g.in_degree(i)
    return in_count
def sumOutDegrees(g):
    out_count=0
    v=listOfNodes(g)
    for i in v:
        out_count+=g.out_degree(i)
    return out_count
def sumEdges(g):return g.number_of_edges()
def compareDegreesAndEdges(g):return sumInDegrees(g)==sumOutDegrees(g)==sumEdges(g)
def graphDiameter(g): return nt.diameter(g)
def graphDensity(g): return nt.density(g)


def Bracket(exp,p):
##    print (exp)
    if p=='()':
        openp,closep='(',')'
    elif p=='{}':
        openp,closep='{','}'
    l=[]
    k=[]
    m=[]
    zx=[]
    ocount=0
    ccount=0
    for i in range(len(exp)):
        if exp[i]==openp or exp[i]==closep:
            l.append(exp[i])
            k.append(exp[i])
            m.append(exp[i])
            zx.append(exp[i])
    if len(l)==0:
        return 'List Empty'
    for i in range(len(l)):
        a=l.pop()
        if a==openp:
            ocount+=1
        elif a==closep:
            ccount+=1
    o= ocount==ccount
    if o==False:
        return o
    elif o==True:
        un_resolved=0
        rev1,rev2=[],[]
        for i in range(len(k)):
            abc=k.pop()
            rev1.append(abc)
            rev2.append(abc)
        if zx.pop()==openp or rev1.pop()==closep:
            return False
        for i in range(len(m)):
##            print (m)
##            print (un_resolved)
            a=m.pop()
            if a==closep:
                un_resolved+=1
            elif a==openp:
                un_resolved-=1
            if un_resolved<0:
                return False
    return True




def checkRoundCurlyPBalance(exp):
##    print (exp)
    l=[]
    k=[]
    m=[]
    zx=[]
    xy=[]
    Cocount=0
    Cccount=0
    Rocount=0
    Rccount=0
    for i in range(len(exp)):
        if exp[i] in '(){}':
            l.append(exp[i])
            k.append(exp[i])
            m.append(exp[i])
            zx.append(exp[i])
            xy.append(exp[i])
    if len(l)==0:
        return 'List Empty'
    sC,sC2=[],[]
    sR,sR2=[],[]
    for i in range(len(l)):
        a=l.pop()
        if a=='(':
            Rocount+=1
            sR.append(a)
            sR2.append(a)
        elif a==')':
            Rccount+=1
            sR.append(a)
            sR2.append(a)
        elif a=='}':
            sC.append(a)
            sC2.append(a)
            Cccount+=1
        elif a=='{':
            sC.append(a)
            sC2.append(a)
            Cocount+=1
##    print (Cocount,Cccount)
##    print (Rocount,Rccount)
    if not sR:
        return checkCurlyPBalance(exp)
    if not sC:
        return checkRoundPBalance(exp)
    sCR,sRR=[],[]
    for i in range(len(sC)):
        sCR.append(sC.pop())
    for i in range(len(sR)):
        sRR.append(sR.pop())
##    print (sCR,sRR)
##    sc2,scr,sr2,srr=sC2.pop(),sCR.pop(),sR2.pop(),sRR.pop()
    if sC2.pop()=='}' or sCR.pop()=='{':
        print ('l')
        return False
    if sR2.pop()==')' or sRR.pop()=='(':
        return False
##    print (sC2.pop(),sCR.pop(),sR2.pop(),sRR.pop())
    o= (Cocount==Cccount or Rocount==Rccount)
    if o==False:
        return o
    elif o==True:
        un_resolvedR=0
        un_resolvedC=0
        un_resolvedCR=-1
        rev1,rev2,rev3=[],[],[]
        for i in range(len(k)):
            abc=k.pop()
            rev1.append(abc)
            rev2.append(abc)
            rev3.append(abc)
        if zx.pop()=='(' or rev1.pop()==')':
            return False
        if xy.pop()=='{' or rev3.pop()=='}':
            return False
        for i in range(len(m)):
##            print (m)
##            print ('R=',un_resolvedR)
##            print ('C=',un_resolvedC)
            a=m.pop()
            if a=='(':
                if un_resolvedCR>=0:
                    unresolvedCR+=1
                un_resolvedR-=1
##                print ('k')
            elif a==')':
                if un_resolvedCR>=0:
                    unresolvedCR-=1
                un_resolvedR+=1
            elif a=='{':
                if unresolvedCR==0:
                    un_resolvedC-=1
                if unresolvedCR<0:
                    return False
                unresolvedCR=-1
            elif a=='}':
                unresolvedCR=0
                un_resolvedC+=1
##            if unresolvedCR<0:
##                return False
##            print (i+1,'R=',un_resolvedR,'C=',un_resolvedC)
##            print ('C=',un_resolvedC)
##            print (un_resolvedC, un_resolvedR)
            if un_resolvedC<0 or un_resolvedR<0:
                return False
    return True
##------------------------------------

## Q1)
def Question1():
    g=nt.Graph([(1,2),(2,3),(2,5),(2,4),(1,5),(4,3),(4,5)])
    print(listOfNodes(g),'\n',listOfEdges(g),'\n',adjacencyMatrix(g),'\n',adjacencyList(g),'\n',dnd(g))

##------------------------------------

## Q2)
def Question2():
    a=nt.MultiDiGraph([(1,2),(2,4),(3,1),(3,2),(4,3),(4,4)])
    nt.draw(a,with_labels=True)
    print ('Nodes=\n',listOfNodes(a))
    print ('Edges=\n',listOfEdges(a))
    print ('Adjacency Matrix=\n',adjacencyMatrix(a))
    print ('Adjacency List=\n',adjacencyList(a))
    print ('Neighbors and In and Out Degree of each Node:\n')
    print (dnd(a))
    plt.show()

##-------------------------------------

## Q3)
def Question3():
    m=nt.MultiDiGraph()
    c=['Denver','Chicago','Houston','Austin','Washington','Atlanta','Dallas']

    m.add_edge(c[0],c[1],weight=1000)
    m.add_edge(c[0],c[5],weight=1400)

    m.add_edge(c[1],c[0],weight=1000)

    m.add_edge(c[2],c[5],weight=800)

    m.add_edge(c[3],c[6],weight=200)
    m.add_edge(c[3],c[2],weight=160)

    m.add_edge(c[4],c[5],weight=600)
    m.add_edge(c[4],c[6],weight=1300)

    m.add_edge(c[5],c[4],weight=600)
    m.add_edge(c[5],c[2],weight=800)

    m.add_edge(c[6],c[0],weight=780)
    m.add_edge(c[6],c[3],weight=200)
    m.add_edge(c[6],c[1],weight=900)

##    nt.draw(m,with_labels=True)
    nt.draw_circular(m, with_labels=True,node_size=500,node_color='0.8',font_size=6)
    edge_labels = nt.draw_networkx_edge_labels(m, with_labels=True,node_size=800,node_color='0.8',font_size=6,pos=nt.circular_layout(m))
    in_count=0
    out_count=0
    for i in range(len(c)):
        in_count+=m.in_degree(c[i])
        out_count+=m.out_degree(c[i])
        print (c[i],':\n'+'In Degree=',m.in_degree(c[i]),'\nOut Degree=',m.out_degree(c[i]),'\n')
    print ("\nAre the number of edges equal to in degrees and out degrees of nodes?\n"+str(in_count==out_count==m.number_of_edges()))
    print('Diameter of Graph=',nt.diameter(m))
    print ('Density of Graph=',nt.density(m))
    plt.show()
    return

##---------------------------------------

## Q4)
def Question4():
    G1=nt.Graph([('a','b'),('b','c'),('c','e'),('b','e'),('e','d'),('a','d')])
    G2=nt.Graph([('a','b'),('b','c'),('b','d'),('b','f'),('c','f')])
    G=nt.compose(G1,G2)
    nt.draw(G,with_labels=True)
    print ('Nodes=',listOfNodes(G),'\nEdges=',listOfEdges(G),'\nAdjacency Matrix=\n',adjacencyMatrix(G),'\nAdjacency List=\n',adjacencyList(G))
    plt.show()
    return

##---------------------------------------

## Q5
def LoadDataIntoGraph(filename):
    c=[x for x in csv.reader(open(filename))]
    G=nt.Graph()
##    print (G.nodes())
##    print(listOfNodes(G))
    for i in c[1:]:
        for j in range(1,len(i)):
            if i[j]!='-1' and i[j]!='0':
                G.add_edge(i[0],c[0][j],weight=int(i[j]))
    print ('Nodes:\n',listOfNodes(G))
    print ('Edges:\n',listOfEdges(G))
    print ('Adjacency Matrix:\n',adjacencyMatrix(G))
    print ('Adjacency List:\n',adjacencyList(G))
    print ('Neighbors and Degrees:')
    print (printNeighboursAndDegrees(G))
    nt.draw(G,with_labels=True)
    plt.show()

##print (LoadDataIntoGraph('connections.csv'))

##---------------------------------------

## Q6)
def reverseString(string):
    lst=[x for x in string]
    l=[]
    for i in range(len(lst)):
        l.append(lst.pop())
    return ''.join(l)

##----------------------------------------

## Q7)
## This function uses a previously defined helper function called Bracket(exp,p)
## which takes in the expression and type of parenthesis to evaluate. That
## helper function uses stacks.
def checkRoundPBalance(exp): return Bracket(exp,'()')
def checkCurlyPBalance(exp): return Bracket(exp,'{}')

##----------------------------------------

## Q8)
##def checkRoundCurlyPBalance(exp): 
##    print (exp)
##    if checkRoundPBalance(exp)=="List Empty":
####        print ('() Empty')
##        if checkCurlyPBalance(exp)=='List Empty':
####            print ('() {} Empty')
##            return False
##        else:
##            return checkCurlyPBalance(exp)
##    elif checkCurlyPBalance(exp)=="List Empty":
####        print ('{} Empty')
##        if checkRoundPBalance(exp)=='List Empty':
####            print ('{} () Empty')
##            return False
##        else:
##            return checkRoundPBalance(exp)
##    else:
##        return (checkRoundPBalance(exp) and checkCurlyPBalance(exp))

z=checkRoundCurlyPBalance
##----------------------------------------

## Q9)
def postfixEval(exp):
    print (exp)
    m=[]
    for i in exp.split():
        if i in '+-*/':
            a1,a2=m.pop(),m.pop()
            m.append(str(eval(a2+i+a1)))
        else:
            m.append(i)
    return float(''.join(m))

##print (postfixEval('10 4 /'))
##--------------------------------------##
##              The End                 ##
##--------------------------------------##
