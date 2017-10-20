path = 'WODList.txt'
wod_file = open(path, 'r')
wod = wod_file.read()
print(wod)

wod_file.close()
