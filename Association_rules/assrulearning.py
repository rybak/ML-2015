import ml

support = {}


def count_support(baskets, X):
    X = tuple(X)
    if X not in support:
        count = 0
        for basket_id, basket in baskets.items():
            if all(x in basket for x in X):
                count += 1
        support[X] = count / len(baskets)
    return support.get(X)


def count_confidence(data):
    return None


def count_lift(data):
    return None


def count_conviction(data):
    return None


def initL(transactions):
    pass


def updateCk(C, L, k):
    pass


def updateCt(C, t, k):
    pass


def generateLk(C, k, count):
    pass


def apriori(transactions, eps):
    L = initL(transactions)
    k = 2
    C = {}
    while len(L[k - 1]) > 0:
        C[k] = updateCk(C, L, k)
        count = {}
        for t in transactions:
            C[t] = updateCt(C, t, k)
            for c in C[t]:
                count.setdefault(c, 0)
                count[c] += 1
        # update L[k]
        L[k] = generateLk(C, k, count)
        k += 1
    return L
