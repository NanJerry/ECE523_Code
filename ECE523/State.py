import numpy as np
X_Stabilizer = ["XIXIXIXIXIXIXIX","IXXIIXXIIXXIIXX","IIIXXXXIIIIXXXX","IIIIIIIXXXXXXXX"]
a=['0','1']
combi_X = [ele1+ele2 for ele1 in a for ele2 in a]
combi_X = [ele1+ele2 for ele1 in combi_X for ele2 in combi_X]

def addStabilizer(a,b):
    new =''
    for k in range(len(a)):
        if (a[k] != b[k]):
            new += 'X'
        else:
            new += 'I'
    return new

def stateChange(s):
    state=''
    for k in range(len(s)):
        if (s[k] == 'I'):
            state+='0'
        else:
            state+='1'
    return state


New_combination = []
for i in range(len(combi_X)):
    conbinedS = 'IIIIIIIIIIIIIII'
    for j in range(len(X_Stabilizer)):
        if (combi_X[i][j] == '1'):
            conbinedS=addStabilizer(conbinedS,X_Stabilizer[j])
    New_combination.append(conbinedS)

Latex = '\\frac{1}{4}\\left('
for i in range(len(New_combination)):
    Latex += '\\ket{' + stateChange(New_combination[i]) + "}+"
    if (i % 4) == 0:
        Latex += "\\\\"
Latex = Latex[:-1]
Latex += '\\right)'

logical_X = "IIXIXXIIXXIXIIX"
logical_one = []
for i in range(len(New_combination)):
    logical_one.append(addStabilizer(New_combination[i],logical_X))

Latex2 = '\\frac{1}{4}\\left('
for i in range(len(logical_one)):
    Latex2 += '\\ket{' + stateChange(logical_one[i]) + "}+"
    if (i % 4) == 0:
        Latex2 += "\\\\"
Latex2 = Latex2[:-1]
Latex2 += '\\right)'
count_logical_zero = [ele.count('X') for ele in New_combination]
count_logical_one = [ele.count('X') for ele in logical_one]

Zs='ZZZII IIIII IIIII \
ZIIZZ IIIII IIIII \
IZIZI ZIIII IIIII \
ZZIZI IZIII IIIII \
ZIIII IIZZI IIIII \
IZIII IIZIZ IIIII \
ZZIII IIZII ZIIII \
IIIZI IIZII IZIII \
ZIIZI IIZII IIZII \
IZIZI IIZII IIIZI \
ZZIZI IIZII IIIIZ'
Zs = Zs.split()
ZSS =[]
for i in range(11):
    ZSS.append(Zs[3*i]+Zs[3*i+1]+Zs[3*i+2])

T_S="\
ZIZIZIZIZIZIZIZ IZZIIZZIIZZIIZZ IIIZZZZIIIIZZZZ \
IIIIIIIZZZZZZZZ IIZIIIZIIIZIIIZ IIIIZIZIIIIIZIZ IIIIIZZIIIIIIZZ \
IIIIIIIIIZZIIZZ IIIIIIIIIIIZZZZ IIIIIIIIZIZIZIZ"
T_S=T_S.split()
sequence=[]
for i in range(len(T_S)):
    sequence.append([])

def addZStabilizer(a,b):
    new =''
    for k in range(len(a)):
        if (a[k] != b[k]):
            new += 'Z'
        else:
            new += 'I'
    return new

for i in range(int(np.exp2(len(ZSS)))):
    a = '{0:011b}'.format(i)
    newchar ='IIIIIIIIIIIIIII'
    for j in range(len(a)):
        if a[j] == '1':
            newchar=addZStabilizer(newchar,ZSS[j])
    for j in range(len(T_S)):
        if newchar == T_S[j]:
            sequence[j].append(a)


