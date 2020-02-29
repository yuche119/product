products = []
while True:
    names = input ('請輸入商品名稱')
    if names == 'q':
        break
    price = input('請輸入商品價格')
    # p = []
    # p.append(names)
    # p.append(price)
    # products.append(p)
    products.append([names, price]) #可以用這樣更簡潔方式
print(products)