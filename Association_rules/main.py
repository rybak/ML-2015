import textwrap
from ml import *

big_data = load_super_market_dataset()

attr = big_data['attributes']
data = big_data['data']

baskets = {}  # empty dictionary
for (name, category, department, basket_id) in data:
    baskets.setdefault(basket_id, [])
    baskets[basket_id].append((name, category, department))

print("Example of a basket:")
example = "somebody is preparing dinner:\n" + str(", ".join(map(lambda x: x[0], baskets.get(data[2][3]))))
print(textwrap.fill(example, 80))

print("number of baskets = {}".format(len(baskets)))
# for i, basket in enumerate(baskets.items()):
#     print(i, basket[1])
