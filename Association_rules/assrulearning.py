support = {}


def count_support(baskets, item_set):
    item_set = tuple(item_set)
    if item_set not in support:
        count = 0
        for basket in baskets.values():
            if all(x in basket for x in X):
                count += 1
        support[item_set] = count / len(baskets)
    return support[item_set]


def count_item_support(baskets, x):
    if x not in support:
        n = 0
        for basket in baskets.values():
            n += sum(n == item for item in basket)
        support[x] = n / len(baskets)
    return support[x]


def count_confidence(data):
    return None


def count_lift(data):
    return None


def count_conviction(data):
    return None


def initL(baskets, products, minimal_support):
    def has_minimal_support(x):
        return count_item_support(baskets, x) > minimal_support
    large_1_itemsets = filter(has_minimal_support, products)
    return large_1_itemsets


def updateCk(C, L, k):
    pass


def updateCt(C, t, k):
    pass


def generateLk(C, k, count):
    pass


def apriori(transactions, eps):
    L = initL(transactions, eps)
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
