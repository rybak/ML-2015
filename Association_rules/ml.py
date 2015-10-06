import arff
# pip install liac-arff for the arff module

def load_super_market_dataset():
    return arff.load(open('supermarket.arff', 'r'))


