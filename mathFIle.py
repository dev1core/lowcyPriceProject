from random import randint

'''
Rozwiązanie zagadki cyfrowy wiek
Umieść dokładnie trzy symbole matematyczne między cyframi 1 2 3 4 5 6 7 8 9,
tak, aby otrzymać wynik 100.Uwaga! Możesz powtórzyć ten sam symbol, ale każde
powtórzenie liczy się do limitu trzech powtórzeń, które możesz wykorzystać.
Nie wolno zmieniać kolejności cyfr!
'''

def respChar(c, n1, n2):
    resNum = 0
    if(c == '+'):
        resNum = n1 + n2
    elif(c == '-'):
        resNum = n1 - n2
    elif(c == '*'):
        resNum = n1 * n2
    elif(c == '/'):
        if(n2!=0):
            resNum = n1 / n2
    return resNum

result = 100
num = [1,2,3,4,5,6,7,8,9]
charTab = ['+','-','*','/']
randCharTab = [""]
iterat = 0

while True:
    randCharTab.clear();
    rNum1 = ""
    rNum2 = ""
    rNum3 = ""
    rNum4 = ""

    r1 = randint(1,5)
    min1 = 0
    max1 = r1
    for i in range(min1, max1):
        rNum1 = int(str(rNum1) + str(num[i]))

    min2 = max1
    max2 = randint(min2,6)

    for i2 in range(min2, max2 + 1):
        rNum2 = int(str(rNum2) + str(num[i2]))

    min3 = max2 + 1
    max3 = randint(min3,7)

    for i3 in range(min3, max3+ 1):
        rNum3 = int(str(rNum3)+ str(num[i3]))

    min4 = max3 + 1
    max4 = 8

    for i4 in range(min4, max4 + 1):
        rNum4 = int(str(rNum4) + str(num[i4]))

    p = 1
    for p in range(3):
        randCharTab.append(charTab[randint(0,3)])
    s1 = respChar(randCharTab[0], float(rNum1), float(rNum2))
    s2 = respChar(randCharTab[1], s1, float(rNum3))
    finResult = respChar(randCharTab[2], s2, float(rNum4))

   # finResult = respChar(randCharTab[2], respChar(randCharTab[1], respChar(randCharTab[0], int(rNum1), int(rNum2)), int(rNum3)), int(rNum4))

    if(finResult == 100):
        print(str(rNum1) + " " + randCharTab[0] + " " + str(rNum2) + " " + randCharTab[1] + " " + str(rNum3) + " " + randCharTab[2] + " " + str(rNum4) + " result is " + str(finResult) + "| iteration: " + str(iterat))
    iterat = iterat + 1