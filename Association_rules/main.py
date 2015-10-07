import textwrap
from ml import *
from assrulearning import *
# import numpy as np

big_data = load_super_market_dataset()

attr = big_data['attributes']
data = big_data['data']

data_example = data[2]
print("number of data : ", len(data))
print("data example: ", data_example)
print("prod name: ", data_example[PRODUCT_NAME_INDEX])
print("prod cat : ", data_example[PRODUCT_CAT_INDEX])
print("prod dept: ", data_example[PRODUCT_DEPT_INDEX])
print("basket id: ", data_example[BASKET_ID_INDEX])

# aggregating data in baskets (aka transactions)
baskets = {}  # empty dictionary
for (name, category, department, basket_id) in data:
    baskets.setdefault(basket_id, [])
    baskets[basket_id].append((name, category, department))

# more examples
for basket in baskets.values():
    print("First basket : ", basket)
    break
print("Example of a basket: //somebody is preparing dinner")
example = str(", ".join(map(lambda x: x[0], baskets.get(data[2][BASKET_ID_INDEX]))))
print(textwrap.fill(example, 80))

print("number of baskets = {}".format(len(baskets)))
# for i, basket in enumerate(baskets.items()):
#     print(i, basket[1])

# example of support : lettuce and beer in one basket
print(count_support(baskets,
                    (('Tri-State Lettuce', 'Vegetables', 'Produce'),
                     ('Good Imported Beer', 'Beer and Wine', 'Alcoholic Beverages'))))


test_support = {}
test_size = 3
i = 0
for basket in baskets.values():
    assert len(basket) > 0
    if len(basket) >= test_size:
        X = tuple(basket[:test_size])
        test_support[X] = count_support(baskets, X)
        i += 1
        if i > 100:
            break

for (X, s) in test_support.items():
    print(tuple(map(lambda x: str(x[0]), X)), " \t ", s)

def uniqify(seq, idfun=None):
    # order preserving
    if idfun is None:
        def idfun(x): return x
    seen = {}
    result = []
    for item in seq:
        marker = idfun(item)
        # in old Python versions:
        # if seen.has_key(marker)
        # but in new ones:
        if marker in seen: continue
        seen[marker] = 1
        result.append(item)
    return result

sizes = sorted(list(map(len, baskets.values())), reverse=True)
sizes = uniqify(sizes)
print(sizes[:10])
print("Average basket size : ", sum(sizes) / len(sizes))


# print(count_support(baskets,
#                     (('Good Imported Beer', 'Beer and Wine', 'Alcoholic Beverages'),
#
#                     ))
