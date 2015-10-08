from assrulearning import *
from ml import *
import textwrap

big_data, attr, data = load_super_market_dataset()

baskets, products = aggregate_baskets(data)
print(big_data.keys())
print("Relation : " + str(big_data['relation']))
print("Description : " + str(big_data['description']))

for (x, y) in attr:
    print(x)
products_str = ''
product_names_list = []
for (x, y) in attr:
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

### Examples
data_example = data[2]
print("number of data : ", len(data))
print("data example: ", data_example)
print("prod name: ", data_example[PRODUCT_NAME_INDEX])
print("prod cat : ", data_example[PRODUCT_CAT_INDEX])
print("prod dept: ", data_example[PRODUCT_DEPT_INDEX])
print("basket id: ", data_example[BASKET_ID_INDEX])

# more examples

for basket in baskets.values():
    print("First basket : ", basket)
    break
print("Example of a basket: //somebody is preparing dinner")
example = str(", ".join(map(lambda x: x[0], baskets.get(data[2][BASKET_ID_INDEX]))))
print(textwrap.fill(example, 80))

print("number of baskets = {}".format(len(baskets)))

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

# products = {}
# for datum in data:
#     if datum[PRODUCT_NAME_INDEX] not in products:
#         name = datum[PRODUCT_NAME_INDEX]
#         products[name] = (datum[PRODUCT_NAME_INDEX], datum[PRODUCT_CAT_INDEX], datum[PRODUCT_DEPT_INDEX])
#
# open("products.txt", "w").write(str("\n".join(map(str, products.values()))))
