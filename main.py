def tuple_product(tup):
    product = 1
    for num in tup:
        product *= num
    return product

# Example usage:
tup1 = (4, 3, 2, 2, -1, 18)
tup2 = (2, 4, 8, 8, 3, 2, 9)

product1 = tuple_product(tup1)
product2 = tuple_product(tup2)

print("Product of tup1:", product1)
print("Product of tup2:", product2)