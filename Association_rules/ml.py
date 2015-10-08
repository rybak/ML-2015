import arff
# pip install liac-arff for the arff module

def load_super_market_dataset():
    big_data = arff.load(open('supermarket.arff', 'r'))
    attr = big_data['attributes']
    data = big_data['data']
    return big_data, attr, data

def aggregate_baskets(data):
    # aggregating data in baskets (aka transactions)
    baskets = {}  # empty dictionary
    products = set() # empty set
    for (name, category, department, basket_id) in data:
        baskets.setdefault(basket_id, [])
        product = (name, category, department)
        products.add(product)
        baskets[basket_id].append(product)
    return baskets, products

PRODUCT_NAME_INDEX = 0
PRODUCT_CAT_INDEX = 1
PRODUCT_DEPT_INDEX = 2
BASKET_ID_INDEX = 3

