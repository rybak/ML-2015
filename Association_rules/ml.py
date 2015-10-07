import arff
# pip install liac-arff for the arff module

def load_super_market_dataset():
    return arff.load(open('supermarket.arff', 'r'))
PRODUCT_NAME_INDEX = 0
PRODUCT_CAT_INDEX = 1
PRODUCT_DEPT_INDEX = 2
BASKET_ID_INDEX = 3

