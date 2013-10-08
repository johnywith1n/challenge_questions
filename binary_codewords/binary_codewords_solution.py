from math import factorial
import itertools

def combo(n, k):
    return factorial(n) / (factorial(k) * factorial(n-k))

def getNumIndexAndOnes(n,k):
    start = 0
    end = 0
    for x in xrange(n):
        combos = combo(n, x)
        end += combos
        if k <= end:
            return x, k - start
        start = end
    return n, k - start

def pick_codeword(n,k):
    numOnes, index = getNumIndexAndOnes(n,k)
    numBitsCompleted = 0
    result = ""
    for i in range(n, 0, -1):
        if numOnes == 0 or i-1 < numOnes:
            break
        testNum = combo(i-1, numOnes)
        if testNum >= index:
            result += "0"
            numBitsCompleted += 1
        else:
            result += "1"
            numOnes -= 1
            numBitsCompleted += 1
            index -= testNum
    for i in range(numOnes):
        result += "1"
        numBitsCompleted += 1
    for i in range(n-numBitsCompleted):
        result += "0"
    return result

def cmp (x,y):
    diffNumOnes = x.count('1') - y.count('1')
    if diffNumOnes == 0:
        return x > y
    else:
        return diffNumOnes

def getBitStrings(n):
    return ["".join(seq) for seq in itertools.product("01", repeat=n)]

def test(n):
    strings = sorted(getBitStrings(n), cmp = cmp)
    for i in range(len(strings)):
        assert(pick_codeword(n, i+1) == strings[i])

def testAll():
    for i in range(1,11):
        test(i)