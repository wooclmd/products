#讀取檔案
products = []
with open('products.csv', 'r', encoding='utf-8') as f:
	for line in f:
		if '商品,價格' in line:
			continue
		s = line.strip().split(',')
		products.append(s) #印出來變一行的清單
print(products)


products = []
while True:
	name = input('東西: ')
	if name == 'q':
		break
	price = input('價格: ')
	p = []
	p.append(name)
	p.append(price)
	products.append(p)
	#products.append([name,price])
print(products)

#for
for p in products:
	print(p[0])

#寫入檔案
with open('products.csv', 'w', encoding='utf-8') as f:
	f.write('商品,價格\n')
	for p in products:
	    f.write(p[0] + ',' + p[1] + '\n')