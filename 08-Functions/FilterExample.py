products = [
    {'id':101,'name':'Samsung','price':45000,'color':'Red'},
    {'id':102,'name':'Apple','price':65000,'color':'Silver'},
    {'id':103,'name':'Redmi','price':15000,'color':'White'},
    {'id':104,'name':'Samsung','price':55000,'color':'Silver'},
    {'id':105,'name':'Apple','price':85000,'color':'Black'},
    {'id':106,'name':'Nokia','price':18000,'color':'Black'},
    {'id':107,'name':'Redmi','price':10000,'color':'Silver'},
    {'id':108,'name':'Redmi','price':12000,'color':'Gray'},
    {'id':109,'name':'Vivo','price':20000,'color':'White'},
    ]

output = list(filter(lambda x : x['name'] == 'Apple', products))

sort_by_price = list(sorted(products, key=lambda x : x['price']))
# print(sort_by_price)

for res in sort_by_price:
    print(res)

# for result in output:
#     print(result)