from ml import *
import textwrap

big_data = load_super_market_dataset()
print(big_data.keys())
print("Relation : " + str(big_data['relation']))
print("Description : " + str(big_data['description']))

attrs = big_data['attributes']
for (x, y) in attrs:
    print(x)
products_str = ''
product_names_list = []
for (x, y) in attrs:
    if x == 'product_department':
        print("Departments:")
        print(textwrap.indent(textwrap.fill(", ".join(map(str, y)), 80), "\t"))
    if x == 'product_category':
        print("Categories:")
        print(textwrap.indent(textwrap.fill(", ".join(map(str, y)), 80), "\t"))
    if x == 'product_name':
        print("Products:")
        product_names_list = y
        products_str = textwrap.indent(textwrap.fill(", ".join(map(str, y)), 200), "\t")
        print(products_str)

data = big_data['data']
products = {}
for datum in data:
    if datum[PRODUCT_NAME_INDEX] not in products:
        name = datum[PRODUCT_NAME_INDEX]
        products[name] = (datum[PRODUCT_NAME_INDEX], datum[PRODUCT_CAT_INDEX], datum[PRODUCT_DEPT_INDEX])

open("products.txt", "w").write(str("\n".join(map(str, products.values()))))
