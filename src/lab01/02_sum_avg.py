a = float(input('a: ').replace(',','.'))
b = float(input('b: ').replace(',','.'))
print('sum=' + '{:.2f}'.format(a+b) + ';', 'sum=' + '{:.2f}'.format((a+b)/2))