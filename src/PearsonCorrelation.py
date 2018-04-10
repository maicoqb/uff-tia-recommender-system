import math

def mean(A):
    m = 0
    for n in A: m += int(n)
    return (1 / len(A)) * m

def covariance(X, Y):
    mx = mean(X)
    my = mean(Y)

    C = 0
    for i, x in enumerate(X):
        y = Y[i]
        C += (x - mx)*(y - my)

    return C

def standardDeviation(A):
    ma = mean(A)

    sd = 0
    for a in A: sd += math.pow(a - ma, 2)

    return sd

def pearsonCorrelation(X, Y):
    a = covariance(X, Y)
    b = math.sqrt(standardDeviation(X) * standardDeviation(Y))

    if b == 0: return 0
    return a / b
