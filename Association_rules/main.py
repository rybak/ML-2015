from ml import *
from utils import *
from assrulearning import *
# import numpy as np

big_data, attr, data = load_super_market_dataset()
baskets, products = aggregate_baskets(data)

sizes = sorted(list(map(len, baskets.values())), reverse=True)
sizes = uniqify(sizes)
print(sizes[:10])
print("Average basket size : ", sum(sizes) / len(sizes))

# print(count_support(baskets,
#                     (('Good Imported Beer', 'Beer and Wine', 'Alcoholic Beverages'),
#
#                     ))
