from ml import *
import textwrap

data = load_super_market_dataset()
print(data.keys())
print("Relation : " + str(data['relation']))
print("Description : " + str(data['description']))

attrs = data['attributes']
for (x, y) in attrs:
    print(x)
print("Departments:")
for (x, y) in attrs:
    if x == 'product_department':
        print(textwrap.indent(textwrap.fill(", ".join(map(str, y)), 80), "\t"))
print("Categories:")
for (x, y) in attrs:
    if x == 'product_category':
        print(textwrap.indent(textwrap.fill(", ".join(map(str, y)), 80), "\t"))


