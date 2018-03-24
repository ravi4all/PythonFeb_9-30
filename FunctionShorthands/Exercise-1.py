products = [
    {'id':101,'name':'Apple','price':86000,'color':'silver'},
    {'id':102,'name':'Samsung','price':55000,'color':'gray'},
    {'id':103,'name':'Vivo','price':22000,'color':'white'},
    {'id':104,'name':'Apple','price':36000,'color':'silver'},
    {'id':105,'name':'Redmi','price':12000,'color':'silver'},
    {'id':106,'name':'Redmi','price':15000,'color':'black'},
    {'id':107,'name':'Vivo','price':18000,'color':'black'},
    {'id':108,'name':'Samsung','price':66500,'color':'silver'},
    {'id':109,'name':'Samsung','price':56500,'color':'white'},
    {'id':110,'name':'Apple','price':96000,'color':'gray'},
]

# to_search = input("Enter product name : ")

# def search(prod):
    # return prod['name'] == to_search.capitalize()
    # return prod['price'] > 20000

# for p in products:
#     print(search(p))

# p = list(filter(search, products))

p = list(filter(lambda prod : prod['price'] > 20000, products))

for data in p:
    print(data)