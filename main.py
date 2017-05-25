#!/usr/bin/python
import json
import math

# An Array that contains all the product information read from produts.txt
products = []

# A HashMap in the form of a python dictionary which maps
# product_name for each Product with an array of its respective listings
# key: product_name, value: [Listing]
products_table = {}

"""
    Returns an Array of Products that matches this manufacturer and this query
    using a divide and conquer algorithm

    @products Original Array containing all the products
    @query title of this listing
    @manufacturer manufacturer of this listing
"""
def find_products(products, query, manufacturer):
    if len(products) > 1:
        m = math.floor(len(products)/2)

        first = find_products(products[0:m], query, manufacturer)
        second = find_products(products[m:len(products)], query, manufacturer)

        return first + second

    else:
        # convert everything to upper case since might be case sensitive
        title = query.upper()
        product = products[0]

        manuf = product["manufacturer"].upper()
        is_manuf = (manuf == manufacturer.upper())

        # add spaces before and after since we want to match whole words
        model = " " + product["model"].upper() + " "
        is_model = (model in title)

        # not every product has a family, if it doesnt no need to search it
        if "family" in product.keys():
            family = " " + product["family"].upper() + " "
            is_family = (family in title)
        else:
            is_family = True


        if (is_manuf and is_model and is_family):
            return [product]
        else:
            return []


# create product listings for each product
with open("products.txt") as p:
    print("Working...")
    for line in p:
        product = json.loads(line)

        # create an empty field in the hashmap
        products_table[product["product_name"]] = []

        # every product should be inside products to be used later
        products.append(product)

with open("listings.txt") as l:
    for line in l:
        listing = json.loads(line)

        title = listing["title"]
        manufacturer = listing["manufacturer"]
        found_products = find_products(products, title, manufacturer)

        #if product is found append this listing in the hashmap
        for found_product in found_products:
            products_table[found_product["product_name"]].append(listing)

with open("results.txt", "w") as r:
    # re-arrange the data to get the desired output format
    print("Writing to results.txt...")
    for product, listings in products_table.items():
        product_listing = {"product_name": product, "listings": listings}
        json.dump(product_listing, r)
        r.write("\n")
    print("Done!")
