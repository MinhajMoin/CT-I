from time import clock
import random
import csv
##import matplotlib.pyplot as plt
filename='books.csv'
##--------------------------------------------------------------------------
## Helper Functions

#### Checks if the given string is a true integer or not
##def is_int(s):
##    try:
##        int(s)
##        return True
##    except ValueError:
##        return False
##
#### Checks if the given string is a true float or not
##def is_float(s):
##    try:
##        float(s)
##        return True
##    except ValueError:
##        return False
##
#### Builds a Full List based on the order of sorted column
##def list_builder(sortedlist,col):
##    m=LoadData(filename)
##    l=[]
##    for h in sortedlist:            
##        for i in range(len(m)):
##            if col==4:
##                if is_int(m[i][4]):
##                    if h==int(m[i][4]):
##                        l.append(m[i])
##                        m[i]=('done','done','done','done','done')
##            elif col==3:
##                if is_float(m[i][3]):
##                    if h==float(m[i][3]):
##                        l.append(m[i])
##                        m[i]=('done','done','done','done','done')
##            elif h==m[i][col]:
##                l.append(m[i])
##                m[i]=('done','done','done','done','done')
##    return l
##
#### Time Print and List Ascending/Descending Order
##def timer(initial_time,building_time,final_time,sortedlist,ascending):
####    print ('Sorting Time=',final_time-initial_time)
####    print ('Listing Building time=',-(building_time-final_time))
####    print ('Total Time=',building_time-initial_time,end='\n\n')
##    print ('initial time=',initial_time)
##    print ('final_time=',final_time)
##    print ('building time=',building_time)
##    if ascending==False:
##        sortedlist.reverse()
##    return sortedlist

##--------------------------------------------------------------------------

## Core Sorting Functions

## MergeSort
def msort(lst,col,ascending):
    if len(lst) < 2:
        return lst
    sorted_list = []
    mid = int(len(lst) / 2)
    y = msort(lst[:mid],col,ascending)
    z = msort(lst[mid:],col,ascending)
    i = 0
    j = 0
    if ascending==True:
        while i < len(y) and j < len(z):
                if y[i][col] > z[j][col]:
                    sorted_list.append(z[j])
                    j += 1
                elif y[i][col] < z[j][col]:
                    sorted_list.append(y[i])
                    i += 1
                elif y[i][col] == z[j][col]:
                    sorted_list.append(y[i])
                    i += 1
    else:
        while i < len(y) and j < len(z):
                if y[i][col] < z[j][col]:
                    sorted_list.append(z[j])
                    j += 1
                elif y[i][col] > z[j][col]:
                    sorted_list.append(y[i])
                    i += 1
                elif y[i][col] == z[j][col]:
                    sorted_list.append(y[i])
                    i += 1
    sorted_list += y[i:]
    sorted_list += z[j:]
    return sorted_list

#### SelectionSort
##def sst(lst,col):
##    for h in range(0, len(lst)):
##        j = h
##        for i in range(h,len(lst)):
##            if col==3:
##                if float(lst[j][col])>float(lst[i][col]):
##                    j = i
##            elif col==4:
##                if int(lst[j][col])>int(lst[i][col]):
##                    j = i
##            else:
##                if lst[j][col] > lst[i][col]:
##                    j = i
##        lst[j],lst[h]=lst[h],lst[j]
####        lst.insert (h,lst.pop(j))
##    return lst

##def quicksort(lst,col,ascending):
##    if len(lst)==0:
##        return lst
##    if ascending==True:
##        return quicksort([x for x in lst if x[col] < lst[0][col]],col,ascending) \
##            + [x for x in lst if x[col] == lst[0][col]] \
##            + quicksort([x for x in lst if x[col] > lst[0][col]],col,ascending)
##    else:
##        return quicksort([x for x in lst if x[col] > lst[0][col]],col,ascending) \
##            + [x for x in lst if x[col] == lst[0][col]] \
##            + quicksort([x for x in lst if x[col] < lst[0][col]],col,ascending)

def quicksort(lst,col,ascending):
    if len(lst)<1:
        return []
    big=[]
    medium=[]
    small=[]
    p=random.choice(lst)
    pivot=p[col]
    for i in lst:
        if i[col] > pivot:
            big.append(i)
        if i[col] < pivot:
            small.append(i)
        if i[col]==pivot:
            medium.append(i)
    a=quicksort(small,col,ascending)
    b=medium
    c=quicksort(big,col,ascending)
    if ascending == True:
        return a+b+c
    else:
        return c+b+a



##def q1(lst):
##    if len(lst)==0:
##        return lst
##    a= q1([x for x in lst if x < lst[0]])
##    b= [x for x in lst if x == lst[0]]
##    c= q1([x for x in lst if x > lst[0]])
##    print (a)
##    print (b)
##    print (c)
##    return a+b+c
##
##def e(lst,col=-1):
##    if lst:
##        p=random.choice(lst)
##    elif not lst:
##        return lst
##    if col==-1:
##        return e([x for x in lst if x < p],col) \
##            + [x for x in lst if x == p] \
##            + e([x for x in lst if x > p],col)
##    elif col==3:
##        i=p[col]
##        return e([x for x in lst if float(x[col]) < float(i)],col) \
##            + [x for x in lst if float(x[col]) == float(i)] \
##            + e([x for x in lst if float(x[col]) > float(i)],col)
##    elif col==4:
##        i=p[col]
##        return e([x for x in lst if int(x[col]) < int(i)],col) \
##            + [x for x in lst if int(x[col]) == int(i)] \
##            + e([x for x in lst if int(x[col]) > int(i)],col)
##    else:
##        i=p[col]
##        return e([x for x in lst if x[col] < i],col) \
##            + [x for x in lst if x[col] == i] \
##            + e([x for x in lst if x[col] > i],col)


#### Quick Sort
##def qsort(lst):
##    slist=[]
##    blist=[]
##    mlist=[]
##    if len(lst) == 0:
##        return lst
##    pivot=int(len(lst)/2)
##    for j in lst:
##        if j<pivot:
##            slist.insert(-1,j)
##        elif j>pivot:
##            blist.insert(-1,j)
##        elif j==pivot:
##            mlist.insert(-1,j)
##    print (slist)
##    print (mlist)
##    print (blist)
##    return slist+mlist+blist
##--------------------------------------------------------------------

## Programming Assignment Questions

##--------------------------------------------------------------------
## Part 1: LoadData Function
def LoadData(filename):
    a= [tuple([r[0],r[1],r[2],float(r[3]),float(r[4])]) for r in csv.reader(open(filename))]
##    for i in a:
##        print a
    return a

##lst=LoadData(filename)

## Helper Function
## Controls the type of data in the list being fed into the sorter
##def list_loader(col,lst):
##    a= [i[col] for i in lst]
##    if col==3:
##        lst=[float(x) for x in a]
##    elif col==4:
##        lst=[int(x) for x in a]
##    else:
##        lst=a
##    return lst

##-------------------------------------------------------------------
## Part 2: Selection Sort
def selectionSort(lst,col,ascending=True):
##    print (col)
    initial_time=clock()
    if ascending==True:
        for h in range(0, len(lst)):
            j = h
            for i in range(h,len(lst)):
                if lst[j][col] > lst[i][col]:
                    j = i
            lst[j],lst[h]=lst[h],lst[j]
    else:
        for h in range(0, len(lst)):
            j = h
            for i in range(h,len(lst)):
                if lst[j][col] < lst[i][col]:
                    j = i
            lst[j],lst[h]=lst[h],lst[j]
    final_time=clock()
    global selectiontime
    selectiontime=final_time-initial_time
##    print (selectiontime,'seconds')
    return lst
##-------------------------------------------------------------------
## Part 3: Merge Sort
def mergeSort(lst,col,ascending=True):
    initial_time=clock()
    l=msort(lst,col,ascending)
    final_time=clock()
    global mergetime
    mergetime=final_time-initial_time
##    print (mergetime,'seconds')
    return l
##-------------------------------------------------------------------
#### Part 4: Quick Sort
def quickSort(lst,col,ascending=True):
    initial_time=clock()
    l=quicksort(lst,col,ascending)
    final_time=clock()
    global quicktime
    quicktime=final_time-initial_time
    print (quicktime,'seconds')
    return l

##SelectionList=[selectionSort(lst[:x+1], for x in range(1000,11000,1000)]

##def timeit(lst,col):
##    si=clock()
##    a=selectionSort(lst,col)
##    print ("Selection Sort Time=",clock()-si,"seconds")
##    mi=clock()
##    b=mergeSort(lst,col)
##    print ("Merge Sort Time:",clock()-mi,"seconds")
##    qi=clock()
##    c=quickSort(lst,col)
##    print ("Quick Sort Time:",clock()-qi,"seconds")
##    x = [i[col] for i in a]
##    y = [i[col] for i in b]
##    z = [i[col] for i in c]
##    if x==y==z:
##            print ("Same Sorted Columns")
##            print ("*******************")
##
##    if  a==b==c:
##            print ('Same Sorted List')
##            print ("*****************")
##                   
##def k(lst,col):
##    x=[]
##    y=[]
##    z=[]
##    for i in range(1000,11000,1000):
####        a=selectionSort(lst[:i],col)
####        x.append(selectiontime)
##        b=mergeSort(lst[:i],col)
##        y.append(mergetime)
##        c=quickSort(lst[:i],col)
##        z.append(quicktime)
##    plt.xlabel('Time')
##    print(y,z)
##    plt.plot(x,[x for x in range(1000,11000,1000)],'r')
##    plt.plot(y,[x for x in range(1000,11000,1000)],'b')
##    plt.plot(z,[x for x in range(1000,11000,1000)],'g')
##    plt.show()
##
##for i in range(0,5):
##    a=timeit(lst,i)
##    print ('******************************')
