from ml import *
import textwrap

data = load_super_market_dataset()


# print(data['description'])
print("Relation : " + str(data['relation']))

attrs = data['attributes']
print("Departments:")
for (x, y) in attrs:
    if x == 'product_department':
        pass
print("Categories:")
for (x, y) in attrs:
    if x == 'product_category':
        print(textwrap.indent(textwrap.fill(", ".join(map(str, y)), 80), "\t"))

for (x, y) in data['attributes']:
    print(x)

