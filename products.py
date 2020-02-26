product = []
while True:
	name = input('東西: ')
	if name == 'q':
		break
	price = input('價格: ')
	product.append([name, price])
	#簡化 p = []
	#p.append(name)
	#p.append(price)
	#p = [name, price]
	#product.append(p)
print(product)

for p in product:
	print(p[0])