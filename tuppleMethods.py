countries = ("India", "spain", "japan", "iran")
temp = list(countries)
temp.append("russia")
temp.pop(3)
temp[2] = "finland"
countries = tuple(temp)
print(countries)

tuple1 = (0, 1, 2, 4, 3, 5, 6, 7, 8, 9)
res = tuple1.count(3)
print('count of 3 in Tuple is: ', res)
ind = tuple1.index(5)
print(ind)
iength = len(tuple1)
print(iength)