#imports csv module or whatever it's fucking called#
import csv

#opens the file in this line only so everything outside this function isn't opened#
with open('T-Test.csv') as csvfile:
    #creates a variable named readCSV that has all the data in lists by row#
    readCSV = csv.reader(csvfile, delimiter=',')
    #creates a class for all the data#
    class Datas(object):
        def __init__(self,minority,female,ses,math):
            self.minority=minority
            self.female=female
            self.ses=ses
            self.math=math
    #m1 is non-minorities#
    m1=[]
    m2=[]
    for row in readCSV:
        row[0]=Datas(row[1],row[2],row[3],row[4])
        if (row[0].minority)=='0':
            m1.append(row[0].ses)
        elif(row[0].minority)=='1':
            m2.append(row[0].ses)
        else:
            pass
    #group sums#
    m1sum=0
    m2sum=0
    for n in m1:
        m1sum+=float(n)
    print(m1sum)
    for n in m2:
        m2sum+=float(n)
    print(m2sum)
    #averages#
    m1average=m1sum/len(m1)
    m2average=m2sum/(len(m2))
    print (m1average,m2average)
    #variances and SD#
    m1vars=[]
    m2vars=[]
    for n in m1:
        m1vars.append(float(n)-m1average)
    for n in m2:
        m2vars.append(float(n)-m2average)
    m1var=0
    m2var=0
    for n in m1vars:
        m1var+=(float(n)**2)
    for n in m2vars:
        m2var+=(float(n)**2)
    m1sd=(m1var/len(m1vars))**0.5
    m2sd=(m2var/len(m2vars))**0.5
    print (m1average, m1sd)
    print (m2average, m2sd)
    # sum of scores#
    m1ss=0
    m2ss=0
    for n in m1:
        m1ss+=float(n)**2
    for n in m2:
        m2ss+=float(n)**2
    #actual t-test#
    t=((m1average-m2average)/((((m1ss-((m1sum**2)/len(m1))+(m2ss-((m2sum**2)/len(m2))))/(lenm1)+len(m2)-2))*((1/len(m1))+(1/len(m2))))**0.5))
    print(t)
