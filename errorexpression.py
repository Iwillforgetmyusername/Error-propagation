def listify(x):

    elem, outlis = x.split('/'),[]
    
    for i in range(len(elem)):
        if '(' in elem[i] and ')' in elem[i]:
            elem[i] = elem[i][1:len(elem[i])-1]

    elem[0]+= ' '
    count0 = 0
    power0 = '1'
    powexist0=False

    
    for j in range(len(elem[0])):
        
        if elem[0][j] == '^':

            conf0=0
            powexist0=True
            start0 = j+1
            chk0=j+1

            while conf0 == False:
                if elem[0][chk0] == '*' or chk0 == len(elem[0])-1:
                    end0=chk0
                    conf0=1
                chk0+=1
            power0 = elem[0][start0:end0]
        
        if elem[0][j] == '*' or j == len(elem[0])-1:
            if powexist0 == False:
                start0=j+1
            outlis.append(elem[0][count0:start0-1])
            outlis[len(outlis)-1]+= '^'+ power0
            count0 = j+1
            power0 = '1'
            powexist0 = False
            
    if len(elem) > 1:
        elem[1] += ' '
        count1 = 0
        powexist1=False
        power1 = '-1'
        
        for k in range(len(elem[1])):
            if elem[1][k] == '^':
                conf1=0
                powexist1=True
                chk1=k+1
                start1=k+1
                while conf1 == False:
                    if elem[1][chk1] == '*' or chk1 == len(elem[1])-1:
                        end1=chk1
                        conf1=1
                    chk1+=1
                power1 = '-' + elem[1][k+1:end1]
            
            if elem[1][k] == '*' or k == len(elem[1])-1:
                if powexist1 == False:
                    start1=k+1
                outlis.append(elem[1][count1:start1-1])
                outlis[len(outlis)-1]+= '^'+ power1
                count1 = k+1
                power1 = '-1'
                powexist1 = False
                
    return outlis

def derive(inlist,num):

    midlist = inlist
    deriv = midlist[num].split('^')

    try:
        floatchk=float(deriv[0])
        return '0'
    except ValueError:

        coeff = deriv[1]
        deriv[1] = float(deriv[1])
        deriv[1]-= 1.0
        if deriv[1] == 0.0:
            midlist[num] = '1^1'

        else:
            midlist[num] = deriv[0] + '^' + str(deriv[1])

        outlist = [coeff,'1']
        for i in range(len(midlist)):
            part = midlist[i].split('^')
            if float(part[1]) > 0:
                if float(part[1]) != 1.0:
                    outlist[0]+= '*' + part[0] + '^' + part[1]
                else:
                    outlist[0]+= '*' + part[0]
            else:
                if float(part[1]) != -1.0:
                    outlist[1]+= '*' + part[0] + '^' + str(-float(part[1]))
                else:
                    outlist[1]+= '*' + part[0]

        if outlist[1] == '1':
            return '(' + outlist[0] + ')'
        else:
            return '((' + outlist[0] + ')/(' + outlist[1] + '))'
        
        
print '''input style:
a^n*b^m*c^p.../d^q*e^r... or (a^n*b^m*c^p...)/(d^q*e^r...)
doesn't doesn't matter which of these, they will mean the same thing
Any more complicated expressions, though, with sums and subtractions
and logs and trig, well, maybe I'll add that later. Have fun
'''
x= raw_input('expression:')
for n in range(len(x)):
    if x[n] == ',':
        x = x[:n]+'.'+x[n+1:]
lis = listify(x)
liss = tuple(lis)
endlist=[]
for i in range(len(lis)):
    endlist.append(derive(lis,i))
    lis = list(liss)
    if endlist[i] != '0':
        var = lis[i].split('^')
        endlist[i] = '('+ endlist[i] + '*ERROR[' + var[0] + '])^2'

            
endstring='SQRT('
for j in range(len(endlist)-1):
    endstring+=endlist[j]+'+'
endstring+= endlist[len(endlist)-1] + ')'
for k in range(len(endstring)):
    if endstring[k] == '.':
        endstring = endstring[:k] + ',' + endstring[k+1:]

print  'final result: ', endstring
